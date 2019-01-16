#!/usr/bin/env python3

import os
import time
from mflog import getLogger
from mfutil import BashWrapper, BashWrapperOrRaise
from conf_monitor import ConfMonitorRunner, md5sumfile

LOGGER = getLogger("conf_monitor")
MODULE_RUNTIME_HOME = os.environ['MODULE_RUNTIME_HOME']


def make_new_nginx_conf():
    new_nginx_conf = "%s/tmp/tmp_nginx_conf2" % MODULE_RUNTIME_HOME
    cmd = "_make_nginx_conf >%s" % new_nginx_conf
    BashWrapperOrRaise(cmd)
    return (new_nginx_conf, md5sumfile(new_nginx_conf))


def get_old_nginx_conf():
    old_nginx_conf = "%s/tmp/config_auto/nginx.conf" % MODULE_RUNTIME_HOME
    return (old_nginx_conf, md5sumfile(old_nginx_conf))


def restart_nginx(old_conf, new_conf):
    os.unlink(old_conf)
    os.rename(new_conf, old_conf)
    x = BashWrapper("_nginx.reload")
    if not x:
        LOGGER.warning(x)


class MfservConfMonitorRunner(ConfMonitorRunner):

    def manage_nginx(self):
        new_conf, new_md5 = make_new_nginx_conf()
        old_conf, old_md5 = get_old_nginx_conf()
        if new_md5 != old_md5:
            LOGGER.info("nginx conf changed => restart nginx...")
            restart_nginx(old_conf, new_conf)
            time.sleep(3)
        else:
            LOGGER.debug("nginx conf didn't change")
        return True

    def handle_event(self):
        return self.manage_circus() and self.manage_nginx() and \
            self.manage_crontab()


if __name__ == '__main__':
    x = MfservConfMonitorRunner()
    x.run()
