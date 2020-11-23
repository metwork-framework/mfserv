CONFIGS=config.ini nginx.conf mflog_override.conf mfserv/stats.lua mfserv/upstream_status.lua mfserv/init_worker_by_lua.lua mfserv/socket_updown.lua mfserv/health.lua

include ../adm/root.mk
include $(MFEXT_HOME)/share/subdir_root.mk
include $(MFEXT_HOME)/share/config_subdir.mk

test:
	layer_wrapper --layers=devtools@mfext noutf8.sh

all:: $(MFMODULE_HOME)/config/circus.ini $(MFMODULE_HOME)/config/telegraf.conf

$(MFMODULE_HOME)/config/mfserv/stats.lua: stats.lua
	@mkdir -p $(MFMODULE_HOME)/config/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/config/mfserv/upstream_status.lua: upstream_status.lua
	@mkdir -p $(MFMODULE_HOME)/config/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/config/mfserv/init_worker_by_lua.lua: init_worker_by_lua.lua
	@mkdir -p $(MFMODULE_HOME)/config/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/config/mfserv/socket_updown.lua: socket_updown.lua
	@mkdir -p $(MFMODULE_HOME)/config/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/config/mfserv/health.lua: health.lua
	@mkdir -p $(MFMODULE_HOME)/config/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@
