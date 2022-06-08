MFMODULE=MFSERV
MFMODULE_LOWERCASE=mfserv

-include adm/root.mk
-include $(MFEXT_HOME)/share/main_root.mk

all:: directories
	cd adm && $(MAKE)
	cd config && $(MAKE)
	cd layers && $(MAKE)
	cd plugins && $(MAKE)

clean::
	cd config && $(MAKE) clean
	cd adm && $(MAKE) clean
	cd layers && $(MAKE) clean
	cd plugins && $(MAKE) clean

directories:
	@for DIR in config bin opt/python3/lib/python$(PYTHON3_SHORT_VERSION)/site-packages; do mkdir -p $(MFSERV_HOME)/$$DIR; done

test::
	cd config && $(MAKE) test
