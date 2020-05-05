#!/bin/bash

text2workspace.py  datacard_CR123_2016.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --expectSignal 2 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --expectSignal 2 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --expectSignal 2 -o impacts_toy_2016.json
plotImpacts.py -t rename.json -i impacts_toy_2016.json -o impacts_toy_2016

########
text2workspace.py  datacard_CR123_2017.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 -t -1 --expectSignal 2 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 -t -1 --expectSignal 2 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 -t -1 --expectSignal 2 -o impacts_toy_2017.json
plotImpacts.py -t rename.json -i impacts_toy_2017.json -o impacts_toy_2017

##############
text2workspace.py  datacard_CR123_2018.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 -t -1 --expectSignal 2 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 -t -1 --expectSignal 2 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 -t -1 --expectSignal 2 -o impacts_toy_2018.json
plotImpacts.py -t rename.json -i impacts_toy_2018.json -o impacts_toy_2018


#############
#########


text2workspace.py  datacard_CR123_2016.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125  -o impacts_data_2016.json
plotImpacts.py -t rename.json -i impacts_data_2016.json -o impacts_data_2016


text2workspace.py  datacard_CR123_2017.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125  -o impacts_data_2017.json
plotImpacts.py -t rename.json -i impacts_data_2017.json -o impacts_data_2017


text2workspace.py  datacard_CR123_2018.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125  -o impacts_data_2018.json
plotImpacts.py -t rename.json -i impacts_data_2018.json -o impacts_data_2018



