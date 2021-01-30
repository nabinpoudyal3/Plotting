#!/bin/bash

##$1= control region with year
declare -a CHANNEL=("ele")
#declare -a YEAR=("2018" "2018" "2018")
declare -a YEAR=("2018")
#declare -a DISTRIBUTION=("M3" "ChIso" "M30photon" "M30btag")
declare -a DISTRIBUTION=("M30btag")


#ValidateDatacards.py datacard_ele_2018_M30photon.txt --printLevel 3 --checkUncertOver 0.1
#
##closure test
#text2workspace.py datacard_ele_2018_M30photon.txt
#combine datacard_ele_2018_M30photon.root -M FitDiagnostics -n .datacard_ele_2018_M30photon -t -1 --expectSignal 1 -s 314159  
#python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_ele_2018_M30photon.root --all
#
## data seems to not failed in minimization so use --robustFit=1 to 
#combineTool.py -M Impacts -d datacard_ele_2018_M30photon.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
#combineTool.py -M Impacts -d datacard_ele_2018_M30photon.root -m 125 -t -1 --expectSignal 1 --doFits 
#combineTool.py -M Impacts -d datacard_ele_2018_M30photon.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2018_M30photon.json
#plotImpacts.py -i impacts_toy_2018_M30photon.json -o impacts_toy_2018_M30photon
#
#
#combineTool.py -M Impacts -d datacard_ele_2018_M30photon.root -m 125 --doInitialFit --robustFit=1
#combineTool.py -M Impacts -d datacard_ele_2018_M30photon.root -m 125 --doFits --robustFit=1
#combineTool.py -M Impacts -d datacard_ele_2018_M30photon.root -m 125 -o impacts_data_2018_M30photon.json 
#plotImpacts.py -i impacts_data_2018_M30photon.json -o impacts_data_2018_M30photon
#
#
#for dist in ${DISTRIBUTION[@]};do
#	for year in ${YEAR[@]}; do
#		for channel in ${CHANNEL[@]}; do
#			text2workspace.py datacard_"$channel"_"$year"_"$dist".txt
#			combine -M MultiDimFit datacard_"$channel"_"$year"_"$dist".root  -s 314159  --rMin -5 --rMax 5 --algo grid --points 500 -n .Main
#			combine -M MultiDimFit datacard_"$channel"_"$year"_"$dist".root -n .snapshot -s 314159  --rMin -5 --rMax 5 --saveWorkspace
#			combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin -5 --rMax 5 --algo grid --points 500 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit
#			python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_"$channel"_"$year"_"$dist"
#		done
#	done
#done
#
#exit 1

ValidateDatacards.py datacard_ele_2018_M3.txt --printLevel 3 --checkUncertOver 0.1

#closure test
text2workspace.py datacard_ele_2018_M3.txt
combine datacard_ele_2018_M3.root -M FitDiagnostics -n .datacard_ele_2018_M3 -t -1 --expectSignal 1 -s 314159  --saveNLL --autoBoundsPOIs * --saveNormalizations --saveShapes --saveWithUncertainties --justFit
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_ele_2018_M3.root --all

# data seems to not failed in minimization so use --robustFit=1 to 
combineTool.py -M Impacts -d datacard_ele_2018_M3.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
combineTool.py -M Impacts -d datacard_ele_2018_M3.root -m 125 -t -1 --expectSignal 1 --doFits 
combineTool.py -M Impacts -d datacard_ele_2018_M3.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2018_M3.json
plotImpacts.py -i impacts_toy_2018_M3.json -o impacts_toy_2018_M3


combineTool.py -M Impacts -d datacard_ele_2018_M3.root -m 125 --doInitialFit --robustFit=1
combineTool.py -M Impacts -d datacard_ele_2018_M3.root -m 125 --doFits --robustFit=1
combineTool.py -M Impacts -d datacard_ele_2018_M3.root -m 125 -o impacts_data_2018_M3.json 
plotImpacts.py -i impacts_data_2018_M3.json -o impacts_data_2018_M3


exit 1


ValidateDatacards.py datacard_ele_2018_ChIso.txt --printLevel 3 --checkUncertOver 0.1

#closure test
text2workspace.py datacard_ele_2018_ChIso.txt
combine datacard_ele_2018_ChIso.root -M FitDiagnostics -n .datacard_ele_2018_ChIso -t -1 --expectSignal 1 -s 314159  
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_ele_2018_ChIso.root --all

# data seems to not failed in minimization so use --robustFit=1 to 
combineTool.py -M Impacts -d datacard_ele_2018_ChIso.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
combineTool.py -M Impacts -d datacard_ele_2018_ChIso.root -m 125 -t -1 --expectSignal 1 --doFits 
combineTool.py -M Impacts -d datacard_ele_2018_ChIso.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2018_ChIso.json
plotImpacts.py -i impacts_toy_2018_ChIso.json -o impacts_toy_2018_ChIso


combineTool.py -M Impacts -d datacard_ele_2018_ChIso.root -m 125 --doInitialFit --robustFit=1
combineTool.py -M Impacts -d datacard_ele_2018_ChIso.root -m 125 --doFits --robustFit=1
combineTool.py -M Impacts -d datacard_ele_2018_ChIso.root -m 125 -o impacts_data_2018_ChIso.json 
plotImpacts.py -i impacts_data_2018_ChIso.json -o impacts_data_2018_ChIso



ValidateDatacards.py datacard_ele_2018_M30btag.txt --printLevel 3 --checkUncertOver 0.1

#closure test
text2workspace.py datacard_ele_2018_M30btag.txt
combine datacard_ele_2018_M30btag.root -M FitDiagnostics -n .datacard_ele_2018_M30btag -t -1 --expectSignal 1 -s 314159  
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_ele_2018_M30btag.root --all

# data seems to not failed in minimization so use --robustFit=1 to 
combineTool.py -M Impacts -d datacard_ele_2018_M30btag.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
combineTool.py -M Impacts -d datacard_ele_2018_M30btag.root -m 125 -t -1 --expectSignal 1 --doFits 
combineTool.py -M Impacts -d datacard_ele_2018_M30btag.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2018_M30btag.json
plotImpacts.py -i impacts_toy_2018_M30btag.json -o impacts_toy_2018_M30btag


combineTool.py -M Impacts -d datacard_ele_2018_M30btag.root -m 125 --doInitialFit --robustFit=1
combineTool.py -M Impacts -d datacard_ele_2018_M30btag.root -m 125 --doFits --robustFit=1
combineTool.py -M Impacts -d datacard_ele_2018_M30btag.root -m 125 -o impacts_data_2018_M30btag.json 
plotImpacts.py -i impacts_data_2018_M30btag.json -o impacts_data_2018_M30btag
