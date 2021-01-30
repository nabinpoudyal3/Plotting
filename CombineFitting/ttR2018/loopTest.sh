#!/bin/bash

text2workspace.py  datacard_ele_2018.txt

for i in {0..10};do
	for j in {5..30};do
		combine -M MultiDimFit datacard_ele_2018.root -s 314159 --rMin=-$i --rMax=$j --algo grid --points=300 -n .Main --setParameterRanges nonPromptSF=-10,10 -v -1
		combine -M MultiDimFit datacard_ele_2018.root -s 314159 --rMin=-$i --rMax=$j --saveWorkspace -n .snapshot --setParameterRanges nonPromptSF=-10,10 -v -1
		combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll --rMin=-$i --rMax=$j --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --setParameterRanges nonPromptSF=-10,10 -v -1
		python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_-"$i"_"$j"_ele_2018 
	done
done

text2workspace.py  datacard_mu_2018.txt

for i in {0..10};do
	for j in {5..30};do
		combine -M MultiDimFit datacard_mu_2018.root -s 314159 --rMin=-$i --rMax=$j --algo grid --points=300 -n .Main --setParameterRanges nonPromptSF=-10,10 -v -1
		combine -M MultiDimFit datacard_mu_2018.root -s 314159 --rMin=-$i --rMax=$j --saveWorkspace -n .snapshot --setParameterRanges nonPromptSF=-10,10 -v -1
		combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll --rMin=-$i --rMax=$j --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --setParameterRanges nonPromptSF=-10,10 -v -1
		python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_-"$i"_"$j"_mu_2018 
	done
done
