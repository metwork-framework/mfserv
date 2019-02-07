include $(MFCOM_HOME)/share/plugin.mk

NAME:=$(shell config.py config.ini general name)

custom::
	plugin_wrapper $(NAME) -- npm run transpile
