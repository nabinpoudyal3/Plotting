#!/bin/bash

set -x

# combineCards.py -S M3=datacard_ele_2016_M3.dat \
# 				ChIso=datacard_ele_2016_ChIso.dat \
#              zerobtag=datacard_ele_2016_M30btag.dat \
#             M30photon=datacard_ele_2016_M30photon.dat \
#              >  datacard_ele_2016.dat

# combineCards.py -S M3=datacard_mu_2016_M3.dat \
# 				ChIso=datacard_mu_2016_ChIso.dat \
#              zerobtag=datacard_mu_2016_M30btag.dat \
#             M30photon=datacard_mu_2016_M30photon.dat \
#              >  datacard_mu_2016.dat

# combineCards.py -S ele=datacard_ele_2016.dat  mu=datacard_mu_2016.dat > datacard_both_2016.dat

# text2workspace.py datacard_ele_2016.dat  --out=datacard_ele_2016.root  --default-morphing=DEFMORPH --no-b-only 
# text2workspace.py datacard_mu_2016.dat   --out=datacard_mu_2016.root   --default-morphing=DEFMORPH --no-b-only 
# text2workspace.py datacard_both_2016.dat --out=datacard_both_2016.root --default-morphing=DEFMORPH --no-b-only 

# myFreezeNP=" --freezeParameters OtherSF,Other_norm,TTbarSF,WGSF,ZGSF,misIDE,JER,PhoEff,Q2,BTagSF_b,lumi,BTagSF_l,Pdf,JECTotal,PU,isr,prefireEcal,EleEff,MuEff,fsr" 
# myFreezeNP=" --freezeParameters misIDE,JER,PhoEff,Q2,BTagSF_b,lumi,BTagSF_l,Pdf,JECTotal,PU,isr,prefireEcal,EleEff,MuEff,fsr" 
myFreezeNP=" "
# myFreezeNP=" --freezeParameters OtherSF,Other_norm,TTbarSF,WGSF,ZGSF " 
# myFreezeNP=" --freezeParameters rgx{prop_bin*} " #,OtherSF,Other_norm,TTbarSF,WGSF,ZGSF,misIDE,PhoEff,Q2,BTagSF_b,lumi,BTagSF_l,Pdf,JECTotal,PU,isr,prefireEcal,EleEff,MuEff,fsr" 

combine $myFreezeNP --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n .Asimov_ele_2016   datacard_ele_2016.root  --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5 -t -1  --expectSignal 1 -v1
combine $myFreezeNP --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n ele_2016           datacard_ele_2016.root  --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5        --expectSignal 1 -v1
combine $myFreezeNP --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n .TOY_ele_2016      datacard_ele_2016.root  --seed=314159                     --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF              --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5 -t 200  -v1
exit 1

combine $myFreezeNP --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n .Asimov_mu_2016    datacard_mu_2016.root   --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5 -t -1  --expectSignal 1 -v1
combine $myFreezeNP --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n mu_2016            datacard_mu_2016.root   --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5        --expectSignal 1 -v1
combine $myFreezeNP --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n .TOY_mu_2016       datacard_mu_2016.root   --seed=314159                     --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF              --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5 -t 200   --expectSignal 1 -v1

combine $myFreezeNP --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n .Asimov_both_2016  datacard_both_2016.root --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5 -t -1  --expectSignal 1 -v1
combine $myFreezeNP --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n both_2016          datacard_both_2016.root --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5        --expectSignal 1 -v1
combine $myFreezeNP --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n .TOY_both_2016     datacard_both_2016.root --seed=314159                     --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF              --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5 -t 200   --expectSignal 1 -v1

python makettGammaSS.py         
python makettGammaSS_Toy.py     
python makettGammaSS_Asimov.py     
python makeCorrelationMatrix.py   

# myFreezeNP=" --freezeWithAttributes prop_bin "
combineTool.py  $myFreezeNP --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                  -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=2 
combineTool.py  $myFreezeNP --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doFits                        -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=2  --parallel 24
combineTool.py  $myFreezeNP --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_toy_ele_2016.json    -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=2 
plotImpacts.py  -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016 --label-size 0.035

