#!/bin/bash

# This script is used to initialize the docker environment

apt update -y
apt-get full-upgrade -y
apt install vim -y
apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa 

apt install python3.10 python3-pip curl -y 
apt install python3-pyqt5
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1