#!/bin/bash

echo "Starting script"

sum=0

for i in {1..20}
do
  sum=$((sum + i))
done

echo "Sum is $sum"

function print_lines {
  for i in {1..50}
  do
    if (( i % 10 == 0 ))
    then
      echo "Line $i"
    fi
  done
}

print_lines

echo "Done"