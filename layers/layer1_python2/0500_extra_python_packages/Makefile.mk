include ../../../adm/root.mk

include $(MFEXT_HOME)/share/python2_layer.mk

#before:: $(MFMODULE_HOME)/opt/$(LAYER_NAME)/.layerapi2_label

#$(MFMODULE_HOME)/opt/$(LAYER_NAME)/.layerapi2_label:
#	bootstrap_layer.sh python2@mfserv $(MFMODULE_HOME)/opt/python2
#	echo "root@mfserv" >$(MFMODULE_HOME)/opt/python2/.layerapi2_dependencies
#	echo "python2_misc@mfext" >>$(MFMODULE_HOME)/opt/python2/.layerapi2_dependencies
toto:
	pip freeze
