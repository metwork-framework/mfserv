# Upgrade guide

## How to upgrade all metwork modules?

### If your starting version is >= 0.9

!!! warning
    **This procedure only works if your starting version is >= 0.9.**

    If your starting version is < 0.9, see next chapter.

```console tab="CentOS/Fedora"
# We stop metwork services
service metwork stop

# We upgrade metwork modules
yum upgrade "metwork-*"

# We start metwork services
service metwork start
```

```console tab="Mageia"
# We stop metwork services
service metwork stop

# We upgrade metwork modules
urpmi.update -a
urpmi "metwork-*"

# We start metwork services
service metwork start
```

```console tab="SUSE"
# We stop metwork services
service metwork stop

# We upgrade metwork modules
zypper refresh
zypper update "metwork-*"

# We start metwork services
service metwork start
```

!!! note
    If your distribution does not provide `service` command, you can use
    `systemctl stop metwork.service` and `systemctl start metwork.service` instead
     or `/etc/rc.d/init.d/metwork stop` and `/etc/rc.d/init.d/metwork start`
    (if you don't have a `systemd` enabled machine or container).

### If your starting version is < 0.9

!!! warning
    **This procedure is only necessary if your starting version is < 0.9.**

    If your starting version is >= 0.9, see previous chapter.

If your starting version is < 0.9 (for example: `0.8.X`), the update process
does not support major/minor update.

**So if you want to update, you have to remove everything and, then, reinstall
with the new version.**

!!! warning
    There is an automatic backup for files (but please backup by yourself
    your database content or anything else).

## FAQ

### Another major/minor version is available but I want to do only a patch update

Let's say you have a `mfext-0.8.3` version and you want to update to `mfext-0.8.5`
(patch update) even if another major/minor (for example: `mfext-0.9.Z`) version is available.

To do that, you have first to check (and change if necessary) your packages repository configuration (see "Installation Guide"). As `/stable/` `BaseUrls` point to the latest stable
versions, you have to change them to explicitly points to `/release_0.8/`.

Then you can use the standard procedure described at the beginning of this document.

!!! note
    You can use use the standard procedure even if your starting version is < 0.9 as
    the "patch update" is supported for all versions (without reinstalling everything).