combineTool.py  $myFreezeNP --cminPreScan -M Impacts -d datacard_mu_2016.root -m 125  --doInitialFit                   -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=2 
combineTool.py  $myFreezeNP --cminPreScan -M Impacts -d datacard_mu_2016.root -m 125  --doFits                         -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=2  --parallel 24
combineTool.py  $myFreezeNP --cminPreScan -M Impacts -d datacard_mu_2016.root -m 125  -o impacts_toy_mu_2016.json      -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=2 
plotImpacts.py  -i impacts_toy_mu_2016.json -o impacts_toy_mu_2016 --label-size 0.035

combineTool.py  $myFreezeNP --cminPreScan -M Impacts -d datacard_both_2016.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=2 
combineTool.py  $myFreezeNP --cminPreScan -M Impacts -d datacard_both_2016.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=2  --parallel 24
combineTool.py  $myFreezeNP --cminPreScan -M Impacts -d datacard_both_2016.root -m 125  -o impacts_toy_both_2016.json  -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=2 
plotImpacts.py  -i impacts_toy_both_2016.json -o impacts_toy_both_2016 --label-size 0.035



combine -M MultiDimFit datacard_ele_2016.root $myFreezeNP \
--seed=314159 --expectSignal 1 --redefineSignalPOIs=r,nonPromptSF \
--rMin=0 --rMax=2 -v0 \
--setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5


combine -M MultiDimFit datacard_mu_2016.root $myFreezeNP \
--seed=314159 --expectSignal 1 --redefineSignalPOIs=r,nonPromptSF \
--rMin=0 --rMax=2 -v0 \
--setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5


combine -M MultiDimFit datacard_both_2016.root $myFreezeNP \
--seed=314159 --expectSignal 1 --redefineSignalPOIs=r,nonPromptSF \
--rMin=0 --rMax=2 -v0 \
--setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5


exit 1


combine -M MultiDimFit datacard_ele_2016_M30photon.dat $myFreezeNP \
--seed=314159 --expectSignal 1 --redefineSignalPOIs=TTbarSF,Other_norm \
--setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5:Other_norm=0,5 \
-v2 \
--freezeParameters JER,Q2,BTagSF_b,lumi,BTagSF_l,Pdf,JECTotal,PU,isr,prefireEcal,EleEff,fsr,WGSF,ZGSF


# myFreezeNorm=" --freezeParameters OtherSF,Other_norm,TTbarSF,WGSF,ZGSF " 
# myFreezeNP=" --freezeParameters misIDE,JER,PhoEff,Q2,BTagSF_b,lumi,BTagSF_l,Pdf,JECTotal,PU,isr,prefireEcal,EleEff,fsr  " 


# exit 1

echo "*********************************************************************************************************************"

combine --cminPreScan --forceRecreateNLL --skipBOnlyFit $myFreezeNP \
-M FitDiagnostics -n .Asimov_ele_2016 datacard_ele_2016.root \
--seed=314159 --saveOverallShapes --plots --saveNLL \
--redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations \
--rMin=0 --rMax=2 \
-t -1 --expectSignal 1 -v1 \
--setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5 \

echo "*********************************************************************************************************************"

python makeCorrelationMatrix.py
python makettGammaSS_Asimov.py  

evince impacts_toy_ele_2016.pdf


echo "*********************************************************************************************************************"
combine -M MultiDimFit datacard_ele_2016.root $myFreezeNP \
--seed=314159 --expectSignal 1 --redefineSignalPOIs=r,nonPromptSF \
--rMin=0 --rMax=2 \
--setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5 \

echo "*********************************************************************************************************************"
combine --cminPreScan --skipBOnlyFit --forceRecreateNLL $myFreezeNP \
-M FitDiagnostics -n ele_2016 datacard_ele_2016.root \
--expectSignal 1 -v1 \
--seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF \
--saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 \
--setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5 \


echo "*********************************************************************************************************************"
combine --cminPreScan --skipBOnlyFit --forceRecreateNLL $myFreezeNP \
-M FitDiagnostics -n TOY.ele_2016 datacard_ele_2016.root \
-t 5 --expectSignal 1 -v1 \
--seed=314159 --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF \
--saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 \


