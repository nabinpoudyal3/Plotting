#!/bin/bash



year="2016"
controlregion="CR123"
points="500"

echo $year
echo $points

#text2workspace.py  datacard_"$controlregion"_"$year".txt -v 0 

#combine datacard_"$controlregion"_"$year".root  -M FitDiagnostics -n .datacard_"$controlregion"_"$year" --toys=-1 --expectSignal=1  --seed=314159 -v1 --rMin=0 --rMax=5 
#python diffNuisances.py fitDiagnostics.datacard_"$controlregion"_"$year".root --all 

# exit 1

#combine  -M MultiDimFit datacard_"$controlregion"_"$year".root -s 314159 --algo grid --points=$points -n .total_toy --rMin=0 --rMax=5 -v 0 -t -1 --expectSignal=1 
#combine  -M MultiDimFit datacard_"$controlregion"_"$year".root -s 314159  --saveWorkspace -n .snapshot_toy --rMin=0 --rMax=5 -t -1 --expectSignal=1 
#combine  -M MultiDimFit higgsCombine.snapshot_toy.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll_toy  --algo grid --points=$points --freezeNuisanceGroups mySyst -t -1 --expectSignal=1 --snapshotName MultiDimFit --rMin=0 --rMax=5 
#python plot1DScan.py  higgsCombine.total_toy.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll_toy.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_toy_"$controlregion"_"$year" 

#combine  -M MultiDimFit datacard_"$controlregion"_"$year".root -s 314159 --algo grid --points=$points -n .total_data --rMin=0 --rMax=5 -v 0 
#combine  -M MultiDimFit datacard_"$controlregion"_"$year".root -s 314159  --saveWorkspace -n .snapshot_data --rMin=0 --rMax=5  
#combine  -M MultiDimFit higgsCombine.snapshot_data.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll_data  --algo grid --points=$points --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --rMin=0 --rMax=5 
#python plot1DScan.py  higgsCombine.total_data.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll_data.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_data_"$controlregion"_"$year" 

# exit 1
#combine -M FitDiagnostics -n "$controlregion"_"$year" datacard_"$controlregion"_"$year".root --plots --saveNLL --robustFit=1 -s 314159 --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --skipBOnlyFit -v1

combineTool.py  -M Impacts -d datacard_"$controlregion"_"$year".root -m 125  --doInitialFit                                -t -1 --expectSignal=1 --freezeNuisanceGroups autoMCStats --robustFit=1 --rMin=0.1 --rMax=2  
combineTool.py  -M Impacts -d datacard_"$controlregion"_"$year".root -m 125  --doFits                                      -t -1 --expectSignal=1 --freezeNuisanceGroups autoMCStats --robustFit=1 --rMin=0.1 --rMax=2 --parallel 24
combineTool.py  -M Impacts -d datacard_"$controlregion"_"$year".root -m 125  -o impacts_toy_"$controlregion"_"$year".json  -t -1 --expectSignal=1 --freezeNuisanceGroups autoMCStats --robustFit=1 --rMin=0.1 --rMax=2 
plotImpacts.py -i impacts_toy_"$controlregion"_"$year".json -o impacts_toy_"$controlregion"_"$year" 

combineTool.py  -M Impacts -d datacard_"$controlregion"_"$year".root -m 125  --doInitialFit                                --robustFit=1 --rMin=0.1 --freezeNuisanceGroups autoMCStats --rMax=2  
combineTool.py  -M Impacts -d datacard_"$controlregion"_"$year".root -m 125  --doFits                                      --robustFit=1 --rMin=0.1 --freezeNuisanceGroups autoMCStats --rMax=2 --parallel 24
combineTool.py  -M Impacts -d datacard_"$controlregion"_"$year".root -m 125  -o impacts_data_"$controlregion"_"$year".json --robustFit=1 --rMin=0.1 --freezeNuisanceGroups autoMCStats --rMax=2 
plotImpacts.py -i impacts_data_"$controlregion"_"$year".json -o impacts_data_"$controlregion"_"$year" 

#python makeCovarianceMatrix.py

exit 1

--X-rtd MINIMIZER_analytic # use this for sth, see combine tutorial
