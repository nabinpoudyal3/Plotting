#!/bin/bash

myParameterRange=" --setParameterRanges nonPromptSF=0,5:TTbarSF=0,4:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 "
mySignalParamters=" --redefineSignalPOIs=r,nonPromptSF "
mySignalModifierRange=" --rMin=-1 --rMax=5 "
myAsimovFit=" -t -1 --expectSignal 1 "
myFakeDataFit=" -t 1 --expectSignal 1 "
myToyFit=" -t 300 --expectSignal 1 "
verbose=" -v1 "
myTrackParameters=" --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
mySeed=" --seed=314159 "
myPoints=" --points=100 "
year="2016"
channel="ele"

rm *.png
rm *.json
rm *.tex
rm single_scan_*.pdf
rm impacts*.pdf
rm freeze*.pdf
rm datacard_*_"$year".root
rm higgsCombine.*.root
rm higgsCombine_*.root
rm single_scan_*.root
rm fitDiagnostics*.root

./allCombine.sh
text2workspace.py    datacard_"$channel"_"$year".txt 
ValidateDatacards.py datacard_"$channel"_"$year".txt  --printLevel 3 --checkUncertOver 0.1 


combine -M ChannelCompatibilityCheck --expectSignal=1  datacard_"$channel"_"$year".root $verbose $mySignalParamters  $myParameterRange
combine datacard_"$channel"_"$year".root -M FitDiagnostics -n .datacard_"$channel"_"$year" $myAsimovFit  $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
python diffNuisances.py fitDiagnostics.datacard_"$channel"_"$year".root --all 

combine datacard_"$channel"_"$year".root -M FitDiagnostics -n .datacard_"$channel"_"$year" $myFakeDataFit $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
python diffNuisances.py fitDiagnostics.datacard_"$channel"_"$year".root --all 

combine -M MultiDimFit datacard_"$channel"_"$year".root $mySeed $myAsimovFit --algo grid $myPoints -n .Main $mySignalModifierRange  $myParameterRange
combine -M MultiDimFit datacard_"$channel"_"$year".root $mySeed $myAsimovFit --saveWorkspace -n .snapshot $mySignalModifierRange  $myParameterRange
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myAsimovFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_"$year"_Asimov 

combine -M MultiDimFit datacard_"$channel"_"$year".root $mySeed $myFakeDataFit --algo grid $myPoints -n .Main $mySignalModifierRange    $myParameterRange
combine -M MultiDimFit datacard_"$channel"_"$year".root $mySeed $myFakeDataFit --saveWorkspace -n .snapshot $mySignalModifierRange     $myParameterRange
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myFakeDataFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_"$year"_Data 

combine -M FitDiagnostics -n .Asimov_"$channel"_"$year" datacard_"$channel"_"$year".root $mySeed $mySignalParamters --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL $mySignalModifierRange  $myParameterRange $myAsimovFit $verbose --skipBOnlyFit

combine -M FitDiagnostics -n "$channel"_"$year" datacard_"$channel"_"$year".root $myFakeDataFit --plots --saveNLL --robustFit=1 $mySeed $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations $verbose $mySignalModifierRange  $myParameterRange --skipBOnlyFit
python mlfitNormsToText.py fitDiagnostics"$channel"_"$year".root --uncertainties

combine -M FitDiagnostics -n .TOY_"$channel"_"$year" datacard_"$channel"_"$year".root $mySeed --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL $mySignalModifierRange  $myParameterRange $myToyFit -v3  --skipBOnlyFit $myTrackParameters 

# no need to redefine POIs r and nonPromptSF but use the range for nonPromptSF 
combineTool.py -M Impacts -d datacard_"$channel"_"$year".root -m 125  --doInitialFit                 $myAsimovFit  --robustFit=1 $mySignalModifierRange  $myParameterRange 
combineTool.py -M Impacts -d datacard_"$channel"_"$year".root -m 125  --doFits                       $myAsimovFit  --robustFit=1 $mySignalModifierRange  $myParameterRange  --parallel 24
combineTool.py -M Impacts -d datacard_"$channel"_"$year".root -m 125  -o impacts_toy_"$channel"_"$year".json   $myAsimovFit  --robustFit=1 $mySignalModifierRange  $myParameterRange 
plotImpacts.py -i impacts_toy_"$channel"_"$year".json -o impacts_toy_"$channel"_"$year" 

combineTool.py -M Impacts -d datacard_"$channel"_"$year".root -m 125  --doInitialFit                 $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange 
combineTool.py -M Impacts -d datacard_"$channel"_"$year".root -m 125  --doFits                       $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
combineTool.py -M Impacts -d datacard_"$channel"_"$year".root -m 125  -o impacts_data_"$channel"_"$year".json  $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange 
plotImpacts.py -i impacts_data_"$channel"_"$year".json -o impacts_data_"$channel"_"$year" 

declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "Other_norm" "nonPromptSF")
for parameter in ${PARAMETERS[@]}; do
  combine -M MultiDimFit datacard_"$channel"_"$year".root $mySeed $myAsimovFit --algo grid $myPoints -n .Asimov_Main_"$channel"_"$parameter" $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange
  python plot1DScan.py higgsCombine.Asimov_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_"$channel"_"$parameter"

  combine -M MultiDimFit datacard_"$channel"_"$year".root $mySeed --algo grid $myFakeDataFit $myPoints -n .Data_Main_"$channel"_"$parameter" $mySignalModifierRange -P $parameter --floatOtherPOIs 1  $myParameterRange
  python plot1DScan.py higgsCombine.Data_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_"$channel"_"$parameter"
done

wait

echo "python make"$year"ttGammaSS.py"
python make"$year"ttGammaSS.py
echo "python make"$year"ttGammaSS_Toy.py"
python make"$year"ttGammaSS_Toy.py
echo "python make"$year"ttGammaSS_Toy.py"
python make"$year"ttGammaSS_Asimov.py
echo "python makeCovarianceMatrix.py"
python makeCovarianceMatrix.py
echo "python getTrackParameterPlots.py"
python getTrackParameterPlots.py
echo "python getNPToyDistribution.py"
python getNPToyDistribution.py

exit 1

setenv myParameterRange " --setParameterRanges nonPromptSF=0,5:TTbarSF=0,4:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 "
setenv mySignalParamters " --redefineSignalPOIs=r,nonPromptSF "
setenv mySignalModifierRange " --rMin=-1 --rMax=5 "
setenv myAsimovFit " -t -1 --expectSignal 1 "
setenv myFakeDataFit " -t 1 --expectSignal 1 "
setenv myToyFit " -t 300 --expectSignal 1 "
setenv verbose " -v1 "
setenv myTrackParameters " --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
setenv mySeed " --seed=314159 "
setenv myPoints " --points=100 "
setenv year "2016"
setenv channel "ele"