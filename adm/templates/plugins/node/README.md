# README

## Introduction

This template is made for building [NodeJS](https://nodejs.org) plugins.

!!! warning
    To use this template, you need the `metwork-mfext-layer-nodejs` `mfext` extra layer.

    Please refer to the [installation guide]({{installation_guide}}) if you don't
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
