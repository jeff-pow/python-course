# !/bin/bash

for i in {1..5}; do
    python3 project1.py < input0${i}.txt > actual0${i}.txt
    diff expected0${i}.txt actual0${i}.txt
done
