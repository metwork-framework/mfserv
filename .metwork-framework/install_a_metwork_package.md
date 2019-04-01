# How to install/upgrade/remove mfserv metwork module (with internet access)

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/.metwork-framework/install_a_metwork_package.md)

## Prerequisites

You must:

- have configured the metwork yum repository. Please see [the corresponding document](configure_metwork_repo.md) document to do that.
- have an internet access on this computer

## Install mfserv metwork module

## Full installation

You just have to execute the following command (as `root` user):

```bash
yum install metwork-mfserv
```

## Minimal installation

If you prefer to start with a minimal installation, you have to execute the following command
(as `root` user):

```bash
yum install metwork-mfserv-minimal
```

## Optional Addons

### Optional dependencies addons

```bash
# To install some devtools
yum install metwork-mfext-devtools

# To install some scientific libraries
yum install metwork-mfext-scientific

# To install python2 support
# (including corresponding scientific and devtools addons)
yum install metwork-mfext-python2
```



### Optional mfserv addons

```bash
# To install python2 support
# (see above to install full scientific and devtools support)
yum install metwork-mfserv-python2

# To install nodejs support
yum install metwork-mfserv-nodejs
```




## Services

You can start corresponding services with the root command:

```bash
service metwork start
```

Or you can also reboot your computer (because metwork services are started automatically on boot).



## Uninstall mfserv metwork module


To uninstall mfserv metwork module, please stop corresponding metwork services with the `root` command:

```bash
service metwork stop mfserv
```

Then, use the following command (still as `root` user):


```bash
yum remove "metwork-mfserv*"
```

## Upgrade mfserv metwork module

To upgrade mfserv metwork module, use the following commands (still as `root` user):


```bash
# We stop mfserv services
service metwork stop mfserv
```


```bash
# We upgrade mfserv metwork module
yum upgrade "metwork-mfserv*"
```


```bash
# We start mfserv services
service metwork start mfserv
```


## Uninstall all metwork modules

To uninstall all metwork modules, use following root commands:

```bash
# We stop metwork services
service metwork stop

# we remove metwork modules
yum remove "metwork-*"
```

## Upgrade all metwork modules

The same idea applies to upgrade.

For example, to upgrade all metwork modules on a computer, use following root commands:

```bash
# We stop metwork services
service metwork stop

# We upgrade metwork modules
yum upgrade "metwork-*"

# We start metwork services
service metwork start
```
