#!/bin/bash

echo Starting Dynamine Site...
#python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000 --verbosity 0
