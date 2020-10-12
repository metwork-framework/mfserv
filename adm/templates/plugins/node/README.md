# README

## Introduction

This template is made for building [NodeJS](https://nodejs.org) plugins.

!!! warning
    To use this template, you need the `metwork-mfext-layer-nodejs` `mfext` extra layer.

    Please refer to the [installation guide](../../../../100-installation_guide) if you don't
    know how to do that.

With this plugin template, you will be able to host one `NodeJS` app and its
`node_modules`. For technical reasons, you can't host several `NodeJS` apps under
the same plugin (like with most of Python templates).

## How to play with it?

By default, the plugin will launch several `node` processes (each process will listen
to a dedicated unix socket load balanced behind `nginx` webserver). This is a "production ready"
installation and you don't need any additional cluster or processes manager.

You can change the `node` command in `cmd_and_args` configuration option. By default,
we launch a minimal `server.js` file (built with `express` library) but of course you can change this.

In the plugin directory, you will find a `package.json` to manage your `node_modules` dependencies (dedicated to your plugin) with `npm` tool in a standard way.

## Tutorial

Let's create a plugin based on the Node plugin template. We will called it **foo_nodejs**.

First, **bootstrap** the plugin with the command:
```bash
bootstrap_plugin.py create --template=node foo_nodejs
```

Once you have entered this command, you will be asked to fill in some fields to configure and customize your plugin: for now, press `[ENTER]` to set the default values, you will be able to modify your plugin configuration anytime later.

The plugin is created in the current directory, inside the directory named `foo_nodejs`.

Check this directory, it contains few files, including: 

- **foo_nodejs** directory: the node.js scripts for your project. Its name is the package name you’ll need to use to import anything inside it. This directory contains:
    - **server.js**: An entry-point for Node.js web servers to serve your project.
- **package.json** file: A kind of a manifest for your project. It can do a lot of things, completely unrelated. It’s a central repository of configuration for tools.


Let's now **build** the plugin by entering the command from the `foo_nodejs` plugin directory:

```bash
make develop
```
This command will download and install needed Javascript node modules.

A **package-lock.json** file is automatically generated for any operations where npm modifies either the node_modules tree, or **package.json**.
It describes the exact tree that was generated, such that subsequent installs are able to generate identical trees, regardless of intermediate dependency updates.and some other dependencies.

You may also check the **node_modules** directory.

!!! note "What is the difference between package.json and package-lock.json ?  "
     - **package-lock.json**: records the exact version of each installed package which allows you to re-install them. Future installs will be able to build an identical dependency tree. ...
     - **package.json**: records the minimum version you app needs.

!!! important "**package-lock.json** is intended to be checked into source control, as Git. You should commit this file."

!!! important
    - If you are behind a proxy, you have to set `http_proxy` and `https_proxy` environment variables in order to be able to download any Python package you may need.
    - You may also need to disable your Linux firewall:
    ```
          systemctl status firewalld
          systemctl stop firewalld.service
          systemctl disable firewalld
    ```


Check the `foo_nodejs/server.js` script. It is a basic [Express](https://expressjs.com/) application (app) which starts a server and listens for connection.
This application responds with `Hello World from foo_nodejs!` for requests to the homepage. For every other path, it will respond with an `HTTP 404 Not Found`.


Express application uses a callback function whose parameters are request and response objects:
```js

app.get('/foo_nodejs', function (req, res) {
      res.send('Hello World from foo_nodejs!')
})

```

Now, you can check your application works by invoking the following URL: http://localhost:18868/foo_nodejs (you may replace localhost by your remote host if needed). A HTML page must display `Hello World from foo_nodejs!`.

We will extend our "Hello World!" application to handle more types of HTTP requests. Edit the the `foo_nodejs/server.js` script and add the following lines:
```js
// This responds a POST request for the /foo_nodejs home url
app.post('/foo_nodejs', function (req, res) {
   res.send('Hello World foo_nodejs from a POST request');
})

// This responds a GET request for wxy, waxy, w1234bxy, and so on...
app.get('/foo_nodejs/w*xy', function(req, res) {
   res.send('Page Pattern Match foo_nodejs');
})

// This responds a DELETE request for the /foo_nodejs/del_user url.
app.delete('/foo_nodejs/del_user', function (req, res) {
   res.send('Hello World foo_nodejs from a DELETE request');

})

// This responds a GET request for the /foo_nodejs/list_user url.
app.get('/foo_nodejs/list_user', function (req, res) {
   res.send('Page listing foo_nodejs');
})

```

Build the plugin with `make develop` command.

Check your application works by invoking the relevant URLs you added.

!!! info "See also [Configure a Metwork module](../../../../300-configuration_guide/#2-how-to-configure-a-metwork-module)"

