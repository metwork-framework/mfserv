# README

## Introduction

This template is made for building [php] applications
TODO : more explanations

## How to play with it?

TODO : more explanations
the warnings below may be not relevant

!!! warning
    Your code is directly integrated into the `mfserv` nginx server (at module level). So you can break up the whole `mfserv` module with your plugin.

!!! warning
    As we are at very low level, the autorestart feature does not work in all cases. Of course, you can reload the mfserv running instance with `mfserv.stop ; mfserv.start` but it's a little bit slow. So in this particular use case, you can use `circusctl restart nginx` to force reload in all cases.

!!! tip
    As you can break the nginx configuration, we recommend you to keep a `tail -f ${MODULE_RUNTIME_HOME}/log/nginx_error.log` in a terminal to see some errors. And also, please execute frequently `mfserv.status`.
