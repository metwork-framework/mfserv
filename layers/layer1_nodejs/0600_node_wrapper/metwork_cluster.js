//
// metwork_cluster.js : Node Server with Workers
//
// Author: Frederic DURET meteo-france (2018)
//
// Purpose : Run Node Server With Workers
//
'use strict';

module.exports = function(setup) {

    var fs = require('fs');
    var cluster = require('cluster');
    var process = require('process');

    var parseArgs = function() {

        var argv = process.argv;
        var args = {
            workers: 1,
            loglevel: false,
            bind: false
        };

        var i;
        var match1;
        var match2;
        var match3;
        var arg;

        for (i=0; i<argv.length ;i++) {
            arg = argv[i];

            match1 = arg.match(/--workers=(\d+)/);
            match2 = arg.match(/--loglevel=(\w+)/);
            match3 = arg.match(/--bind=(unix:\/[\w^ \/\.]+)/)

            if (match1) {
                // workers
                args.workers = parseInt(match1[1]);
            }
            else if (match2) {
                // log-level
                args.loglevel = match2[1]
            }
            else if (match3) {
                // bind socket
                args.bind = match3[1]
            }
        }

        return args;
    };

    var args = parseArgs();

    global.__SOCKET_PATH = args['bind'].split("unix:")[1];
    global.__LOG_LEVEL = args['loglevel']
    global.__NB_WORKERS = args['workers']

    process.stdout.write("socket_path = " + global.__SOCKET_PATH + "\n");
    process.stdout.write("loglevel = " + global.__LOG_LEVEL +"\n");
    process.stdout.write("nb workers = " + global.__NB_WORKERS + "\n");

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
        process.stdout.write('serverCluster call shutdown\n');
        removeSocket();
        process.exit();
    };

    process.on('SIGINT', shutdown)
    process.on('SIGTERM', shutdown)
    process.on('SIGILL', shutdown)
    process.on('SIGFPE', shutdown)
    process.on('SIGSEGV', shutdown)

    var startWorker = function() {
        var worker = cluster.fork();
        process.stdout.write('CLUSTER: Worker ' + worker.id + ' started.');
    }

    var runServer = function(setup) {

        var app = require('metwork/metwork_server');

        try {
            if (typeof setup == "function") {
                 // call setup to configure app
                app(setup);
            }
            else {
                app();
            }
        }
        catch(e) {
            process.stderr.write("CLUSTER: Worker Error = " + e.message + "\n");
        }
    }

    if (global.__NB_WORKERS === 1 ) {
        runServer(setup);
    }
    else {
        if (cluster.isMaster) {
            // Master : prepare worker
            var i;
            if (typeof global.__NB_WORKERS == "number" && global.__NB_WORKERS > 0) {
                for (i=0; i<global.__NB_WORKERS ; i++ ) {
                    startWorker();
                }
            }
            else {
                require('os').cpus().forEach(function() {
                    startWorker();
                });
            }

            cluster.on('disconnect', function(worker) {
                process.stdout.write('CLUSTER: Worker ' + worker.id + ' disconnected from the cluster.\n');
            });

            // launch a new worker to keep NB_WORKERS
            cluster.on('exit', function(worker, code, signal) {
                process.stdout.write('CLUSTER: Worker ' + worker.id + ' died with exit code ' + code + '(' + signal + ')\n');
                startWorker();
            });
        }

        else {
            // Worker : run server
            runServer(setup);
        }
    }
}
