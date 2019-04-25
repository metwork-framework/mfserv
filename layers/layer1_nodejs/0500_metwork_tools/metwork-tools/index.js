const process = require('process')
const fs = require('fs')
const http = require('http')
const base64url = require('base64url')

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

exports.before_start = before_start
exports.before_stop = before_stop
exports.after_start = after_start
exports.after_stop = after_stop
