#!/bin/bash

#echo "Running makeAllZJets Prefit for all 3 years"
#./makeAllZJetsPrefit.sh
#echo "Now Run combine Jupyter and get ZJetsSF for all 3 years!!"
#while [ true ] ; do
#	read -t 60 -n 1
#	if [ $? = 0 ] ; then
#	echo "got all Zjets SFs"
#	break;
#	else
#	echo "waiting to finish extraction of ZJetsSF."
#	fi
#done

echo "Now running makeAllMisIDPrefit.sh Prefit for all 3 years"
./makeAllMisIDPrefit.sh

echo "Run makeAllYearSystTemplateForMisIDElePrefitRoot.sh to make nominal and syst templates for misIDEle "
./makeAllYearSystTemplateForMisIDElePrefitRoot.sh


echo "Runing Up, Down and nominal plots creator "
./makeUpDown.sh

echo "Running combine fitting"

cd CombineFitting/MisIDEleFittingSystematicsSeparateYear

./runFitting.sh

cd ../..

echo "Now Run combine Jupyter and get MisIDEleSF, misID and VG vs jetmultiplicity plots plots, for all 3 years!!"


while [ true ] ; do
	read -t 60 -n 1
	if [ $? = 0 ] ; then
	echo "got all MisIDEleSFs"
	break;	
	else
	echo "waiting to finish the extraction of MisIDEleSF and plots."
	fi
done

echo "Now runing  all postfit plots "
#./makeAllZJetsPostfit.sh
./makeAllMisIDPostfit.sh
echo "Copy Pre post plots and tex files to make slides"
