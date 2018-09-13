#!/bin/bash

pygmentize -O full,style=stata -f html -l stata -o compiled/sample-do.html  sample-hljs.do
pygmentize -O full,style=sas   -f html -l sas   -o compiled/sample-sas.html sample-hljs.sas
pandoc sample-pandoc.md \
    -o compiled/sample-pandoc.html \
    --syntax-definition=../skylighting/stata.xml \
    --syntax-definition=../skylighting/sas.xml \
    --highlight-style=tango --standalone
