#!/bin/bash

myParameterRange=" --setParameterRanges nonPromptSF=0,5:TTbarSF16=0,5:WGSF16=0,5:OtherSF16=0,5:Other_norm16=0,5:ZGSF16=0,5:TTbarSF17=0,5:WGSF17=0,5:OtherSF17=0,5:Other_norm17=0,5:ZGSF17=0,5:TTbarSF18=0,5:WGSF18=0,5:OtherSF18=0,5:Other_norm18=0,5:ZGSF18=0,5 "
mySignalParamters=" --redefineSignalPOIs=r,nonPromptSF "
mySignalModifierRange=" --rMin=0 --rMax=2 "
myAsimovFit=" -t -1 --expectSignal 1 "
myFakeDataFit=" -t 1 --expectSignal 1 "
# myFakeDataFit=""
myToyFit=" -t 200 --expectSignal 1 "
verbose=" -v0 "
# myTrackParameters=" --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
# myTrackParameters=" --trackParameters r,EleEff,MuEff,PhoEff,misIDE,Pdf,isr,fsr,PU,prefireEcal,JECTotal,Q2,nonPromptSF "
mySeed=" --seed=314159 "
myPoints=" --points=100 "
myFreezingParamters=" Q2,JER18,JER17,JER16,MuEff,BTagSF_b17,lumi18,PU,lumi16,lumi17,EleEff,BTagSF_b18,lumiXY,BTagSF_b16,PhoEff,lumi1718,lumi1617,Pdf,JECTotal,isr,prefireEcal,BTagSF_l18,fsr,BTagSF_l17,BTagSF_l16,TTbarSF16,TTbarSF17,OtherSF18,Other_norm16,Other_norm17,Other_norm18,TTbarSF18,WGSF17,WGSF18,ZGSF16,OtherSF17,OtherSF16,ZGSF17,WGSF16,ZGSF18 "
# myFreezingParamters=" lumi16,lumiXY,BTagSF_b16,PhoEff,lumi1718,lumi1617,Pdf,JECTotal,isr,prefireEcal,BTagSF_l18,fsr,BTagSF_l17,BTagSF_l16,TTbarSF16,TTbarSF17,OtherSF18,Other_norm16,Other_norm17,Other_norm18,TTbarSF18,WGSF17,WGSF18,ZGSF16,OtherSF17,OtherSF16,ZGSF17,WGSF16,ZGSF18 "

# add this to have correct covariance matrix --robustHesse 1

# text2workspace.py datacard.dat  --out=datacard.root  --default-morphing=DEFMORPH 
# ValidateDatacards.py datacard.txt  --printLevel 3 --checkUncertOver 0.1 

# combineTool.py -M FastScan -w datacard.root:w --points=50 --expectSignal 1 --redefineSignalPOIs=r,nonPromptSF
# combine -M ChannelCompatibilityCheck --expectSignal=1  datacard.root -v1 --redefineSignalPOIs=r,nonPromptSF   --rMin=0 --rMax=2 

# combine datacard.root -M FitDiagnostics  -n .datacard_Asimov $myAsimovFit  $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange --freezeParameters $myFreezingParamters
# python diffNuisances.py fitDiagnostics.datacard_Asimov.root --all 

# combine datacard.root -M FitDiagnostics -n .datacard_Data $myFakeDataFit   $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange --robustHesse 1
# python diffNuisances.py fitDiagnostics.datacard_Data.root --all 

set -x 


# combine -M MultiDimFit datacard.root \
# --seed=314159 -t 1 --expectSignal 1 --redefineSignalPOIs=r,nonPromptSF \
# --rMin=0 --rMax=2 -v1 \
# --setParameterRanges nonPromptSF=0,5:TTbarSF16=0,5:WGSF16=0,5:OtherSF16=0,5:Other_norm16=0,5:ZGSF16=0,5:TTbarSF17=0,5:WGSF17=0,5:OtherSF17=0,5:Other_norm17=0,5:ZGSF17=0,5:TTbarSF18=0,5:WGSF18=0,5:OtherSF18=0,5:Other_norm18=0,5:ZGSF18=0,5

