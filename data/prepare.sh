#!/bin/bash

#git clone git@github.com:NiuTrans/Classical-Modern.git
cd Classical-Modern
find 古文原文 -name "text.txt" | xargs cat > classical_raw.txt
sed -i .bak 's/\<[^\<\>]*\>//g' classical_raw.txt

