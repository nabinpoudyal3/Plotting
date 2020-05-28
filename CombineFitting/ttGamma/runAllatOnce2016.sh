#!/bin/bash

text2workspace.py  datacard_ele_2016.txt
text2workspace.py  datacard_mu_2016.txt 
text2workspace.py  datacard_both_2016.txt 

combine -M FitDiagnostics -n   el_2016   datacard_ele_2016.root  -s 314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF  --saveNormalizations  -v2  --robustFit=1 --plots
combine -M FitDiagnostics -n   mu_2016   datacard_mu_2016.root   -s 314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF  --saveNormalizations  -v2  --robustFit=1 --plots
combine -M FitDiagnostics -n   both_2016 datacard_both_2016.root -s 314159 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF  --saveNormalizations  -v2  --robustFit=1 --plots


wait
python make2016ttGammaSS.py
python makeCovarianceMatrix.py
wait

#tnink if you need robustFit or not.

combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit --robustFit 1
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doFits --robustFit 1
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_data_ele_2016.json 
plotImpacts.py -i impacts_data_ele_2016.json -o impacts_data_ele_2016 

combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  --doInitialFit  --robustFit 1
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  --doFits --robustFit 1
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  -o impacts_data_mu_2016.json
plotImpacts.py -i impacts_data_mu_2016.json -o impacts_data_mu_2016

combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  --doInitialFit  --robustFit 1
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  --doFits --robustFit 1
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  -o impacts_data_both_2016.json
plotImpacts.py -i impacts_data_both_2016.json -o impacts_data_both_2016

########################################################################################################################################################

combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1  --doInitialFit  
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1   --doFits 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_ele_2016.json
plotImpacts.py -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016

combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1  --doInitialFit  
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1   --doFits 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_mu_2016.json
plotImpacts.py -i impacts_toy_mu_2016.json -o impacts_toy_mu_2016

combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1  --doInitialFit  
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1   --doFits 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_both_2016.json
plotImpacts.py -i impacts_toy_both_2016.json -o impacts_toy_both_2016



