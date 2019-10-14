const process = require('process')
const fs = require('fs')
const http = require('http')
const base64url = require('base64url')
const fsext = require('fs-ext')
const util = require('util')

const LOG_LEVELS = {
    DEBUG: 1,
    INFO: 2,
    WARNING: 3,
    ERROR: 4,
    CRITICAL: 5
}
const LOG_MINIMAL_LEVEL = LOG_LEVELS[process.env.MFSERV_LOG_MINIMAL_LEVEL]
const LOG_JSON_MINIMAL_LEVEL = LOG_LEVELS[process.env.MFSERV_LOG_JSON_MINIMAL_LEVEL]
const LOG_JSON_FILE = process.env.MFSERV_LOG_JSON_FILE || "null"
const PID = process.pid
const PLUGIN = process.env.MFSERV_CURRENT_PLUGIN_NAME || "unknown"

function before_start(unix_socket_path) {
    if (fs.existsSync(unix_socket_path) === true) {
        try {
            fs.unlinkSync(unix_socket_path)
        } catch(e) {
            process.stderr.write("can't unlink: " + unix_socket_path + " => exiting\n")
            process.exit(1)
        }
    }
}

function after_start(unix_socket_path) {
    var req = http.get("http://127.0.0.1:" + process.env.MFSERV_NGINX_PORT + "/__socket_up/" + base64url(unix_socket_path), function(res) {
        res.resume()
        process.stdout.write("ok: process #" + process.pid + " is listening on " + unix_socket_path + "\n")
    })
    req.on('error', function(e) {
        // maybe we are in starting mode and nginx is not started yet
        process.stdout.write("ok: process #" + process.pid + " is listening on " + unix_socket_path + "\n")
    })
}

function before_stop(unix_socket_path) {
    process.stdout.write("SIGTERM catched => calling close\n")
    var req = http.get("http://127.0.0.1:" + process.env.MFSERV_NGINX_PORT + "/__socket_down/" + base64url(unix_socket_path) + "?wait=1", function(res) {
        res.resume()
        server.close()
    })
    req.on('error', function(e) {
        // nginx is not available ?, we are maybe in stopping mode
        server.close()
    })
}

function after_stop(unix_socket_path) {
    process.stdout.write("exiting !\n")
    if (fs.existsSync(unix_socket_path) === true) {
        try {
            fs.unlinkSync(unix_socket_path)
        } catch(e) {
            process.stderr.write("can't unlink: " + unix_socket_path + " => exiting\n")
        }
    }
}

function _console_log(level, data, ...args) {
    if (level < LOG_MINIMAL_LEVEL) {
        return
    }
    if (level <= 2) {
        console.log(data, ...args)
    } else {
        console.error(data, ...args)
    }
}

function _json_lock_log_then_close(fd, record) {
    fsext.flock(fd, 'exnb', function(err4) {
        if (err4) {
            if (err4.code == "EAGAIN") {
                setTimeout(function() {
                    _json_lock_log_then_close(fd, record)
                }, 1)
                return
            }
            if (err4.code == "EWOULDBLOCK") {
                setTimeout(function() {
                    _json_lock_log_then_close(fd, record)
                }, 1)
                return
            }
            console.error("WARNING: can't get lock to %s with error: %s", LOG_JSON_FILE, err4.message)
            return
        }
        fs.write(fd, JSON.stringify(record) + "\n", function(err, bytesWritten, str) {
            if (err) {
                console.error("WARNING: can't log to %s with error: %s", LOG_JSON_FILE, err.message)
            }
            fs.close(fd, function(err3) {
                if (err3) {
                    console.error("WARNING: can't close: %s with message: %s", LOG_JSON_FILE, err3.message)
                }
            })
        })
    })
}

function _json_log(level, data, ...args) {
    if (level < LOG_JSON_MINIMAL_LEVEL) {
        return
    }
    if (LOG_JSON_FILE == "null") {
        return
    }
    fs.open(LOG_JSON_FILE, 'a', (err, fd) => {
        if (err) {
            console.error("can't log to %s with error: %s", LOG_JSON_FILE, err.message)
            return
        }
        var timestamp = (new Date()).toISOString()
        var level_str = "unknown"
        switch (level) {
            case 1:
                level_str = "debug"
                break
            case 2:
                level_str = "info"
                break
            case 3:
                level_str = "warning"
                break
            case 4:
                level_str = "error"
                break
            case 5:
                level_str = "critical"
                break
        }
        var record = {
            name: "default",
            event: util.format(data, ...args),
            level: level_str,
            pid: PID,
            plugin: PLUGIN,
            timestamp: timestamp
        }
        _json_lock_log_then_close(fd, record)
    })
}

function console_debug(data, ...args) {
    _console_log(1, data, ...args)
    _json_log(1, data, ...args)
}

function console_info(data, ...args) {
    _console_log(2, data, ...args)
    _json_log(2, data, ...args)
}

function console_warn(data, ...args) {
    _console_log(3, data, ...args)
    _json_log(3, data, ...args)
}

function console_error(data, ...args) {
    _console_log(4, data, ...args)
    _json_log(4, data, ...args)
}

function console_critical(data, ...args) {
    _console_log(5, data, ...args)
    _json_log(5, data, ...args)
}

exports.before_start = before_start
exports.before_stop = before_stop
exports.after_start = after_start
exports.after_stop = after_stop
exports.console_debug = console_debug
exports.console_info = console_info
exports.console_warn = console_warn
exports.console_error = console_error
exports.console_critical = console_critical
