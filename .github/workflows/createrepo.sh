#!/bin/bash
#Shell to be run on metwork-framework.org as metworkpub user
if test -d $1/.repodata; then
    for i in 1 2 3 4 5 6 7 8 9 10; do
        echo "Sleeping 1 minute, waiting lock on $1/.repodata directory"
        sleep 60
        if test -d $1/.repodata; then
            continue
        else
            break
        fi
    done
fi
if test -d $1/.repodata; then
    echo "Can't obtain lock on $1/.repodata directory"
    exit 1
fi
createrepo --update $1
