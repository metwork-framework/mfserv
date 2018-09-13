include ../../../adm/root.mk

include $(MFEXT_HOME)/share/python2_layer.mk

#before:: $(MODULE_HOME)/opt/$(LAYER_NAME)/.layerapi2_label

#$(MODULE_HOME)/opt/$(LAYER_NAME)/.layerapi2_label:
#	bootstrap_layer.sh python2@mfserv $(MODULE_HOME)/opt/python2
#	echo "root@mfserv" >$(MODULE_HOME)/opt/python2/.layerapi2_dependencies
#	echo "python2@mfcom" >>$(MODULE_HOME)/opt/python2/.layerapi2_dependencies
toto:
	pip freeze
