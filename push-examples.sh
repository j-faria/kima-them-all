#!/bin/sh

cd $SHIPPABLE_BUILD_DIR

for e in 51Peg #BL2009 CoRoT7
do
    mv kima/examples/$e/report.html reports/report_$e.html
done

git add reports
git commit -m "ran examples on shippable [ci skip]"
git push
