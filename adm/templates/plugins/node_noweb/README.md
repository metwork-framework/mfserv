# README

## Introduction

This template is made for hosting [NodeJS](https://nodejs.org) applications
without a web part (see the `node` plugin template if you need a web app).

!!! warning
    To use this template, you need the `metwork-mfext-layer-nodejs` `mfext` extra layer.

    Please refer to the [installation guide]({{installation_guide}}) if you don't
    know how to do that.

## How to play with it?

By default, the plugin will launch nothing.

You can install [NodeJS](https://nodejs.org) things with `npm` or with `package.json` (and `make` command). As there is no automatically configured web part, you have to launch your app by yourself of you can also set up an extra daemon with `config.ini` (to have a monitored automatic launch).
