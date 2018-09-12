//
// server.js : Node Server Worker
//
// Author: Frederic DURET meteo-france (2018)
//
// Purpose : Server Running in Workers
//           this module is required by ServerCluster
//
'use strict';

module.exports = function(setup) {

    var http = require('http');
    var fs = require('fs');
    var express = require('express');
    var process = require('process');
    var path = require('path');

    var app = express();

    if (typeof setup == "function") {
        setup(app);
    }

    var homedir = process.env['HOME'];

    // Express should work with socket :
    // 1- need to create an http server with socket
    // 2- export app with module.export

    var socketpath = global.__SOCKET_PATH;
    process.stdout.write("server socketpath = " + socketpath + "\n");

    var server = http.createServer(app).listen(socketpath);

    var removeSocket = function() {
        try {
            if (fs.existsSync(global.__SOCKET_PATH) === true) {
                fs.unlinkSync(global.__SOCKET_PATH);
            }
        }
        catch(e) {
            process.stderr.write(e.message);
        }
    };

    var shutdown = function() {
        process.stdout.write('server call shutdown\n');
        server.close();
        removeSocket();
        process.exit();
    };

    process.on('SIGINT', shutdown)
    process.on('SIGTERM', shutdown)
    process.on('SIGILL', shutdown)
    process.on('SIGFPE', shutdown)
    process.on('SIGSEGV', shutdown)

    server.on('error', function(e) {
        if (e.code == 'EADDRINUSE') {
            setTimeout(function() {
                removeSocket();
            }, 1000);
        }
    });
}
