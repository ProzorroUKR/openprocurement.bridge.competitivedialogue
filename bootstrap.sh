#!/bin/sh
virtualenv .
./bin/pip install setuptools==33.1.1
./bin/pip install zc.buildout
./bin/buildout -N

