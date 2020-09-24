# Configuration guide

## Concepts

There are several concepts about configuration in MetWork framework.

### Configuration name

This is a completely optional step/concept.

You can set a configuration name globally for one machine in `/etc/metwork.config` file.

This file contains a single line with an **uppercase configuration name**.
By default, its value is `GENERIC`.

!!! warning
    Please use only alphanumeric uppercase characters here

!!! note
    The `underscore` character has a special inheritance meaning. You can use it but read
    this configuration guide before to understand its special meaning.

This *configuration name* will be used to select special configuration values in all metwork modules
and plugins. But you have to define them! If these special configuration values
do not exist for the given "configuration name", standard configuration values
are used. So if you set a silly value like `ZEERT455FRO` as configuration name,
it will probably change anything unless you defined (before!) some custom
configuration value for this silly configuration name.

So changing the configuration name with `/etc/metwork.config` file can be a
fast and practical way to select a kind of configuration variant
(for example: `PROD_DATACENTER1`, `DEV_JOHN`...). But this variant must exist
in other configuration files (see below). If not, default values will be used.

!!! note
    Even, if the default value in `/etc/metwork.config` is `GENERIC`, you won't
    find any configuration variant with this name in upstream configuration files. So
    default values are used.

!!! note
    With a MetWork profile loaded, you will also find the configuration name under
    the `${MFCONFIG}` environment variable (read from the `/etc/metwork.config` file).

### Overriding roles

The plugin *developer* (and/or the MetWork Framework *developer*) provide some configuration
files with **default values**.

These default values can be overriden by a *user* (who works with metwork runtime users (like `mfserv`, `mfdata`...)
and who will use `${MFMODULE_RUNTIME_HOME}/config/*.ini` files to do that).

But these default values (or *user* overriden ones) can also be overriden by an *admin*
(who works with `root` rights and who will use `/etc/metwork.config.d/...` directories to do that).

!!! note
    Of course, you don't need each role in your organization! For example, you can choose
    not to configure anything at the *user* level or at the *admin* level.

### Configuration groups and keys

