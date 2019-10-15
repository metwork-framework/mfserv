include ../../../adm/root.mk
include $(MFEXT_HOME)/share/simple_layer.mk

all:: $(PREFIX)/lib/node_modules/metwork-tools/index.js

$(PREFIX)/lib/node_modules/metwork-tools/index.js: metwork-tools/index.js
	rm -Rf node_modules
	npm config set strict-ssl false
	source scl_source enable devtoolset-7 && npm install
	mkdir -p $(PREFIX)/lib/node_modules/metwork-tools
	cp -Rf node_modules/* $(PREFIX)/lib/node_modules/
	cp -f $< $@

clean::
	rm -Rf node_modules
