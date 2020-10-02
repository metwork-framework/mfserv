# MFSERV Log

## Default logs files
MFSERV produces logs files stored in the `log` directory of the MFSERV root directory.

Logs parameters as log retention, log level are configured in the [log] section of the `config/config.ini` file in the MFSERV root directory. Check this file for further details.

Each MFSERV plugin has its own logs files:

- app_{plugin_name}_{app_name}_{worker`n`}.stdout
- app_{plugin_name}_{app_name}_{worker`n`}.stderr

There is one log file per worker. For instance, if the workers setting in the plugin configuration file is `4`, you will find 4 `.stdout` log files and 4 `.stderr` log files for your plugin.

The `.sddout` file contains `INFO` and `DEBUG` level logs. The `.stderr` file contains `WARNING`, `ERROR` and `CRITICAL`.

When you want to log data from a MFSERV plugin, you just have to call one of the implemented methods:

- Python plugin with [mflog](https://github.com/metwork-framework/mflog):

    ```python
    
    from mflog import get_logger
    logger = get_logger("myapp")
    
    ...
    logger.info(...)
    logger.debug(...)
    logger.warning(...)
    logger.error(...)
    logger.critical(...)
    logger.exception(...)
    ```

- Node.js plugin:

    ```js
    
    console.log(...)
    console.info(...)
    console.warn(...)
    console.error(...)
    
    ```    
or     
    ```javascript
    
    
    const process = require('process')
    
    process.stdout.write(...)
    process.stderr.write(...)
    
    ```

.. seealso::
    :ref:`mfadmin:mfadmin_miscellaneous:Exporting logs`

## Custom logs files

### Classic Python logger
You may want to create your own additional logs files to log specific data and store it in the MFSERV `log` directory. In order to do this, check this :ref:`example <mfdata:mfdata_log:Classic Python logger>`.

### Metwork MFLOG logger

You may also use the 'structured' Metwork MFLOG logger. Check [Metwork MFLOG](https://github.com/metwork-framework/mflog) for more details and example.
