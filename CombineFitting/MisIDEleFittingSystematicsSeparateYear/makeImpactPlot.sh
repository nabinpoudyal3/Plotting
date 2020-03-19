

text2workspace.py  datacard_CR123_2016.txt 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --redefineSignalPOIs WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1.23 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --redefineSignalPOIs WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1.23 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --redefineSignalPOIs WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1.23 -o impacts_toy_2016.json
plotImpacts.py -i impacts_toy_2016.json -o impacts_toy_2016


#text2workspace.py  datacard_CR123_2016.txt 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs WGammaBkgPhotonSF -o impacts_data_2016.json
#plotImpacts.py -i impacts_data_2016.json -o impacts_data_2016
