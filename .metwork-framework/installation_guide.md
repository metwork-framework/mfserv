# Installation guide

## Prerequisites

- a `CentOS 6`, `CentOS 7` or `CentOS 8` `x86_64` linux distribution installed (it should also work with correponding RHEL or ScientificLinux distribution)
- (or) a `Fedora 29` or `Fedora 30` `x86_64` linux distribution
- (or) a `mageia 6` or `mageia 7` `x86_64` linux distribution
- (or) an `opensuse/leap:15.0`, `opensuse/leap:15.1`, `opensuse/leap:42.3` `x86_64` linux distribution (it should also work with corresponding SLES distribution)

.. note::
    As we develop MetWork Framework mainly on `CentOS` linux distributions, this is
    our recommendation if you can choose your OS.

.. note::
    As we build reasonably "portable" RPM packages, it should work with any RPM based linux distribution
    more recent than `CentOS 6` linux distribution (2011).

.. note::
    We are working right now on supporting other Linux distributions (debian, ubuntu). Please contact us if you
    are interested in.

- disabled `SELinux`

.. note::
    It could work with enabled `SELinux` but we never tested so comments and help are welcome.

    To disable `SELinux` on a `CentOS` Linux distribution, which is enabled by default, you have to change the file
    `/etc/selinux/config` to set `SELINUX=disabled`, then reboot the system.

- internet access to metwork-framework.org (on standard TCP/80 port)

.. note::
    Of course, you can deploy on a computer without internet access but you will have to build your own
    mirror or you will have to install correspondings RPM files manually (not difficult but a little boring).

## Configure the metwork RPM repository

### Check

First check the output of `uname -a |grep x86_64`. If you have nothing, you don't have a `x86_64` distribution installed and you can't install MetWork on it.

### Choose a version

Depending on your needs (stability versus new features), you can choose between several versions :

