#!/bin/bash

#important notes:

#--exclude lumi --splitInitial --allPars --approx
#combineTool.py -M Impacts -d datacard_ele_2018.root -m 125  --doInitialFit                 -t 10 --expectSignal 1  --rMin=-1 --rMax=10
#combineTool.py -M Impacts -d datacard_ele_2018.root -m 125  --doFits                       -t 10 --expectSignal 1  --rMin=-1 --rMax=10
#combineTool.py -M Impacts -d datacard_ele_2018.root -m 125  -o impacts_toy_ele_2018.json   -t 10 --expectSignal 1  --rMin=-1 --rMax=10
#plotImpacts.py -i impacts_toy_ele_2018.json -o impacts_toy_ele_2018 

#submitting the crab3 jobs
#combineTool.py -M FitDiagnostics -n .test -d datacard_ele_2018.root --toys=1000 --expectSignal=1 --seed=314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm --saveNormalizations --rMin=-1 --rMax=5 --setParameterRanges nonPromptSF=-10,10 --minos all --saveToys --job-mode crab3 --task-name grid-test --dry-run
# 
#python mlfitNormsToText.py fitDiagnosticsel_2018.root --uncertainties

text2workspace.py  datacard_ele_2018.txt
ValidateDatacards.py datacard_ele_2018.txt --printLevel 3 --checkUncertOver 0.1
combine -M ChannelCompatibilityCheck datacard_ele_2018.root -v2

# old combine datacard_ele_2018.root -M FitDiagnostics -n=.datacard_ele_2018 --toys=-1 --expectSignal=1 --seed=314159 --redefineSignalPOIs=r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm -v2 --rMin=-2 --rMax=5 --setParameterRanges nonPromptSF=-10,10
combine datacard_ele_2018.root -M FitDiagnostics -n .datacard_ele_2018 --toys=-1 --expectSignal=1 --seed=314159 --redefineSignalPOIs=r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm -v2 --rMin=-2 --rMax=5 --setParameterRanges nonPromptSF=-10,10 --minos all
python diffNuisances.py fitDiagnostics.datacard_ele_2018.root --all -g plots_ele_2018.root

exit 1


combine -M MultiDimFit datacard_ele_2018.root -s 314159 --rMin=-1 --rMax=10 --algo grid --points=300 -n .Main --setParameterRanges nonPromptSF=-10,10 
combine -M MultiDimFit datacard_ele_2018.root -s 314159 --rMin=-1 --rMax=10 --saveWorkspace -n .snapshot --setParameterRanges nonPromptSF=-10,10 
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll --rMin=-1 --rMax=10 --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --setParameterRanges nonPromptSF=-10,10
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_ele_2018 

combine -H FitDiagnostics -n .hint_ele_2018 datacard_ele_2018.root -s 314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm -v2 --rMin=-1 --rMax=10 

combine -M FitDiagnostics -n   el_2018     datacard_ele_2018.root   -s 314159 --plots --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm --saveShapes --saveWithUncertainties  -v2  --rMin=-1 --rMax=10  --setParameterRanges nonPromptSF=-10,10 --minos all

combine -M FitDiagnostics -n .TOY_ele_2018 datacard_ele_2018.root --toys=100 --expectSignal=1 --seed=314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm --saveShapes --saveNormalizations --rMin=-1 --rMax=10 --setParameterRanges nonPromptSF=-10,10 --minos all --saveToys

combineTool.py -M Impacts -d datacard_ele_2018.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --rMin=-1 --rMax=10
combineTool.py -M Impacts -d datacard_ele_2018.root -m 125  --doFits                       -t -1 --expectSignal 1  --rMin=-1 --rMax=10
combineTool.py -M Impacts -d datacard_ele_2018.root -m 125  -o impacts_toy_ele_2018.json   -t -1 --expectSignal 1  --rMin=-1 --rMax=10
plotImpacts.py -i impacts_toy_ele_2018.json -o impacts_toy_ele_2018 

combineTool.py -M Impacts -d datacard_ele_2018.root -m 125  --doInitialFit                 --rMin=-1 --rMax=10 --robustFit=1   
combineTool.py -M Impacts -d datacard_ele_2018.root -m 125  --doFits                       --rMin=-1 --rMax=10 --robustFit=1   
combineTool.py -M Impacts -d datacard_ele_2018.root -m 125  -o impacts_data_ele_2018.json  --rMin=-1 --rMax=10 --robustFit=1  --algo grid 
plotImpacts.py -i impacts_data_ele_2018.json -o impacts_data_ele_2018 

