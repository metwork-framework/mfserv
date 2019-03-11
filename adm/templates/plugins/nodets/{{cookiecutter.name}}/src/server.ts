'use strict';
import * as metwork from "metwork";
import * as path from "path";
import * as process from "process";

class ServerController {

 setup(app) {

 // app is the Express application already defined
 let plugin_name = "{{cookiecutter.name}}";
 let base_route = "/" + plugin_name;
 app.get(base_route, function(req, res, next) {
 res.send("Bonjour typescript on metwork !");
 });

}

run() {
 metwork(this.setup)
}

}

const main = new ServerController();
main.run();
