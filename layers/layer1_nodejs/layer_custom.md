{% extends "layer.md" %}

{% block overview %}

The `layer1_nodejs` layer includes the :doc:`Node.js <mfext:layer_nodejs>` cross-platform JavaScript runtime environment.

It is included in the `.layerapi2_dependencies` file of the plugin when you create a web server with the :ref:`node template <mfserv_create_plugins_the_node_template>` during the :ref:`creation of a plugin <mfserv_create_plugins:Create and customize the plugin>`.

You may also manually include this [dependencies (i.e. Label)](#label) in the `.layerapi2_dependencies` file.

This layer also include tools to neatly start and stop the :doc:`Node.js <mfext:layer_nodejs>` web server (see `/opt/metwork-mfserv/opt/nodejs/lib/node_modules/metwork-tools/index.js`).


.. seealso::
    | :ref:`mfserv_miscellaneous:Disable request ID to be appeared in the logs`
    | :ref:`mfserv_tutorials:Node.js plugin` tutorial


{% endblock %}
