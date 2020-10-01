# Loading MFSERV environment

## General

After MFSERV installation, all files are located in `/opt/metwork-mfserv-{BRANCH}` directory with probably a `/opt/metwork-mfserv => /opt/metwork-mfserv-{BRANCH}` symbolic link (depending on what you have installed). Have a look in the `/opt` directory.

Because `/opt` is not used by default on [standard Linux](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard), the installation shouldn't break anything.

Therefore, if you do nothing specific after the installation, you won't benefit
of MFSERV environment.

In order to work with MFSERV, you have to load/activate the "Metwork MFSERV environment". There are several ways to do that, described in the sections below.

In the following sections, we use `{MFSERV_HOME}` as the installation directory of the `mfserv` module.


## Activate MFSERV environment by logging in as mfserv user.

Once MFSERV is installed, a `mfserv` user and, therefore, a `/home/mfserv` directory are created.

Log in as the mfserv user:
```bash
su - mfserv
```

!!! note
	If it's the first time you log in as mfserv user, there is no default password. You have to either set a password before (`passwd mfserv` or `sudo passwd mfserv`), or or use `su - mfserv` from `root` to log in as `mfserv` user.

Then, the MFSERV environment is loaded/activated for the whole session of the `mfserv` user.

From now, you are able to work with your plugin(s) in this `/home/mfserv` directory.

## Activate MFSERV environment from any user.

You can activate the MFSERV environment from your own account.

**This way is a good one if you intend to share the same Metwork environment on the same Linux machine with other users.**

Load the `mfserv` environment for the whole shell session by entering:
```bash
# {MFSERV_HOME} is the root mfbase directory, e.g. /opt/metwork-mfserv
source {MFSERV_HOME}/share/interative_profile
```

Then, the MFSERV environment is loaded/activated for the whole session of your account. A `metwork/mfserv` directory is created in your home directory. From now, you are able to work with your plugin(s) in this `~/metwork/mfserv` directory.

!!! warning
	The `~/metwork/mfserv` directory has nothing to do with the `/home/mfserv` [directory](#2-activate-mfserv-environment-by-logging-in-as-mfserv-user) and they don't share anything.

!!! warning
	Before sourcing `interactive_profile`, mfserv service must not be started, for instance, from a `mfserv` user session. Check from a `mfserv` user session mfserv is stopped : `mfserv.status`, `mfserv.stop`.


	If you are fed up of always entering the `source` command, you may create an `mfserv` alias in your `.bash_profile` file and use this `mfserv` alias when you want to quickly load the "MFSERV environment":
        `MFSERV_HOME=/opt/metwork-mfserv`

        `alias mfserv="source ${MFSERV_HOME}/share/interactive_profile"`

!!! warning
	We don't recommend to source directly `mfserv interactive_profile` in your `.bash_profile` if you are working with a full graphical interface because of possible side effects with desktop environment.


## Activate MFSERV for one command only from any user.

If you want to load the "MFSERV environment" for only one command and then return back to a standard running environment, you can use the specific wrapper `{MFSERV_HOME}/bin/mfserv_wrapper`:
```bash
##### mfserv_wrapper example #####

# where is the system python command ?
$ which python
/usr/bin/python
# => this is the standard/system python command (in /usr/bin)

# what is the version of the system python command ?
$ python --version
Python 2.7.5
# => this is a python2 version

# execute python through the wrapper
# (please replace {MFSERV_HOME} by the real mfserv home !)
$ {MFSERV_HOME}/bin/mfserv_wrapper which python
/opt/metwork-mfext-master/opt/python3_core/bin/python
# => this is the metwork python command included in this module

# what is the version of the mfbase python command ?
$ {MFSERV_HOME}/bin/mfserv_wrapper python --version
Python 3.5.6
# => this is a python3 version
```

For more details, enter `{MFSERV_HOME}/bin/mfserv_wrapper --help` command.

## Miscellaneous

You may also be interested in the `outside` Metwork command. Check the [related documentation](../../../mfdata/950-old_docs/mfdata_miscellaneous/#9-the-outside-metwork-command)



