#!/bin/bash

run()
{
    echo "Running: $1"
    eval "$1"
}

Check()
{

    echo "Checking correctness againts small test sample\n"
    cmd="python3 run_book.py -i data/input/check.txt -o data/output/check.txt"
    run "$cmd"

    cmd="diff data/output/check_golden.txt  data/output/check.txt"
    run "$cmd"

    if [ $? -eq 0 ]
    then
      echo "No differences between the golden output and your output!"
    else
      echo "There were differences between the golden output and your output :("
    fi
}

Run()
{
    echo "Checking correctness agaisnt full orders file"
    cmd="python3 run_book.py -i data/input/test.txt -o data/output/test.txt"
    run "$cmd"

    cmd="diff data/output/golden.txt  data/output/test.txt"
    run "$cmd"

    if [ $? -eq 0 ]
    then
      echo "No differences between the golden output and your output!"
    else
      echo "There were differences between the golden output and your output :("
    fi
}

Time()
{
    echo "Timing run on full orders file"
    cmd="time python3 run_book.py -i data/input/test.txt -o data/output/test_time.txt"
    run "$cmd"
}

tar xf data.tar.gz

while getopts ":crt" option; do
    case $option in
        c) # Check correctness against small test sample
            Check
            break;;
        r) # Check correctness against full orders file
            Run
            break;;
        t) # Time run on full orders file
            Time
            break;;
    esac
done
            
