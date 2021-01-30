#!/bin/bash


combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doInitialFit                 -t -1 --expectSignal 0.01  --robustFit=1  --rMin=0 --rMax=0.1 --stepSize=0.001 --setRobustFitTolerance=0.001  --cminPreScan --cminDefaultMinimizerStrategy=0  
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doFits                       -t -1 --expectSignal 0.01  --robustFit=1  --rMin=0 --rMax=0.1 --stepSize=0.001 --setRobustFitTolerance=0.001  --cminPreScan --cminDefaultMinimizerStrategy=0   --parallel 24
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  -o impacts_toy_ele_2017.json   -t -1 --expectSignal 0.01  --robustFit=1  --rMin=0 --rMax=0.1 --stepSize=0.001 --setRobustFitTolerance=0.001  --cminPreScan --cminDefaultMinimizerStrategy=0  
plotImpacts.py -i impacts_toy_ele_2017.json -o impacts_toy_ele_2017 

exit 1

#./allCombine.sh
combineCards.py -S M3=datacard_ele_2017_M3_DD.txt ChIso=datacard_ele_2017_ChIso_DD.txt  zerobtag=datacard_ele_2017_M30btag_DD.txt M30photon=datacard_ele_2017_M30photon_DD.txt >  datacard_ele_2017.txt
text2workspace.py  datacard_ele_2017.txt 
#ValidateDatacards.py datacard_ele_2017.txt --printLevel 3 --checkUncertOver 0.1 
#combine -M ChannelCompatibilityCheck datacard_ele_2017.root -v1 

combine -M FitDiagnostics -V -n el_2017 datacard_ele_2017.root -s 314159 -v2 --rMin=0 --rMax=0.1 --stepSize=0.001 --setRobustFitTolerance=0.001 --autoBoundsPOIs "*" --autoMaxPOIs "*" --minos all --cminPreScan --cminDefaultMinimizerStrategy=0 --redefineSignalPOIs=r,nonPromptSF
#combine -M MultiDimFit    -V -n el_2017 datacard_ele_2017.root -s 314159 -v3 --rMin=0 --rMax=0.1 --stepSize=0.001 --setRobustFitTolerance=0.001 --autoBoundsPOIs "*" --autoMaxPOIs "*" --cminPreScan

exit 1
combine -H FitDiagnostics -V -n el_2017 datacard_ele_2017.root -s 314159 -v1 --rMin=0 --rMax=0.1 --cminPreScan


exit 1 

text2workspace.py  datacard_mu_2017.txt 
ValidateDatacards.py datacard_mu_2017.txt --printLevel 3 --checkUncertOver 0.1 
combine -M ChannelCompatibilityCheck datacard_mu_2017.root -v1 

combine -M FitDiagnostics -V -n mu_2017 datacard_mu_2017.root -s 314159 -v3 --rMin=0 --rMax=0.1 --stepSize=0.001 --setRobustFitTolerance=0.001 --autoBoundsPOIs "*" --autoMaxPOIs "*" --minos all --cminPreScan
combine -M MultiDimFit    -V -n mu_2017 datacard_mu_2017.root -s 314159 -v3 --rMin=0 --rMax=0.1 --stepSize=0.001 --setRobustFitTolerance=0.001 --autoBoundsPOIs "*" --autoMaxPOIs "*" --cminPreScan

exit 1
combine datacard_ele_2017.root -M FitDiagnostics -V -n .datacard_ele_2017 --toys=-1 --expectSignal=1  --seed=314159 --redefineSignalPOIs=r,nonPromptSF -v1 --rMin=0 --rMax=5 --cminDefaultMinimizerStrategy 0
python diffNuisances.py fitDiagnostics.datacard_ele_2017.root --all -g plots_ele_2017.root


combine -M MultiDimFit datacard_ele_2017.root -s 314159  --algo grid --points=300 -n .Main --rMin=0 --rMax=5
combine -M MultiDimFit datacard_ele_2017.root -s 314159  --saveWorkspace -n .snapshot --rMin=0 --rMax=5
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll  --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --rMin=0 --rMax=5 
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_ele_2017 

combine -M FitDiagnostics -V -n .Asimov_ele_2017 datacard_ele_2017.root --seed=314159 --redefineSignalPOIs=r,nonPromptSF --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=5  --expectSignal=1 -t -1 -v0 --skipBOnlyFit --cminDefaultMinimizerStrategy 0

combine -M FitDiagnostics -V -n el_2017 datacard_ele_2017.root --plots --saveNLL --robustFit=1 -s 314159 --redefineSignalPOIs r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations -v1 --rMin=0 --rMax=5  --skipBOnlyFit #--cminDefaultMinimizerStrategy 0

#combine -M FitDiagnostics -V -n .TOY_ele_2017 datacard_ele_2017.root --seed=314159 --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=5  --expectSignal=1 -t 500 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF >& /dev/null

combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=5  
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=5   --parallel 24
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  -o impacts_toy_ele_2017.json   -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=5  
plotImpacts.py -i impacts_toy_ele_2017.json -o impacts_toy_ele_2017 

combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doInitialFit                 --robustFit=1   --rMin=0 --rMax=5  
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doFits                       --robustFit=1   --rMin=0 --rMax=5   --parallel 24
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  -o impacts_data_ele_2017.json  --robustFit=1   --rMin=0 --rMax=5  
plotImpacts.py -i impacts_data_ele_2017.json -o impacts_data_ele_2017 


exit 1


renormTTGamma rateParam * *TTGamma 0.04312947468299836
nuisance edit freeze renormTTGamma ifexists

renormTTbar   rateParam * *TTbar   0.0012022698855439068
nuisance edit freeze renormTTbar ifexists

#renormTTbar   rateParam * TTbar*   0.0012022698855439068
#nuisance edit freeze renormTTbar ifexists

#TTbarSF       rateParam * TT*      831.76
TTbarSF       rateParam * *TT       831.76

Best fit r: 0.0236887  -0.00148534/+0.0015207  (68% CL) with out 0photon and 0btag CR


 --rMin=0 --rMax=0.1 --preFitValue=0.02 --stepSize=0.001 --setRobustFitTolerance=0.001
 
 
 combine -M FitDiagnostics -V -n el_2017 datacard_ele_2017.root --robustFit=1 -s 314159 --redefineSignalPOIs r,nonPromptSF -v1 --rMin=0 --rMax=0.1 --skipBOnlyFit --stepSize=0.001 --setRobustFitTolerance=0.001