# --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5 \
exit 1



--freezeParameters WGSF

# --freezeParameters JER,PhoEff,Q2,BTagSF_b,lumi,BTagSF_l,Pdf,JECTotal,PU,isr,misIDE,prefireEcal,EleEff,fsr,OtherSF,Other_norm,TTbarSF,WGSF,ZGSF




 
less TTGamma_nonPrompt_2016_Asimov.txt
exit 1



exit 1
python makettGammaSS.py         
python makettGammaSS_Toy.py     
python makeCorrelationMatrix.py   
python makeTotalCovarianceMatrix.py 


exit 1



./allCombine.sh

text2workspace.py    datacard_ele_2016.txt 
text2workspace.py    datacard_mu_2016.txt 
text2workspace.py    datacard_both_2016.txt 

ValidateDatacards.py datacard_ele_2016.txt  --printLevel 3 --checkUncertOver 0.1 
ValidateDatacards.py datacard_mu_2016.txt   --printLevel 3 --checkUncertOver 0.1 
ValidateDatacards.py datacard_both_2016.txt --printLevel 3 --checkUncertOver 0.1 

combine --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n .Asimov_ele_2016 datacard_ele_2016.root --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5 -t -1 --expectSignal 1 -v1
combine --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n ele_2016 datacard_ele_2016.root         --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5 --expectSignal 1 -v1
combine --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n TOY.ele_2016 datacard_ele_2016.root     --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5 -t 200 --expectSignal 1 -v3

############## impact plots
# combineTool.py  --freezeParameters OtherSF,Other_norm,TTbarSF,JECTotal,isr,fsr,JER,Q2 --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=3 
# combineTool.py  --freezeParameters OtherSF,Other_norm,TTbarSF,JECTotal,isr,fsr,JER,Q2 --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=3  --parallel 24
# combineTool.py  --freezeParameters OtherSF,Other_norm,TTbarSF,JECTotal,isr,fsr,JER,Q2 --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_toy_ele_2016.json   -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=3 
# plotImpacts.py  -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016 --label-size 0.035


combineTool.py  --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=5 
combineTool.py  --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=5  --parallel 24
combineTool.py  --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_toy_ele_2016.json   -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=5 
plotImpacts.py  -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016 --label-size 0.035

combineTool.py  --cminPreScan -M Impacts -d datacard_mu_2016.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=5 
combineTool.py  --cminPreScan -M Impacts -d datacard_mu_2016.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=5  --parallel 24
combineTool.py  --cminPreScan -M Impacts -d datacard_mu_2016.root -m 125  -o impacts_toy_mu_2016.json    -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=5 
plotImpacts.py  -i impacts_toy_mu_2016.json -o impacts_toy_mu_2016 --label-size 0.035

combineTool.py  --cminPreScan -M Impacts -d datacard_both_2016.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=5 
combineTool.py  --cminPreScan -M Impacts -d datacard_both_2016.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=5  --parallel 24
combineTool.py  --cminPreScan -M Impacts -d datacard_both_2016.root -m 125  -o impacts_toy_both_2016.json  -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=5 
plotImpacts.py  -i impacts_toy_both_2016.json -o impacts_toy_both_2016 --label-size 0.035


exit 1

###################### Likelihood fit
combine -M MultiDimFit datacard_ele_2016.root  --seed=314159 -t -1 --expectSignal 1
combine -M MultiDimFit datacard_ele_2016.root  --seed=314159 -t  5 --expectSignal 1
combine -M MultiDimFit datacard_ele_2016.root  --seed=314159       --expectSignal 1


combine -H FitDiagnostics datacard_ele_2016.root --expectSignal=1
combine --freezeParameters OtherSF,Other_norm,TTbarSF,JECTotal,isr,fsr,JER,Q2 --cminPreScan --skipBOnlyFit -M FitDiagnostics -n .Asimov_ele_2016 datacard_ele_2016.root   --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 -t -1 --expectSignal 1 -v1
combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n .Asimov_ele_2016 datacard_ele_2016.root   --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 -t -1 --expectSignal 1 -v1


