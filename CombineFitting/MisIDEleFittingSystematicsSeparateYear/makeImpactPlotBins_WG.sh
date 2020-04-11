


text2workspace.py  datacard_CR123_2016.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1 -o impacts_toy_2016_WG.json
plotImpacts.py -t rename.json -i impacts_toy_2016_WG.json -o impacts_toy_2016_WG



########
text2workspace.py  datacard_CR123_2017.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1 -o impacts_toy_2017_WG.json
plotImpacts.py -t rename.json -i impacts_toy_2017_WG.json -o impacts_toy_2017_WG


##############
text2workspace.py  datacard_CR123_2018.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters WGammaBkgPhotonSF=1 -o impacts_toy_2018_WG.json
plotImpacts.py -t rename.json -i impacts_toy_2018_WG.json -o impacts_toy_2018_WG


#############
#########


#text2workspace.py  datacard_CR123_2016.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -o impacts_data_2016_WG.json
#plotImpacts.py -t rename.json -i impacts_data_2016_WG.json -o impacts_data_2016_WG


#text2workspace.py  datacard_CR123_2016.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -o impacts_data_2016_WG.json
#plotImpacts.py -t rename.json -i impacts_data_2016_WG.json -o impacts_data_2016_WG


#text2workspace.py  datacard_CR123_2016.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -o impacts_data_2016_WG.json
#plotImpacts.py -t rename.json -i impacts_data_2016_WG.json -o impacts_data_2016_WG

########
#text2workspace.py  datacard_CR123_2017.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -o impacts_data_2017_WG.json
#plotImpacts.py -t rename.json -i impacts_data_2017_WG.json -o impacts_data_2017_WG


#text2workspace.py  datacard_CR123_2017.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -o impacts_data_2017_WG.json
#plotImpacts.py -t rename.json -i impacts_data_2017_WG.json -o impacts_data_2017_WG


#text2workspace.py  datacard_CR123_2017.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2017.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -o impacts_data_2017_WG.json
#plotImpacts.py -t rename.json -i impacts_data_2017_WG.json -o impacts_data_2017_WG


##############
#text2workspace.py  datacard_CR123_2018.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -o impacts_data_2018_WG.json
#plotImpacts.py -t rename.json -i impacts_data_2018_WG.json -o impacts_data_2018_WG


#text2workspace.py  datacard_CR123_2018.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -o impacts_data_2018_WG.json
#plotImpacts.py -t rename.json -i impacts_data_2018_WG.json -o impacts_data_2018_WG


#text2workspace.py  datacard_CR123_2018.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2018.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -o impacts_data_2018_WG.json
#plotImpacts.py -t rename.json -i impacts_data_2018_WG.json -o impacts_data_2018_WG
