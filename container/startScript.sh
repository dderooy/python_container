#!/bin/sh

if [ ! -e /script/main.py ]
then
    echo 'ERROR: python main script not provided. Please name your starting script main.py'
fi

python /script/main.py