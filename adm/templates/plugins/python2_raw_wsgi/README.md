# README

## Introduction

This template is made for building Python2 webservices/websites using
the [WSGI interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface).

Every framework made for `WSGI` should work with this plugin. Or, of course,
you can use plain `WSGI` protocol by hand.

## How to play with it?

By default, the main entry point is in `main/wsgi.py` file.

Note that an interactive debugger is automatically configured if you use `debug=1`
in your plugin `config.ini` file.

??? question "Want to change everything?"
    The file `main/wsgi.py` must define a `WSGI` `application()` function (you can change this in the plugin `config.ini` file in the `_cmd_and_args` key)
