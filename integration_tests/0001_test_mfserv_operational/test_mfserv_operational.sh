#!/bin/bash

# Test if mfserv.start/status/stop are ok
su --command="mfserv.start" - mfserv
if test $? -ne 0; then
    echo "Test mfserv.start KO"
    exit 1
else
    echo "Test mfserv.start OK"
fi
su --command="mfserv.status" - mfserv
if test $? -ne 0; then
    echo "Test mfserv.status KO"
    exit 1
else
    echo "Test mfserv.status OK"
fi
su --command="mfserv.stop" - mfserv
if test $? -ne 0; then
    echo "Test mfserv.stop KO"
    exit 1
else
    echo "Test mfserv.stop OK"
fi
exit 0
