include $(MFCOM_HOME)/share/plugin.mk

{% if cookiecutter.type == "node" %}
unexport http_proxy
unexport https_proxy
unexport HTTP_PROXY
unexport HTTPS_PROXY

all: local/lib/node_modules/README

local/lib/node_modules/README: package-lock.json
	mkdir -p local/lib
	rm -Rf node_modules local/lib/node_modules
	layer_wrapper --layers=nodejs@mfserv -- npm ci install
	if ! test -d node_modules ; then mkdir -p node_modules ; fi
	mv node_modules local/lib/
	echo "created by plugin" >local/lib/node_modules/README

superclean:
	rm -Rf local/lib/node_modules node_modules
	rm -f package-lock.json

freeze: superclean package-lock.json

package-lock.json: package.json
	layer_wrapper --layers=nodejs@mfserv -- npm install
{% endif %}
