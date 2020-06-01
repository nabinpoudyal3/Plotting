text2workspace.py  datacard_CR123_2016.txt 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1  --expectSignal 1  --doInitialFit --robustFit 1  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1  --expectSignal 1 --robustFit 1 --doFits  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1  --expectSignal 1 -o impacts_toy_2016.json  --rMin=0 --rMax=5
plotImpacts.py -i impacts_toy_2016.json -o impacts_toy_2016


text2workspace.py  datacard_CR123_2017.txt 
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 -t -1  --expectSignal 1 --doInitialFit --robustFit 1  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 -t -1  --expectSignal 1 --robustFit 1 --doFits  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 -t -1  --expectSignal 1 -o impacts_toy_2017.json  --rMin=0 --rMax=5
plotImpacts.py -i impacts_toy_2017.json -o impacts_toy_2017


text2workspace.py  datacard_CR123_2018.txt 
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 -t -1  --expectSignal 1 --doInitialFit --robustFit 1  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 -t -1  --expectSignal 1 --robustFit 1 --doFits  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 -t -1  --expectSignal 1 -o impacts_toy_2018.json  --rMin=0 --rMax=5
plotImpacts.py -i impacts_toy_2018.json -o impacts_toy_2018



# for data


text2workspace.py  datacard_CR123_2016.txt 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125  --doInitialFit --robustFit 1  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125  --robustFit 1 --doFits  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125  -o impacts_data_2016.json  --rMin=0 --rMax=5
plotImpacts.py -i impacts_data_2016.json -o impacts_data_2016



text2workspace.py  datacard_CR123_2017.txt 
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125  --doInitialFit --robustFit 1  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125  --robustFit 1 --doFits  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125  -o impacts_data_2017.json  --rMin=0 --rMax=5
plotImpacts.py -i impacts_data_2017.json -o impacts_data_2017


text2workspace.py  datacard_CR123_2018.txt 
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125   --doInitialFit --robustFit 1   --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125   --robustFit 1 --doFits  --rMin=0 --rMax=5
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125   -o impacts_data_2018.json  --rMin=0 --rMax=5
plotImpacts.py -i impacts_data_2018.json -o impacts_data_2018
