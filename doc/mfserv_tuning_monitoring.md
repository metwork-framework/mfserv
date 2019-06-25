
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

You are able to control resource limits for each step of a plugin by setting the following parameters in the [step....] section of the `config.ini` plugin configuration file, e.g.:

```cfg
# resource limit for each step process
# rlimit_as => maximum area (in bytes) of address space which may be taken by the process.
# rlimit_nofile => maximum number of open file descriptors for the current process.
# rlimit_stack => maximum size (in bytes) of the call stack for the current process.
#     This only affects the stack of the main thread in a multi-threaded process.
# rlimit_core => maximum size (in bytes) of a core file that the current process can create.
# rlimit_fsize =>  maximum size of a file which the process may create.
# (empty value means no limit)
rlimit_as = 1000000000
rlimit_nofile = 1000
rlimit_nproc = 100
rlimit_stack = 10000000
rlimit_core = 10000000
rlimit_fsize = 100000000
```

For further information about Linux resource limits, check [Linux documentation](http://man7.org/linux/man-pages/man2/setrlimit.2.html).

### Miscellaneous

You are able to act on others tuning parameters for each step of a plugin.

```cfg 
# The number of seconds to wait for a step to terminate gracefully
# before killing it. When stopping a process, we first send it a TERM signal.
# A step may catch this signal to perform clean up operations before exiting.
# If the worker is still active after graceful_timeout seconds, we send it a
# KILL signal. It is not possible to catch a KILL signal so the worker will stop.
# If you use the standard Acquisition framework to implement your step, the
# TERM signal is handled like this: "we don't process files anymore but we
# try to end with the current processed file before stopping". So the
# graceful_timeout must by greater than the maximum processing time of one file.
# Default value is 600 seconds
graceful_timeout = 600

# If set then the step will be restarted sometime after max_age seconds.
# Default value is 310 seconds
max_age = 310

# If max_age is set then the step will live between max_age and
# max_age + random(0, max_age_variance) seconds.
# This avoids restarting all processes for a step at once.
# Default value is 300 seconds
max_age_variance = 300
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
