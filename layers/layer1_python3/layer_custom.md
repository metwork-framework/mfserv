{% extends "layer.md" %}

{% block overview %}
    
The `layer1_python3` layer includes Python3 MFSERV packages.

.. index:: middleware
.. _mfserv_aiohttp_middleware:
For :index:`asyncio` and :index:`aiohttp` python web server implementation, it also provides mechanism for customizing request handlers via [middleware](https://docs.aiohttp.org/en/stable/web_advanced.html#aiohttp-web-middlewares).
Currently, this layer provides :
- a `timeout` middleware which returns a context manager that cancels the request on timeout expiring (see [asyncio-compatible timeout context manager documentation](https://pypi.org/project/async_timeout))

.. index:: request ID, X-Request-ID
.. _mfserv_mflog_middleware:
- a `log` middleware which adds into the log, the unique request ID from the HTTP header `X-Request-ID` attributes.

.. seealso::
    | :ref:`mfserv_miscellaneous:Disable request ID to be appeared in the logs`
    | :ref:`mfserv_miscellaneous:Disable middleware (asyncio, aiohttp plugins)` and :ref:`mfserv_tutorials:aiohttp python plugin` tutorial

The `layer1_python3` layer is included in the `.layerapi2_dependencies` file of the plugin when you choose python3 during the :ref:`creation of a plugin <mfserv_create_plugins:Create and customize the plugin>`.

You may also manually include this [dependencies (i.e. Label)](#label) in the `.layerapi2_dependencies` file.

{% endblock %}
