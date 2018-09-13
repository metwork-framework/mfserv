include ../../../adm/root.mk

include $(MFEXT_HOME)/share/python3_layer.mk

#before:: $(MODULE_HOME)/opt/$(LAYER_NAME)/.layerapi2_label

#$(MODULE_HOME)/opt/$(LAYER_NAME)/.layerapi2_label:
#	bootstrap_layer.sh python3@mfserv $(MODULE_HOME)/opt/python3
#	echo "root@mfserv" >$(MODULE_HOME)/opt/python3/.layerapi2_dependencies
#	echo "python3@mfcom" >>$(MODULE_HOME)/opt/python3/.layerapi2_dependencies
