const express = require('express')
const process = require('process')
const metwork_tools = require('metwork-tools')

// read CLI arguments
var args = process.argv.slice(2)
const unix_socket_path = args[0]
const timeout = parseInt(args[1], 10)

// call metwork before_start
metwork_tools.before_start(unix_socket_path)

// set the express app
const app = express()
app.get('/{{cookiecutter.name}}', function (req, res) {
      res.send('Hello World {{cookiecutter.name}}!')
})

// call before_stop on SIGTERM
process.on('SIGTERM', function () {
    metwork_tools.before_stop(unix_socket_path)
})

// call after_stop on exit
process.on('exit', function () {
    metwork_tools.after_stop(unix_socket_path)
})

// listen to the unix socket, set timeout and call after_start
server = app.listen(unix_socket_path, function () {
    metwork_tools.after_start(unix_socket_path)
})
server.timeout = timeout * 1000
