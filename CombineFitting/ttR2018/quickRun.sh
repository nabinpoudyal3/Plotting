#!/bin/bash

myParameterRange=" --setParameterRanges nonPromptSF=0,5:TTbarSF=0,3:WGSF=0,3:OtherSF=0,3:Other_norm=0,3:ZGSF=0,3 "
mySignalParamters=" --redefineSignalPOIs=r,nonPromptSF "
mySignalModifierRange=" --rMin=0.001 --rMax=0.2 "
myAsimovFit=" -t -1 --expectSignal 0.02 "
myFakeDataFit=" -t 1 --expectSignal 0.02 --saveToys " #if toysFrequentist is used the setParameter will be ignored.
# myFakeDataFit=" "
myToyFit=" -t 300 --expectSignal 0.02 "
verbose=" -v0 "
myTrackParameters=" --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
mySeed=" --seed=314159 "
myPoints=" --points=200 "
# myOptions=" --stepSize 0.001 "
myOptions=" "
declare -a CHANNEL=("ele")
 # "mu" "both") 
for channel in ${CHANNEL[@]}; do

    combine -M ChannelCompatibilityCheck --expectSignal=1  datacard_"$channel"_2016.root $verbose $mySignalParamters  $myParameterRange 
    combine datacard_"$channel"_2016.root -M FitDiagnostics -n .datacard_"$channel"_2016 $myAsimovFit  $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange $myOptions
    python diffNuisances.py fitDiagnostics.datacard_"$channel"_2016.root --all 

    combine datacard_"$channel"_2016.root -M FitDiagnostics -n .datacard_"$channel"_2016 $myFakeDataFit $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange $myOptions
    python diffNuisances.py fitDiagnostics.datacard_"$channel"_2016.root --all 

    combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myOptions $myAsimovFit --algo grid $myPoints -n .Main $mySignalModifierRange  $myParameterRange 
    combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myOptions $myAsimovFit --saveWorkspace -n .snapshot $mySignalModifierRange  $myParameterRange 
    combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myOptions $myAsimovFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
    python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2016_Asimov 

    combine -M MultiDimFit datacard_"$channel"_2018.root                            $mySeed  $myOptions $myFakeDataFit --algo grid $myPoints -n .Main_Data                                                                  $mySignalModifierRange    $myParameterRange 
    combine -M MultiDimFit datacard_"$channel"_2018.root                            $mySeed  $myOptions $myFakeDataFit --saveWorkspace       -n .snapshot_Data                                                              $mySignalModifierRange    $myParameterRange
    combine -M MultiDimFit higgsCombine.snapshot_Data.MultiDimFit.mH120.314159.root $mySeed  $myOptions $myFakeDataFit --algo grid $myPoints -n .freezeAll_Data    --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
    combine -M FitDiagnostics -n .Asimov_"$channel"_2016 datacard_"$channel"_2016.root $mySeed $mySignalParamters --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL $mySignalModifierRange  $myParameterRange $myAsimovFit $verbose --skipBOnlyFit
    python plot1DScan.py  higgsCombine.Main_Data.MultiDimFit.mH120.314159.root  --others  'higgsCombine.freezeAll_Data.MultiDimFit.mH120.314159.root:Stat:2'   --breakdown Syst,Stat  -o freeze_"$channel"_2018_Data 

    combine -M FitDiagnostics -n "$channel"_2016 datacard_"$channel"_2016.root $myFakeDataFit --plots --saveNLL --robustFit=1 $mySeed $myOptions $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations $verbose $mySignalModifierRange  $myParameterRange --skipBOnlyFit
    python mlfitNormsToText.py fitDiagnostics"$channel"_2016.root --uncertainties

    combine -M FitDiagnostics -n .TOY_"$channel"_2016 datacard_"$channel"_2016.root $mySeed $myOptions --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL $mySignalModifierRange  $myParameterRange $myToyFit -v3  --skipBOnlyFit $myTrackParameters 

    # no need to redefine POIs r and nonPromptSF but use the range for nonPromptSF 
    combineTool.py -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                        $myAsimovFit $myOptions   --robustFit=1 $mySignalModifierRange  $myParameterRange 
    combineTool.py -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                              $myAsimovFit $myOptions   --robustFit=1 $mySignalModifierRange  $myParameterRange --parallel 24
    combineTool.py -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_toy_"$channel"_2016.json   $myAsimovFit $myOptions   --robustFit=1 $mySignalModifierRange  $myParameterRange 
    plotImpacts.py -i impacts_toy_"$channel"_2016.json -o impacts_toy_"$channel"_2016 

    combineTool.py -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                        $myFakeDataFit $myOptions --robustFit=1 $mySignalModifierRange  $myParameterRange 
    combineTool.py -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                              $myFakeDataFit $myOptions --robustFit=1 $mySignalModifierRange  $myParameterRange --parallel 24
    combineTool.py -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_data_"$channel"_2016.json  $myFakeDataFit $myOptions --robustFit=1 $mySignalModifierRange  $myParameterRange 
    plotImpacts.py -i impacts_data_"$channel"_2016.json -o impacts_data_"$channel"_2016 

    
done

echo "python make2016ttGammaSS.py"
python make2016ttGammaSS.py
echo "python make2016ttGammaSS_Toy.py"
python make2016ttGammaSS_Toy.py
echo "python make2016ttGammaSS_Toy.py"
python make2016ttGammaSS_Asimov.py
echo "python makeCovarianceMatrix.py"
python makeCovarianceMatrix.py
echo "python getTrackParameterPlots.py"
python getTrackParameterPlots.py
echo "python getNPToyDistribution.py"
python getNPToyDistribution.py
