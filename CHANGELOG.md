<a name=""></a>
# (unreleased)


### Bug Fixes

* add missing file for node plugin template ([cf66783](https://github.com/metwork-framework/mfserv/commit/cf66783))
* better plugin routing ([2f831d0](https://github.com/metwork-framework/mfserv/commit/2f831d0))
* don't start plugins during installation or uninstallation ([e5a667b](https://github.com/metwork-framework/mfserv/commit/e5a667b)), closes [#77](https://github.com/metwork-framework/mfserv/issues/77)
* fix lua lib paths ([048af60](https://github.com/metwork-framework/mfserv/commit/048af60)), closes [#34](https://github.com/metwork-framework/mfserv/issues/34)
* fix the node plugin template ([31a6318](https://github.com/metwork-framework/mfserv/commit/31a6318))
* fix timeout issues around conf_monitor restarts ([d4e21bc](https://github.com/metwork-framework/mfserv/commit/d4e21bc)), closes [#46](https://github.com/metwork-framework/mfserv/issues/46)
* handle NOTSET logging level value in nginx configuration ([bd8c35e](https://github.com/metwork-framework/mfserv/commit/bd8c35e))


### Features

* add a redis_service option ([3a7db68](https://github.com/metwork-framework/mfserv/commit/3a7db68)), closes [#5](https://github.com/metwork-framework/mfserv/issues/5)
* add an internal welcome plugin ([e2d41f2](https://github.com/metwork-framework/mfserv/commit/e2d41f2)), closes [#43](https://github.com/metwork-framework/mfserv/issues/43)
* add plugin app directory into lua_package_path ([6e940f0](https://github.com/metwork-framework/mfserv/commit/6e940f0))
* Add static plugin type and corresponding template ([50333a4](https://github.com/metwork-framework/mfserv/commit/50333a4)), closes [#51](https://github.com/metwork-framework/mfserv/issues/51)
* aiohttp upgrade (now 3.4.4) ([984c57f](https://github.com/metwork-framework/mfserv/commit/984c57f))
* better plugin crontab example ([841f3a5](https://github.com/metwork-framework/mfserv/commit/841f3a5))
* change default configuration ([2b2044d](https://github.com/metwork-framework/mfserv/commit/2b2044d))
* delete "blank only" files during bootstrap ([572fe38](https://github.com/metwork-framework/mfserv/commit/572fe38))
* filter gunicorn messages in stdout/stderr depending on their level ([5afcce0](https://github.com/metwork-framework/mfserv/commit/5afcce0)), closes [#47](https://github.com/metwork-framework/mfserv/issues/47)
* first version of inotify powered conf_monitor ([ca30691](https://github.com/metwork-framework/mfserv/commit/ca30691)), closes [metwork-framework/resources#25](https://github.com/metwork-framework/resources/issues/25)
* introduce an empty plugin type ([1ad9762](https://github.com/metwork-framework/mfserv/commit/1ad9762)), closes [#10](https://github.com/metwork-framework/mfserv/issues/10)
* provide a better plugin crontab bootstrap ([0509e1b](https://github.com/metwork-framework/mfserv/commit/0509e1b))
* provide a way for plugins to launch their own daemons ([79b7324](https://github.com/metwork-framework/mfserv/commit/79b7324)), closes [#39](https://github.com/metwork-framework/mfserv/issues/39)
* publish MFSERV environment variables into nginx environment ([624bad6](https://github.com/metwork-framework/mfserv/commit/624bad6))
* remove crontab support useless choice ([04331f1](https://github.com/metwork-framework/mfserv/commit/04331f1)), closes [#68](https://github.com/metwork-framework/mfserv/issues/68)


### BREAKING CHANGES

* no admin module configured by default



