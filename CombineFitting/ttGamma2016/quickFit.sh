
combineCards.py -S M3=datacard_ele_2016_M3_DD.txt ChIso=datacard_ele_2016_ChIso_DD.txt  zerobtag=datacard_ele_2016_M30btag_DD.txt M30photon=datacard_ele_2016_M30photon_DD.txt >  datacard_ele_2016.txt

text2workspace.py  datacard_ele_2016.txt 
# ValidateDatacards.py datacard_ele_2016.txt --printLevel 3 --checkUncertOver 0.1 
combine -M ChannelCompatibilityCheck --expectSignal=1  datacard_ele_2016.root -v1 --redefineSignalPOIs=r,nonPromptSF
#--autoMaxPOIs "*" --runMinos=1

combine datacard_ele_2016.root -M FitDiagnostics -n .datacard_ele_2016 --toys=-1 --expectSignal=1  --seed=314159 --redefineSignalPOIs=r,nonPromptSF -v1 --rMin=0 --rMax=10  --setParameterRanges nonPromptSF=0,100


combine -M FitDiagnostics -n el_2016 datacard_ele_2016.root --plots --saveNLL --robustFit=1 -s 314159 --redefineSignalPOIs r,nonPromptSF --expectSignal=1 --saveShapes --saveWithUncertainties --saveNormalizations -v1 --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 --skipBOnlyFit



combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100  --parallel 24
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_toy_ele_2016.json   -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 
plotImpacts.py -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016 

combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 --robustFit=1   --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       --robustFit=1   --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100  --parallel 24
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_data_ele_2016.json  --robustFit=1   --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 
plotImpacts.py -i impacts_data_ele_2016.json -o impacts_data_ele_2016 



exit 1

#freezeNuisanceGroups mySyst
python diffNuisances.py fitDiagnostics.datacard_ele_2016.root --all -g plots_ele_2016.root

combine -M MultiDimFit datacard_ele_2016.root -s 314159  --algo grid --points=300 -n .Main --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100
#python plot1DScan.py higgsCombine.Main.MultiDimFit.mH120.314159.root --POI ZGSF -o single_scan
combine -M MultiDimFit datacard_ele_2016.root -s 314159  --saveWorkspace -n .snapshot --rMin=0 --rMax=10  --setParameterRanges nonPromptSF=0,100
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll  --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_ele_2016 

#combine -H FitDiagnostics -n .hint_ele_2016 datacard_ele_2016.root -s 314159 --redefineSignalPOIs r,nonPromptSF -v1  

combine -M FitDiagnostics -n .Asimov_ele_2016 datacard_ele_2016.root --seed=314159 --redefineSignalPOIs=r,nonPromptSF \
--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 \
--expectSignal=1 -t -1 -v0 --skipBOnlyFit


combine -M FitDiagnostics -n el_2016 datacard_ele_2016.root --plots --saveNLL --robustFit=1 -s 314159 --redefineSignalPOIs r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations -v1 --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 --skipBOnlyFit
#--freezeNuisanceGroups mySyst
#python mlfitNormsToText.py fitDiagnosticsel_2016.root --uncertainties


combine -M FitDiagnostics -n .TOY_ele_2016 datacard_ele_2016.root --seed=314159 \
--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 \
--expectSignal=1 -t 300 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF 

# something wrong with the commands below. I think it should work.
#combine -M GenerateOnly -n .Gen_ele_2016 datacard_ele_2016.txt --toys=1000 --toysFrequentist \
#--expectSignal=1 --seed=314159 --redefineSignalPOIs r,nonPromptSF \
#--rMin=0 --rMax=10 -v0 --setParameterRanges nonPromptSF=0,100 --saveToys 

#combine -M FitDiagnostics -n .TOY_ele_2016 datacard_ele_2016.root --seed=314159 --redefineSignalPOIs r,nonPromptSF \
#--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=10 -v1 --setParameterRanges nonPromptSF=0,100 \
#--toysFile higgsCombine.Gen_ele_2016.GenerateOnly.mH120.314159.root

# no need to redefine POIs r and nonPromptSF but use the range for nonPromptSF 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100  --parallel 24
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_toy_ele_2016.json   -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 
plotImpacts.py -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016 

combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 --robustFit=1   --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       --robustFit=1   --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100  --parallel 24
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_data_ele_2016.json  --robustFit=1   --rMin=0 --rMax=10 --setParameterRanges nonPromptSF=0,100 
plotImpacts.py -i impacts_data_ele_2016.json -o impacts_data_ele_2016 

#The following test to find out the range of 
#combine -M Asymptotic htt_mt.root -m 125

################################################################################################
################################################################################################
################################################################################################
################################################################################################
exit 1
################################################################################################
################################################################################################
################################################################################################
################################################################################################


declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "nonPromptSF")
for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_ele_2016.root -s 314159 -t -1 --expectSignal=1 --algo grid --points=100 -n .Asimov_Main_ele_"$parameter" --rMin=0 --rMax=10  -P $parameter --floatOtherPOIs 1 
done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Asimov_Main_ele_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_ele_"$parameter"
done
echo "Done"

wait

for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_ele_2016.root -s 314159 --algo grid --points=100 -n .Data_Main_ele_"$parameter" --rMin=0 --rMax=10 -P $parameter --floatOtherPOIs 1 
done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Data_Main_ele_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_ele_"$parameter"
done
echo "Done"


