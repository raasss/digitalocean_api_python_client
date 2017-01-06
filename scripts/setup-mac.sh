#!/usr/bin/env bash

VENV_ROOTPATH="$(dirname $0)/../virtualenv"

if [ ! -f /usr/local/bin/brew ]; then
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    if [ $? != 0 ]; then
        echo "ERROR: Installation of Homebrew failed. Exiting...."
        exit $?
    fi
fi

brew install python
brew install python3

pip2 install virtualenv
pip3 install virtualenv

mkdir -v "${VENV_ROOTPATH}"
mkdir -v "${VENV_ROOTPATH}/python2"
mkdir -v "${VENV_ROOTPATH}/python3"

VENV_PATH="${VENV_ROOTPATH}/python2"
if [ ! -f "${VENV_PATH}/bin/activate" ]; then
    virtualenv -p python2 "${VENV_PATH}"
fi
source "${VENV_PATH}/bin/activate" && \
    pip install requests PyYAML nose mock
deactivate

VENV_PATH="${VENV_ROOTPATH}/python3"
if [ ! -f "${VENV_PATH}/bin/activate" ]; then
    virtualenv -p python3 "${VENV_PATH}"
fi
source "${VENV_PATH}/bin/activate" && \
    pip install requests PyYAML nose
deactivate
