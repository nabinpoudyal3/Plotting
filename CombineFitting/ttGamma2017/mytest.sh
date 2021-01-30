#!/bin/bash

#ValidateDatacards.py datacard_both_2017.txt --printLevel 3 --checkUncertOver 0.1
#closure test
text2workspace.py datacard_both_2017.txt
combine datacard_both_2017.root -M FitDiagnostics -n .datacard_both_2017 --plots -t -1 --expectSignal 1 -s 314159  --saveNormalizations -v2 --rMin=0 --rMax=5
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_both_2017.root --all

combine -M MultiDimFit datacard_both_2017.root  -s 314159  --rMin=0 --rMax=5 --algo grid --points 500 -n .Main   --robustFit=1
combine -M MultiDimFit datacard_both_2017.root -n .snapshot -s 314159  --rMin=0 --rMax=5 --saveWorkspace   --robustFit=1
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin -5 --rMax 5 --algo grid --points 500   --freezeNuisanceGroups mySyst --snapshotName MultiDimFit  --robustFit=1
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_both_2017

# data seems to not failed in minimization so use --robustFit=1 
#combineTool.py -M Impacts -d datacard_both_2017.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
#combineTool.py -M Impacts -d datacard_both_2017.root -m 125 -t -1 --expectSignal 1 --doFits 
#combineTool.py -M Impacts -d datacard_both_2017.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_both_2017.json 
#plotImpacts.py -i impacts_toy_both_2017.json -o impacts_toy_both_2017

#combineTool.py -M Impacts -d datacard_both_2017.root -m 125 --doInitialFit --robustFit=1 
#combineTool.py -M Impacts -d datacard_both_2017.root -m 125 --doFits --robustFit=1 
#combineTool.py -M Impacts -d datacard_both_2017.root -m 125 -o impacts_data_2017.json  
#plotImpacts.py -i impacts_data_both_2017.json -o impacts_data_both_2017

##############
####       ###
##############
#
#ValidateDatacards.py datacard_mu_2017.txt --printLevel 3 --checkUncertOver 0.1
##closure test
text2workspace.py datacard_mu_2017.txt
combine datacard_mu_2017.root -M FitDiagnostics -n .datacard_mu_2017 --plots -t -1 --expectSignal 1 -s 314159   --saveNormalizations -v2 --rMin=0 --rMax=5
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_mu_2017.root --all

combine -M MultiDimFit datacard_mu_2017.root  -s 314159  --rMin=0 --rMax=5 --algo grid --points 500 -n .Main  
combine -M MultiDimFit datacard_mu_2017.root -n .snapshot -s 314159  --rMin=0 --rMax=5 --saveWorkspace  
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin=0 --rMax=5 --algo grid --points 500   --freezeNuisanceGroups mySyst --snapshotName MultiDimFit
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_mu_2017
#
## data seems to not failed in minimization so use --robustFit=1 
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -t -1 --expectSignal 1 --doFits 
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2017_mu.json 
#plotImpacts.py -i impacts_toy_2017_mu.json -o impacts_toy_2017_mu
#
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 --doInitialFit 
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 --doFits 
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -o impacts_data_2017_mu.json  
#plotImpacts.py -i impacts_data_2017_mu.json -o impacts_data_2017_mu
#
##############
####       ###
##############
#
#ValidateDatacards.py datacard_ele_2017.txt --printLevel 3 --checkUncertOver 0.1
##closure test
text2workspace.py datacard_ele_2017.txt
combine datacard_ele_2017.root -M FitDiagnostics -n .datacard_ele_2017 --plots -t -1 --expectSignal 1 -s 314159   --saveNormalizations -v2 --rMin=0 --rMax=5
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_ele_2017.root --all
#
combine -M MultiDimFit datacard_ele_2017.root  -s 314159  --rMin=0 --rMax=5 --algo grid --points 500 -n .Main  
combine -M MultiDimFit datacard_ele_2017.root -n .snapshot -s 314159  --rMin=0 --rMax=5 --saveWorkspace  
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin=0 --rMax=5 --algo grid --points 500   --freezeNuisanceGroups mySyst --snapshotName MultiDimFit
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_ele_2017
#
## data seems to not failed in minimization so use --robustFit=1 
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -t -1 --expectSignal 1 --doFits 
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2017_mu.json 
#plotImpacts.py -i impacts_toy_2017_mu.json -o impacts_toy_2017_mu
#
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 --doInitialFit 
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 --doFits 
#combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -o impacts_data_2017_mu.json  
#plotImpacts.py -i impacts_data_2017_mu.json -o impacts_data_2017_mu
