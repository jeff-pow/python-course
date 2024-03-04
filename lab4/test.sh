# !/bin/bash

for i in {1..1}; do
    python3 lab4.py < actual0${i}.txt
    echo "expected0${i}.txt"
    sdiff expected0${i}.txt actual0${i}.txt
#    meld expected0${i}.txt actual0${i}.txt
done

