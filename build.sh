#!/bin/bash

# 1. Install dependencies from the current directory (uses your pyproject.toml)
# The "." tells pip to install the current project and its dependencies
echo "Installing dependencies..."
python3.12 -m pip install .

# 2. Run Django commands
echo "Running Migrations..."
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput

echo "Collecting Static Files..."
# This is vital for your admin sidebar and profile pictures!
python3.12 manage.py collectstatic --noinput --clear
