#!/bin/bash


# Get directory of this script
DIR="$( dirname -- "$0"; )"

cd "$DIR"/.. || extit

echo "Starting server"
export PYTHONPATH=$PWD && python src/main.py