The configuration use [ini files](https://en.wikipedia.org/wiki/INI_file). So you will find
some configurations files with *configuration groups* or *sections* with a name in square brackets (`[` and `]`)
and keys (every key has a name and a value delimited by an equals sign (`=`).

Example:

```ini
[nginx]
# This is comment
port=8080

workers=8

[log]
level=debug
```

In this example, we have two configuration groups: `[nginx]` and `[log]`.
And we have two keys under `[nginx]` and one key under `[log]`.


### Configuration variants and inheritance

#### Basic behavior

Let's say you have the following configuration files:

```ini
[group1]
debug=0
debug[DEV]=1
```

If you don't do anything special, the `debug` value will be `0` (standard default value).

But, if you set `DEV` in `/etc/metwork.config` (configuration name), the `debug` value will be `1`
because of the `debug[DEV]=1` line/variant.

Now, if you set `PROD` in `/etc/metwork.config` (configuration name), as there is no `debug[PROD]` line/variant,
the debug value will failback to the default value: `0` (in this example).

#### Inheritance behavior

Still with the same example:

```ini
[group1]
debug=0
debug[DEV]=1
```

What about if we use `DEV_JOHN_MONDAY` in `/etc/metwork.config`? As there is no `debug[DEV_JOHN_MONDAY]` line,
one might think that the retained value would be the default one: `0`.

In fact, the retained value will be `1`! Why? Because `_` (underscore) has a special meaning
in configuration names. This is a kind of inheritance mark.

So `DEV_JOHN_MONDAY` means as a configuration name:

- use `DEV_JOHN_MONDAY` if there is a variant with this exact name
- (else) use `DEV_JOHN` (first level of inheritance) if there is a variant with this name: `DEV_JOHN`
- (else) use `DEV` (second level of inheritance) if there is a variant with this name: `DEV`
- (else) use standard/default value

So with this example:

```ini
[group1]
debug=0
debug[DEV]=1
debug[DEV_JOHN]=2
debug[DEV_PETER]=3
debug[DEV_JOHN_MONDAY]=4
debug[DEV_JOHN_TUESDAY]=5
debug[QA]=6
```

We get this table:

Configuration name | selected value for `debug` key | comment
--- | --- | ---
`FOO` | `0` | standard value is used
`DEV` | `1` | exact variant
`DEV_JOHN_MONDAY` | `4` | exact variant
`DEV_JOHN_FRIDAY` | `2` | `DEV_JOHN` level of inheritance is used
`DEV_PETER` | `3` | exact variant
`DEV_KATE` | `1` | `DEV` level of inheritance is used
`DEV_SMITH_FOO_BAR_1` | `1` | `DEV` level of inheritance is used
`DEV_JOHN_QA` | `2` | `DEV_JOHN` level of inheritance is used
`FOO_QA` | `0` | the `QA` level can be used only if the configuration name begins with `QA`
`QA5` | `0` | the `QA5` variant does not exist and there is no inheritance because there is no `underscore`
`QA_5` | `6` | `QA` level of inheritance

### Configuration files and environment variables

The value in the configuration file is read only by a custom profile script that will transform it
into an environment variable.

**Only this environment variable will be used by the rest of the module.**

To resume the previous example, the selected value for the key `debug` in `[group1]` group of the `mfserv` module configuration is put into `MFSERV_GROUP1_DEBUG` environment variable.

In a more general way, every configuration option is stored in an environment variable:
`{MFMODULE}_{SECTION}_{KEY}`.

And this environment variable is set **only during profile loading**.

!!! warning
    When you change the configuration file, it does not change existing environment variables,
    so in some cases you will have to close and reopen your terminal to get new environment
    variable values.

!!! note
    To get current environment variables values for the current module, you can use for example:

    ```bash
    env |grep "^${MFMODULE}_"
    ```

!!! note
    There is no configuration variants anymore in environment values as the "good" value has
    been selected before. So environment variables contain "already resolved" values and that's
    why all metwork applications read the configuration from environment variables and
    not directly from ini configuration files.

## How to configure a MetWork module?

In this chapter, we don't talk about plugins. But only  about MetWork modules: `mfserv`, `mfdata`...

Let's take `mfadmin` module as an example. When you install the `mfadmin` module, you get a default configuration
file for the module. With standard packaging, the file is available in `/opt/metwork-mfadmin/config/config.ini`. In this file,
for instance, you will find a default `port` value of `15605` for the `[nginx]` group.

This is default values provided by MetWork Framework developers. Let's name it: the *upstream configuration file*.

!!! failure
    **NEVER** edit the upstream configuration file. **There is no good reason to do that.**

To override these default values, there are two ways: the *user* way or the *admin* way.

??? question "I'm lost! Which way should I use: user or admin?"
    If you are lost, use the *user* way first (easier but less powerful)


### As a user

With `mfadmin` unix user, you will find a `config/config.ini` file in `mfadmin` home directory (probably `/home/mfadmin`).

This file is created (if necessary) when you first log in as `mfadmin` unix user. It's a copy of the *upstream configuration file*
will all keys commented. As it overrides the *upstream configuration file*, if the key is commented, the *upstream* value is used.
If you uncomment a key, the corresponding value in this file is used for this key and the value in *upstream* is not used any more.

!!! note
    Configuration groups `[name_of_the_group]` are not commented and it is normal! Never comment them!

So to keep our example, in this file, you will find a `[nginx]` group with a commented line `# port=15605` in it.

If you want to change this port, first uncomment the line and set a new value to get (for example): `port=8080`.

??? warning "you are using a <= 0.9 version?"
    If you are using a <= 0.9 version, you also need a `[INCLUDE_config.ini]` special line at the very beginning of your `config.ini` file.

??? warning "My new environment variables values are not taken into account"
    Remember : When you change the configuration file, it does not change existing environment variables,
    so you will probably have to close and reopen your terminal to get new environment
    variable values.

### As an admin

With `root` user, you can set a `/etc/metwork.config.d/mfadmin/config.ini` file with the groups/keys you want to override.

There is no commented lines by default. You have to create the file by yourself.

To override the `port` of `[nginx]` to `8081` you can use for example:

```console
$ # as root user
$ cat >/etc/metwork.config.d/mfadmin/config.ini <<EOF
[nginx]
port=8081
EOF
```

!!! note
    Admin values can't be overridden.

??? warning "you are using a <= 0.9 version?"
    If you are using a <= 0.9 version, you also need a `[INCLUDE_config.ini]` special line at the very beginning of your `config.ini` file.

## How to configure a MetWork plugin?

Most of configuration concepts explained here are also available for MetWork plugins.

Please refer ton the "Plugin Guide" for details and specific things.
