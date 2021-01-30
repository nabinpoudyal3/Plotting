#!/bin/bash

ValidateDatacards.py datacard_both_2016_4.txt --printLevel 3 --checkUncertOver 0.1
#closure test
text2workspace.py datacard_both_2016_4.txt
#combine datacard_both_2016_4.root -M FitDiagnostics -n .datacard_both_2016_4 -t -1 --expectSignal 1 -s 314159  --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF  --autoBoundsPOIs "*" --saveNormalizations -v2
combine datacard_both_2016_4.root -M FitDiagnostics -n .datacard_both_2016_4 -t -1 --expectSignal 1 -s 314159  --autoBoundsPOIs "*" --saveNormalizations -v2
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_both_2016_4.root --all

combine -M MultiDimFit datacard_both_2016_4.root  -s 314159  --rMin -5 --rMax 5 --algo grid --points 500 -n .Main --autoBoundsPOIs "*" 
combine -M MultiDimFit datacard_both_2016_4.root -n .snapshot -s 314159  --rMin -5 --rMax 5 --saveWorkspace --autoBoundsPOIs "*" 
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin -5 --rMax 5 --algo grid --points 500 --autoBoundsPOIs "*"  --freezeNuisanceGroups mySyst --snapshotName MultiDimFit
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_both_2016_4

# data seems to not failed in minimization so use --robustFit=1 
combineTool.py -M Impacts -d datacard_both_2016_4.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
combineTool.py -M Impacts -d datacard_both_2016_4.root -m 125 -t -1 --expectSignal 1 --doFits 
combineTool.py -M Impacts -d datacard_both_2016_4.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2016_4.json 
plotImpacts.py -i impacts_toy_2016_4.json -o impacts_toy_2016_4

combineTool.py -M Impacts -d datacard_both_2016_4.root -m 125 --doInitialFit 
combineTool.py -M Impacts -d datacard_both_2016_4.root -m 125 --doFits 
combineTool.py -M Impacts -d datacard_both_2016_4.root -m 125 -o impacts_data_2016_4.json  
plotImpacts.py -i impacts_data_2016_4.json -o impacts_data_2016_4

#############
###       ###
#############

ValidateDatacards.py datacard_both_2017_4.txt --printLevel 3 --checkUncertOver 0.1
#closure test
text2workspace.py datacard_both_2017_4.txt
#combine datacard_both_2017_4.root -M FitDiagnostics -n .datacard_both_2017_4 -t -1 --expectSignal 1 -s 314159  --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF  --autoBoundsPOIs "*" --saveNormalizations -v2
combine datacard_both_2017_4.root -M FitDiagnostics -n .datacard_both_2017_4 -t -1 --expectSignal 1 -s 314159  --autoBoundsPOIs "*" --saveNormalizations -v2
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_both_2017_4.root --all

combine -M MultiDimFit datacard_both_2017_4.root  -s 314159  --rMin -5 --rMax 5 --algo grid --points 500 -n .Main --autoBoundsPOIs "*" 
combine -M MultiDimFit datacard_both_2017_4.root -n .snapshot -s 314159  --rMin -5 --rMax 5 --saveWorkspace --autoBoundsPOIs "*" 
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin -5 --rMax 5 --algo grid --points 500 --autoBoundsPOIs "*"  --freezeNuisanceGroups mySyst --snapshotName MultiDimFit
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_both_2017_4

# data seems to not failed in minimization so use --robustFit=1 
combineTool.py -M Impacts -d datacard_both_2017_4.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
combineTool.py -M Impacts -d datacard_both_2017_4.root -m 125 -t -1 --expectSignal 1 --doFits 
combineTool.py -M Impacts -d datacard_both_2017_4.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2017_4.json 
plotImpacts.py -i impacts_toy_2017_4.json -o impacts_toy_2017_4

combineTool.py -M Impacts -d datacard_both_2017_4.root -m 125 --doInitialFit  
combineTool.py -M Impacts -d datacard_both_2017_4.root -m 125 --doFits  
combineTool.py -M Impacts -d datacard_both_2017_4.root -m 125 -o impacts_data_2017_4.json  
plotImpacts.py -i impacts_data_2017_4.json -o impacts_data_2017_4

#############
###       ###
#############

ValidateDatacards.py datacard_both_2018_4.txt --printLevel 3 --checkUncertOver 0.1
#closure test
text2workspace.py datacard_both_2018_4.txt
#combine datacard_both_2018_4.root -M FitDiagnostics -n .datacard_both_2018_4 -t -1 --expectSignal 1 -s 314159  --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF  --autoBoundsPOIs "*" --saveNormalizations -v2
combine datacard_both_2018_4.root -M FitDiagnostics -n .datacard_both_2018_4 -t -1 --expectSignal 1 -s 314159  --autoBoundsPOIs "*" --saveNormalizations -v2
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.datacard_both_2018_4.root --all

combine -M MultiDimFit datacard_both_2018_4.root  -s 314159  --rMin -5 --rMax 5 --algo grid --points 500 -n .Main --autoBoundsPOIs "*" 
combine -M MultiDimFit datacard_both_2018_4.root -n .snapshot -s 314159  --rMin -5 --rMax 5 --saveWorkspace --autoBoundsPOIs "*" 
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin -5 --rMax 5 --algo grid --points 500 --autoBoundsPOIs "*"  --freezeNuisanceGroups mySyst --snapshotName MultiDimFit
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_both_2018_4

# data seems to not failed in minimization so use --robustFit=1 
combineTool.py -M Impacts -d datacard_both_2018_4.root -m 125 -t -1 --expectSignal 1 --doInitialFit  
combineTool.py -M Impacts -d datacard_both_2018_4.root -m 125 -t -1 --expectSignal 1 --doFits 
combineTool.py -M Impacts -d datacard_both_2018_4.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_2018_4.json 
plotImpacts.py -i impacts_toy_2018_4.json -o impacts_toy_2018_4

combineTool.py -M Impacts -d datacard_both_2018_4.root -m 125 --doInitialFit  
combineTool.py -M Impacts -d datacard_both_2018_4.root -m 125 --doFits  
combineTool.py -M Impacts -d datacard_both_2018_4.root -m 125 -o impacts_data_2018_4.json  
plotImpacts.py -i impacts_data_2018_4.json -o impacts_data_2018_4

