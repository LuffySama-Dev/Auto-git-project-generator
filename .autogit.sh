#!/bin/bash

# $1 and $2 takes argument passed.

PAR=$2
NAME="Add path where you want to add your repository locally"
NAME+=$2"/"


# Call's Python function
function create(){
	python create.py $NAME	$PAR
}

create


echo "Git repo Created"
cd $NAME
touch README.md
git init
git add .
git commit -m "first commit"
git remote add origin "Add your remote username without double quotes and don't add space at end""$PAR".git
git push -u origin master


exec bash