# combine -M MultiDimFit datacard.root $mySeed $myAsimovFit --algo grid $myPoints -n .Main $mySignalModifierRange  $myParameterRange
# combine -M MultiDimFit datacard.root $mySeed $myAsimovFit --saveWorkspace -n .snapshot $mySignalModifierRange  $myParameterRange
# combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myAsimovFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
# python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_Asimov 

# combine -M MultiDimFit datacard.root $mySeed --algo grid $myFakeDataFit $myPoints -n .Data_Main_r $mySignalModifierRange  $myParameterRange
# python plot1DScan.py higgsCombine.Data_Main_r.MultiDimFit.mH120.314159.root  -o single_scan_data_r

# combine -M MultiDimFit datacard.root $mySeed $myFakeDataFit --algo grid $myPoints -n .Main $mySignalModifierRange    $myParameterRange
# combine -M MultiDimFit datacard.root $mySeed $myFakeDataFit --saveWorkspace -n .snapshot $mySignalModifierRange     $myParameterRange
# combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myFakeDataFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
# python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_Data 

combine -v1 --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics  -n .Asimov datacard.root $mySeed $myAsimovFit   --saveWithUncertainties --saveNormalizations --plots --saveShapes $mySignalModifierRange  $mySignalParamters $myParameterRange 
combine -v1 --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics  -n .Data   datacard.root $mySeed $myFakeDataFit --saveWithUncertainties --saveNormalizations --plots --saveShapes $mySignalModifierRange  $mySignalParamters $myParameterRange 
combine -v1 --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics  -n .TOY    datacard.root $mySeed $myToyFit      --saveWithUncertainties --saveNormalizations --plots              $mySignalModifierRange  $mySignalParamters $myParameterRange 

# no need to redefine POIs r and nonPromptSF but use the range for nonPromptSF 
# combineTool.py --cminPreScan -M Impacts -d datacard.root -m 125  --doInitialFit        $myAsimovFit    --robustFit=1   $mySignalModifierRange  $myParameterRange 
# combineTool.py --cminPreScan -M Impacts -d datacard.root -m 125  --doFits              $myAsimovFit    --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
# combineTool.py --cminPreScan -M Impacts -d datacard.root -m 125  -o impacts_toy.json   $myAsimovFit    --robustFit=1   $mySignalModifierRange  $myParameterRange 
# plotImpacts.py -i impacts_toy.json -o impacts_toy 

combineTool.py --cminPreScan -M Impacts -d datacard.root -m 125  --doInitialFit        $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange 
combineTool.py --cminPreScan -M Impacts -d datacard.root -m 125  --doFits              $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
combineTool.py --cminPreScan -M Impacts -d datacard.root -m 125  -o impacts_data.json  $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange 
plotImpacts.py -i impacts_data.json -o impacts_data 

# declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "Other_norm" "nonPromptSF")
# for parameter in ${PARAMETERS[@]}; do
#   combine -M MultiDimFit datacard.root $mySeed $myAsimovFit --algo grid $myPoints -n .Asimov_Main_"$parameter" $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange
#   python plot1DScan.py higgsCombine.Asimov_Main_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_"$parameter"

#   combine -M MultiDimFit datacard.root $mySeed --algo grid $myFakeDataFit $myPoints -n .Data_Main_"$parameter" $mySignalModifierRange -P $parameter --floatOtherPOIs 1  $myParameterRange
#   python plot1DScan.py higgsCombine.Data_Main_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_"$parameter"
# done

# exit 1

wait
echo "Done fitting only!!!"


python makettGammaSS.py
python makettGammaSS_Toy.py
python makettGammaSS_Asimov.py
python makeCovarianceMatrix.py
# python getTrackParameterPlots.py
# python getNPToyDistribution.py

echo "Done fitting and Extraction!!!"
exit 1
myFreezingParamters=" Q2,JER18,JER17,JER16,MuEff,BTagSF_b17,lumi18,PU,lumi16,lumi17,EleEff,BTagSF_b18,lumiXY,BTagSF_b16,PhoEff,lumi1718,lumi1617,Pdf,JECTotal,isr,prefireEcal,BTagSF_l18,fsr,BTagSF_l17,BTagSF_l16,TTbarSF16,TTbarSF17,OtherSF18,Other_norm16,Other_norm17,Other_norm18,TTbarSF18,WGSF17,WGSF18,ZGSF16,OtherSF17,OtherSF16,ZGSF17,WGSF16,ZGSF18 "
