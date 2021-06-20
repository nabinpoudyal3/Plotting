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

# rm datacard_*_2016.root

./allCombine.sh
text2workspace.py datacard_ele_2016.dat  --out=datacard_ele_2016.root  --default-morphing=DEFMORPH 
text2workspace.py datacard_mu_2016.dat   --out=datacard_mu_2016.root   --default-morphing=DEFMORPH 
text2workspace.py datacard_both_2016.dat --out=datacard_both_2016.root --default-morphing=DEFMORPH 

# ValidateDatacards.py datacard_ele_2016.dat  --printLevel 3 --checkUncertOver 0.1 
# ValidateDatacards.py datacard_mu_2016.dat   --printLevel 3 --checkUncertOver 0.1 
# ValidateDatacards.py datacard_both_2016.dat --printLevel 3 --checkUncertOver 0.1 

mySignalParamters=" --redefineSignalPOIs=r,nonPromptSF "
# myAsimovFit=" -t -1 --expectSignal 1 "
myAsimovFit=" -t -1"
myExpectSignal=" --setParameters r=1 "
myToyFit=" -t 50 --setParameters r=1 "
verbose=" -v1 "
# myTrackParameters=" --trackParameters r,BTagSF_b,BTagSF_l,PhoEff,lumi,misIDE,Pdf,isr,fsr,PU,prefireEcal,JECTotal,JER,Q2,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
mySeed=" --seed=314159 "
myPoints=" --points=100 "
myFakeDataFit=" "
mySignalModifierRange=" --rMin=0 --rMax=2 "
# myParameterRange=" "
myParameterRange=" --setParameterRanges nonPromptSF=0,5:TTbarSF=0,5:WGSF=0,5:OtherSF=0,5:Other_norm=0,5:ZGSF=0,5:SingleTopSF=0,2 "
# myParameterRange=" --autoBoundsPOIs "WGSF,OtherSF,Other_norm" "

