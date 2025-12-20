#!/bin/bash
pyinstaller --onefile pypassword_protect/run/main.py
mv dist/main bin/passprotect