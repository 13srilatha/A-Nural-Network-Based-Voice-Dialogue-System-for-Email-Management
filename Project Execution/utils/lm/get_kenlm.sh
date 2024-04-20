#!/bin/bash
wget -O - https://kheafield.com/code/kenlm.tar.gz |tar xz
mkdir kenlm/build
cd kenlm/build
cmake ..
make -j2
#cd ..
#python3 -m venv newv
#source /mnt/c/Users/srila/OneDrive/Desktop/project2/blind-mailAI/newv/scripts/activate
#python3 -m pip install -e .