# python diffNuisances.py fitDiagnostics.Asimov_ele_2016.root --all
###########

# ele,mu,both Asimov
####################################
combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n .Asimov_ele_2016 datacard_ele_2016.root   --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 -t -1 --expectSignal 1 -v1
combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n .Asimov_mu_2016 datacard_mu_2016.root     --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=2 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 -t -1 --expectSignal 1 -v1
combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n .Asimov_both_2016 datacard_both_2016.root --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 -t -1 --expectSignal 1 -v1

# ele,mu,both data
#####################################

combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n ele_2016 datacard_ele_2016.root   --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 --expectSignal 1 -v1
combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n mu_2016 datacard_mu_2016.root     --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 --expectSignal 1 -v1
combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n both_2016 datacard_both_2016.root --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 --expectSignal 1 -v1

# ele,mu,both TOY
###########################################

combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n TOY.ele_2016 datacard_ele_2016.root   --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 -t 200 --expectSignal 1 -v3
combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n TOY.mu_2016 datacard_mu_2016.root     --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 -t 200 --expectSignal 1 -v3
combine --cminPreScan --skipBOnlyFit -M FitDiagnostics -n TOY.both_2016 datacard_both_2016.root --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 -t 200 --expectSignal 1 -v3



combine -M MultiDimFit datacard_ele_2016.root  --seed=314159 -t -1 --expectSignal 1 --algo grid  --points=200 -n .Asimov_Main_ele_TTbarSF --rMin=0 --rMax=5  -P TTbarSF --floatOtherPOIs 1 --setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4
python plot1DScan.py  higgsCombine.Asimov_Main_ele_TTbarSF.MultiDimFit.mH120.314159.root --POI TTbarSF -o single_scan_Asimov_ele_TTbarSF


############## impact plots
combineTool.py  --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=3 
combineTool.py  --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=3  --parallel 24
combineTool.py  --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_toy_ele_2016.json   -t -1 --expectSignal 1  --robustFit=1   --rMin=0 --rMax=3 
plotImpacts.py  -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016 --label-size 0.035


combineTool.py  --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 -t 1 --expectSignal 1  --rMin=0 --rMax=5 
combineTool.py  --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       -t 1 --expectSignal 1  --rMin=0 --rMax=5  --parallel 24
combineTool.py  --cminPreScan -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_toy_ele_2016.json   -t 1 --expectSignal 1  --rMin=0 --rMax=5 
plotImpacts.py  -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016 --label-size 0.035

exit 1

python makettGammaSS.py         
python makettGammaSS_Toy.py     
python makettGammaSS_Asimov.py   
python makeCorrelationMatrix.py   
python makeTotalCovarianceMatrix.py 

exit 1
###### Lukas
combine -M MultiDimFit cards/shapecard_inclusive.txt  
combine --robustHesse 1 --robustFit 1 --forceRecreateNLL -M FitDiagnostics --saveShapes --saveNormalizations --saveOverall --saveWithUncertainties --customStartingPoint --setParameters r=1 cards/shapecard_inclusive.txt  
combine -M MultiDimFit -n Nominal --saveNLL --forceRecreateNLL --freezeParameters r --expectSignal=1 --setParameters r=1 cards/shapecard_inclusive.txt  

































# text2workspace.py    datacard_ele_2016.txt 

combine --skipBOnlyFit -M FitDiagnostics \
--redefineSignalPOIs=r,nonPromptSF \
-v1 \
--seed=314159 \
--saveShapes --saveOverallShapes --saveWithUncertainties --saveNormalizations \
--toysFrequentist \
--plots --saveNLL \
-t -1 --expectSignal 1 \
--rMin=0 --rMax=5 \
-n .Asimov_ele_2016 datacard_ele_2016.root

exit 1
--setParameterRanges nonPromptSF=-3,3:TTbarSF=-2,2:WGSF=-3,3:OtherSF=-3,3:Other_norm=-3,3:ZGSF=-3,3 
--autoBoundsPOIs "*" \
# --freezeParameters TTbarSF,OtherSF,Other_norm,JECTotal,WGSF,nonPromptSF,ZGSF \
# --cminDefaultMinimizerStrategy 0 \
# --X-rtd MINIMIZER_analytic \
# --robustHesse=1 \
# --robustFit=1 \

