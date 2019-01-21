# How to install/upgrade/remove mfserv metwork package (with internet access)

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/.metwork-framework/install_a_metwork_package.md)

## Prerequisites

You must:

- have configured the metwork yum repository. Please see [the corresponding document](configure_metwork_repo.md) document to do that.
- have an internet access on this computer

## Install mfserv metwork package

You just have to execute the following command (as `root` user):

```
yum install metwork-mfserv
```

Of course, you can install several metwork packages on the same linux box.


You can start corresponding services with the root command:

```
service metwork start
```

Or you can also reboot your computer (because metwork services are started automatically on boot).



## Uninstall mfserv metwork package


To uninstall mfserv metwork package, please stop corresponding metwork services with the `root` command:

```
# note: this is not necessary with mfext or mfcom
# because there is no corresponding services
service metwork stop mfserv
```

Then, use the following command (still as `root` user):


```
yum remove "metwork-mfserv*"
```

## Uninstall all metwork packages

To uninstall all metwork packages, use following root commands:

```
# We stop metwork services
service metwork stop

# we remove metwork packages
yum remove "metwork-*"
```

## Upgrade all metwork packages

The same idea applies to upgrade.

For example, to upgrade all metwork packages on a computer, use following root commands:

```
# We stop metwork services
service metwork stop

# We upgrade metwork packages
yum upgrade "metwork-*"

# We start metwork services
service metwork start
```
