#!/bin/bash

sudo apt-get install python-matplotlib
sudo apt install clustalw
sudo apt install muscle
sudo apt install primer3
sudo apt-get install python-biopython -y
tar -xzvf biopython-1.69.tar.gz
cd biopython-1.69 
python setup.py build
python setup.py test
sudo python setup.py install
cd ..
tar -xzvf primer3-2.3.7.tar.gz
cd primer3-2.3.7/src
make all
make test

