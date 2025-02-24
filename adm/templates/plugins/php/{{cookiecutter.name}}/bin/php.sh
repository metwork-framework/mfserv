#!/bin/bash

export MFMODULE_RUNTIME_GROUP=metwork
export PHPFPMCONF=${MFMODULE_RUNTIME_HOME}/tmp/config_auto/php-fpm.${MFSERV_CURRENT_PLUGIN_NAME}.conf
export WWWCONF=${MFMODULE_RUNTIME_HOME}/tmp/config_auto/www.${MFSERV_CURRENT_PLUGIN_NAME}.conf

cat ${MFEXT_HOME}/opt/php/etc/php-fpm.conf | envtpl > "${PHPFPMCONF}"
cat ${MFEXT_HOME}/opt/php/etc/php-fpm.d/www.conf | envtpl > ${WWWCONF}

exec ${MFEXT_HOME}/opt/php/sbin/php-fpm --nodaemonize --force-stderr --fpm-config="${PHPFPMCONF}"
