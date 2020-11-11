#!/bin/bash

rm *.root
rm *.png
rm *.pdf
rm *.json

./allCombine.sh

./oneEle.sh
./oneMu.sh
./oneBoth.sh

wait

echo "python make2016ttGammaSS.py"
python make2016ttGammaSS.py
echo "python make2016ttGammaSS_Toy.py"
python make2016ttGammaSS_Toy.py
echo "python make2016ttGammaSS_Toy.py"
python make2016ttGammaSS_Asimov.py
echo "python makeCovarianceMatrix.py"
python makeCovarianceMatrix.py
echo "python getTrackParameterPlots.py"
python getTrackParameterPlots.py
echo "python getNPToyDistribution.py"
python getNPToyDistribution.py

cd ../../
./makePrePostFitTTGamma.sh
cd CombineFitting/ttGamma

