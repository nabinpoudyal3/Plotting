


text2workspace.py  datacard_CR123_2016_nbins3.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2016_nbins3.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2016_nbins3.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2016_nbins3.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 -o impacts_toy_2016_nbins3_ZG.json
plotImpacts.py -t rename.json -i impacts_toy_2016_nbins3_ZG.json -o impacts_toy_2016_nbins3_ZG


text2workspace.py  datacard_CR123_2016_nbins6.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2016_nbins6.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2016_nbins6.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2016_nbins6.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 -o impacts_toy_2016_nbins6_ZG.json
plotImpacts.py -t rename.json -i impacts_toy_2016_nbins6_ZG.json -o impacts_toy_2016_nbins6_ZG


text2workspace.py  datacard_CR123_2016_nbins9.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2016_nbins9.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2016_nbins9.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2016_nbins9.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 -o impacts_toy_2016_nbins9_ZG.json
plotImpacts.py -t rename.json -i impacts_toy_2016_nbins9_ZG.json -o impacts_toy_2016_nbins9_ZG

########
text2workspace.py  datacard_CR123_2017_nbins3.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2017_nbins3.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2017_nbins3.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2017_nbins3.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 -o impacts_toy_2017_nbins3_ZG.json
plotImpacts.py -t rename.json -i impacts_toy_2017_nbins3_ZG.json -o impacts_toy_2017_nbins3_ZG


text2workspace.py  datacard_CR123_2017_nbins6.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2017_nbins6.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2017_nbins6.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2017_nbins6.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 -o impacts_toy_2017_nbins6_ZG.json
plotImpacts.py -t rename.json -i impacts_toy_2017_nbins6_ZG.json -o impacts_toy_2017_nbins6_ZG


text2workspace.py  datacard_CR123_2017_nbins9.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2017_nbins9.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2017_nbins9.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2017_nbins9.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 -o impacts_toy_2017_nbins9_ZG.json
plotImpacts.py -t rename.json -i impacts_toy_2017_nbins9_ZG.json -o impacts_toy_2017_nbins9_ZG


##############
text2workspace.py  datacard_CR123_2018_nbins3.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2018_nbins3.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2018_nbins3.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2018_nbins3.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 -o impacts_toy_2018_nbins3_ZG.json
plotImpacts.py -t rename.json -i impacts_toy_2018_nbins3_ZG.json -o impacts_toy_2018_nbins3_ZG


text2workspace.py  datacard_CR123_2018_nbins6.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2018_nbins6.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2018_nbins6.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2018_nbins6.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 -o impacts_toy_2018_nbins6_ZG.json
plotImpacts.py -t rename.json -i impacts_toy_2018_nbins6_ZG.json -o impacts_toy_2018_nbins6_ZG


text2workspace.py  datacard_CR123_2018_nbins9.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2018_nbins9.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2018_nbins9.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2018_nbins9.root -m 125 -t -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1 -o impacts_toy_2018_nbins9_ZG.json
plotImpacts.py -t rename.json -i impacts_toy_2018_nbins9_ZG.json -o impacts_toy_2018_nbins9_ZG
############
#############
#########


#text2workspace.py  datacard_CR123_2016_nbins3.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2016_nbins3.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2016_nbins3.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2016_nbins3.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   -o impacts_data_2016_nbins3_ZG.json
#plotImpacts.py -t rename.json -i impacts_data_2016_nbins3_ZG.json -o impacts_data_2016_nbins3_ZG


#text2workspace.py  datacard_CR123_2016_nbins6.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2016_nbins6.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2016_nbins6.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2016_nbins6.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   -o impacts_data_2016_nbins6_ZG.json
#plotImpacts.py -t rename.json -i impacts_data_2016_nbins6_ZG.json -o impacts_data_2016_nbins6_ZG


#text2workspace.py  datacard_CR123_2016_nbins9.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2016_nbins9.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2016_nbins9.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2016_nbins9.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   -o impacts_data_2016_nbins9_ZG.json
#plotImpacts.py -t rename.json -i impacts_data_2016_nbins9_ZG.json -o impacts_data_2016_nbins9_ZG

########
#text2workspace.py  datacard_CR123_2017_nbins3.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2017_nbins3.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2017_nbins3.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2017_nbins3.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   -o impacts_data_2017_nbins3_ZG.json
#plotImpacts.py -t rename.json -i impacts_data_2017_nbins3_ZG.json -o impacts_data_2017_nbins3_ZG


#text2workspace.py  datacard_CR123_2017_nbins6.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2017_nbins6.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2017_nbins6.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2017_nbins6.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   -o impacts_data_2017_nbins6_ZG.json
#plotImpacts.py -t rename.json -i impacts_data_2017_nbins6_ZG.json -o impacts_data_2017_nbins6_ZG


#text2workspace.py  datacard_CR123_2017_nbins9.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2017_nbins9.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2017_nbins9.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2017_nbins9.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   -o impacts_data_2017_nbins9_ZG.json
#plotImpacts.py -t rename.json -i impacts_data_2017_nbins9_ZG.json -o impacts_data_2017_nbins9_ZG


##############
#text2workspace.py  datacard_CR123_2018_nbins3.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2018_nbins3.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2018_nbins3.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2018_nbins3.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   -o impacts_data_2018_nbins3_ZG.json
#plotImpacts.py -t rename.json -i impacts_data_2018_nbins3_ZG.json -o impacts_data_2018_nbins3_ZG


#text2workspace.py  datacard_CR123_2018_nbins6.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2018_nbins6.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2018_nbins6.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2018_nbins6.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   -o impacts_data_2018_nbins6_ZG.json
#plotImpacts.py -t rename.json -i impacts_data_2018_nbins6_ZG.json -o impacts_data_2018_nbins6_ZG


#text2workspace.py  datacard_CR123_2018_nbins9.txt # saveworkspace while doing fitting and use the rootfile here to make impact plot
#combineTool.py -M Impacts -d datacard_CR123_2018_nbins9.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --doInitialFit --robustFit 1 
#combineTool.py -M Impacts -d datacard_CR123_2018_nbins9.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   --robustFit 1 --doFits 
#combineTool.py -M Impacts -d datacard_CR123_2018_nbins9.root -m 125 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF   -o impacts_data_2018_nbins9_ZG.json
#plotImpacts.py -t rename.json -i impacts_data_2018_nbins9_ZG.json -o impacts_data_2018_nbins9_ZG