# myFreeze=" --freezeParameters shapeDD "
myFreeze=" "
declare -a CHANNEL=("ele" "mu") 
# declare -a CHANNEL=("ele" "mu" "both") 
for channel in ${CHANNEL[@]}; do
# trap read debug
set -x
    # combine -M ChannelCompatibilityCheck datacard_"$channel"_2016.root $verbose $mySignalParamters  $myParameterRange $myExpectSignal
    # combine datacard_"$channel"_2016.root --skipBOnlyFit --skipBOnlyFit -M FitDiagnostics -n .datacard_"$channel"_2016_Asimov $myAsimovFit   $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange
    # python diffNuisances.py fitDiagnostics.datacard_"$channel"_2016_Asimov.root
    # combine datacard_"$channel"_2016.root --skipBOnlyFit --skipBOnlyFit -M FitDiagnostics -n .datacard_"$channel"_2016_Data   $myFakeDataFit $mySeed $mySignalParamters $verbose $mySignalModifierRange   $myParameterRange $myExpectSignal
    # python diffNuisances.py fitDiagnostics.datacard_"$channel"_2016_Data.root --all 
    
    combine --cminPreScan --skipBOnlyFit  -M FitDiagnostics -n .Asimov_"$channel"_2016 datacard_"$channel"_2016.root $mySeed   --saveOverallShapes     --plots --saveNLL   $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations  $mySignalModifierRange  $myParameterRange $myAsimovFit   $myExpectSignal $verbose 
    combine --cminPreScan --skipBOnlyFit  -M FitDiagnostics -n "$channel"_2016         datacard_"$channel"_2016.root $mySeed   --saveOverallShapes     --plots --saveNLL   $mySignalParamters --saveShapes --saveWithUncertainties --saveNormalizations  $mySignalModifierRange  $myParameterRange $myFakeDataFit $myExpectSignal $verbose 
    # # combine --cminPreScan --skipBOnlyFit  -M FitDiagnostics -n .TOY_"$channel"_2016    datacard_"$channel"_2016.root $mySeed                           --plots --saveNLL   $mySignalParamters              --saveWithUncertainties --saveNormalizations  $mySignalModifierRange  $myParameterRange $myToyFit                      -v3   

    combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myAsimovFit $myExpectSignal --algo grid $myPoints -n .Main $mySignalModifierRange  $myParameterRange
    combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myAsimovFit $myExpectSignal --saveWorkspace -n .snapshot $mySignalModifierRange  $myParameterRange
    combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myAsimovFit $myExpectSignal -n .freezeAll  --algo grid $myPoints --freezeNuisanceGroups mySyst --snapshotName MultiDimFit $mySignalModifierRange    $myParameterRange
    python plot1DScan.py  --translate rename.json  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2016_Asimov 

    combine -M MultiDimFit datacard_"$channel"_2016.root                       $mySeed $myFakeDataFit --algo grid $myPoints -n .Main       $mySignalModifierRange  $myParameterRange $myExpectSignal
    combine -M MultiDimFit datacard_"$channel"_2016.root                       $mySeed $myFakeDataFit --saveWorkspace       -n .snapshot   $mySignalModifierRange  $myParameterRange $myExpectSignal
    combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root $mySeed $myFakeDataFit --algo grid $myPoints -n .freezeAll  $mySignalModifierRange  $myParameterRange $myExpectSignal --freezeNuisanceGroups mySyst --snapshotName MultiDimFit 
    python plot1DScan.py  --translate rename.json  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$channel"_2016_Data 
    
    combineTool.py  --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                        $myAsimovFit    --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
    combineTool.py  --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                              $myAsimovFit    --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py  --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_toy_"$channel"_2016.json   $myAsimovFit    --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2016.json -o impacts_toy_"$channel"_2016 --label-size 0.035

    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                        $myFakeDataFit  --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                              $myFakeDataFit  --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_data_"$channel"_2016.json  $myFakeDataFit  --robustFit=1 $myExpectSignal  $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_data_"$channel"_2016.json -o impacts_data_"$channel"_2016 --label-size 0.035

    combineTool.py $myFreeze --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                                   $myAsimovFit --redefineSignalPOIs PhoEff --setParameters PhoEff=0  --robustFit=1   $mySignalModifierRange  $myParameterRange 
    combineTool.py $myFreeze --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                         $myAsimovFit --redefineSignalPOIs PhoEff --setParameters PhoEff=0  --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py $myFreeze --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_toy_"$channel"_2016_PhoEff.json       $myAsimovFit --redefineSignalPOIs PhoEff --setParameters PhoEff=0  --robustFit=1   $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2016_PhoEff.json -o impacts_toy_"$channel"_2016_PhoEff  --label-size 0.035 --POI PhoEff

    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                                   $myFakeDataFit --redefineSignalPOIs   PhoEff --robustFit=1 --setParameters PhoEff=0  $mySignalModifierRange  $myParameterRange 
    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                         $myFakeDataFit --redefineSignalPOIs   PhoEff --robustFit=1 --setParameters PhoEff=0  $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_data_"$channel"_2016_PhoEff.json      $myFakeDataFit --redefineSignalPOIs   PhoEff --robustFit=1 --setParameters PhoEff=0  $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_data_"$channel"_2016_PhoEff.json -o impacts_data_"$channel"_2016_PhoEff --label-size 0.035 --POI PhoEff

    combineTool.py $myFreeze --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                                   $myAsimovFit --redefineSignalPOIs JER0 --setParameters JER0=0  --robustFit=1   $mySignalModifierRange  $myParameterRange 
    combineTool.py $myFreeze --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                         $myAsimovFit --redefineSignalPOIs JER0 --setParameters JER0=0  --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py $myFreeze --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_toy_"$channel"_2016_JER0.json         $myAsimovFit --redefineSignalPOIs JER0 --setParameters JER0=0  --robustFit=1   $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2016_JER0.json -o impacts_toy_"$channel"_2016_JER0  --label-size 0.035 --POI JER0

    combineTool.py $myFreeze --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doInitialFit                                   $myAsimovFit --redefineSignalPOIs JECTotal0 --setParameters JECTotal0=0  --robustFit=1   $mySignalModifierRange  $myParameterRange 
    combineTool.py $myFreeze --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  --doFits                                         $myAsimovFit --redefineSignalPOIs JECTotal0 --setParameters JECTotal0=0  --robustFit=1   $mySignalModifierRange  $myParameterRange  --parallel 24
    combineTool.py $myFreeze --cminPreScan -M Impacts -d datacard_"$channel"_2016.root -m 125  -o impacts_toy_"$channel"_2016_JECTotal0.json    $myAsimovFit --redefineSignalPOIs JECTotal0 --setParameters JECTotal0=0  --robustFit=1   $mySignalModifierRange  $myParameterRange 
    plotImpacts.py  -t rename.json  -i impacts_toy_"$channel"_2016_JECTotal0.json -o impacts_toy_"$channel"_2016_JECTotal0  --label-size 0.035 --POI JECTotal0


    # declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "Pdf" "isr" "fsr" "PU" "prefireEcal" "JECTotal" "JER" "Q2" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "Other_norm" "nonPromptSF")
    # # declare -a PARAMETERS=("TTbarSF")
    # for parameter in ${PARAMETERS[@]}; do
    #   combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myAsimovFit   --algo grid  $myPoints -n .Asimov_Main_"$channel"_"$parameter" $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange
    #   python plot1DScan.py  --translate rename.json higgsCombine.Asimov_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_"$channel"_"$parameter"

    #   combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed $myFakeDataFit --algo grid  $myPoints -n .Data_Main_"$channel"_"$parameter"   $mySignalModifierRange  -P $parameter --floatOtherPOIs 1  $myParameterRange $myExpectSignal
    #   python plot1DScan.py  --translate rename.json higgsCombine.Data_Main_"$channel"_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_"$channel"_"$parameter"
    # done
