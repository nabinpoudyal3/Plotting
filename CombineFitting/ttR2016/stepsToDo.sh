#!/bin/bash


#if there is a rateParam there must be --saveNormalizations

##Validate the Datacard
ValidateDatacards.py datacard_CR123_2016.txt --printLevel 3 --checkUncertOver 0.1

##convert Datacard into workspace
#text2workspace.py datacard_CR123_2016.txt -o workspace.root

##Closure test on pre-fit Asimov with b-only fit and b+s fit, after fitDiagnostics..see everything inside the rootfile, check if it has cov matrix or not
# all fit status -1 means fit failed.
#covariance matrix quality: Full, accurate covariance matrix
                #Status : MINIMIZE=0 HESSE=0  means cov and minimisation passed. 
# when it fails, do --robustHesse 1
#--saveNormalizations --saveWithUncertainties --plots

combine -M FitDiagnostics datacard_CR123_2016.root -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --freezeNuisanceGroups mySyst 
combine -M FitDiagnostics datacard_CR123_2016.root -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --freezeParameters lumi

combine datacard_CR123_2016.root -M FitDiagnostics -t -1 --expectSignal 0 -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --minos all
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.root --all
root -l fitDiagnostics.root 
fit_b->Print()
fit_s->Print()

combine datacard_CR123_2016.root -M FitDiagnostics -t -1 --expectSignal 2 -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF 
#--saveNormalizations --saveWithUncertainties --plots
python /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py fitDiagnostics.root --all
root -l fitDiagnostics.root 
fit_b->Print()
fit_s->Print()

## Adding control regions
# rateParams
#Nuisance parameter impacts
#text2workspace.py  datacard_CR123_2016.root # saveworkspace while doing fitting and use the rootfile here to make impact plot
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --expectSignal 2 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --expectSignal 2 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -t -1 --expectSignal 2 -o impacts_toy_2016.json
plotImpacts.py -t rename.json -i impacts_toy_2016.json -o impacts_toy_2016

#Post-fit distributions
combine -M FitDiagnostics datacard_CR123_2016.root -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --saveShapes --saveWithUncertainties --saveNormalizations --saveWorkspace

#Calculating the significance
#Signal strength measurement and uncertainty breakdown
#combine -M MultiDimFit datacard_CR123_2016.root -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF
# usually works for only one POI
combine -M MultiDimFit datacard_CR123_2016.root -s 314159  --rMin -5 --rMax 5 --algo grid --points 500 -n .Main
#root -l higgsCombine.Main.MultiDimFit.mH120.314159.root
#limit->Scan("r:deltaNLL")
python plot1DScan.py higgsCombine.Main.MultiDimFit.mH120.314159.root --POI r -o single_scan
combine -M MultiDimFit datacard_CR123_2016.root -n .snapshot -s 314159 --rMin -5 --rMax 5 --saveWorkspace
#combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll --rMin -5 --rMax 5 --algo grid --points 500 --freezeParameters allConstrainedNuisances --snapshotName MultiDimFit
#freezing nuisance parameter gives better result
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll --rMin -5 --rMax 5 --algo grid --points 500 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root  --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_first_attempt
##
#combine -M MultiDimFit datacard_CR123_2016.root -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --rMin -1 --rMax 5 --algo grid --points 100 -n .Main
#combine -M MultiDimFit datacard_CR123_2016.root -s 314159 --algo grid --points 100
#root -l higgsCombine.Main.MultiDimFit.mH120.314159.root
#limit->Scan("r:deltaNLL")

#python plot1DScan.py higgsCombine.Main.MultiDimFit.mH120.314159.root -o single_scan


#combine -M MultiDimFit datacard_CR123_2016.root -n .snapshot -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --rMin -1 --rMax 5 --saveWorkspace
#combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --rMin -1 --rMax 5 --algo grid --points 100 --freezeParameters allConstrainedNuisances --snapshotName MultiDimFit
#python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:FreezeAll:2' --breakdown Syst,Stat -o freeze_first_attempt


#Use of channel masking

# to freeze nuisance parameters
#combine -M FitDiagnostics datacard_CR123_2016.root -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --freezeNuisanceGroups mySyst 
#combine -M FitDiagnostics datacard_CR123_2016.root -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --freezeParameters BTagSF_b
