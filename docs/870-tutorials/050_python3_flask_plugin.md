# Python3_flask plugin tutorial

Let's create a plugin based on the [python3_flask plugin template](../../850-reference/plugin_templates/python3_flask/100-intro/). We will called it **foo_nodejs**.

First, **bootstrap** the plugin with the command:
```bash
bootstrap_plugin.py create --template=python3_flask foo_flask
```

Once you have entered this command, you will be asked to fill in some fields to configure and customize your plugin: for now, press `[ENTER]` to set the default values, you will be able to modify your plugin configuration anytime later.

The plugin is created in the current directory, inside the directory named `foo_flask`.

Check this directory, it contains few files, including:

- **main** directory: the Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it. This directory contains:
    - **\_\_init\_\_.py**: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
    - **wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project.


Let's now **build** the plugin by entering the command from the `foo_django` plugin directory:

```bash
make develop
```

This command will download and install Flaks framework and some other dependencies. It will also create a Flask project with an "Hello World!" application.

!!! important

    - if you are behind a proxy, you have to set `http_proxy` and `https_proxy` environment variables in order to be able to download any Python package you may need.
    - you may also need to disable your Linux firewall:
    ```
          systemctl status firewalld
          systemctl stop firewalld.service
          systemctl disable firewalld
    ```


Now, you can check your application works by invoking the following URL: http://localhost:18868/foo_flask (you may replace localhost by your remote host if needed). A HTML page must display `Hello World!`.

