#!/usr/bin/env python

import argparse
import signal
import functools
import base64
import time
import os
import requests
import threading
import mflog
import sys
import subprocess
import datetime
from mfutil import kill_process_and_children


LOGGER = mflog.get_logger("signal_wrapper")
MFSERV_NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])
NGINX_TIMEOUT = 10
SMART_SHUTDOWN = None
SIG_SHUTDOWN = None
HARD_SHUTDOWN = None


def unix_socket_encode(unix_socket):
    return base64.urlsafe_b64encode(unix_socket.encode('utf8')).decode('ascii')


def get_socket_conns(unix_socket):
    url = "http://127.0.0.1:%i/__upstream_status" % MFSERV_NGINX_PORT
    try:
        res = requests.get(url, timeout=NGINX_TIMEOUT).json()
        for peers in res.values():
            for peer in peers:
                if peer.get('name', None) == 'unix:' + unix_socket:
                    return peer.get('conns', None)
    except Exception:
        return None


def socket_down(unix_socket, wait, timeout):
    new_timeout = None if timeout <= 0 else timeout
    params = {}
    reply = None
    if wait:
        params = {"wait": "1"}
    try:
        reply = requests.get(
            "http://127.0.0.1:%i/__socket_down/%s" % (
                MFSERV_NGINX_PORT, unix_socket_encode(unix_socket)),
            params=params, timeout=new_timeout)
    except Exception:
        pass
    if reply is None or reply.status_code != 200:
        return False
    else:
        return True


def send_signal_when_no_connection(pid, unix_socket, sig, timeout):
    global SIG_SHUTDOWN, HARD_SHUTDOWN
    LOGGER.info("stopping new connections and waiting for no connection "
                "left on %s (timeout: %i seconds)" %
                (unix_socket, timeout))
    if socket_down(unix_socket, True, timeout):
        SIG_SHUTDOWN = datetime.datetime.now()
        LOGGER.info("sending %s to %i",
                    signal.Signals(sig).name, pid)  # pylint: disable=E1101
        os.kill(pid, sig)
    else:
        HARD_SHUTDOWN = datetime.datetime.now()
        LOGGER.warning("sending SIGKILL to %i and its children", pid)
        kill_process_and_children(pid)


def on_signal(unix_socket, pid, signal, timeout, signum, frame):
    global SMART_SHUTDOWN, HARD_SHUTDOWN
    if signum == 15:
        if SMART_SHUTDOWN is not None:
            LOGGER.info("received SIGTERM but SMART_SHUTDOWN already in "
                        "progress => ignoring")
            return
        LOGGER.info("received SIGTERM => smart closing...")
        SMART_SHUTDOWN = datetime.datetime.now()
        x = threading.Thread(target=send_signal_when_no_connection,
                             args=(pid, unix_socket, signal, timeout))
        x.daemon = True
        x.start()
    elif signum == 2:
        if HARD_SHUTDOWN:
            return
        HARD_SHUTDOWN = datetime.datetime.now()
        LOGGER.warning("received SIGINT => (non smart) stopping...")
        LOGGER.warning("sending SIGKILL to %i and its children", pid)
        kill_process_and_children(pid)


def socket_up_after(unix_socket, after):
    time.sleep(after)
    LOGGER.debug("socket_up on nginx")
    url = "http://127.0.0.1:%i/__socket_up/%s" % (
        MFSERV_NGINX_PORT,
        unix_socket_encode(unix_socket)
    )
    try:
        requests.get(url, timeout=NGINX_TIMEOUT)
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(
        description="nginx upstream server wrapper "
        "(gracefully shutdown an nginx upstream server in case of SIGTERM)")
    parser.add_argument("unix_socket", help="unix socket to listen path")
    parser.add_argument("--socket-up-after", default=3, type=int,
                        help="wait this number of seconds after start before "
                        "doing a socket up (default: 3)")
    parser.add_argument("--timeout", default=0, type=int,
                        help="number of seconds to wait for gracefull "
                        "shutdown (0 (default) means no timeout)")
    parser.add_argument("--timeout-after-signal", default=3, type=int,
                        help="number of seconds to wait for child exit after "
                        "signal (0 means no timeout), after that delay "
                        "=> SIGKILL (default: 3)")
    parser.add_argument("--signal", default=15, type=int,
                        help="signal to send to child process if the "
                        "gracefull process was ok")
    tmp = parser.parse_known_args()
    args = tmp[0]
    remaining_args = tmp[1]
    if len(remaining_args) == 0:
        print("ERROR: you have to provide a command to execute")
        sys.exit(1)
    if remaining_args[0] == "--":
        remaining_args.pop(0)
    try:
        os.remove(args.unix_socket)
    except Exception:
        pass
    p = subprocess.Popen(remaining_args)
    pid = p.pid
    for signum in (signal.SIGTERM, signal.SIGINT):
        signal.signal(signum,
                      functools.partial(on_signal,
                                        args.unix_socket, pid, args.signal,
                                        args.timeout))
    x = threading.Thread(target=socket_up_after,
                         args=(args.unix_socket, args.socket_up_after))
    x.daemon = True
    x.start()
    while True:
        try:
            p.wait(timeout=1)
            if SMART_SHUTDOWN:
                LOGGER.info("process: %i (smart) stopped" % pid)
            elif HARD_SHUTDOWN:
                pass
            else:
                LOGGER.warning("process: %i stopped for an unknown reason "
                               "=> let's shutdown the corresponding socket "
                               "before restart" % pid)
                socket_down(args.unix_socket, False, 10)
                # wait a little bit to be sure that all nginx workers
                # record that the socket is closed
                time.sleep(0.5)
            break
        except subprocess.TimeoutExpired:
            pass
        except Exception:
            LOGGER.exception("Exception during process waiting => exiting")
            break
        if SIG_SHUTDOWN is not None and args.timeout_after_signal > 0:
            now = datetime.datetime.now()
            delta = now - SIG_SHUTDOWN
            if delta.total_seconds() > args.timeout_after_signal:
                LOGGER.warning("sending SIGKILL to %i and its children", pid)
                kill_process_and_children(pid)
    try:
        os.remove(args.unix_socket)
    except Exception:
        pass


if __name__ == '__main__':
    main()
