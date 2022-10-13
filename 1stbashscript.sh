#!/bin/bash

n=1
while [ $n -le 5 ]; do
	echo "iteration number $n"
	((n+=1))
done

for fruit in peach orange apple; do
    echo "I like $fruit"
done
