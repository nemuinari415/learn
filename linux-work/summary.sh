#!/bin/bash

for file in "#@"
do
	if [ -d "$file" ]; then
		echo "$file is a directory:"
		ls "$file"
	elif [ -f "$file is a regular file:"
		head -n 5 "$file"
	fi
done
