#!/bin/bash

printf "Start Running at ";/bin/date
printf "Worker node hostname ";/bin/hostname
echo "---------------------------------------------"

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
    echo "Running Interactively" ; 
else
    echo "Running In Batch"
    cd ${_CONDOR_SCRATCH_DIR}
    echo ${_CONDOR_SCRATCH_DIR}
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    xrdcp -f root://cmseos.fnal.gov//store/user/npoudyal/CMSSW_10_2_14.tgz .
    tar -xvf CMSSW_10_2_14.tgz
    cd CMSSW_10_2_14/src
    eval `scramv1 runtime -sh`
    cd ../..
    tar -xvf myHistograms.tar

fi

outputdir="root://cmseos.fnal.gov//store/user/npoudyal/Fitting_Test"

text2workspace.py  datacard_ele_2016.txt 

for i in {0..10};do
	for j in {5..30};do
		combine -M MultiDimFit datacard_ele_2016.root -s 314159 --rMin=-$i --rMax=$j --algo grid --points=300 -n .Main --setParameterRanges nonPromptSF=-10,10 -v -1
		combine -M MultiDimFit datacard_ele_2016.root -s 314159 --rMin=-$i --rMax=$j --saveWorkspace -n .snapshot --setParameterRanges nonPromptSF=-10,10 -v -1
		combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll --rMin=-$i --rMax=$j --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --setParameterRanges nonPromptSF=-10,10 -v -1
		python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_-"$i"_"$j"_ele_2016
	done
done


for i in {0..10};do
	for j in {5..30};do
		echo xrdcp -f freeze_-"$i"_"$j"_ele_2016.pdf $outputdir
		xrdcp -f freeze_-"$i"_"$j"_ele_2016.pdf $outputdir
		
	done
done



printf "Done at ";/bin/date


