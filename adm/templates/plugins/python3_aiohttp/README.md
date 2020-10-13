# README

## Introduction

This template is made for building Python3 webservices/websites using
the [AioHttp server](https://docs.aiohttp.org/en/stable/web.html) async framework.

## How to play with it?

By default, the main entry point is in `main/application.py` file.

??? question "Want to change everything?"
    The file `main/application.py` (you can change this in the plugin `config.ini` file)
    is called (through python interpreter) one time for each configured worker/process.

    It's called by the framework with two arguments as CLI:
        - a private unix socket to listen
        - a timeout (in seconds) for the webservice

    You can change everything you want but you have to keep this!

You will find a tutorial about this plugin at [https://metwork-framework.org/pub/metwork/continuous_integration/docs/integration/mfserv/870-tutorials/030_python3_aiohttp_plugin/](https://metwork-framework.org/pub/metwork/continuous_integration/docs/integration/mfserv/870-tutorials/020_python3_aiohttp_plugin/)
