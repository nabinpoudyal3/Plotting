#!/bin/bash
declare -a CONTROLREGION=("CR123" "CR1" "CR2" "CR3" "CR4" "CR5" "CR6" "CR7" "SR8" )
declare -a YEAR=("2016" "2017" "2018")
#declare -a CONTROLREGION=("CR123")
#declare -a YEAR=("2016")
rMin=0
rMax=5
points=300
for year in ${YEAR[@]}; do
	for controlregion in ${CONTROLREGION[@]}; do
		text2workspace.py datacard_"$controlregion"_"$year".txt
		combine -M MultiDimFit datacard_"$controlregion"_"$year".root  -s 314159  --rMin $rMin --rMax $rMax --algo grid --points $points -n .Main --robustFit=1
		combine -M MultiDimFit datacard_"$controlregion"_"$year".root -n .snapshot -s 314159  --rMin $rMin --rMax $rMax --saveWorkspace --robustFit=1
		combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin $rMin --rMax $rMax --algo grid --points $points --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --robustFit=1
		python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_"$controlregion"_"$year"

	done
done

#exit 1
## data seems to not failed in minimization so use --robustFit=1 to 
#

#
#
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --doInitialFit --robustFit=1
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --doFits --robustFit=1
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -o impacts_data_2016.json 
#plotImpacts.py -i impacts_data_2016.json -o impacts_data_2016


#ValidateDatacards.py datacard_CR123_2016.txt --printLevel 3 --checkUncertOver 0.1
#closure test
#text2workspace.py datacard_CR123_2016.txt
#combine datacard_CR123_2016.root -M FitDiagnostics -n CR123_2016 --plots -t -1 --expectSignal 1 -s 314159  --saveNormalizations -v2 --rMin=0 --rMax=5
#python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnosticsCR123_2016.root --all

#combine -M MultiDimFit datacard_CR123_2016.root  -s 314159  --rMin 0 --rMax 5 --algo grid --points 500 -n .Main   --robustFit=1
#combine -M MultiDimFit datacard_CR123_2016.root -n .snapshot -s 314159  --rMin 0 --rMax 5 --saveWorkspace   --robustFit=1
#combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin 0 --rMax 5 --algo grid --points 500   --freezeNuisanceGroups mySyst --snapshotName MultiDimFit  --robustFit=1
#python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_CR123_2016

#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --expectSignal 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2016.json
#plotImpacts.py -i impacts_toy_2016.json -o impacts_toy_2016

#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --doInitialFit --robustFit=1
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --doFits --robustFit=1
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -o impacts_data_2016.json --robustFit=1
#plotImpacts.py -i impacts_data_2016.json -o impacts_data_2016


#--robustFit=1
