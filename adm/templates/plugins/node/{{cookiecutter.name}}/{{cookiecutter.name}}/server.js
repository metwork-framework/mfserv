const process = require('process')
const express = require('express')
const fs = require('fs')
const app = express()

app.get('/{{cookiecutter.name}}', function (req, res) {
      res.send('Hello World {{cookiecutter.name}}!')
})

var args = process.argv.slice(2);
if (fs.existsSync(args[0]) === true) {
    try {
        fs.unlinkSync(args[0])
    } catch(e) {
        process.stderr.write("can't unlink: " + args[0] + " => exiting")
        process.exit(1)
    }
}
app.listen(args[0], function () {
    process.stdout.write("good: process #" + process.pid + " is listening on " + args[0])
})
