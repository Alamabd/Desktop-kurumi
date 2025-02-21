#!/bin/bash

VENV_DIR=".venv"
SCRIPT="Documents/python/Desktop-kurumi/run.py"

if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment '$VENV_DIR' tidak ditemukan. Membuat virtual envi>
    python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

python "$SCRIPT"

deactivate