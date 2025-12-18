.PHONY: all build test lint clean run

all: build test lint

build:
	@echo "Building..."
	./build.sh

test:
	@echo "Running tests..."
	pytest
	rm -rf test/tmp_test_files/*

lint:
	@echo "Linting..."
	black pypassword_protect
	isort pypassword_protect

format:
	echo

clean:
	@echo "Cleaning..."
	rm -rf dist build *.egg-info
	rm -rf test/tmp_test_files/*

run:
	python -m pypassword