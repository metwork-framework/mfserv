{% extends "_common/Makefile" %}

{% block extra %}
transpile::
	plugin_wrapper $(NAME) -- npm run transpile
{% endblock %}

{% block custom %}
custom::
	export METWORK_LAYERS_PATH=`pwd`:$(METWORK_LAYERS_PATH) ; plugin_wrapper $(NAME) -- npm run transpile
{% endblock %}
