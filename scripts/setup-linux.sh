#!/usr/bin/env bash

VENV_ROOTPATH="$(dirname $0)/../virtualenv"

sudo apt-get -y install python python-pip
sudo apt-get -y install python3 python3-pip

sudo pip2 install --upgrade pip
sudo pip3 install --upgrade pip

sudo -H pip2 install virtualenv
sudo -H pip3 install virtualenv

mkdir -v "${VENV_ROOTPATH}"
mkdir -v "${VENV_ROOTPATH}/python2"
mkdir -v "${VENV_ROOTPATH}/python3"

VENV_PATH="${VENV_ROOTPATH}/python2"
if [ ! -f "${VENV_PATH}/bin/activate" ]; then
    virtualenv -p python2 "${VENV_PATH}"
fi
source "${VENV_PATH}/bin/activate" && \
    pip install requests PyYAML
deactivate

VENV_PATH="${VENV_ROOTPATH}/python3"
if [ ! -f "${VENV_PATH}/bin/activate" ]; then
    virtualenv -p python3 "${VENV_PATH}"
fi
source "${VENV_PATH}/bin/activate" && \
    pip install requests  PyYAML
deactivate
