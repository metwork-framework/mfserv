PWD=$(shell pwd)
PLUGIN_NAME=$(shell basename $(PWD))

precustom:: .layerapi2_label .layerapi2_dependencies .releaseignore .plugin_format_version .gitignore .autorestart_includes .autorestart_excludes

.layerapi2_label:
	echo "plugin_$(PLUGIN_NAME)@mfserv" >$@

.layerapi2_dependencies: ../../adm/templates/plugins/python3_noweb/{{cookiecutter.name}}/.layerapi2_dependencies
	cp -f $< $@

.releaseignore: ../../adm/templates/plugins/_common/releaseignore
	cp -f $< $@

.gitignore:
	echo ".layerapi2_label" >>$@
	echo ".releaseignore" >>$@
	echo ".plugin_format_version" >>$@
	echo ".autorestart_includes" >>$@
	echo ".autorestart_excludes" >>$@
	echo "python3_virtualenv_sources/src" >>$@
	echo "local" >>$@

.autorestart_includes: ../../adm/templates/plugins/_common/autorestart_includes
	cp -f $< $@

.autorestart_excludes: ../../adm/templates/plugins/_common/autorestart_excludes
	cp -f $< $@

clean::
	rm -f .layerapi2_label
	rm -f .releaseignore
	rm -f .plugin_format_version
	rm -f .autorestart_includes
	rm -f .autorestart_excludes
