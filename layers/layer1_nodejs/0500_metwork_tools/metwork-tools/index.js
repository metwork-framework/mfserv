const process = require('process')
const os = require('os')
const util = require('util')
const syslog = require("syslog-client");

const LOG_LEVELS = {
    DEBUG: 1,
    INFO: 2,
    WARNING: 3,
    ERROR: 4,
    CRITICAL: 5
}
const LOG_MINIMAL_LEVEL = LOG_LEVELS[process.env.MFLOG_MINIMAL_LEVEL]
const LOG_SYSLOG_MINIMAL_LEVEL = LOG_LEVELS[process.env.MFLOG_SYSLOG_MINIMAL_LEVEL]
const LOG_SYSLOG_ADDRESS = process.env.MFLOG_SYSLOG_ADDRESS || "null"
const PID = process.pid
const PLUGIN = process.env.MFSERV_CURRENT_PLUGIN_NAME || "unknown"


function _get_console_args(level, data, ...args) {
    var new_args = [];
    var d = new Date();
    new_args.push(d.toISOString());
    switch (level) {
        case 1:
            new_args.push("   [DEBUG]")
            break
        case 2:
            new_args.push("    [INFO]")
            break
        case 3:
            new_args.push(" [WARNING]")
            break
        case 4:
            new_args.push("   [ERROR]")
            break
        case 5:
            new_args.push("[CRITICAL]")
            break
    }
    new_args.push("(" + PLUGIN + "#" + process.pid + ")")
    new_args.push(data);
    for( var i = 0; i < args.length; i++ ) {
        new_args.push(args[i]);
    }
    return new_args;
}

function _console_log(level, data, ...args) {
    if (level < LOG_MINIMAL_LEVEL) {
        return
    }
    var new_args = _get_console_args(level, data, ...args)
    if (level <= 2) {
        console.log(...new_args)
    } else {
        console.error(...new_args)
    }
}

function _json_log(level, data, ...args) {
    if (level < LOG_SYSLOG_MINIMAL_LEVEL) {
        return
    }
    if (LOG_SYSLOG_ADDRESS == "null") {
        return
    }
    if (typeof _json_log.syslog_client_instance == 'undefined') {
        var options = {
            syslogHostname: os.hostname(),
            transport: syslog.Transport.Udp,
            port: parseInt(LOG_SYSLOG_ADDRESS.split(":")[1])
        }
        _json_log.syslog_client_instance = syslog.createClient(LOG_SYSLOG_ADDRESS.split(":")[0], options)
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
    _json_log.syslog_client_instance.log(JSON.stringify(record))
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

exports.console_debug = console_debug
exports.console_info = console_info
exports.console_warn = console_warn
exports.console_error = console_error
exports.console_critical = console_critical
