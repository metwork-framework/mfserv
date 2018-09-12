include ../../../adm/root.mk
include $(MFEXT_HOME)/share/simple_layer.mk

all:: $(PREFIX)/lib/node_modules/metwork/metwork_cluster.js $(PREFIX)/lib/node_modules/metwork/metwork_server.js $(PREFIX)/lib/node_modules/metwork/package.json

$(PREFIX)/lib/node_modules/metwork/metwork_server.js: metwork_server.js
	mkdir -p $(PREFIX)/lib/node_modules/metwork/
	cp -f $< $@

$(PREFIX)/lib/node_modules/metwork/metwork_cluster.js: metwork_cluster.js
	mkdir -p $(PREFIX)/lib/node_modules/metwork/
	cp -f $< $@

$(PREFIX)/lib/node_modules/metwork/package.json: package.json
	mkdir -p $(PREFIX)/lib/node_modules/metwork/
	cp -f $< $@
