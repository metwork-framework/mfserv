CONFIGS=config.ini nginx.conf redis_plugin_xxx.conf mflog_override.conf stats.lua upstream_status.lua init_worker_by_lua.lua socket_updown.lua health.lua

include ../adm/root.mk
include $(MFEXT_HOME)/share/subdir_root.mk
include $(MFCOM_HOME)/share/config_subdir.mk

test:
	layer_wrapper --layers=devtools@mfext noutf8.sh

all:: $(MODULE_HOME)/config/circus.ini $(MODULE_HOME)/config/telegraf.conf

$(MODULE_HOME)/config/stats.lua: stats.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MODULE_HOME)/config/upstream_status.lua: upstream_status.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MODULE_HOME)/config/init_worker_by_lua.lua: init_worker_by_lua.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MODULE_HOME)/config/socket_updown.lua: socket_updown.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MODULE_HOME)/config/health.lua: health.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@
