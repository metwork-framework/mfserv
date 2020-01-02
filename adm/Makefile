BINS=_make_circus_conf mfserv_conf_monitor.py _make_nginx_conf __make_nginx_conf _plugins.is_dangerous bjoern_wrapper.py plugins.hotswap _plugins.postinstall _check_circus_conf _check_nginx_conf signal_wrapper.py

include root.mk
include $(MFEXT_HOME)/share/subdir_root.mk
include $(MFEXT_HOME)/share/startup_scripts_profiles.mk

TEMPLATES=$(shell find templates ! -type d)
TARGET_TEMPLATES:=$(addprefix $(PREFIX)/share/,$(TEMPLATES))

all:: profiles $(PREFIX)/bin/cronwrap.sh $(PREFIX)/bin/mfserv.status $(PREFIX)/bin/mfserv.start $(PREFIX)/bin/mfserv.stop $(PREFIX)/bin/mfserv.init load_env $(TARGET_TEMPLATES) noutf8_check $(PREFIX)/bin/mfserv.autorestart $(PREFIX)/lib/mfserv/__init__.py $(PREFIX)/lib/mfserv/plugins_common.py $(PREFIX)/lib/mfserv/plugins_deprecated.py

noutf8_check:
	cd templates && layer_wrapper --layers=devtools@mfext noutf8.sh

$(PREFIX)/lib/mfserv/__init__.py:
	mkdir -p $(PREFIX)/lib/mfserv
	touch $@

$(PREFIX)/lib/mfserv/plugins_common.py: plugins_common.py
	cp -f $< $@

$(PREFIX)/lib/mfserv/plugins_deprecated.py: plugins_deprecated.py
	cp -f $< $@
