#!/bin/sh

echo "running kima examples"

cd examples

for e in 51Peg #BL2009 CoRoT7
do
    cd $e
    pwd
    
    $HOME/run
    
    # report
    jupyter nbconvert --to notebook $HOME/templates/report.ipynb --output-dir .
    jupyter nbconvert --to html --execute report.ipynb

    cd ..
done
