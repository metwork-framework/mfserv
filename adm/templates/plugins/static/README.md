# README

## Introduction

This template is made for serving static files with the [nginx](https://nginx.org/) webserver.

## How to play with it?

By default, just put your static files in the `main/` subdirectory of the plugin.

`nginx` will serve them through:

- `http://{host}:{port}/{plugin_name}/main/...` (and)
- `http://{host}:{port}/{plugin_name}/...`

Of course, you can add several apps (like `main` in the default configuration) or
configure extra things like virtualdomain based routing. See `config.ini` file for options.
