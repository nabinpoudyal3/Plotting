#!/bin/bash

# rm *.png
# rm impacts*.json
# rm validation.json
# rm single_scan_*.pdf
# rm impacts*.pdf
# rm freeze*.pdf
# rm datacard_*_2018.root
# rm higgsCombine.*.root
# rm higgsCombine_*.root
# rm single_scan_*.root
# rm fitDiagnostics*.root
# rm combine_logger.out
# rm *.tex

./allCombine.sh
text2workspace.py    datacard_ele_2018.dat   --out=datacard_ele_2018.root   --default-morphing=DEFMORPH 
text2workspace.py    datacard_mu_2018.dat    --out=datacard_mu_2018.root    --default-morphing=DEFMORPH 
text2workspace.py    datacard_both_2018.dat  --out=datacard_both_2018.root  --default-morphing=DEFMORPH 

# ValidateDatacards.py datacard_ele_2018.dat  --printLevel 3 --checkUncertOver 0.1 
# ValidateDatacards.py datacard_mu_2018.dat   --printLevel 3 --checkUncertOver 0.1 
# ValidateDatacards.py datacard_both_2018.dat --printLevel 3 --checkUncertOver 0.1 

myParameterRange=" --setParameterRanges nonPromptSF=0,5:WGSF=0,5:TTbarSF=500,1100:OtherSF=0,5:Other_norm=0,5:ZGSF=0,5:SingleTopSF=0,2 "
mySignalParamters=" --redefineSignalPOIs=r,nonPromptSF,TTbarSF "
mySignalModifierRange=" --rMin=0 --rMax=0.1 "
myExpectSignal=" --setParameters r=0.02 "
myAsimovFit=" -t -1 "
myFakeDataFit="  "
myToyFit=" -t 100 --setParameters r=0.02 "
verbose=" -v2 "
# myTrackParameters=" --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,Pdf,isr,fsr,PU,prefireEcal,JECTotal,JER,Q2,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
mySeed=" --seed=314159 "
myPoints=" --points=300 "
mystepSize=" --stepSize=0.001 "


