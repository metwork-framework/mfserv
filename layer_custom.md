{% extends "layer.md" %}

{% block overview %}
This is the `root` layer of the MFDATA module.

This layer mainly includes core libraries and utilities like :

- :doc:`layerapi2 <mfext:layerapi2>` library and utilities which manage the layer system
- wrappers (`python3`, `python`...)
- (and some other documented below)

The `root` layer is loaded by default and does not depend on another layer. This
is the layer dependencies root.

## Special focus on python wrappers

.. _layer_root_python3_wrapper:

### python3 wrapper

The `python3` wrapper is available in `${MFEXT_HOME}/bin`. It executes
a python3 interpreter with following layers loaded :

- `python3_core@mfext`
- `python3@mfext` (if installed)
- `python3@{current_module}` (if installed)

So, if you want to execute a python3 script without any question about currently
loaded layers, this is the way to go.

For example:

```python

#!/usr/bin/env python3

print("this code will be always executed in python3 environment")
print("(thanks to the above python3 shebang)")
```

or

```bash
python3 /path/to/a/python3/script.py
```

### python wrapper

The `python` wrapper is available in `${MFEXT_HOME}/bin`. It works exactly
as the two above wrappers. But the major python version is selected with
the `METWORK_PYTHON_MODE` environment variable.

{% endblock %}
