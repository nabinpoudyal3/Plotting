#!/bin/bash

text2workspace.py  datacard_ele_2016.txt
text2workspace.py  datacard_mu_2016.txt 
text2workspace.py  datacard_both_2016.txt 

combine -M FitDiagnostics -n   el_2016   datacard_ele_2016.root  -s 314159 --plots --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF --saveShapes --saveWithUncertainties --saveNormalizations  -v2  --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combine -M FitDiagnostics -n   mu_2016   datacard_mu_2016.root   -s 314159 --plots --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF --saveShapes --saveWithUncertainties --saveNormalizations  -v2  --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combine -M FitDiagnostics -n   both_2016 datacard_both_2016.root -s 314159 --plots --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF --saveShapes --saveWithUncertainties --saveNormalizations  -v2  --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2


wait
python make2016ttGammaSS.py
python makeCovarianceMatrix.py
wait

#tnink if you need robustFit or not.

combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doFits --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_data_ele_2016.json --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
plotImpacts.py -i impacts_data_ele_2016.json -o impacts_data_ele_2016 

combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  --doInitialFit  --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  --doFits --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  -o impacts_data_mu_2016.json --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
plotImpacts.py -i impacts_data_mu_2016.json -o impacts_data_mu_2016

combineTool.py -M Impacts -d datacard_both_2016.root -m 125  --doInitialFit  --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_both_2016.root -m 125  --doFits --robustFit 1 --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_both_2016.root -m 125  -o impacts_data_both_2016.json --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
plotImpacts.py -i impacts_data_both_2016.json -o impacts_data_both_2016

########################################################################################################################################################

combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1  --doInitialFit  --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1   --doFits --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_ele_2016.json --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
plotImpacts.py -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016

combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1  --doInitialFit  --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1   --doFits --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_mu_2016.json --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
plotImpacts.py -i impacts_toy_mu_2016.json -o impacts_toy_mu_2016

combineTool.py -M Impacts -d datacard_both_2016.root -m 125 -t -1 --expectSignal 1  --doInitialFit  --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_both_2016.root -m 125 -t -1 --expectSignal 1   --doFits --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
combineTool.py -M Impacts -d datacard_both_2016.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_both_2016.json --cminDefaultMinimizerStrategy 0 --rMin=0 --rMax=2
plotImpacts.py -i impacts_toy_both_2016.json -o impacts_toy_both_2016



