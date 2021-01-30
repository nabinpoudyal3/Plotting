#!/bin/bash

for i in {1..3}; do
echo "********************************************************************************************************************************"
echo "(@@) (  ) (@)  ( )  @@    ()    @     O     @
                     (   )
                 (@@@@)
              (    )

            (@@@)
         ====        ________                ___________
     _D _|  |_______/        \__I_I_____===__|_________|
      |(_)---  |   H\________/ |   |        =|___ ___|      ________________
      /     |  |   H  |  |     |   |         ||_| |_||     _|
     |      |  |   H  |__--------------------| [___] |   =|
     | ________|___H__/__|_____/[][]~\_______|       |   -|
     |/ |   |-----------I_____I [][] []  D   |=======|____|_________________
   __/ =| o |=-O=====O=====O=====O \ ____Y___________|__|___________________
    |/-=|___|=    ||    ||    ||    |_____/~\___/          |_D__D__D_|  |_D_
     \_/      \__/  \__/  \__/  \__/      \_/               \_/   \_/    \_/"
echo "********************************************************************************************************************************"
done

######################################################
######### MUON CHANNEL
#####################################################
declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "nonPromptSF" "PU" "prefireEcal")

text2workspace.py  datacard_mu_2018.txt
ValidateDatacards.py datacard_mu_2018.txt --printLevel 3 --checkUncertOver 0.1
combine -M ChannelCompatibilityCheck datacard_mu_2018.root -v1 --redefineSignalPOIs=r,nonPromptSF

combine datacard_mu_2018.root -M FitDiagnostics -V -n .datacard_mu_2018 --toys=-1 --expectSignal=1 --seed=314159 --redefineSignalPOIs=r,nonPromptSF -v1 --rMin=0 --rMax=5    --cminDefaultMinimizerStrategy 0
python diffNuisances.py fitDiagnostics.datacard_mu_2018.root --all -g plots_mu_2018.root

combine -M MultiDimFit datacard_mu_2018.root -s 314159  --algo grid --points=300 -n .Main --rMin=0 --rMax=5   
combine -M MultiDimFit datacard_mu_2018.root -s 314159  --saveWorkspace -n .snapshot --rMin=0 --rMax=5   
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll  --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --rMin=0 --rMax=5   
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_mu_2018 

#combine -H FitDiagnostics -n .hint_mu_2018 datacard_mu_2018.root -s 314159 --redefineSignalPOIs r,nonPromptSF -v1  

combine -M FitDiagnostics -V -n .Asimov_mu_2018 datacard_mu_2018.root --seed=314159 --redefineSignalPOIs=r,nonPromptSF --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=5 --expectSignal=1 -t -1 -v0 --skipBOnlyFit --cminDefaultMinimizerStrategy 0

combine -M FitDiagnostics -V -n mu_2018 datacard_mu_2018.root --plots --saveNLL  --robustFit=1 -s 314159 --redefineSignalPOIs r,nonPromptSF --saveOverallShapes --saveWithUncertainties --saveNormalizations -v1 --rMin=0 --rMax=5    --skipBOnlyFit
#python mlfitNormsToText.py fitDiagnosticsmu_2018.root --uncertainties


combine -M FitDiagnostics -V -n .TOY_mu_2018 datacard_mu_2018.root --seed=314159 --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=5 --expectSignal=1 -t 500 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF >& /dev/null


combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=5   
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=5 --parallel 24   
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  -o impacts_toy_mu_2018.json    -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=5   
plotImpacts.py -i impacts_toy_mu_2018.json -o impacts_toy_mu_2018 

combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  --doInitialFit                  --robustFit=1   --rMin=0 --rMax=5   
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  --doFits                        --robustFit=1   --rMin=0 --rMax=5 --parallel 24   
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125  -o impacts_data_mu_2018.json   --robustFit=1    --rMin=0 --rMax=5   
plotImpacts.py -i impacts_data_mu_2018.json -o impacts_data_mu_2018 


for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_mu_2018.root -s 314159 -t -1 --expectSignal=1 --algo grid --points=100 -n .Asimov_Main_mu_"$parameter" --rMin=0 --rMax=5  -P $parameter --floatOtherPOIs 1 &
done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Asimov_Main_mu_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o MinimizationPlots/single_scan_Asimov_mu_"$parameter"&
done
echo "Done"

wait

for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_mu_2018.root -s 314159 --algo grid --points=100 -n .Data_Main_mu_"$parameter" --rMin=0 --rMax=5 -P $parameter --floatOtherPOIs 1 &

done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Data_Main_mu_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o MinimizationPlots/single_scan_data_mu_"$parameter"&
done
echo "Done"
