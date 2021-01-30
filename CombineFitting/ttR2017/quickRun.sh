#!/bin/bash

text2workspace.py  datacard_ele_2017.txt 
ValidateDatacards.py datacard_ele_2017.txt --printLevel 3 --checkUncertOver 0.1 
combine -M ChannelCompatibilityCheck datacard_ele_2017.root -v1 --redefineSignalPOIs=r,nonPromptSF
#--autoMaxPOIs "*" --runMinos=1

combine datacard_ele_2017.root -M FitDiagnostics -n .datacard_ele_2017 --toys=-1 --expectSignal=1  --seed=314159 --redefineSignalPOIs=r,nonPromptSF -v1 --rMin=-5 --rMax=5  --setParameterRanges nonPromptSF=-10,10
#freezeNuisanceGroups mySyst
python diffNuisances.py fitDiagnostics.datacard_ele_2017.root --all -g plots_ele_2017.root


combine -M MultiDimFit datacard_ele_2017.root -s 314159  --algo grid --points=300 -n .Main --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10
#python plot1DScan.py higgsCombine.Main.MultiDimFit.mH120.314159.root --POI ZGSF -o single_scan
combine -M MultiDimFit datacard_ele_2017.root -s 314159  --saveWorkspace -n .snapshot --rMin=-5 --rMax=5  --setParameterRanges nonPromptSF=-10,10
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll  --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_ele_2017 

#combine -H FitDiagnostics -n .hint_ele_2017 datacard_ele_2017.root -s 314159 --redefineSignalPOIs r,nonPromptSF -v1  

combine -M FitDiagnostics -n .Asimov_ele_2017 datacard_ele_2017.root --seed=314159 --redefineSignalPOIs=r,nonPromptSF \
--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
--expectSignal=1 -t -1 -v0 --skipBOnlyFit


combine -M FitDiagnostics -n el_2017 datacard_ele_2017.root --plots --saveNLL --robustFit=1 -s 314159 --redefineSignalPOIs r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations -v1 --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 --skipBOnlyFit
#--freezeNuisanceGroups mySyst
#python mlfitNormsToText.py fitDiagnosticsel_2017.root --uncertainties


# combine -M FitDiagnostics -n .TOY_ele_2017 datacard_ele_2017.root --seed=314159 \
# --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
# --expectSignal=1 -t 500 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF &

# something wrong with the commands below. I think it should work.
#combine -M GenerateOnly -n .Gen_ele_2017 datacard_ele_2017.txt --toys=1000 --toysFrequentist \
#--expectSignal=1 --seed=314159 --redefineSignalPOIs r,nonPromptSF \
#--rMin=-5 --rMax=5 -v0 --setParameterRanges nonPromptSF=-10,10 --saveToys 

#combine -M FitDiagnostics -n .TOY_ele_2017 datacard_ele_2017.root --seed=314159 --redefineSignalPOIs r,nonPromptSF \
#--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 -v1 --setParameterRanges nonPromptSF=-10,10 \
#--toysFile higgsCombine.Gen_ele_2017.GenerateOnly.mH120.314159.root

# no need to redefine POIs r and nonPromptSF but use the range for nonPromptSF 
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1 --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1 --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10  --parallel 24
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  -o impacts_toy_ele_2017.json   -t -1 --expectSignal 1  --robustFit=1 --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 
plotImpacts.py -i impacts_toy_ele_2017.json -o impacts_toy_ele_2017 

combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doInitialFit                 --robustFit=1   --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  --doFits                       --robustFit=1   --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10  --parallel 24
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  -o impacts_data_ele_2017.json  --robustFit=1   --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 
plotImpacts.py -i impacts_data_ele_2017.json -o impacts_data_ele_2017 

#The following test to find out the range of 
#combine -M Asymptotic htt_mt.root -m 125
exit 1

declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "nonPromptSF")
for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_ele_2017.root -s 314159 -t -1 --expectSignal=1 --algo grid --points=100 -n .Asimov_Main_ele_"$parameter" --rMin=-5 --rMax=5  -P $parameter --floatOtherPOIs 1 &
done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Asimov_Main_ele_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_ele_"$parameter"&
done
echo "Done"

wait

for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_ele_2017.root -s 314159 --algo grid --points=100 -n .Data_Main_ele_"$parameter" --rMin=-5 --rMax=5 -P $parameter --floatOtherPOIs 1 &

done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Data_Main_ele_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_ele_"$parameter"&
done
echo "Done"

exit 1

echo "python make2017ttGammaSS.py"
python make2017ttGammaSS.py
echo "python make2017ttGammaSS_Toy.py"
python make2017ttGammaSS_Toy.py
echo "python make2017ttGammaSS_Toy.py"
python make2017ttGammaSS_Asimov.py
echo "python makeCovarianceMatrix.py"
python makeCovarianceMatrix.py
echo "python getTrackParameterPlots.py"
python getTrackParameterPlots.py
echo "python getNPToyDistribution.py"
python getNPToyDistribution.py

cd ../../
./makePrePostFitTTGamma.sh
cd CombineFitting/ttGamma
