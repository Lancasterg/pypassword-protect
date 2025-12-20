.PHONY: all build test lint clean run

all: build test lint

build:
	./build.sh

test:
	pytest
	rm -rf test/tmp_test_files/*

lint:
	black pypassword_protect
	isort pypassword_protect

clean:
	rm -rf dist build *.egg-info main.spec
	rm -rf test/tmp_test_files/*
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/

run:
	python -m pypassword