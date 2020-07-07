# README

## Introduction

This template is made for building [OpenResty](https://openresty.org/) applications
(written in Lua) directly integrated into the [nginx](https://nginx.org/) webserver.

## How to play with it?

By default, you will find these special files:

- `nginx_extra_http.conf`: nginx configuration fragment injected in the `http` nginx configuration section
- `nginx_extra_server.conf`: nginx configuration fragment injected in the `server` nginx configuration section
- `init_worker_by_lua.lua`: custom lua code to execute during worker initialization (see [openresty init_by_lua doc](https://github.com/openresty/lua-nginx-module#init_by_lua))
- `content_by_lua.lua`: file loaded (by default) in `nginx_extra_server.conf` to provide an example content

!!! warning
    Your code is directly integrated into the `mfserv` nginx server (at module level). So you can break up the whole `mfserv` module with your plugin.

!!! warning
    As we are at very low level, the autorestart feature does not work in all cases. Of course, you can reload the mfserv running instance with `mfserv.stop ; mfserv.start` but it’s a little bit slow. So in this particular use case, you can use `circusctl restart nginx` to force reload in all cases.

!!! tip
    As you can break the nginx configuration, we recommend you to keep a `tail -f ${MODULE_RUNTIME_HOME}/log/nginx_error.log` in a terminal to see some errors. And also, please execute frequently `mfserv.status`.
