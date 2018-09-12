include ../../../adm/root.mk
include $(MFEXT_HOME)/share/simple_layer.mk

unexport http_proxy
unexport https_proxy
unexport HTTP_PROXY
unexport HTTPS_PROXY

all:: node_modules/express/Readme.md $(PREFIX)/lib/node_modules/express/Readme.md

node_modules/express/Readme.md:
	layer_wrapper --layers=nodejs@mfext npm ci install

$(PREFIX)/lib/node_modules/express/Readme.md: node_modules/express/Readme.md
	rm -Rf $(PREFIX)/lib/node_modules
	mkdir -p $(PREFIX)/lib/
	cp -Rf node_modules $(PREFIX)/lib/

clean::
	rm -Rf node_modules
