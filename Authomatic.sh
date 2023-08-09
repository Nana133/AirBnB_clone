#!/bin/bash

echo "Hello Comfort, please enter your commit message"
read message


git add .
git commit -m "$message"
git push
