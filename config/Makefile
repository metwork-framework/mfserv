CONFIGS=config.ini nginx.conf mflog_override.conf

include ../adm/root.mk
include $(MFEXT_HOME)/share/subdir_root.mk
include $(MFEXT_HOME)/share/config_subdir.mk

test:
	layer_wrapper --layers=devtools@mfext noutf8.sh

all:: $(MFMODULE_HOME)/config/circus.ini $(MFMODULE_HOME)/config/telegraf.conf $(MFMODULE_HOME)/lib/mfserv/stats.lua $(MFMODULE_HOME)/lib/mfserv/upstream_status.lua $(MFMODULE_HOME)/lib/mfserv/init_worker_by_lua.lua $(MFMODULE_HOME)/lib/mfserv/socket_updown.lua $(MFMODULE_HOME)/lib/mfserv/health.lua

$(MFMODULE_HOME)/lib/mfserv/stats.lua: stats.lua
	@mkdir -p $(MFMODULE_HOME)/lib/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/lib/mfserv/upstream_status.lua: upstream_status.lua
	@mkdir -p $(MFMODULE_HOME)/lib/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/lib/mfserv/init_worker_by_lua.lua: init_worker_by_lua.lua
	@mkdir -p $(MFMODULE_HOME)/lib/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/lib/mfserv/socket_updown.lua: socket_updown.lua
	@mkdir -p $(MFMODULE_HOME)/lib/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@

$(MFMODULE_HOME)/lib/mfserv/health.lua: health.lua
	@mkdir -p $(MFMODULE_HOME)/lib/mfserv
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@