# exit 1

# --X-rtd MINIMIZER_analytic \

combine --skipBOnlyFit -M FitDiagnostics \
--redefineSignalPOIs=r,nonPromptSF \
-v1 \
-n .Asimov_ele_2016 datacard_ele_2016.root \
--seed=314159 \
--rMin=0 --rMax=5 -t -1 --expectSignal 1 \
--saveWithUncertainties --saveNormalizations \
--autoBoundsPOIs "*" \
--robustFit=1 \
--toysFrequentist
  


combine --skipBOnlyFit -M FitDiagnostics \
--redefineSignalPOIs=r,nonPromptSF \
-v1 \
-n .Asimov_mu_2016 datacard_mu_2016.root \
--seed=314159 \
--rMin=0 --rMax=5 -t -1 --expectSignal 1 \
--saveWithUncertainties --saveNormalizations \
--autoBoundsPOIs "*" \
--toysFrequentist \
# --robustFit=1
exit 1
--X-rtd MINIMIZER_analytic \









exit 1
















# rm *.png
# rm impacts*.json
# rm validation.json
# rm single_scan_*.pdf
# rm impacts*.pdf
# rm freeze*.pdf
# rm datacard_*_2016.root
# rm higgsCombine.*.root
# rm higgsCombine_*.root
# rm single_scan_*.root
# rm fitDiagnostics*.root
# rm combine_logger.out


# ./allCombine.sh
# text2workspace.py    datacard_ele_2016.txt 
# ValidateDatacards.py datacard_ele_2016.txt  --printLevel 3 --checkUncertOver 0.1 
# text2workspace.py    datacard_mu_2016.txt 
# ValidateDatacards.py datacard_mu_2016.txt   --printLevel 3 --checkUncertOver 0.1 
# text2workspace.py    datacard_both_2016.txt 
# ValidateDatacards.py datacard_both_2016.txt --printLevel 3 --checkUncertOver 0.1 

myStats=" --freezeParameters prop_binChIso_bin0,prop_binChIso_bin1,prop_binChIso_bin10,prop_binChIso_bin2,prop_binChIso_bin3,prop_binChIso_bin4,prop_binChIso_bin5,prop_binChIso_bin6,prop_binChIso_bin7,prop_binChIso_bin8,prop_binChIso_bin9,prop_binM30photon_bin0,prop_binM30photon_bin1,prop_binM30photon_bin2,prop_binM30photon_bin3,prop_binM30photon_bin4,prop_binM30photon_bin5,prop_binM30photon_bin6,prop_binM30photon_bin7,prop_binM3_bin0,prop_binM3_bin1,prop_binM3_bin2,prop_binM3_bin3,prop_binM3_bin4,prop_binM3_bin5,prop_binM3_bin6,prop_binM3_bin7,prop_binzerobtag_bin0,prop_binzerobtag_bin1,prop_binzerobtag_bin2,prop_binzerobtag_bin3,prop_binzerobtag_bin4,prop_binzerobtag_bin5,prop_binzerobtag_bin6,prop_binzerobtag_bin7 "

mySignalParamters=" --redefineSignalPOIs=r,nonPromptSF "
myAsimovFit=" -t -1 --expectSignal 1 "
myExpectSignal=" --expectSignal 1 "
myToyFit=" -t 300 --expectSignal 1 "
verbose=" -v1 "
myTrackParameters=" --trackParameters r,BTagSF_b,BTagSF_l,EleEff,PhoEff,lumi,misIDE,Pdf,isr,fsr,PU,prefireEcal,JECTotal,JER,Q2,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
mySeed=" --seed=314159 "
myPoints=" --points=300 "
myFakeDataFit=" "
mySignalModifierRange=" --rMin=0 --rMax=3 "
myParameterRange=" --setParameterRanges nonPromptSF=0,3:TTbarSF=0,3:WGSF=0,3:OtherSF=0,3:Other_norm=0,3:ZGSF=0,3 "
# myParameterRange=" "
channel="ele"
# myAdditional=" --cminPreScan --cminDefaultMinimizerTolerance=0.01 --cminDefaultMinimizerStrategy 2"
myAdditional=" "
# myAdditional=" --cminPreScan --cminDefaultMinimizerTolerance=0.01 "

