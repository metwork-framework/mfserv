#!/bin/bash
# automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/mfxxx_run_integration_tests.sh template

cd integration_tests 2>/dev/null

if test $? != 0; then
    echo "Directory integration_tests is missing"
    exit 0
fi

list_rep=`ls|grep -v data`
if test -z "$list_rep"; then
    echo "There are no integration tests"
    exit 0
fi

ret=0
for rep in $list_rep; do
    if [ -d $rep ]; then
        cd $rep
        if test -s .layerapi2_dependencies; then
             LAYERS_TO_LOAD=`cat .layerapi2_dependencies |xargs |sed 's/ /,/g'`
             WRAPPER=0
        else
             WRAPPER=1
        fi
        for test in test*; do
            echo "Test" $test "in" $rep
            for F in $(ls ${MODULE_RUNTIME_HOME}/log/*.log ${MODULE_RUNTIME_HOME}/log/*.stdout ${MODULE_RUNTIME_HOME}/log/*.stderr 2>/dev/null); do
                truncate -s 0 "${F}"
            done
            if test $WRAPPER -eq 0; then
                layer_wrapper --layers=$LAYERS_TO_LOAD -- ./$test
            else
                ./$test
            fi
            if test $? == 0; then
                echo "Test $test ($rep) OK"
            else
                for F in $(ls ${MODULE_RUNTIME_HOME}/log/*.log ${MODULE_RUNTIME_HOME}/log/*.stdout ${MODULE_RUNTIME_HOME}/log/*.stderr 2>/dev/null); do
                    if test -s "${F}"; then
                        echo "===== 40 last lines of ${F} to debug ====="
                        tail -40 "${F}"
                        echo ""
                        echo ""
                    fi
                done
                for F in ${MODULE_RUNTIME_HOME}/tmp/config_auto/nginx.conf ${MODULE_RUNTIME_HOME}/tmp/config_auto/circus.ini; do
                    if test -f "${F}"; then
                        echo "===== ${F} content to debug ====="
                        cat "${F}"
                        echo ""
                        echo ""
                    fi
                done
                echo "Test $test ($rep) KO"
                exit 1
            fi
        done
        cd ..
    fi
done

exit $ret
