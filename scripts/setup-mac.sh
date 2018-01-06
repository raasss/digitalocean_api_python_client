#!/usr/bin/env bash

set -ex

VENV_ROOTPATH="$(dirname $0)/../venv"

if [ ! -f /usr/local/bin/brew ]; then
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    if [ $? != 0 ]; then
        echo "ERROR: Installation of Homebrew failed. Exiting...."
        exit $?
    fi
fi

if [ ! -f /usr/local/bin/python2 ]; then
    brew install python
fi

if [ ! -f /usr/local/bin/python3 ]; then
    brew install python3
fi

pip2 install virtualenv
pip3 install virtualenv

if [ ! -d "${VENV_ROOTPATH}" ]; then
    mkdir -v "${VENV_ROOTPATH}"
fi

if [ ! -d "${VENV_ROOTPATH}/python2" ]; then
    mkdir -v "${VENV_ROOTPATH}/python2"
fi

if [ ! -d "${VENV_ROOTPATH}/python3" ]; then
    mkdir -v "${VENV_ROOTPATH}/python3"
fi


VENV_PATH="${VENV_ROOTPATH}/python2"

if [ ! -f "${VENV_PATH}/bin/activate" ]; then
    virtualenv -p python2 "${VENV_PATH}"
fi
source "${VENV_PATH}/bin/activate"
pip install -r "${VENV_ROOTPATH}/../requirements.txt"
deactivate

VENV_PATH="${VENV_ROOTPATH}/python3"

if [ ! -f "${VENV_PATH}/bin/activate" ]; then
    virtualenv -p python3 "${VENV_PATH}"
fi
source "${VENV_PATH}/bin/activate"
pip install -r "${VENV_ROOTPATH}/../requirements.txt"
deactivate
