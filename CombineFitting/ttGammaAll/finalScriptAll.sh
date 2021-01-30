#!/bin/bash

myParameterRange=" --setParameterRanges nonPromptSF=0,5:TTbarSF=0,4:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 "
mySignalParamters=" --redefineSignalPOIs=r,nonPromptSF "
mySignalModifierRange=" --rMin=0.01 --rMax=5 "
myAsimovFit=" -t -1 --expectSignal 1 "
myFakeDataFit=" -t 1 --expectSignal 1 "
# myFakeDataFit=""
myToyFit=" -t 300 --expectSignal 1 "
verbose=" -v1 "
myTrackParameters=" --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
mySeed=" --seed=314159 "
myPoints=" --points=100 "

text2workspace.py    datacard.txt 
ValidateDatacards.py datacard.txt  --printLevel 3 --checkUncertOver 0.1 
 
combine -M ChannelCompatibilityCheck --expectSignal=1  datacard.root $verbose $mySignalParamters  $myParameterRange
combine datacard.root -M FitDiagnostics -n .datacard $myAsimovFit  $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
python diffNuisances.py fitDiagnostics.datacard.root --all 

combine datacard.root -M FitDiagnostics -n .datacard $myFakeDataFit $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
python diffNuisances.py fitDiagnostics.datacard.root --all 

combine -M MultiDimFit datacard.root $mySeed $myAsimovFit --algo grid $myPoints -n .Main $mySignalModifierRange  $myParameterRange
combine -M MultiDimFit datacard.root $mySeed $myAsimovFit --saveWorkspace -n .snapshot $mySignalModifierRange  $myParameterRange
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myAsimovFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_Asimov 

combine -M MultiDimFit datacard.root $mySeed $myFakeDataFit --algo grid $myPoints -n .Main $mySignalModifierRange    $myParameterRange
combine -M MultiDimFit datacard.root $mySeed $myFakeDataFit --saveWorkspace -n .snapshot $mySignalModifierRange     $myParameterRange
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myFakeDataFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_Data 

combine -M FitDiagnostics -n .Asimov datacard.root $mySeed $mySignalParamters --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL $mySignalModifierRange  $myParameterRange $myAsimovFit $verbose --skipBOnlyFit

combine -M FitDiagnostics -n "$channel" datacard.root $myFakeDataFit --plots --saveNLL --robustFit=1 $mySeed $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations $verbose $mySignalModifierRange  $myParameterRange --skipBOnlyFit
python mlfitNormsToText.py fitDiagnostics"$channel".root --uncertainties

combine -M FitDiagnostics -n .TOY datacard.root $mySeed --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL $mySignalModifierRange  $myParameterRange $myToyFit -v3  --skipBOnlyFit $myTrackParameters 

# no need to redefine POIs r and nonPromptSF but use the range for nonPromptSF 
combineTool.py -M Impacts -d datacard.root -m 125  --doInitialFit                 $myAsimovFit  --robustFit=1 $mySignalModifierRange  $myParameterRange 
combineTool.py -M Impacts -d datacard.root -m 125  --doFits                       $myAsimovFit  --robustFit=1 $mySignalModifierRange  $myParameterRange  --parallel 24
combineTool.py -M Impacts -d datacard.root -m 125  -o impacts_toy.json   $myAsimovFit  --robustFit=1 $mySignalModifierRange  $myParameterRange 
plotImpacts.py -i impacts_toy.json -o impacts_toy 

combineTool.py -M Impacts -d datacard.root -m 125  --doInitialFit                 $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange 
combineTool.py -M Impacts -d datacard.root -m 125  --doFits                       $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
combineTool.py -M Impacts -d datacard.root -m 125  -o impacts_data.json  $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange 
plotImpacts.py -i impacts_data.json -o impacts_data 

declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "Other_norm" "nonPromptSF")
for parameter in ${PARAMETERS[@]}; do
  combine -M MultiDimFit datacard.root $mySeed $myAsimovFit --algo grid $myPoints -n .Asimov_Main_"$parameter" $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange
  python plot1DScan.py higgsCombine.Asimov_Main_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_"$parameter"

  combine -M MultiDimFit datacard.root $mySeed --algo grid $myFakeDataFit $myPoints -n .Data_Main_"$parameter" $mySignalModifierRange -P $parameter --floatOtherPOIs 1  $myParameterRange
  python plot1DScan.py higgsCombine.Data_Main_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_"$parameter"
done


wait
echo "Done fitting only!!!"

exit 1


echo "python makettGammaSS.py"
python makettGammaSS.py
echo "python makettGammaSS_Toy.py"
python makettGammaSS_Toy.py
echo "python makettGammaSS_Toy.py"
python makettGammaSS_Asimov.py
echo "python makeCovarianceMatrix.py"
python makeCovarianceMatrix.py
echo "python getTrackParameterPlots.py"
python getTrackParameterPlots.py
echo "python getNPToyDistribution.py"
python getNPToyDistribution.py

echo "Done fitting and Extraction!!!"

exit 1
#For test
setenv channel "ele"
setenv myParameterRange " --setParameterRanges nonPromptSF=0,5:TTbarSF=0,4:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 "
setenv mySignalParamters " --redefineSignalPOIs=r,nonPromptSF "
setenv mySignalModifierRange " --rMin=-1 --rMax=5 "
setenv myAsimovFit " -t -1 --expectSignal 1 "
setenv myFakeDataFit " -t 1 --expectSignal 1 "
setenv myToyFit " -t 300 --expectSignal 1 "
setenv verbose " -v3 "
setenv myTrackParameters " --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
setenv mySeed " --seed=314159 "
setenv myPoints " --points=100 "