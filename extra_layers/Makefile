include ../adm/root.mk
include $(MFEXT_HOME)/share/subdir_root.mk

SUBDIRS=$(shell ls -d layer*)

all::
	@for SUBDIR in $(SUBDIRS); do OLDPWD=`pwd`; cd $$SUBDIR || exit 1; $(MAKE) all || exit 1; cd $${OLDPWD}; done

clean::
	@for SUBDIR in $(SUBDIRS); do OLDPWD=`pwd`; cd $$SUBDIR || exit 1; $(MAKE) clean || exit 1; cd $${OLDPWD}; done

doc:
	@for SUBDIR in $(SUBDIRS); do OLDPWD=`pwd`; cd $$SUBDIR || exit 1; $(MAKE) doc || exit 1; cd $${OLDPWD}; done
