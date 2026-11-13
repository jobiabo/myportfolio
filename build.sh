#!/bin/bash

set -e

echo "Building Flask application..."

python3 -m nuitka \
    --mode=onefile \
    --output-dir=dist \
    --output-filename=myapp \
    --include-data-dir=templates=templates \
    app.py

echo "Build completed!"