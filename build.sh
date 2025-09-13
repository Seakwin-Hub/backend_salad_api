#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your project
PYTHON_VERSION=3.9.18

# Install Python 3.9
echo "Installing Python $PYTHON_VERSION"
pyenv install $PYTHON_VERSION -s
pyenv global $PYTHON_VERSION

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# For Flask applications
pip install gunicorn