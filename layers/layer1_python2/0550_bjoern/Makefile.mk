include ../../../adm/root.mk
include $(MFEXT_HOME)/share/package.mk

export NAME=bjoern
export VERSION=metwork-20190515
export EXTENSION=zip
export CHECKTYPE=MD5
export CHECKSUM=0ecf48ca01016ba33eb0ca0e4f15d9ef
DESCRIPTION=\
Fast And Ultra-Lightweight HTTP/1.1 WSGI Server
WEBSITE=https://github.com/thefab/bjoern/tree/metwork
LICENSE=BSD

all:: $(PYTHON2_SITE_PACKAGES)/$(NAME)-3.0.0-py$(PYTHON2_SHORT_VERSION)-linux-x86_64.egg/bjoern.py
$(PYTHON2_SITE_PACKAGES)/$(NAME)-3.0.0-py$(PYTHON2_SHORT_VERSION)-linux-x86_64.egg/bjoern.py:
	$(MAKE) --file=$(MFEXT_HOME)/share/Makefile.standard EXPLICIT_NAME=bjoern-metwork download uncompress
	wget -O build/bjoern-metwork/http-parser/http_parser.c "https://raw.githubusercontent.com/nodejs/http-parser/1786fdae36d3d40d59463dacab1cfb4165cf9f1d/http_parser.c"
	wget -O build/bjoern-metwork/http-parser/http_parser.h "https://raw.githubusercontent.com/nodejs/http-parser/1786fdae36d3d40d59463dacab1cfb4165cf9f1d/http_parser.h"
	$(MAKE) --file=$(MFEXT_HOME)/share/Makefile.standard EXPLICIT_NAME=bjoern-metwork EXTRACFLAGS="-I$(MFEXT_HOME)/opt/core/include" EXTRALDFLAGS="-L$(MFEXT_HOME)/opt/core/lib" python2build python2install
