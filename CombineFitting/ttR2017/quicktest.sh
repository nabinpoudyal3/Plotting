#!/bin/bash

#combine -M FitDiagnostics -n   el_2017   datacard_ele_2017.txt  -s 314159 --redefineSignalPOIs r,nonPromptSF --saveNormalizations --saveWithUncertainties --plots -v2


#combine -M FitDiagnostics -n   el_2017   datacard_ele_2017.txt  -s 314159 --redefineSignalPOIs r,nonPromptSF

#python make2017ttGammaSS.py
#python makeCovarianceMatrix.py

text2workspace.py  datacard_ele_2017.txt -v2
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  -t -1 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF --doInitialFit -v2
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  -t -1 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF --doFits -v2
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125  -t -1 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF -o impacts_data_ele_2017.json -v2
plotImpacts.py -i impacts_data_ele_2017.json -o impacts_data_ele_2017 

echo "exiting"
exit 1

#for i in {1..20}
#do
#   echo "***************************************************************************************************"
#done
#combine -M FitDiagnostics -n   el_2017_M3          datacard_ele_2017_M3.txt         -s 314159 --redefineSignalPOIs r,nonPromptSF --saveNormalizations --saveWithUncertainties --plots -v2
#for i in {1..20}
#do
#   echo "***************************************************************************************************"
#done
#combine -M FitDiagnostics -n   el_2017_ChIso       datacard_ele_2017_ChIso.txt      -s 314159 --redefineSignalPOIs r,nonPromptSF --saveNormalizations --saveWithUncertainties --plots -v2
#for i in {1..20}
#do
#   echo "***************************************************************************************************"
#done
#combine -M FitDiagnostics -n   el_2017_M30btag     datacard_ele_2017_M30btag.txt    -s 314159 --redefineSignalPOIs r,nonPromptSF --saveNormalizations --saveWithUncertainties --plots -v2
#for i in {1..20}
#do
#   echo "***************************************************************************************************"
#done
#combine -M FitDiagnostics -n   el_2017_M30photon   datacard_ele_2017_M30photon.txt  -s 314159 --redefineSignalPOIs r,nonPromptSF --saveNormalizations --saveWithUncertainties --plots -v2
#for i in {1..20}
#do
#   echo "***************************************************************************************************"
#done
#
#exit 1
#
#
#text2workspace.py  datacard_ele_2017_M30photon.txt 
#combineTool.py -M Impacts -d datacard_ele_2017_M30photon.root -m 125  --doInitialFit  --robustFit 1
#combineTool.py -M Impacts -d datacard_ele_2017_M30photon.root -m 125  --doFits --robustFit 1
#combineTool.py -M Impacts -d datacard_ele_2017_M30photon.root -m 125  -o impacts_data_ele_2017_M30photon.json
#plotImpacts.py -i impacts_data_ele_2017_M30photon.json -o impacts_data_ele_M30photon_2017 
