include ../adm/root.mk
PLUGINS=welcome

all:: $(MFSERV_HOME)/share/plugins/.done

$(MFSERV_HOME)/share/plugins/.done:
	mkdir -p $(MFSERV_HOME)/share/plugins
	for PLUGIN in $(PLUGINS); do cd $${PLUGIN} && make clean releasedebug || exit 1 && mv *.plugin $${MFSERV_HOME}/share/plugins && cd ..; done
	touch $@

clean::
	for PLUGIN in $(PLUGINS); do cd $${PLUGIN} && make clean && cd ..; done

superclean: clean
	rm -Rf $(MFSERV_HOME)/share/plugins
