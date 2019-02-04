CONFIGS=config.ini nginx.conf redis_plugin_xxx.conf mflog_override.conf

include ../adm/root.mk
include $(MFEXT_HOME)/share/subdir_root.mk
include $(MFCOM_HOME)/share/config_subdir.mk

test:
	layer_wrapper --layers=devtools@mfext noutf8.sh

all:: $(MODULE_HOME)/config/circus.ini $(MODULE_HOME)/config/telegraf.conf $(MODULE_HOME)/config/stats.lua

$(MODULE_HOME)/config/stats.lua: stats.lua
	layer_wrapper --layers=devtools@mfext -- test_globals_in_lua.sh $<
	cp -f $< $@
