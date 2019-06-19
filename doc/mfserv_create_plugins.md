
# How to create custom plugins
In order to use MFSERV and create your custom plugin, one of the first thing, you have to load the "MFSERV environment" in your shell session. There are several ways to do that: check :doc:`the related documentation <mfserv_load_env>`.

Plugins can be custom made quickly and easily by using existing templates. Making plugins with mfserv is as simple as editing a configuration file. You just have to create a plugin using an existing template, then edit the configuration file so that the plugin fulfills your need, and finally release the plugin. 

Predefined templates are available in order to create your plugin (see [Plugin templates section](#plugin-templates)).

## Create and customize the plugin
To create a plugin, simply **run the command**.
```bash
bootstrap_plugin.py create --template={TEMPLATE} {PLUGIN_NAME}
```
where `{TEMPLATE}` is the tmplate you want to use and `{PLUGIN_NAME}` the name of ypur plugin.

Notice if you omit the `--template` argument, [the default template](#id1) will be used.

Once you have entered this command, you will be asked to fill in some fields to configurate and customize your plugin. 
You can also configure your plugin anytime by **editing the** `mfserv/{PLUGIN_NAME}/config.ini` **config file**. For more details about each field, check the documentation in the `mfserv/{PLUGIN_NAME}/config.ini` file.

.. todo:: to be updated

<!-- :doc:`../mfserv_quick_start`  and :doc:`../mfserv_additional_tutorials` may help you to create your plugin.
-->

.. index:: plugin templates, templates
## Plugin templates

Predefined templates are available in order to create your plugin.

The following command allows to display the available templates:
```bash
bootstrap_plugin.py list
```

```
List of availabel plugin templates:
     * default
     * empty
     * node
     * django
     * static
     * mediation     
```



### The `default` template
.. todo:: to be completed

### The `empty` template
.. todo:: to be completed

### The `node` template
.. todo:: to be completed

### The `django` template
.. todo:: to be completed

### The `static` template
.. todo:: to be completed

### The `mediation` template
.. todo:: to be completed