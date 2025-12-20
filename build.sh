#!/bin/bash
poetry shell
pyinstaller --onefile passprotect/main.py
mv dist/main bin/passprotect