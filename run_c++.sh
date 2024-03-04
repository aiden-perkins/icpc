#!/bin/bash

if [ "$#" == 2 ]; then
    test_count=$(find "$1"/"$2"/ -type f -name "*.in" | wc -l)
    for i in $(seq $test_count); do
        echo Testing file "$i".in...
        g++ "$1"/"$2"/main.cpp -o "$1"/"$2"/main
        ./"$1"/"$2"/main < "$1"/"$2"/"$i".in > "$1"/"$2"/"$i".out
        diff "$1"/"$2"/"$i".out "$1"/"$2"/"$i".ans
        echo
    done
else
    echo Testing file "$3".in...
    g++ "$1"/"$2"/main.cpp -o "$1"/"$2"/main
    ./"$1"/"$2"/main < "$1"/"$2"/"$3".in > "$1"/"$2"/"$3".out
    diff "$1"/"$2"/"$3".out "$1"/"$2"/"$3".ans
    echo
fi
