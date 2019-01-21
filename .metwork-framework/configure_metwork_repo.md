# How to configure the metwork yum repository ?

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/.metwork-framework/configure_metwork_repo.md)

## Prerequisites

- a `Centos 6 x86_64` or `Centos 7 x86_64` linux distribution installed (it should also work with correponding RHEL or ScientificLinux distribution)
- a few GB available on `/opt` 
- a yum repository configured for system packages (done by default)
- no `SELinux` feature (it can work with it but we don't have tested anything with SELinux on, comments and tests welcome)

To disable SELinux, which is enabled by default, you have to change the file `/etc/selinux/config` to set `SELINUX=disabled`, then
reboot the system.

## Choose a version

Depending on your needs (stability versus new features), you can choose between serveral versions :

- released stable versions with a standard [semantic versionning](https://semver.org/) `X.Y.Z` version number *(the more **stable** choice)*
- continuous integration versions of the release branch *(to get future **patch** versions before their release)*
- continuous integration of the `master` branch *(to get future **major** and **minor** versions before their release)*
- continuous integration of the `integration` branch *(the more **bleeding edge** choice)*

For each version, you will find the `BaseURL` in the following table:

Version | BaseURL
------- | -------
released stable | http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos6/ (for centos6)<br/>http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos7/ (for centos7)
continuous stable | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/stable/centos6/ (for centos6)<br/>http://metwork-framework.org/pub/metwork/continuous_integration/rpms/stable/centos7/ (for centos7)
continuous master | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/master/centos6/ (for centos6)<br/>http://metwork-framework.org/pub/metwork/continuous_integration/rpms/master/centos7/ (for centos7)
continuous integration | http://metwork-framework.org/pub/metwork/continuous_integration/rpms/integration/centos6/ (for centos6)<br/>http://metwork-framework.org/pub/metwork/continuous_integration/rpms/integration/centos7/ (for centos7)

## Configure the metwork yum repository for CentOS 6 distribution

First check the output of `uname -a |grep x86_64`. If you have nothing, you don't have a `x86_64` distribution installed and you can't 
install MetWork on it.

Then, if you are still here, check the output of `cat /etc/redhat-release` command. If the result is `CentOS release 6[...]", 
you have a CentOS 6 distribution and you can continue here. Else, jump to the centos7 section.

To configure the metwork yum repository for **releases stable** versions on **centos6**, you just have to create a new `/etc/yum.repos.d/metwork.repo` with the following 
content :

```
[metwork_stable]
name=MetWork Stable
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos6/
gpgcheck=0
enabled=1
metadata_expire=0
```

You can do this with one command:

```
cat >/etc/yum.repos.d/metwork.repo <<EOF
[metwork_stable]
name=MetWork Stable
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos6/
gpgcheck=0
enabled=1
metadata_expire=0
EOF
```

Of course, if you prefer to choose another version, you have to change the `baseurl` parameter. For example, to get `continuous master` version on `centos6`, use:

`baseurl=http://metwork-framework.org/pub/metwork/continuous_integration/rpms/master/centos6/`

## Configure the metwork yum repository for CentOS 7 distribution

First check the output of `uname -a |grep x86_64`. If you have nothing, you don't have a `x86_64` distribution installed and you can't 
install MetWork on it.

Then, if you are still here, check the output of `cat /etc/redhat-release` command. If the result is `CentOS release 7[...]", 
you have a CentOS 7 distribution and you can continue here. Else, go back to the centos6 section.

To configure the metwork yum repository for centos7, you just have to create a new `/etc/yum.repos.d/metwork.repo` with the following 
content :

```
[metwork_stable]
name=MetWork Stable
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos7/
gpgcheck=0
enabled=1
metadata_expire=0
```

You can do this with one command (as `root` user):

```
cat >/etc/yum.repos.d/metwork.repo <<EOF
[metwork_stable]
name=MetWork Stable
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos7/
gpgcheck=0
enabled=1
metadata_expire=0
EOF
```

Of course, if you prefer to choose another version, you have to change the `baseurl` parameter. For example, to get `continuous master` version on `centos7`, use:

`baseurl=http://metwork-framework.org/pub/metwork/continuous_integration/rpms/master/centos7/`

## Test

To test the repository, you can use the command `yum list "metwork*"` (as `root`). You must have several `metwork-...` packages available.