#The following test to find out the range of 
#combine -M Asymptotic htt_mt.root -m 125

text2workspace.py  datacard_mu_2018.txt

ValidateDatacards.py datacard_mu_2018.txt --printLevel 3 --checkUncertOver 0.1

combine -M ChannelCompatibilityCheck datacard_mu_2018.root -v2

combine datacard_mu_2018.root -M FitDiagnostics -n .datacard_mu_2018 --plots -t -1 --expectSignal 1 -s 314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm --saveNormalizations -v2 --rMin=-1 --rMax=5 --saveShapes --setParameterRanges nonPromptSF=-10,10 --minos all --minos all --trackParameters PhoEff,Q2,misIDE,PU,isr,EleEff,fsr,BTagSF_b,lumi,BTagSF_l,MuEff,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm

python diffNuisances.py fitDiagnostics.datacard_mu_2018.root --all

combine -M MultiDimFit datacard_mu_2018.root -s 314159 --rMin=-1 --rMax=5 --algo grid --points=300 -n .Main --setParameterRanges nonPromptSF=-10,10 --minos all
combine -M MultiDimFit datacard_mu_2018.root -s 314159 --rMin=-1 --rMax=5 --saveWorkspace -n .snapshot --setParameterRanges nonPromptSF=-10,10 --minos all
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll --rMin=-1 --rMax=5 --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --setParameterRanges nonPromptSF=-10,10 --minos all
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_mu_2018 

combine -H FitDiagnostics -n mu_2018 datacard_mu_2018.root -s 314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm -v2 --rMin=-1 --rMax=5 

combine -M FitDiagnostics -n   mu_2018     datacard_mu_2018.root   -s 314159 --plots --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm --saveShapes --saveNormalizations  -v2  --rMin=-1 --rMax=5  --setParameterRanges nonPromptSF=-10,10 --minos all

combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --rMin=-1 --rMax=5
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  --doFits                       -t -1 --expectSignal 1  --rMin=-1 --rMax=5
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  -o impacts_toy_mu_2018.json    -t -1 --expectSignal 1  --rMin=-1 --rMax=5
plotImpacts.py -i impacts_toy_mu_2018.json -o impacts_toy_mu_2018 

combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  --doInitialFit                  --rMin=-1 --rMax=5 --robustFit=1
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  --doFits                        --rMin=-1 --rMax=5 --robustFit=1
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  -o impacts_data_mu_2018.json    --rMin=-1 --rMax=5 --robustFit=1
plotImpacts.py -i impacts_data_mu_2018.json -o impacts_data_mu_2018 

text2workspace.py  datacard_both_2018.txt
ValidateDatacards.py datacard_both_2018.txt --printLevel 3 --checkUncertOver 0.1
combine -M ChannelCompatibilityCheck datacard_both_2018.root -v2
combine datacard_both_2018.root -M FitDiagnostics -n .datacard_both_2018 --plots -t -1 --expectSignal 1 -s 314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm --saveNormalizations -v2 --rMin=-1 --rMax=5 --saveShapes --setParameterRanges nonPromptSF=-10,10 --minos all
python diffNuisances.py fitDiagnostics.datacard_both_2018.root --all

combine -M MultiDimFit datacard_both_2018.root -s 314159 --rMin=-1 --rMax=5 --algo grid --points=300 -n .Main --setParameterRanges nonPromptSF=-10,10 --minos all
combine -M MultiDimFit datacard_both_2018.root -s 314159 --rMin=-1 --rMax=5 --saveWorkspace -n .snapshot --setParameterRanges nonPromptSF=-10,10 --minos all
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll --rMin=-1 --rMax=5 --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --setParameterRanges nonPromptSF=-10,10 --minos all
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_ele_2018 

combine -H FitDiagnostics -n both_2018 datacard_both_2018.root -s 314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm -v2 --rMin=-1 --rMax=5 

