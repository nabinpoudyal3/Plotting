#!/bin/bash

# rm *.png
# rm impacts*.json
# rm validation.json
# rm single_scan_*.pdf
# rm impacts*.pdf
# rm freeze*.pdf
# rm combine_logger.out
# rm *.tex
# rm higgsCombine.*.root
# rm higgsCombine_*.root
# rm single_scan_*.root
# rm fitDiagnostics*.root

# rm datacard_*_2017.root

./allCombine.sh
text2workspace.py datacard_ele_2017.dat  --out=datacard_ele_2017.root  --default-morphing=DEFMORPH 
text2workspace.py datacard_mu_2017.dat   --out=datacard_mu_2017.root   --default-morphing=DEFMORPH 
text2workspace.py datacard_both_2017.dat --out=datacard_both_2017.root --default-morphing=DEFMORPH 

ValidateDatacards.py datacard_ele_2017.dat  --printLevel 3 --checkUncertOver 0.1 
ValidateDatacards.py datacard_mu_2017.dat   --printLevel 3 --checkUncertOver 0.1 
ValidateDatacards.py datacard_both_2017.dat --printLevel 3 --checkUncertOver 0.1 

mySignalParamters=" --redefineSignalPOIs=r,nonPromptSF "
myAsimovFit=" -t -1 --expectSignal 1 "
myExpectSignal=" --expectSignal 1 "
myToyFit=" -t 50 --expectSignal 1 "
verbose=" -v1 "
# myTrackParameters=" --trackParameters r,BTagSF_b,BTagSF_l,PhoEff,lumi,misIDE,Pdf,isr,fsr,PU,prefireEcal,JECTotal,JER,Q2,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
mySeed=" --seed=314159 "
myPoints=" --points=50 "
myFakeDataFit=" -t 1 --expectSignal 1  "
mySignalModifierRange=" --rMin=0 --rMax=2 "
# myParameterRange=" "
myParameterRange=" --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:Other_norm=0,5:ZGSF=0,5:SingleTopSF=0,2 "
# myParameterRange=" --autoBoundsPOIs "WGSF,OtherSF,Other_norm" "

