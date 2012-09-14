APPNAME = pylonshq
DEPS =
HERE = $(shell pwd)
BIN = $(HERE)/bin
VIRTUALENV = virtualenv
NOSE = bin/nosetests -s --with-xunit
TESTS = $(APPNAME)/tests
PYTHON = $(HERE)/bin/python
BUILDAPP = $(HERE)/bin/buildapp
BUILDRPMS = $(HERE)/bin/buildrpms
PYPI = http://pypi.python.org/simple
PYPIOPTIONS = -i $(PYPI)
INSTALL = $(HERE)/bin/pip install
PIP_CACHE = /tmp/pip_cache
INSTALLOPTIONS = --download-cache $(PIP_CACHE)  -U -i $(PYPI)

ifdef PYPIEXTRAS
	PYPIOPTIONS += -e $(PYPIEXTRAS)
	INSTALLOPTIONS += -f $(PYPIEXTRAS)
endif

ifdef PYPISTRICT
	PYPIOPTIONS += -s
	ifdef PYPIEXTRAS
		HOST = `python -c "import urlparse; print urlparse.urlparse('$(PYPI)')[1] + ',' + urlparse.urlparse('$(PYPIEXTRAS)')[1]"`

	else
		HOST = `python -c "import urlparse; print urlparse.urlparse('$(PYPI)')[1]"`
	endif

endif

INSTALL += $(INSTALLOPTIONS)
SW = sw

BUILD_DIRS = bin build deps include lib lib64


.PHONY: all build test

all:	build

$(BIN)/python:
	python $(SW)/virtualenv.py --no-site-packages --distribute .
	rm distribute-0.6.19.tar.gz
	$(BIN)/pip install -U pip

$(BIN)/pip: $(BIN)/python

$(BIN)/nosetests:
	$(INSTALL) nose
	$(INSTALL) coverage

$(BIN)/paster: lib $(BIN)/pip
	$(INSTALL) -r requirements.txt
	$(PYTHON) setup.py develop

clean-env:
	rm -rf $(BUILD_DIRS)

clean:	clean-env

build: $(BIN)/pip
	$(INSTALL) -r requirements.txt
	$(PYTHON) setup.py develop

test: $(BIN)/nosetests
	$(NOSE) --with-coverage --cover-package=pylonshq --cover-erase \
	--cover-inclusive $(APPNAME)