# combine -M MultiDimFit datacard_ele_2016.root -v3 $myExpectSignal $myAdditional
# combine -M MultiDimFit datacard_ele_2016.root -v3 $myExpectSignal --fastScan $myAdditional
# combineTool.py -M FastScan -w datacard_ele_2016.root:w -v3 $myAsimovFit $myAdditional
# combine -H MultiDimFit datacard_ele_2016.root -v3 $myAdditional $myExpectSignal
# combine -H MultiDimFit datacard_ele_2016.root -v3 --hintStatOnly $myAdditional $myExpectSignal
# exit 1
# Make impact plots for asimov and toy. See if sth is wrong there.

set -x


# --X-rtd MINIMIZER_analytic \
echo combine --skipBOnlyFit \
-M FitDiagnostics \
-n .Asimov_"$channel"_2016 datacard_"$channel"_2016.root \
--setParameterRanges nonPromptSF=0,4:TTbarSF=0,2:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 \
$mySeed \
-v2 \
$mySignalParamters \
--saveWithUncertainties --saveNormalizations \
$mySignalModifierRange \
$myAsimovFit
# --freezeParameters BTagSF_b

exit 1

--freezeParameters BTagSF_b,BTagSF_l,EleEff,PhoEff,lumi,misIDE,\
Pdf,isr,fsr,PU,prefireEcal,JECTotal,JER,Q2,ZGSF,TTbarSF

#--freezeParameters TTbarSF
exit 1
# python mlfitNormsToText.py fitDiagnostics.Asimov_"$channel"_2016.root --uncertainties
combine --skipBOnlyFit -M FitDiagnostics -n "$channel"_2016 datacard_"$channel"_2016.root $myFakeDataFit --plots --saveNLL --robustFit=1 $mySeed $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations $verbose $mySignalModifierRange  $myParameterRange $myExpectSignal
# python mlfitNormsToText.py fitDiagnostics"$channel"_2016.root --uncertainties
combine --skipBOnlyFit -M FitDiagnostics -n .TOY_"$channel"_2016 datacard_"$channel"_2016.root $mySeed --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL $mySignalModifierRange  $myParameterRange $myToyFit -v3   


combine -M ChannelCompatibilityCheck datacard_"$channel"_2016.root $verbose $mySignalParamters  $myParameterRange $myExpectSignal
combine datacard_"$channel"_2016.root --justFit -M FitDiagnostics -n .datacard_"$channel"_2016_Asimov $myAsimovFit   $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
python diffNuisances.py fitDiagnostics.datacard_"$channel"_2016_Asimov.root --all 
combine datacard_"$channel"_2016.root --justFit -M FitDiagnostics -n .datacard_"$channel"_2016_Data $myFakeDataFit $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange $myExpectSignal
python diffNuisances.py fitDiagnostics.datacard_"$channel"_2016_Data.root --all 

combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myAsimovFit --algo grid $myPoints -n .Main $mySignalModifierRange  $myParameterRange
combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myAsimovFit --saveWorkspace -n .snapshot $mySignalModifierRange  $myParameterRange
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myAsimovFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
python plot1DScan.py  --translate rename.json  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2016_Asimov 

combine -M MultiDimFit datacard_"$channel"_2016.root                       $mySeed $myFakeDataFit --algo grid $myPoints -n .Main $mySignalModifierRange     $myParameterRange $myExpectSignal
combine -M MultiDimFit datacard_"$channel"_2016.root                       $mySeed $myFakeDataFit --saveWorkspace -n .snapshot   $mySignalModifierRange     $myParameterRange $myExpectSignal
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myFakeDataFit -n .freezeAll  --algo grid     $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange $myExpectSignal
python plot1DScan.py  --translate rename.json  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2016_Data 

combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                                   $myAsimovFit    --robustFit=1   $mySignalModifierRange  $myParameterRange 
combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                         $myAsimovFit    --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_toy_"$channel"_2016.json              $myAsimovFit    --robustFit=1   $mySignalModifierRange  $myParameterRange 
plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2016.json -o impacts_toy_"$channel"_2016  --label-size 0.035 

combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                                   $myFakeDataFit  --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                         $myFakeDataFit  --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange  --parallel 24
combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_data_"$channel"_2016.json             $myFakeDataFit  --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
plotImpacts.py  -t rename.json  -i impacts_data_"$channel"_2016.json -o impacts_data_"$channel"_2016 --label-size 0.035 

combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                               -t 1 --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                     -t 1 --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange  --parallel 24
combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_fakedata_"$channel"_2016.json     -t 1 --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
plotImpacts.py  -t rename.json  -i impacts_fakedata_"$channel"_2016.json -o impacts_fakedata_"$channel"_2016 --label-size 0.035 

# combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                                   $myAsimovFit --redefineSignalPOIs   TTbarSF    --robustFit=1   $mySignalModifierRange  $myParameterRange 
# combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                         $myAsimovFit --redefineSignalPOIs   TTbarSF    --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
# combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_toy_"$channel"_2016_TTbarSF.json      $myAsimovFit --redefineSignalPOIs   TTbarSF    --robustFit=1   $mySignalModifierRange  $myParameterRange 
# plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2016_TTbarSF.json -o impacts_toy_"$channel"_2016_TTbarSF  --label-size 0.035 --POI TTbarSF

# combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                                   $myFakeDataFit --redefineSignalPOIs   TTbarSF --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
# combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                         $myFakeDataFit --redefineSignalPOIs   TTbarSF --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange  --parallel 24
# combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_data_"$channel"_2016_TTbarSF.json     $myFakeDataFit --redefineSignalPOIs   TTbarSF --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
# plotImpacts.py  -t rename.json  -i impacts_data_"$channel"_2016_TTbarSF.json -o impacts_data_"$channel"_2016_TTbarSF --label-size 0.035 --POI TTbarSF

# combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                                       -t 1 --redefineSignalPOIs   TTbarSF --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
# combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                             -t 1 --redefineSignalPOIs   TTbarSF --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange  --parallel 24
# combineTool.py $myStats -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_fakedata_"$channel"_2016_TTbarSF.json     -t 1 --redefineSignalPOIs   TTbarSF --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
# plotImpacts.py  -t rename.json  -i impacts_fakedata_"$channel"_2016_TTbarSF.json -o impacts_fakedata_"$channel"_2016_TTbarSF --label-size 0.035 --POI TTbarSF



# declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "EleEff" "Pdf" "isr" "fsr" "PU" "prefireEcal" "JECTotal" "JER" "Q2" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "Other_norm" "nonPromptSF")
# for parameter in ${PARAMETERS[@]}; do
#   combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myAsimovFit   --algo grid  $myPoints -n .Asimov_Main_"$channel"_"$parameter" $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange
#   python plot1DScan.py  --translate rename.json higgsCombine.Asimov_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_"$channel"_"$parameter"
#   combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myFakeDataFit --algo grid  $myPoints -n .Data_Main_"$channel"_"$parameter"   $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange $myExpectSignal
#   python plot1DScan.py  --translate rename.json higgsCombine.Data_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_"$channel"_"$parameter"
# done
exit 1

wait
echo "Done fitting only!!!"

python makettGammaSS.py
python makettGammaSS_Toy.py
python makettGammaSS_Asimov.py
python makeCovarianceMatrix.py

echo "Done fitting and Extraction!!!"
exit 1


March 9: This setting works for Asimov fit. 
combine --cminPreScan --forceRecreateNLL --skipBOnlyFit \
-M FitDiagnostics -n .Asimov_ele_2016 datacard_ele_2016.root \
--seed=314159 --saveOverallShapes --plots --saveNLL \
--redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations \
--rMin=0 --rMax=2 \
-t -1 --expectSignal 1 -v1 \
--setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:ZGSF=0,5 \