declare -a CHANNEL=("ele" "mu") 
for channel in ${CHANNEL[@]}; do
set -x

    # combine -M ChannelCompatibilityCheck datacard_"$channel"_2018.root $verbose $mySignalParamters  $myParameterRange $myExpectSignal

    # combine datacard_"$channel"_2018.root --skipBOnlyFit --skipBOnlyFit -M FitDiagnostics -n .datacard_"$channel"_2018_Asimov $myAsimovFit  $myExpectSignal $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
    # python diffNuisances.py fitDiagnostics.datacard_"$channel"_2018_Asimov.root
    # combine datacard_"$channel"_2018.root --skipBOnlyFit --skipBOnlyFit -M FitDiagnostics -n .datacard_"$channel"_2018_Data   $myFakeDataFit $myExpectSignal $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange $myExpectSignal
    # python diffNuisances.py fitDiagnostics.datacard_"$channel"_2018_Data.root --all 
    
    combine --cminPreScan --skipBOnlyFit  -M FitDiagnostics -n .Asimov_"$channel"_2018 datacard_"$channel"_2018.root $mySeed   --saveOverallShapes     --plots --saveNLL   $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations  $mySignalModifierRange  $myParameterRange $myAsimovFit   $myExpectSignal                $verbose 
    # combine --cminPreScan --skipBOnlyFit  -M FitDiagnostics -n "$channel"_2018         datacard_"$channel"_2018.root $mySeed   --saveOverallShapes     --plots --saveNLL   $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations  $mySignalModifierRange  $myParameterRange $myFakeDataFit $myExpectSignal $verbose 
    # combine --cminPreScan --skipBOnlyFit  -M FitDiagnostics -n .TOY_"$channel"_2018    datacard_"$channel"_2018.root $mySeed                           --plots --saveNLL   $mySignalParamters              --saveWithUncertainties --saveNormalizations  $mySignalModifierRange  $myParameterRange $myToyFit                      -v3   

    combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed $myAsimovFit $myExpectSignal --algo grid $myPoints -n .Main $mySignalModifierRange  $myParameterRange
    combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed $myAsimovFit $myExpectSignal --saveWorkspace -n .snapshot $mySignalModifierRange  $myParameterRange
    combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myAsimovFit $myExpectSignal -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
    python plot1DScan.py  --translate rename.json  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2018_Asimov 

    # combine -M MultiDimFit datacard_"$channel"_2018.root                       $mySeed $myFakeDataFit $myExpectSignal --algo grid $myPoints -n .Main $mySignalModifierRange     $myParameterRange 
    # combine -M MultiDimFit datacard_"$channel"_2018.root                       $mySeed $myFakeDataFit $myExpectSignal --saveWorkspace -n .snapshot   $mySignalModifierRange     $myParameterRange 
    # combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myFakeDataFit $myExpectSignal -n .freezeAll  --algo grid     $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange 
    # python plot1DScan.py  --translate rename.json  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2018_Data 
    

    combineTool.py  $mystepSize --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  --doInitialFit                        $myAsimovFit $myExpectSignal   --robustFit=1   $mySignalModifierRange  $myParameterRange 
    combineTool.py  $mystepSize --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  --doFits                              $myAsimovFit $myExpectSignal   --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py  $mystepSize --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  -o impacts_toy_"$channel"_2018.json   $myAsimovFit $myExpectSignal   --robustFit=1   $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2018.json -o impacts_toy_"$channel"_2018 --label-size 0.035

    # combineTool.py $mystepSize --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  --doInitialFit                        $myFakeDataFit $myExpectSignal --robustFit=1   $mySignalModifierRange  $myParameterRange 
    # combineTool.py $mystepSize --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  --doFits                              $myFakeDataFit $myExpectSignal --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
    # combineTool.py $mystepSize --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  -o impacts_data_"$channel"_2018.json  $myFakeDataFit $myExpectSignal --robustFit=1   $mySignalModifierRange  $myParameterRange 
    # plotImpacts.py  -t rename.json  -i impacts_data_"$channel"_2018.json -o impacts_data_"$channel"_2018 --label-size 0.035

    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  --doInitialFit                                   $myAsimovFit --redefineSignalPOIs   TTbarSF --setParameters TTbarSF=831  $mySignalModifierRange --robustFit=1   $mySignalModifierRange  $myParameterRange 
    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  --doFits                                         $myAsimovFit --redefineSignalPOIs   TTbarSF --setParameters TTbarSF=831  $mySignalModifierRange --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  -o impacts_toy_"$channel"_2018_TTbarSF.json      $myAsimovFit --redefineSignalPOIs   TTbarSF --setParameters TTbarSF=831  $mySignalModifierRange --robustFit=1   $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2018_TTbarSF.json -o impacts_toy_"$channel"_2018_TTbarSF  --label-size 0.035 --POI TTbarSF

    # combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  --doInitialFit                                   $myFakeDataFit --redefineSignalPOIs   TTbarSF --setParameters TTbarSF=831 $mySignalModifierRange --robustFit=1  $mySignalModifierRange  $myParameterRange 
    # combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  --doFits                                         $myFakeDataFit --redefineSignalPOIs   TTbarSF --setParameters TTbarSF=831 $mySignalModifierRange --robustFit=1  $mySignalModifierRange  $myParameterRange  --parallel 24
    # combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2018.root -m 125  -o impacts_data_"$channel"_2018_TTbarSF.json     $myFakeDataFit --redefineSignalPOIs   TTbarSF --setParameters TTbarSF=831 $mySignalModifierRange --robustFit=1  $mySignalModifierRange  $myParameterRange 
    # plotImpacts.py  -t rename.json  -i impacts_data_"$channel"_2018_TTbarSF.json -o impacts_data_"$channel"_2018_TTbarSF --label-size 0.035 --POI TTbarSF

    # declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "Pdf" "isr" "fsr" "PU" "prefireEcal" "JECTotal" "JER" "Q2" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "Other_norm" "nonPromptSF")
    # # declare -a PARAMETERS=("TTbarSF")
    # for parameter in ${PARAMETERS[@]}; do
    #   combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed $myAsimovFit   --algo grid  $myPoints -n .Asimov_Main_"$channel"_"$parameter" $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange
    #   python plot1DScan.py  --translate rename.json higgsCombine.Asimov_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_"$channel"_"$parameter"

    #   combine -M MultiDimFit datacard_"$channel"_2018.root $mySeed $myFakeDataFit --algo grid  $myPoints -n .Data_Main_"$channel"_"$parameter"   $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange $myExpectSignal
    #   python plot1DScan.py  --translate rename.json higgsCombine.Data_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_"$channel"_"$parameter"
    # done
done

wait
"Done fitting only!!!"
# python makettGammaSS.py 
python makettGammaSS_Toy.py 
python makettGammaSS_Asimov.py 
# python makeCorrelationMatrix.py 
python makeCorrelationMatrixNoData.py 
# python makeTotalCovarianceMatrix.py    

# python getTrackParameterPlots.py
# python getNPToyDistribution.py

"Done Ratio fitting and Extraction!!!"





# subl -n makettGammaSS.py makettGammaSS_Toy.py makettGammaSS_Asimov.py makeCorrelationMatrix.py 

exit 1

cp ../ttR2018/finalScript.sh . 
cp ../ttR2018/quickFit.sh . 
cp ../ttR2018/allCombine.sh . 
cp ../ttR2018/*.dat . 
