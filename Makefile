.PHONY: all build test lint clean run

all: build test lint


install:
	@echo Installing project
	poetry install --with dev
	poetry lock

build:
	@echo Building exectutable...
	./build.sh

test:
	@echo Running tests...
	pytest
	rm -rf test/tmp_test_files/*

lint:
	@echo Linting
	black pypassword_protect
	isort pypassword_protect

clean:
	@echo cleaning
	rm -rf dist build *.egg-info main.spec
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
