const express = require('express')
const process = require('process')

// read CLI arguments
var args = process.argv.slice(2)
const unix_socket_path = args[0]
const timeout = parseInt(args[1], 10)

// set the express app
const app = express()
app.get('/{{cookiecutter.name}}', function (req, res) {
      res.send('Hello World from {{cookiecutter.name}}!')
})

// call after_stop on exit
process.on('exit', function () {
    process.stdout.write("exiting !\n")
})

// listen to the unix socket, set timeout and print message
server = app.listen(unix_socket_path, function () {
    process.stdout.write("ok: process #" + process.pid + " is listening on " + unix_socket_path + "\n")
})
server.timeout = timeout * 1000
