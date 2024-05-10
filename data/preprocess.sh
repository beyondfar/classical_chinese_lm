#!/bin/bash

if [[ ! -d "Classical-Modern" ]]; then
  git clone https://github.com/NiuTrans/Classical-Modern.git
fi
python prepare_corpus.py

awk 'BEGIN{srand();}{print rand()"\t"$0}' classical_corpus/classical_articals.txt | sort | cut -f 2 > classical_corpus/classical_articals.sort
mv classical_corpus/classical_articals.sort classical_corpus/classical_articals.txt

python tokenize.py
