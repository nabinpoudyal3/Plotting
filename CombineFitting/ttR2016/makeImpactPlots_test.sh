
text2workspace.py  datacard_ele_2016.txt 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_ele_2016.json
plotImpacts.py -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016
##

text2workspace.py  datacard_mu_2016.txt 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_mu_2016.json
plotImpacts.py -i impacts_toy_mu_2016.json -o impacts_toy_mu_2016
##