declare -a CHANNEL=("ele" "mu") 
for channel in ${CHANNEL[@]}; do
set -x

    combine -M ChannelCompatibilityCheck datacard_"$channel"_2017.root $verbose $mySignalParamters  $myParameterRange $myExpectSignal

    # combine datacard_"$channel"_2017.root --skipBOnlyFit --skipBOnlyFit -M FitDiagnostics -n .datacard_"$channel"_2017_Asimov $myAsimovFit   $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
    # python diffNuisances.py fitDiagnostics.datacard_"$channel"_2017_Asimov.root
    # combine datacard_"$channel"_2017.root --skipBOnlyFit --skipBOnlyFit -M FitDiagnostics -n .datacard_"$channel"_2017_Data   $myFakeDataFit $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange $myExpectSignal
    # python diffNuisances.py fitDiagnostics.datacard_"$channel"_2017_Data.root --all 
    
    combine --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n .Asimov_"$channel"_2017 datacard_"$channel"_2017.root $mySeed   --saveOverallShapes     --plots --saveNLL   $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations  $mySignalModifierRange  $myParameterRange $myAsimovFit                   $verbose 
    # combine --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n "$channel"_2017         datacard_"$channel"_2017.root $mySeed   --saveOverallShapes     --plots --saveNLL   $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations  $mySignalModifierRange  $myParameterRange $myExpectSignal $myFakeDataFit $verbose 
    combine --cminPreScan --skipBOnlyFit --forceRecreateNLL -M FitDiagnostics -n .TOY_"$channel"_2017    datacard_"$channel"_2017.root $mySeed                           --plots --saveNLL   $mySignalParamters              --saveWithUncertainties --saveNormalizations  $mySignalModifierRange  $myParameterRange $myToyFit                      -v3   

    combine -M MultiDimFit datacard_"$channel"_2017.root $mySeed $myAsimovFit --algo grid $myPoints -n .Main $mySignalModifierRange  $myParameterRange
    combine -M MultiDimFit datacard_"$channel"_2017.root $mySeed $myAsimovFit --saveWorkspace -n .snapshot $mySignalModifierRange  $myParameterRange
    combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myAsimovFit -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
    python plot1DScan.py  --translate rename.json  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2017_Asimov 

    # combine -M MultiDimFit datacard_"$channel"_2017.root                       $mySeed $myFakeDataFit --algo grid $myPoints -n .Main $mySignalModifierRange     $myParameterRange $myExpectSignal
    # combine -M MultiDimFit datacard_"$channel"_2017.root                       $mySeed $myFakeDataFit --saveWorkspace -n .snapshot   $mySignalModifierRange     $myParameterRange $myExpectSignal
    # combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myFakeDataFit -n .freezeAll  --algo grid     $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange $myExpectSignal
    # python plot1DScan.py  --translate rename.json  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2017_Data 
    

    # no need to redefine POIs r and nonPromptSF but use the range for nonPromptSF 
    combineTool.py  --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  --doInitialFit                        $myAsimovFit    --robustFit=1   $mySignalModifierRange  $myParameterRange 
    combineTool.py  --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  --doFits                              $myAsimovFit    --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py  --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  -o impacts_toy_"$channel"_2017.json   $myAsimovFit    --robustFit=1   $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2017.json -o impacts_toy_"$channel"_2017 --label-size 0.035

    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  --doInitialFit                        $myFakeDataFit  --robustFit=1  $mySignalModifierRange  $myParameterRange 
    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  --doFits                              $myFakeDataFit  --robustFit=1  $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  -o impacts_data_"$channel"_2017.json  $myFakeDataFit  --robustFit=1  $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_data_"$channel"_2017.json -o impacts_data_"$channel"_2017 --label-size 0.035

    # combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  --doInitialFit                                   $myAsimovFit --redefineSignalPOIs   TTbarSF    --robustFit=1   $mySignalModifierRange  $myParameterRange 
    # combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  --doFits                                         $myAsimovFit --redefineSignalPOIs   TTbarSF    --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
    # combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  -o impacts_toy_"$channel"_2017_TTbarSF.json      $myAsimovFit --redefineSignalPOIs   TTbarSF    --robustFit=1   $mySignalModifierRange  $myParameterRange 
    # plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2017_TTbarSF.json -o impacts_toy_"$channel"_2017_TTbarSF  --label-size 0.035 --POI TTbarSF

    # combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  --doInitialFit                                 $myFakeDataFit --redefineSignalPOIs   TTbarSF --robustFit=1 $mySignalModifierRange  $myParameterRange 
    # combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  --doFits                                         $myFakeDataFit --redefineSignalPOIs   TTbarSF --robustFit=1 $mySignalModifierRange  $myParameterRange  --parallel 24
    # combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2017.root -m 125  -o impacts_data_"$channel"_2017_TTbarSF.json     $myFakeDataFit --redefineSignalPOIs   TTbarSF --robustFit=1 $mySignalModifierRange  $myParameterRange 
    # plotImpacts.py  -t rename.json  -i impacts_data_"$channel"_2017_TTbarSF.json -o impacts_data_"$channel"_2017_TTbarSF --label-size 0.035 --POI TTbarSF

    # declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "Pdf" "isr" "fsr" "PU" "prefireEcal" "JECTotal" "JER" "Q2" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "Other_norm" "nonPromptSF")
    # # declare -a PARAMETERS=("TTbarSF")
    # for parameter in ${PARAMETERS[@]}; do
    #   combine -M MultiDimFit datacard_"$channel"_2017.root $mySeed $myAsimovFit   --algo grid  $myPoints -n .Asimov_Main_"$channel"_"$parameter" $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange
    #   python plot1DScan.py  --translate rename.json higgsCombine.Asimov_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_"$channel"_"$parameter"

    #   combine -M MultiDimFit datacard_"$channel"_2017.root $mySeed $myFakeDataFit --algo grid  $myPoints -n .Data_Main_"$channel"_"$parameter"   $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange $myExpectSignal
    #   python plot1DScan.py  --translate rename.json higgsCombine.Data_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_"$channel"_"$parameter"
    # done
done

echo "Done fitting only!!!"

# python makettGammaSS.py         
python makettGammaSS_Toy.py     
python makettGammaSS_Asimov.py   
python makeCorrelationMatrixNoData.py   
# python makeCorrelationMatrix.py   
# python makeTotalCovarianceMatrix.py    
   
# python getTrackParameterPlots.py
# python getNPToyDistribution.py

echo "Done fitting and Extraction!!!"


# Toy toysFrequentist has the following benifits:
# Your analysis may have parameters which are determined from the observed data (eg, you are fitting a mass spectrum with some function for the background whose parameters are determined from the S+B fit). In this case, you should add --toysFrequentist to your combine line which will first fit the data to produce reasonable estimates for these free parameters. 
# One of your nuisances seems to not close and it is a gmN type nuisance. This is related to the initial guess for the poisson component in these nuisances which is n+1 as opposed to n. This can also be avoided using toysFrequentist 




