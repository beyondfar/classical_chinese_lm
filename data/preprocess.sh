#!/bin/bash

git clone https://github.com/NiuTrans/Classical-Modern.git
python prepare_corpus.py
python tokenize.py