combine -M FitDiagnostics -n   both_2018     datacard_both_2018.root   -s 314159 --plots --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm --saveShapes --saveNormalizations  -v2  --rMin=-1 --rMax=5  --setParameterRanges nonPromptSF=-10,10 --minos all

combineTool.py -M Impacts -d datacard_both_2018.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --rMin=-1 --rMax=5
combineTool.py -M Impacts -d datacard_both_2018.root -m 125  --doFits                       -t -1 --expectSignal 1  --rMin=-1 --rMax=5
combineTool.py -M Impacts -d datacard_both_2018.root -m 125  -o impacts_toy_both_2018.json  -t -1 --expectSignal 1  --rMin=-1 --rMax=5
plotImpacts.py -i impacts_toy_both_2018.json -o impacts_toy_both_2018 

combineTool.py -M Impacts -d datacard_both_2018.root -m 125  --doInitialFit                  --rMin=-1 --rMax=5 --robustFit=1
combineTool.py -M Impacts -d datacard_both_2018.root -m 125  --doFits                        --rMin=-1 --rMax=5 --robustFit=1
combineTool.py -M Impacts -d datacard_both_2018.root -m 125  -o impacts_data_ele_2018.json   --rMin=-1 --rMax=5 --robustFit=1
plotImpacts.py -i impacts_data_both_2018.json -o impacts_data_both_2018 




#check the follwoing

exit 1


>>>There were  19 warnings of type  'up/down templates vary the yield in the same direction'
    For uncertainty isr there were  4  such warnings
        In bin  zerobtag the affected processes are:  ["nonPromptTTGamma", "isolatedTTGamma"]
        In bin  ChIso the affected processes are:  ["isolatedTTbar"]
        In bin  M3 the affected processes are:  ["nonPromptTTGamma"]
    For uncertainty fsr there were  6  such warnings
        In bin  zerobtag the affected processes are:  ["isolatedTTbar"]
        In bin  ChIso the affected processes are:  ["isolatedTTGamma"]
        In bin  M3 the affected processes are:  ["nonPromptTTGamma", "isolatedTTGamma", "nonPromptTTbar", "isolatedTTbar"]
    For uncertainty Q2 there were  7  such warnings
        In bin  zerobtag the affected processes are:  ["nonPromptTTGamma", "nonPromptTTbar"]
        In bin  ChIso the affected processes are:  ["isolatedTTGamma"]
        In bin  M3 the affected processes are:  ["nonPromptTTGamma", "isolatedTTGamma"]
        In bin  M30photon the affected processes are:  ["TTbar", "TTGamma"]
    For uncertainty PU there were  2  such warnings
        In bin  zerobtag the affected processes are:  ["nonPromptZGamma"]
        In bin  ChIso the affected processes are:  ["isolatedZGamma"]
>>>There were no warnings of type  'At least one of the up/down systematic uncertainty templates is empty'
>>>There were no warnings of type  'Uncertainty has normalisation effect of more than 10.0%'
>>>There were  21 warnings of type  'Uncertainty probably has no genuine shape effect'
    For uncertainty PhoEff there were  1  such warnings
        In bin  M3 the affected processes are:  ["isolatedTTGamma"]
    For uncertainty misIDE there were  5  such warnings
        In bin  zerobtag the affected processes are:  ["isolatedTTGamma", "isolatedWGamma"]
        In bin  ChIso the affected processes are:  ["isolatedWGamma"]
        In bin  M3 the affected processes are:  ["isolatedTTGamma", "isolatedWGamma"]
    For uncertainty EleEff there were  1  such warnings
        In bin  ChIso the affected processes are:  ["isolatedTTGamma"]
    For uncertainty BTagSF_b there were  2  such warnings
        In bin  M30photon the affected processes are:  ["TTbar", "TTGamma"]
    For uncertainty BTagSF_l there were  3  such warnings
        In bin  M3 the affected processes are:  ["isolatedTTGamma"]
        In bin  M30photon the affected processes are:  ["TTbar", "TTGamma"]
    For uncertainty MuEff there were  9  such warnings
        In bin  zerobtag the affected processes are:  ["isolatedZGamma", "isolatedTTbar", "isolatedWGamma", "nonPromptTTGamma", "isolatedTTGamma", "isolatedOther", "nonPromptOther", "nonPromptTTbar", "nonPromptZGamma"]
>>>There were no warnings of type 'Empty process'
























