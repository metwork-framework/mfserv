# README

## Introduction

This template is made for building Python3 async webservices/websites using
[ASGI](https://asgi.readthedocs.io/) interface and the [Uvicorn](https://www.uvicorn.org/)
server.

## How to play with it?

By default, the main entry point is in `main/application.py` file (`app()` function).

With this template, you have a raw (without framework) implementation. But of course,
you can use the [ASGI](https://asgi.readthedocs.io/) framework you want (Django/Channels,
FastAPI, Quart, Starlette...).

??? question "change the entry-point?"
    The ASGI entry point is by default the `app()` function in `main/application.py` file.
    But you can change this on the `_cmd_and_args` option in your plugin `config.ini`
