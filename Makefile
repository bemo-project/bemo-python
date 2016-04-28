.PHONY: clean develop

PACKAGE=bemo

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean       => to clean clean all automatically generated files"
	@echo "  develop     => to install $(PACKAGE) in 'development mode'"

clean:
	find src/ -name \*.pyc -delete
	find src/ -name \*__pycache__ -delete

develop:
	python setup.py develop
