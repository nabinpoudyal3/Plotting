#!/bin/bash

######################################################
######### ELECTRON CHANNEL
#####################################################

# If one of the nuisances is quite heavily constrained or (weirder) has a post-fit uncertainty >1! Run the following and check if it has double minima,etc
# combine datacard.txt -M MultiDimFit --algo grid --poi TTbarSF --setPhysicsModelParameterRange X=-3,3
# combine -M MultiDimFit -n _paramFit_Test_OtherSF --algo impact --redefineSignalPOIs r -P OtherSF --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --robustFit=1 --rMin=0 --rMax=5 -m 125 -d datacard_ele_2016.root
# Definition of minimization status minuit.
#       status = 1    : Covariance was made pos defined
#       status = 2    : Hesse is invalid, calculate the  Hesse matrix for error calculation.
#       status = 3    : Edm is above max, expected distance reached from the minimum
#       status = 4    : Reached call limit, 
#       status = 5    : Any other failure
#
# Try to use --rMin and --rMax for stable and accurate result
# Only consider --minos all error calculation if Hesse uncertainties are not accurate. 
# If Minos and Hesse both fail then consider using robustFit=1, robustFit has more options check if you need it.
# If the covariance matrix provided by Hesse is forced positive definite, then use costume covariance matrix --robustHesse=1
# use the following --cminDefaultMinimizerStrategy 0 (for Hessian), --cminDefaultMinimizerStrategy 1 ( using Minos) to  resolve incorrect covariance matrix (parameters being close to their boundaries after the fit, strong anti correlation, discontinuity in NLL or its derivative or near miminum)
#
#
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
combineCards.py -S M3=datacard_ele_2016_M3_DD.txt ChIso=datacard_ele_2016_ChIso_DD.txt  zerobtag=datacard_ele_2016_M30btag_DD.txt  >  datacard_ele_2016.txt

text2workspace.py  datacard_ele_2016.txt 
ValidateDatacards.py datacard_ele_2016.txt --printLevel 3 --checkUncertOver 0.1 
combine -M ChannelCompatibilityCheck datacard_ele_2016.root -v1 --redefineSignalPOIs=r,nonPromptSF
#--autoMaxPOIs "*" --runMinos=1

combine datacard_ele_2016.root -M FitDiagnostics -n .datacard_ele_2016 --toys=-1 --expectSignal=1  --seed=314159 --redefineSignalPOIs=r,nonPromptSF -v1 --rMin=0 --rMax=5  
#freezeNuisanceGroups mySyst
python diffNuisances.py fitDiagnostics.datacard_ele_2016.root --all -g plots_ele_2016.root


combine -M MultiDimFit datacard_ele_2016.root -s 314159  --algo grid --points=300 -n .Main --rMin=0 --rMax=5 
#python plot1DScan.py higgsCombine.Main.MultiDimFit.mH120.314159.root --POI ZGSF -o single_scan
combine -M MultiDimFit datacard_ele_2016.root -s 314159  --saveWorkspace -n .snapshot --rMin=0 --rMax=5  
combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159 -n .freezeAll  --algo grid --points=300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit --rMin=0 --rMax=5 
python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_ele_2016 

#combine -H FitDiagnostics -n .hint_ele_2016 datacard_ele_2016.root -s 314159 --redefineSignalPOIs r,nonPromptSF -v1  

combine -M FitDiagnostics -n .Asimov_ele_2016 datacard_ele_2016.root --seed=314159 --redefineSignalPOIs=r,nonPromptSF --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=5 --expectSignal=1 -t -1 -v0 --skipBOnlyFit


combine -M FitDiagnostics -n el_2016 datacard_ele_2016.root --plots --saveNLL --robustFit=1 -s 314159 --redefineSignalPOIs r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations -v1 --rMin=0 --rMax=5  --skipBOnlyFit
#--freezeNuisanceGroups mySyst
#python mlfitNormsToText.py fitDiagnosticsel_2016.root --uncertainties


combine -M FitDiagnostics -n .TOY_ele_2016 datacard_ele_2016.root --seed=314159 --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=5 --expectSignal=1 -t 5000 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF 

# something wrong with the commands below. I think it should work.
#combine -M GenerateOnly -n .Gen_ele_2016 datacard_ele_2016.txt --toys=1000 --toysFrequentist \
#--expectSignal=1 --seed=314159 --redefineSignalPOIs r,nonPromptSF \
#--rMin=0 --rMax=5 -v0  --saveToys 

#combine -M FitDiagnostics -n .TOY_ele_2016 datacard_ele_2016.root --seed=314159 --redefineSignalPOIs r,nonPromptSF \
#--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=0 --rMax=5 -v1  \
#--toysFile higgsCombine.Gen_ele_2016.GenerateOnly.mH120.314159.root

# no need to redefine POIs r and nonPromptSF but use the range for nonPromptSF 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=5  
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=5   --parallel 24
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_toy_ele_2016.json   -t -1 --expectSignal 1  --robustFit=1 --rMin=0 --rMax=5  
plotImpacts.py -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016 

combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doInitialFit                 --robustFit=1   --rMin=0 --rMax=5  
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  --doFits                       --robustFit=1   --rMin=0 --rMax=5   --parallel 24
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125  -o impacts_data_ele_2016.json  --robustFit=1   --rMin=0 --rMax=5  
plotImpacts.py -i impacts_data_ele_2016.json -o impacts_data_ele_2016 

#The following test to find out the range of 
#combine -M Asymptotic htt_mt.root -m 125

declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "nonPromptSF" "PU" "prefireEcal")
for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_ele_2016.root -s 314159 -t -1 --expectSignal=1 --algo grid --points=100 -n .Asimov_Main_ele_"$parameter" --rMin=0 --rMax=5  -P $parameter --floatOtherPOIs 1 &
done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Asimov_Main_ele_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o MinimizationPlots/single_scan_Asimov_ele_"$parameter"&
done
echo "Done"

wait

for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_ele_2016.root -s 314159 --algo grid --points=100 -n .Data_Main_ele_"$parameter" --rMin=0 --rMax=5 -P $parameter --floatOtherPOIs 1 &

done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Data_Main_ele_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o MinimizationPlots/single_scan_data_ele_"$parameter"&
done
echo "Done"


wait
