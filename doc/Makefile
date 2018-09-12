# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = $(MFEXT_HOME)/bin/sphinx_wrapper
SPHINXPROJ    = mfserv
SOURCEDIR     = .
BUILDDIR      = _build

RST_FILES=$(shell ls *.md |grep -v tempo.md 2>/dev/null |sed 's/\.md$$/\.rst/g')
IPYNB_FILES=$(shell ls *.ipynb 2>/dev/null |sed 's/\.ipynb$$/\.mdtemp/g')

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%.rst: %.md
	rm -f tempo.md
	echo ".. GENERATED FILE, DO NOT EDIT (edit $< instead)" >tempo.md
	echo >>tempo.md
	cat $< |envtpl >>tempo.md
	layer_wrapper --layers=python3_devtools@mfext -- m2r --overwrite tempo.md
	cat tempo.rst |sed 's/^.. code-block::$$/.. code-block:: none\n\n   Output:/g' >$@
	rm -f tempo.md

%.mdtemp: %.ipynb
	layer_wrapper --layers=python3_devtools_jupyter@mfext -- jupyter nbconvert --to markdown --stdout $< >$@

superclean:
	rm -f tempo.*
	rm -f *.mdtemp
	rm -f layer_*.md
	rm -f layer_*.rst

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
html: $(IPYNB_FILES) $(RST_FILES) Makefile
	rm -f tempo.*
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
clean: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	rm -f tempo.*
	rm -f layer_*.rst
