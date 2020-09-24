include ../adm/root.mk

CHANGELOGS_SOURCES=$(shell cd .. && ls CHANGELOG-*.md 2>/dev/null)
CHANGELOGS_TARGETS=$(addprefix 900-changelogs/, $(CHANGELOGS_SOURCES))

CONFIG_INI_TARGET=850-reference/config.ini
PLUGIN_CONFIG_INI_TARGET=850-reference/plugin_templates/default/config.ini

all: $(CHANGELOGS_TARGETS) 850-reference/100-components.md $(CONFIG_INI_TARGET) $(PLUGIN_CONFIG_INI_TARGET)

900-changelogs/%: ../%
	cat $< |sed 's/^# \(.*\) CHANGELOG$$/# \1/g' >$@

850-reference/config.ini: $(MFMODULE_HOME)/config/config.ini
	cp -f $< $@
850-reference/plugin_templates/default/config.ini: $(MFMODULE_HOME)/share/templates/plugins/default/{{cookiecutter.name}}/config.ini
	for T in `ls $(MFMODULE_HOME)/share/templates/plugins |grep -v ^_`; do rm -Rf 850-reference/plugin_templates/$${T} ; mkdir -p 850-reference/plugin_templates/$${T}; layer_wrapper --layers=python3@mfext -- bootstrap_plugin.py create --template=$${T} --no-input foobar; cp foobar/config.ini 850-reference/plugin_templates/$${T}/config.ini; cat 850-reference/_plugin_config_ini.md |sed "s/@@@TEMPLATE@@@/$${T}/g" >850-reference/plugin_templates/$${T}/200-config_ini.md; rm -Rf foobar; if test -f $(MFMODULE_HOME)/share/templates/plugins/$${T}/README.md; then cp -f $(MFMODULE_HOME)/share/templates/plugins/$${T}/README.md 850-reference/plugin_templates/$${T}/100-intro.md; fi; done

850-reference/100-components.md: ../.metwork-framework/components.md
	rm -f $@
	echo "# Available components" >$@
	echo >>$@
	if test "${MFMODULE}" = "MFEXT" -a "${MFEXT_ADDON}" != "1"; then echo "!!! note" >>$@; echo "    Available components in all mfext layers **(excepting add-ons)**" >>$@ ; echo >>$@ ; echo "    :arrow_right: **you will find plenty of other components in [addons]({{addons}}) (even some officially maintained)**" >>$@ ; fi
	cat $< >>$@
	echo >>$@
	if test "${MFMODULE}" = "MFEXT" -a "${MFEXT_ADDON}" != "1"; then echo "!!! note" >>$@; echo "    Available components in all mfext layers **(excepting add-ons)**" >>$@ ; echo >>$@ ; echo "    :arrow_right: **you will find plenty of other components in [addons]({{addons}}) (even some officially maintained)**" >>$@ ; fi

clean:
	rm -f 900-changelogs/*.md
	rm -f 850-reference/100-components.md
	rm -f 850-reference/config.ini
	rm -f 850-components.md
	rm -Rf 850-reference/plugin_templates
