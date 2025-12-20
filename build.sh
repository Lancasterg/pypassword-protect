#!/bin/bash
pyinstaller --onefile passprotect/main.py
mv dist/main bin/passprotect