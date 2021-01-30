#!/bin/bash

rm *.root
rm *.png
rm *.pdf
rm *.json

#cd /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting
#./makeTemplateForTTGamma.sh
#cd /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma

./allCombine.sh

echo "Fitting Electron Channel!!!!!!!!!"
./oneEle.sh
echo "Fitting Muon Channel!!!!!!!!!"
./oneMu.sh
echo "Fitting Ele+Mu Channel!!!!!!!!!"
./oneBoth.sh

wait
# running toy for Ele, Mu and Both
#combine -M FitDiagnostics -n .TOY_ele_2017 datacard_ele_2017.root --seed=314159 \
#--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
#--expectSignal=1 -t 500 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF --cminDefaultMinimizerStrategy 0

#combine -M FitDiagnostics -n .TOY_mu_2017 datacard_mu_2017.root --seed=314159 \
#--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-10 --rMax=10 --setParameterRanges nonPromptSF=-10,10   \
#--expectSignal=1 -t 500 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF --cminDefaultMinimizerStrategy 0

#combine -M FitDiagnostics -n .TOY_both_2017 datacard_both_2017.root --seed=314159 \
#--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
#--expectSignal=1 -t 500 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF --cminDefaultMinimizerStrategy 0
############

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

exit 1 

cd /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting
./makePrePostFitTTGamma.sh
cd /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma


#sampleList = ['TTGamma', 'TTbar', 'SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]






exit 1
























