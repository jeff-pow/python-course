# !/bin/bash

for i in {1..4}; do
    python3 lab3.py < input0${i}.txt > actual0${i}.txt
    diff expected0${i}.txt actual0${i}.txt
done
