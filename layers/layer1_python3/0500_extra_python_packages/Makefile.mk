include ../../../adm/root.mk

include $(MFEXT_HOME)/share/python3_layer.mk

#before:: $(MFMODULE_HOME)/opt/$(LAYER_NAME)/.layerapi2_label

#$(MFMODULE_HOME)/opt/$(LAYER_NAME)/.layerapi2_label:
#	bootstrap_layer.sh python3@mfserv $(MFMODULE_HOME)/opt/python3
#	echo "root@mfserv" >$(MFMODULE_HOME)/opt/python3/.layerapi2_dependencies
#	echo "python3_misc@mfext" >>$(MFMODULE_HOME)/opt/python3/.layerapi2_dependencies