done

echo "Done fitting only!!!"

# python makettGammaSS.py; python makettGammaSS_Toy.py; python makettGammaSS_Asimov.py; python makeCorrelationMatrix.py   

python makettGammaSS.py; 
python makettGammaSS_Asimov.py; 
python makeCorrelationMatrix.py   
python makettGammaSS_Toy.py; 


# subl -n makettGammaSS.py makettGammaSS_Toy.py makettGammaSS_Asimov.py makeCorrelationMatrix.py   

# python makeTotalCovarianceMatrix.py    
   
# python getTrackParameterPlots.py
# python getNPToyDistribution.py

echo "Done fitting and Extraction!!!"


# Toy toysFrequentist has the following benifits:
# Your analysis may have parameters which are determined from the observed data (eg, you are fitting a mass spectrum with some function for the background whose parameters are determined from the S+B fit). In this case, you should add --toysFrequentist to your combine line which will first fit the data to produce reasonable estimates for these free parameters. 
# One of your nuisances seems to not close and it is a gmN type nuisance. This is related to the initial guess for the poisson component in these nuisances which is n+1 as opposed to n. This can also be avoided using toysFrequentist 

exit 1

# cp freeze_ele_2016_Asimov.pdf    ~/cernbox/June17_freeze_MCstat
# cp freeze_ele_2016_Data.pdf    ~/cernbox/June17_freeze_MCstat
# cp impacts_toy_ele_2016.pdf    ~/cernbox/June17_freeze_MCstat
# cp impacts_data_ele_2016.pdf    ~/cernbox/June17_freeze_MCstat
# cp freeze_mu_2016_Asimov.pdf    ~/cernbox/June17_freeze_MCstat
# cp freeze_mu_2016_Data.pdf    ~/cernbox/June17_freeze_MCstat
# cp impacts_toy_mu_2016.pdf    ~/cernbox/June17_freeze_MCstat
# cp impacts_data_mu_2016.pdf    ~/cernbox/June17_freeze_MCstat

# cp correlation_ttgamma_Asimov_mu_2016.pdf    ~/cernbox/June17_freeze_MCstat
# cp correlation_ttgamma_Asimov_ele_2016.pdf    ~/cernbox/June17_freeze_MCstat
# cp correlation_ttgamma_data_mu_2016.pdf    ~/cernbox/June17_freeze_MCstat
# cp correlation_ttgamma_data_ele_2016.pdf    ~/cernbox/June17_freeze_MCstat
# cp correlation_ttgamma_toy_ele_2016.pdf    ~/cernbox/June17_freeze_MCstat
# cp correlation_ttgamma_toy_mu_2016.pdf    ~/cernbox/June17_freeze_MCstat



# cp freeze_ele_2016_Asimov.pdf    ~/cernbox/June17_freeze_Yield
# cp freeze_ele_2016_Data.pdf    ~/cernbox/June17_freeze_Yield
# cp impacts_toy_ele_2016.pdf    ~/cernbox/June17_freeze_Yield
# cp impacts_data_ele_2016.pdf    ~/cernbox/June17_freeze_Yield
# cp freeze_mu_2016_Asimov.pdf    ~/cernbox/June17_freeze_Yield
# cp freeze_mu_2016_Data.pdf    ~/cernbox/June17_freeze_Yield
# cp impacts_toy_mu_2016.pdf    ~/cernbox/June17_freeze_Yield
# cp impacts_data_mu_2016.pdf    ~/cernbox/June17_freeze_Yield

# cp correlation_ttgamma_Asimov_mu_2016.pdf    ~/cernbox/June17_freeze_Yield
# cp correlation_ttgamma_Asimov_ele_2016.pdf    ~/cernbox/June17_freeze_Yield
# cp correlation_ttgamma_data_mu_2016.pdf    ~/cernbox/June17_freeze_Yield
# cp correlation_ttgamma_data_ele_2016.pdf    ~/cernbox/June17_freeze_Yield
# cp correlation_ttgamma_toy_ele_2016.pdf    ~/cernbox/June17_freeze_Yield
# cp correlation_ttgamma_toy_mu_2016.pdf    ~/cernbox/June17_freeze_Yield



