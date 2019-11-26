CONFIGS=config.ini nginx.conf redis_plugin_xxx.conf mflog_override.conf stats.lua upstream_status.lua init_worker_by_lua.lua socket_updown.lua health.lua

include ../adm/root.mk
include $(MFEXT_HOME)/share/subdir_root.mk
include $(MFEXT_HOME)/share/config_subdir.mk

test:
	layer_wrapper --layers=devtools@mfext noutf8.sh

all:: $(MFMODULE_HOME)/config/circus.ini $(MFMODULE_HOME)/config/telegraf.conf

$(MFMODULE_HOME)/config/stats.lua: stats.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/config/upstream_status.lua: upstream_status.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/config/init_worker_by_lua.lua: init_worker_by_lua.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/config/socket_updown.lua: socket_updown.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/config/health.lua: health.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@
