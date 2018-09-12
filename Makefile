MODULE=MFSERV
MODULE_LOWERCASE=mfserv

-include adm/root.mk
-include $(MFEXT_HOME)/share/main_root.mk

all:: directories
	echo "root@mfcom" >$(MFSERV_HOME)/.layerapi2_dependencies
	echo "openresty@mfext" >>$(MFSERV_HOME)/.layerapi2_dependencies
	cd adm && $(MAKE)
	cd config && $(MAKE)
	cd extra_layers && $(MAKE)

clean::
	cd config && $(MAKE) clean
	cd adm && $(MAKE) clean
	cd extra_layers && $(MAKE) clean

directories:
	@for DIR in config bin; do mkdir -p $(PREFIX)/$$DIR; done

test::
	cd config && $(MAKE) test
