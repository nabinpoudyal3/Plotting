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

rm *.png
rm *.json
rm *.tex
rm single_scan_*.pdf
rm impacts*.pdf
rm freeze*.pdf
rm datacard_*_2018.root
rm higgsCombine.*.root
rm higgsCombine_*.root
rm single_scan_*.root
rm fitDiagnostics*.root

./allCombine.sh
text2workspace.py    datacard_ele_2018.txt 
ValidateDatacards.py datacard_ele_2018.txt  --printLevel 3 --checkUncertOver 0.1 
text2workspace.py    datacard_mu_2018.txt 
ValidateDatacards.py datacard_mu_2018.txt   --printLevel 3 --checkUncertOver 0.1 
text2workspace.py    datacard_both_2018.txt 
ValidateDatacards.py datacard_both_2018.txt --printLevel 3 --checkUncertOver 0.1 

declare -a CHANNEL=("ele" "mu" "both") 
for channel in ${CHANNEL[@]}; do

    combine -M ChannelCompatibilityCheck --expectSignal=1  datacard_"$channel"_2018.root $verbose $mySignalParamters  $myParameterRange
    combine datacard_"$channel"_2018.root -M FitDiagnostics -n .datacard_"$channel"_2018 $myAsimovFit  $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
    python diffNuisances.py fitDiagnostics.datacard_"$channel"_2018.root --all 

    combine datacard_"$channel"_2018.root -M FitDiagnostics -n .datacard_"$channel"_2018 $myFakeDataFit $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
    python diffNuisances.py fitDiagnostics.datacard_"$channel"_2018.root --all 

    combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed $myAsimovFit --algo grid $myPoints -n .Main $mySignalModifierRange  $myParameterRange
    combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed $myAsimovFit --saveWorkspace -n .snapshot $mySignalModifierRange  $myParameterRange
    combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myAsimovFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
    python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2018_Asimov 

    combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed $myFakeDataFit --algo grid $myPoints -n .Main $mySignalModifierRange    $myParameterRange
    combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed $myFakeDataFit --saveWorkspace -n .snapshot $mySignalModifierRange     $myParameterRange
    combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myFakeDataFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
    python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2018_Data 

    combine -M FitDiagnostics -n .Asimov_"$channel"_2018 datacard_"$channel"_2018.root $mySeed $mySignalParamters --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL $mySignalModifierRange  $myParameterRange $myAsimovFit $verbose --skipBOnlyFit

    combine -M FitDiagnostics -n "$channel"_2018 datacard_"$channel"_2018.root $myFakeDataFit --plots --saveNLL --robustFit=1 $mySeed $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations $verbose $mySignalModifierRange  $myParameterRange --skipBOnlyFit
    python mlfitNormsToText.py fitDiagnostics$"channel"_2018.root --uncertainties

    combine -M FitDiagnostics -n .TOY_"$channel"_2018 datacard_"$channel"_2018.root $mySeed --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL $mySignalModifierRange  $myParameterRange $myToyFit -v3  --skipBOnlyFit $myTrackParameters 

    # no need to redefine POIs r and nonPromptSF but use the range for nonPromptSF 
    combineTool.py -M Impacts -d datacard_"$channel"_2018.root -m 125  --doInitialFit                 $myAsimovFit  --robustFit=1 $mySignalModifierRange  $myParameterRange 
    combineTool.py -M Impacts -d datacard_"$channel"_2018.root -m 125  --doFits                       $myAsimovFit  --robustFit=1 $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py -M Impacts -d datacard_"$channel"_2018.root -m 125  -o impacts_toy_"$channel"_2018.json   $myAsimovFit  --robustFit=1 $mySignalModifierRange  $myParameterRange 
    plotImpacts.py -i impacts_toy_"$channel"_2018.json -o impacts_toy_"$channel"_2018 

    combineTool.py -M Impacts -d datacard_"$channel"_2018.root -m 125  --doInitialFit                 $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange 
    combineTool.py -M Impacts -d datacard_"$channel"_2018.root -m 125  --doFits                       $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py -M Impacts -d datacard_"$channel"_2018.root -m 125  -o impacts_data_"$channel"_2018.json  $myFakeDataFit  --robustFit=1   $mySignalModifierRange  $myParameterRange 
    plotImpacts.py -i impacts_data_"$channel"_2018.json -o impacts_data_"$channel"_2018 

    declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "Other_norm" "nonPromptSF")
    for parameter in ${PARAMETERS[@]}; do
      combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed $myAsimovFit --algo grid $myPoints -n .Asimov_Main_"$channel"_"$parameter" $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange
      python plot1DScan.py higgsCombine.Asimov_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_"$channel"_"$parameter"

      combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed --algo grid $myFakeDataFit $myPoints -n .Data_Main_"$channel"_"$parameter" $mySignalModifierRange -P $parameter --floatOtherPOIs 1  $myParameterRange
      python plot1DScan.py higgsCombine.Data_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_"$channel"_"$parameter"
    done

done

wait
echo "Done fitting only!!!"

echo "python make2018ttGammaSS.py"
python make2018ttGammaSS.py
echo "python make2018ttGammaSS_Toy.py"
python make2018ttGammaSS_Toy.py
echo "python make2018ttGammaSS_Toy.py"
python make2018ttGammaSS_Asimov.py
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
setenv myParameterRange " --setParameterRanges nonPromptSF=0,10:TTbarSF=0,4:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 "
setenv mySignalParamters " --redefineSignalPOIs=r,nonPromptSF "
setenv mySignalModifierRange " --rMin=0 --rMax=10 "
setenv myAsimovFit " -t -1 --expectSignal 1 "
setenv myFakeDataFit " -t 1 --expectSignal 1 "
setenv myToyFit " -t 300 --expectSignal 1 "
setenv verbose " -v3 "
setenv myTrackParameters " --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
setenv mySeed " --seed=314159 "
setenv myPoints " --points=300 "