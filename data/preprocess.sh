#!/bin/bash

git clone git@github.com:NiuTrans/Classical-Modern.git
python prepare_corpus.py
python tokenize.py
