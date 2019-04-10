#!/bin/sh

echo "running kima examples"

cd $SHIPPABLE_BUILD_DIR/kima
cd examples

for e in 51Peg #BL2009 CoRoT7
do
    cd $e
    pwd

    $SHIPPABLE_BUILD_DIR/run
    
    # report
    jupyter nbconvert --to notebook $SHIPPABLE_BUILD_DIR/templates/report.ipynb --output-dir .
    jupyter nbconvert --to html --execute report.ipynb

    cd ..
    
done
