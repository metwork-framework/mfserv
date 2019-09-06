# Installation guide

## Prerequisites

- a `Centos 6 x86_64` or `Centos 7 x86_64` linux distribution installed (it should also work with correponding RHEL or ScientificLinux distribution).

.. note::
    We are working right now on supporting other Linux distributions. Please contact us if you
    are interested in.

- disabled `SELinux`

.. note::
    It could work with enabled `SELinux` but we never tested so comments and help are welcome.

    To disable `SELinux`, which is enabled by default, you have to change the file
    `/etc/selinux/config` to set `SELINUX=disabled`, then reboot the system.

- internet access to metwork-framework.org (on standard TCP/80 port)

.. note::
    Of course, you can deploy on a computer without internet access but you will have to build your own
    mirror or you will have to install correspondings RPM files manually (not difficult but a little boring).

## Configure the metwork yum repository

### Check

First check the output of `uname -a |grep x86_64`. If you have nothing, you don't have a `x86_64` distribution installed and you can't install MetWork on it.

Then, if you are still here, check the output of `cat /etc/redhat-release` command. If the result is `CentOS release 6[...]`,
you have a **CentOS 6** distribution. If the result is `CentOS Linux release 7[...]`, you have a **CentOS 7** distribution.


### Choose a version

Depending on your needs (stability versus new features), you can choose between several versions :

- released stable versions with a standard [semantic versionning](https://semver.org/) `X.Y.Z` version number *(the more **stable** choice)*, we call it **released stable**
- continuous integration versions of the release branch *(to get future **patch** versions before their release)*, we call it **continuous stable**
- continuous integration of the `master` branch *(to get future **major** and **minor** versions before their release)*, we call it **continuous master**
- continuous integration of the `integration` branch *(the more **bleeding edge** choice)*, we call it **continuous integration**

For each version, you will find the `BaseURL` in the following table:

Version | BaseURL
------- | -------
released stable | http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos6/ (for centos6)<br/>http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos7/ (for centos7)
continuous stable | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/stable/centos6/ (for centos6)<br/>http://metwork-framework.org/pub/metwork/continuous_integration/rpms/stable/centos7/ (for centos7)
continuous master | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/master/centos6/ (for centos6)<br/>http://metwork-framework.org/pub/metwork/continuous_integration/rpms/master/centos7/ (for centos7)
continuous integration | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/integration/centos6/ (for centos6)<br/>http://metwork-framework.org/pub/metwork/continuous_integration/rpms/integration/centos7/ (for centos7)

.. note::
    We are working right now on supporting other Linux distributions. Please contact us if you
    are interested in.

### Configure

To configure the metwork yum repository, you just have to create a new `/etc/yum.repos.d/metwork.repo` with the following
content (example for a **released stable** version and **CentOS 7** distribution):

```cfg
[metwork]
name=MetWork Repository
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos7/
gpgcheck=0
enabled=1
metadata_expire=0
```

If you prefer to copy/paste something, you can do that with following root commands
(still for a **released stable** version and **CentOS 7** distribution):

```bash
cat >/etc/yum.repos.d/metwork.repo <<EOF
[metwork]
name=MetWork Repository
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos7/
gpgcheck=0
enabled=1
metadata_expire=0
EOF
```

.. warning::
    Previous examples are about stable release with CentOS 7 distribution. **Be sure
    to change the "baseurl" value if you are working with a CentOS 6 distribution or
    if you want a "non stable" MetWork version.**

### Test

To test the repository, you can use the command `yum list "metwork*"` (as `root`). You must have several `metwork-...` modules available.

## How to install mfserv metwork module

### Minimal installation

You just have to execute the following command (as `root` user):

```console
yum install metwork-mfserv
```

### Full installation (all layers, except addons)

If you prefer a full installation (as `root` user):

```console
yum install metwork-mfserv-full
```



### Optional mfserv layers

To list available (and not already installed) mfserv additional
layers, you can use the following command:

```console
yum list |grep 'metwork-mfserv-layer-.*:'
```



### Optional mfext layers


After a minimal installation, you can add some optional layers (as `root` user):


```console
# To install some devtools
yum install metwork-mfext-layer-python3_devtools

# To install some (base) scientific libraries
yum install metwork-mfext-layer-scientific_core

# To install python2 support
# (including corresponding scientific and devtools addons)
yum install metwork-mfext-python2
yum install metwork-mfext-python2_devtools
```

Note: you can also install some optional layers (provided by some mfext add-ons)

For example (please refer to corresponding add-on documentation)

```console
# To install opinionated VIM with Python3 support
yum install metwork-mfext-layer-python3_vim

# To install all scientific libraries (for Python3)
yum install metwork-mfext-layer-python3_scientific

# To install "machine learning" Python3 libraries
yum install metwork-mfext-layer-python3_ia

# To install "mapserver" stuff for Python3
yum install metwork-mfext-layer-python3_mapserverapi

# [...]
```

## How to uninstall mfserv module

To uninstall mfserv metwork module, use the following command (as `root` user):

```console
yum remove "metwork-mfserv*"
```

## How to uninstall all metwork modules

To uninstall all metwork modules, use following `root` commands:

```console
# We stop metwork services
service metwork stop

# we remove metwork modules
yum remove "metwork-*"
```

.. note::
    When you remove a module, the corresponding home directory will be deleted.
    For example, if you remove mfbase module, the `/home/mfbase` directory
    will be dropped. To avoid losing some work, the removal process will make a
    backup directoy in `/home/mfbase.rpmsave{date}` (without the content of
    `log` and `tmp` subdir). If you really want to clean all metwork stuff on
    this machine, you can also drop these backup directories. Same idea for
    `/etc/metwork.config.d/{module}`.


## How to upgrade all metwork modules (for a patch update)

```console
# We stop metwork services
service metwork stop

# We upgrade metwork modules
yum upgrade "metwork-*"

# We start metwork services
service metwork start
```

.. warning::
    This will only work for a patch update (for example `0.8.1 => 0.8.3`).
    For a major/minor update, see next chapter.

## How to upgrade all metwork modules (for a major/minor update)

.. warning::
    This is only for a major/minor update (for example `0.8.1 => 0.9.2`).
    For a patch update, see previous chapter.

**At the moment, the update process does not support major/minor update. So
if you want to do this, you have to remove and reinstall**

**This will be fixed with the 0.9 release**

.. warning::
    There is an automatic backup for files (but please backup by yourself
    your database content or anything else).

```console
# We stop metwork services
service metwork stop

# We remove metwork modules
yum remove "metwork-*"

# Reinstall what you need
yum install metwork-mfxxx metwork-mfyyy [...]

# Migrate manually want you need from /home/mf*.rpmsave* directories
# [...]

# We start metwork services
service metwork start
```



## How to start all metwork modules (after installation)

```console
# As root user
service metwork start
```

## How to stop all metwork modules (after installation)

```console
# As root user
service metwork stop
```

## How to get the status of all metwork modules (after installation)

```console
# As root user
service metwork status
```
