#!/bin/bash

#git clone git@github.com:NiuTrans/Classical-Modern.git
cd Classical-Modern
find 古文原文 -name "text.txt" | awk 'BEGIN{srand()}{print rand()"\t"$0}' | sort -r | cut -f2- | xargs cat | sed 's/\<[^\<\>]*\>//g' | awk '{if(length($0)> 10) print}' > classical_raw.txt