# # this is workign one 
# cp -R ttgamma_tightplots_mu_2016     ttgamma_tightplots_mu_2016_Jun17_backup
# cp -R ttgamma_tightplots_ele_2016   ttgamma_tightplots_ele_2016_Jun17_backup
# cp -R ttgamma_tightplots_ele_2017   ttgamma_tightplots_ele_2017_Jun17_backup
# cp -R ttgamma_tightplots_ele_2018   ttgamma_tightplots_ele_2018_Jun17_backup
# cp -R ttgamma_tightplots_mu_2017     ttgamma_tightplots_mu_2017_Jun17_backup
# cp -R ttgamma_tightplots_mu_2018     ttgamma_tightplots_mu_2018_Jun17_backup

# back this up for yeild only for finding syst relationship
# Here ====>  

cp -R ttgamma_tightplots_ele_2016   ttgamma_tightplots_ele_2016_Jun19_1Bins
cp -R ttgamma_tightplots_ele_2017   ttgamma_tightplots_ele_2017_Jun19_1Bins
cp -R ttgamma_tightplots_ele_2018   ttgamma_tightplots_ele_2018_Jun19_1Bins
cp -R ttgamma_tightplots_mu_2016     ttgamma_tightplots_mu_2016_Jun19_1Bins
cp -R ttgamma_tightplots_mu_2017     ttgamma_tightplots_mu_2017_Jun19_1Bins
cp -R ttgamma_tightplots_mu_2018     ttgamma_tightplots_mu_2018_Jun19_1Bins

cp -R ttgamma_tightplots_mu_2016     ttgamma_tightplots_mu_2016_Jun19_3Bins
cp -R ttgamma_tightplots_ele_2016   ttgamma_tightplots_ele_2016_Jun19_3Bins
cp -R ttgamma_tightplots_ele_2017   ttgamma_tightplots_ele_2017_Jun19_3Bins
cp -R ttgamma_tightplots_ele_2018   ttgamma_tightplots_ele_2018_Jun19_3Bins
cp -R ttgamma_tightplots_mu_2017     ttgamma_tightplots_mu_2017_Jun19_3Bins
cp -R ttgamma_tightplots_mu_2018     ttgamma_tightplots_mu_2018_Jun19_3Bins

cp -R ttgamma_tightplots_ele_2016   ttgamma_tightplots_ele_2016_Jun19_10Bins
cp -R ttgamma_tightplots_ele_2017   ttgamma_tightplots_ele_2017_Jun19_10Bins
cp -R ttgamma_tightplots_ele_2018   ttgamma_tightplots_ele_2018_Jun19_10Bins
cp -R ttgamma_tightplots_mu_2016     ttgamma_tightplots_mu_2016_Jun19_10Bins
cp -R ttgamma_tightplots_mu_2017     ttgamma_tightplots_mu_2017_Jun19_10Bins
cp -R ttgamma_tightplots_mu_2018     ttgamma_tightplots_mu_2018_Jun19_10Bins

# Test
# firefox freeze_ele_2016_Asimov.pdf freeze_ele_2016_Data.pdf   impacts_toy_ele_2016.pdf   impacts_data_ele_2016.pdf  freeze_mu_2016_Asimov.pdf  freeze_mu_2016_Data.pdf    impacts_toy_mu_2016.pdf    impacts_data_mu_2016.pdf   

rm -rf ttgamma_tightplots_ele_2016/
rm -rf ttgamma_tightplots_ele_2017/
rm -rf ttgamma_tightplots_ele_2018/
rm -rf ttgamma_tightplots_mu_2016/
rm -rf ttgamma_tightplots_mu_2017/
rm -rf ttgamma_tightplots_mu_2018/



# cp freeze_ele_2016_Asimov.pdf    ~/cernbox/June17_3Bins
# cp freeze_ele_2016_Data.pdf      ~/cernbox/June17_3Bins
# cp impacts_toy_ele_2016.pdf      ~/cernbox/June17_3Bins
# cp impacts_data_ele_2016.pdf     ~/cernbox/June17_3Bins
# cp freeze_mu_2016_Asimov.pdf     ~/cernbox/June17_3Bins
# cp freeze_mu_2016_Data.pdf       ~/cernbox/June17_3Bins
# cp impacts_toy_mu_2016.pdf       ~/cernbox/June17_3Bins
# cp impacts_data_mu_2016.pdf      ~/cernbox/June17_3Bins


cp -R   ttgamma_tightplots_ele_2016_Jun19_3Bins ttgamma_tightplots_ele_2016 
cp -R   ttgamma_tightplots_ele_2017_Jun19_3Bins ttgamma_tightplots_ele_2017 
cp -R   ttgamma_tightplots_ele_2018_Jun19_3Bins ttgamma_tightplots_ele_2018 
cp -R    ttgamma_tightplots_mu_2016_Jun19_3Bins ttgamma_tightplots_mu_2016  
cp -R    ttgamma_tightplots_mu_2017_Jun19_3Bins ttgamma_tightplots_mu_2017  
cp -R    ttgamma_tightplots_mu_2018_Jun19_3Bins ttgamma_tightplots_mu_2018  