- released stable versions with a standard [semantic versionning](https://semver.org/) `X.Y.Z` version number *(the more **stable** choice)*, we call it **released stable**
- continuous integration versions of the release branch *(to get future **patch** versions before their release)*, we call it **continuous stable**
- continuous integration of the `master` branch *(to get future **major** and **minor** versions before their release)*, we call it **continuous master**
- continuous integration of the `integration` branch *(the more **bleeding edge** choice)*, we call it **continuous integration**

For each version, you will find the `BaseURL` in the following table:

Version | BaseURL
------- | -------
released stable | http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/
continuous stable | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/stable/portable/
continuous master | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/master/portable/
continuous integration | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/integration/portable/

.. note::
    Before `0.9` version, the `portable` subdirectory did not exist, it was replaced
    by `centos6` and `centos7` directory with dedicated builds inside. If you are
    using a `< 0.9` version, please change `portable` by the corresponding value.

### Configure

#### For CentOS and Fedora distributions

To configure the metwork RPM repository for CentOS and Fedora distributions,
you just have to create a new `/etc/yum.repos.d/metwork.repo` with the following
content (example for a **released stable** version):

```cfg
[metwork_stable]
name=MetWork Repository Stable
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/
gpgcheck=0
enabled=1
metadata_expire=0
```

If you prefer to copy/paste something, you can do that with following root commands
(still for a **released stable**):

```bash
cat >/etc/yum.repos.d/metwork.repo <<EOF
[metwork]
name=MetWork Repository
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/
gpgcheck=0
enabled=1
metadata_expire=0
EOF
```

.. warning::
    Previous examples are about stable release. **Be sure
    to change the "baseurl" value if you want a "non stable" MetWork version.**


#### For Mageia distributions

To configure the metwork RPM repository for Mageia distributions, use the following `root` command:

```console
urpmi.addmedia metwork http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/
```

.. warning::
    Previous example is about stable release. **Be sure
    to change the "baseurl" value if you want a "non stable" MetWork version.**

#### For SUSE distributions

To configure the metwork RPM repository for Mageia distributions, use the following `root` command:

```console
zypper ar -G http://metwork-framework.org/pub/metwork/releases/rpms/stable/portable/ metwork
```

.. warning::
    Previous example is about stable release. **Be sure
    to change the "baseurl" value if you want a "non stable" MetWork version.**

### Test

#### For CentOS and Fedora distributions

To test the repository, you can use the command `yum list "metwork*"` (as `root`). You must have several `metwork-...` modules available.

#### For Mageia distributions

To test the repository, you can use the command `urpmq --list |grep metwork |uniq` (as `root`). You must have several `metwork-...` modules available.

#### For SUSE distributions

To test the repository, you can use the command `zypper pa |grep metwork` (as `root`). You must have several `metwork-...` modules available.

## How to install mfserv metwork module

.. note::
    For Mageia distributions, replace `yum install` by `urpmi` in the next
    following examples and `yum list` by `urpmq`.

.. note::
    For SUSE distributions, replace `yum install` by `zypper install` in the next
    following examples and `yum list` by `zypper pa`.

### Minimal installation

You just have to execute the following command (as `root` user):

```console
# For CentOS or Fedora (see above note for other distributions)
yum install metwork-mfserv
```

### Full installation (all layers, except addons)

If you prefer a full installation (as `root` user):

```console
# For CentOS or Fedora (see above note for other distributions)
yum install metwork-mfserv-full
```



### Optional mfserv layers

To list available (and not already installed) mfserv additional
layers, you can use the following command:

```console
# For CentOS or Fedora (see above note for other distributions)
yum list |grep 'metwork-mfserv-layer-.*:'
```



### Optional mfext layers


After a minimal installation, you can add some optional layers (as `root` user):


```console
# To install some devtools
# for CentOS or Fedora (see above note for other distributions)
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
# for CentOS or Fedora (see above note for other distributions)
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
# for CentOS or Fedora (see following note for other distributions)
yum remove "metwork-mfserv*"
```

.. note::
    For Mageia distributions, replace `yum remove` by `urpme`.

.. note::
    For SUSE distributions, replace `yum remove` by `zypper remove`.

## How to uninstall all metwork modules

To uninstall all metwork modules, use following `root` commands:

```console
# for CentOS or Fedora (see previous note for other distributions)
# We stop metwork services
service metwork stop

# we remove metwork modules
yum remove "metwork-*"
```

.. note::
    If your distribution does not provide `service` command, you can use
    `systemctl stop metwork.service` instead or `/etc/rc.d/init.d/metwork stop`
    (if you don't have a `systemd` enabled machine or container).

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
# for CentOS or Fedora (see previous note for other distributions)
# We stop metwork services
service metwork stop

# We upgrade metwork modules
yum upgrade "metwork-*"

# We start metwork services
service metwork start
```

.. note::
    If your distribution does not provide `service` command, you can use
    `systemctl stop metwork.service` instead or `/etc/rc.d/init.d/metwork stop`
    (if you don't have a `systemd` enabled machine or container).

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

.. note::
    If your distribution does not provide `service` command, you can use
    `systemctl stop metwork.service` instead or `/etc/rc.d/init.d/metwork stop`
    (if you don't have a `systemd` enabled machine or container).



## How to start all metwork modules (after installation)

```console
# As root user
service metwork start
```

.. note::
    If your distribution does not provide `service` command, you can use
    `systemctl start metwork.service` instead or `/etc/rc.d/init.d/metwork start`
    (if you don't have a `systemd` enabled machine or container).

## How to stop all metwork modules (after installation)

```console
# As root user
service metwork stop
```

.. note::
    If your distribution does not provide `service` command, you can use
    `systemctl stop metwork.service` instead or `/etc/rc.d/init.d/metwork stop`
    (if you don't have a `systemd` enabled machine or container).

## How to get the status of all metwork modules (after installation)

```console
# As root user
service metwork status
```

.. note::
    If your distribution does not provide `service` command, you can use
    `systemctl status metwork.service` instead or `/etc/rc.d/init.d/metwork status`
    (if you don't have a `systemd` enabled machine or container).
