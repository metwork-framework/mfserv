#!/bin/bash
#Shell to be run on metwork-framework.org as metworkpub user (archived copy)
if test -d $1/.repodata; then
    for i in 1 2 3 4 5; do
        echo "Sleeping 30s, waiting lock on $1/.repodata directory"
        sleep 30
        if test -d repodata2; then
            continue
        else
            break
        fi
    done
fi
createrepo --update $1
