
# Tuning, Monitoring and Dashboard
.. index:: tuning
## Tuning
.. index:: number of processes
### Number of processes

A plugin is able to run multiple processes simultaneously.

You may change the number of process allocated for each step of each plugin. In order to configure this number of processes, add or update the `numprocesses` parameter in the [step....] section of the `config.ini` plugin configuration file, e.g.:
```cfg
# Number of process allocate to the step. Default value is 1
numprocesses = 3
```
.. index:: limits, resource
### Resource limits

You are able to control resource limits for each app workers of a plugin by setting the following parameters in the `[app....]` section of the `config.ini` plugin configuration file, e.g.:

```cfg
# resource limit for each app worker
# rlimit_as => maximum area (in bytes) of address space which may be taken by the worker.
# rlimit_nofile => maximum number of open file descriptors for the current worker.
# rlimit_stack => maximum size (in bytes) of the call stack for the current worker.
#     This only affects the stack of the main thread in a multi-threaded worker.
# rlimit_core => maximum size (in bytes) of a core file that the current worker can create.
# rlimit_fsize =>  maximum size of a file which the worker may create.
# (empty value means no limit)
rlimit_as = 1000000000
rlimit_nofile = 1000
rlimit_stack = 10000000
rlimit_core = 100000
rlimit_fsize = 100000000
```

For further information about Linux resource limits, check [Linux documentation](http://man7.org/linux/man-pages/man2/setrlimit.2.html).

.. index:: Nginx, Request body size limit, Nginx workers, Nginx timeout, Nginx rate limiting, Rate limiting, extra_nginx_conf_filename
### Nginx tuning an rate limiting

You are able to act on Nginx tuning parameters: refer to the `[nginx]` section of the `config/config.ini` file of the MFSERV module (in the root directory of the MFSERV user).

Nginx server allows you to limit the amount of HTTP requests a user can make in a given period of time.

You can easily implement this feature by setting your plugin configuration for this purpose. 

In order to understand the 'Nginx Rate limiting' and learn how to implement it in your plugin, read this MetWork [Implement a MFSERV plugin with rate limiting](https://medium.com/metwork-framework/implement-a-mfserv-plugin-with-rate-limiting-fd38d2d5ccd8).

### Advanced settings

Some advanced settings are available for each application. Check the `[app....]` section of the `config.ini` plugin configuration file, e.g.: `extra_nginx_conf_filename`, `extra_nginx_conf_static_filename`


### Miscellaneous

You are able to act on others tuning parameters for each app of a plugin.

```cfg 

# If set then the process will be restarted sometime after max_age and
# max_age + random(0, max_age) seconds.
# 0 => disable this feature
# Note: the feature is automatically disabled if workers=1
# Note: 60 seconds is a minimum
max_age = 3600

# The number of seconds to wait for a process to terminate gracefully before killing it.
# When stopping a worker process, we first send it a SIGTERM.
# A worker may catch this signal to perform clean up operations before exiting
# like finishing to reply to already accepted requests.
# If the worker is still active after graceful_timeout seconds, we send it a
# SIGKILL signal. It is not possible to catch SIGKILL signals so the worker will stop.
graceful_timeout = 30
```

.. index:: monitoring, MFADMIN, dashboard
## Monitoring and Dashboards

.. seealso::
    | :doc:`MFADMIN Documentation <mfadmin:index>`
    | :doc:`mfadmin:mfadmin_monitoring_plugins`.

### Monitor a plugin
Through Metwork MFADMIN module, you may monitor the MFSERV plugins: refer to the :doc:`related MFADMIN topic <mfadmin:mfadmin_monitoring_plugins>`.

.. index:: Grafana dashboards, Kibana dashboards
### Dashboards
:index:`Time-series dashboards` are available from :ref:`MFADMIN Grafana GUI Interface <mfadmin:mfadmin_monitoring_plugins:Grafana Time-series dashboards>`.

:index:`Logs dashboards`, i.e. [mflog](https://github.com/metwork-framework/mflog) logs and [Nginx](https://www.nginx.com/) access logs are available from :ref:`MFADMIN Kibana GUI Interface <mfadmin:mfadmin_monitoring_plugins:Kibana dashboards>`.

You may also create your own dashboards: refer to the :ref:`MFADMIN topic <mfadmin:mfadmin_miscellaneous:Create specific dashboards>` documentation.

### Useful links and Tips

Check :ref:`MFADMIN tips <mfadmin:mfadmin_miscellaneous:Useful links and Tips>` documentation.

<!--
Intentional comment to prevent m2r from generating bad rst statements when the file ends with a block .. xxx ::
-->
