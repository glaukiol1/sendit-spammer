#!/bin/bash

# This file will only run in GNU-Linux systems.
echo "Usage: sendit.sh [Number of bot instances to spawn; recommended: 15-75] \n\t For Help with getting the sendit JSON payload, visit the GitHub"

for i in `seq 2 $1`
do
    python3 /home/kali/Desktop/main.py &
done
