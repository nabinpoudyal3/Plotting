#!/bin/bash
#./allCombine.sh
#text2workspace.py  datacard_ele_2016.txt
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

#combine -M FitDiagnostics -n .TOY_ele_2016_test datacard_ele_2016.root --seed=314159 --redefineSignalPOIs r,nonPromptSF --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 --expectSignal=1 -t 10 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF

combine -M FitDiagnostics -n .TOY_ele_2016 datacard_ele_2016.root --seed=314159 --redefineSignalPOIs r,nonPromptSF \
--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
--expectSignal=1 -t 5000 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF &

combine -M FitDiagnostics -n .TOY_mu_2016 datacard_mu_2016.root --seed=314159 --redefineSignalPOIs r,nonPromptSF \
--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
--expectSignal=1 -t 5000 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF &

combine -M FitDiagnostics -n .TOY_both_2016 datacard_both_2016.root --seed=314159 --redefineSignalPOIs r,nonPromptSF \
--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
--expectSignal=1 -t 5000 -v3 --skipBOnlyFit --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,nonPromptSF &


exit 1


# Asimov fitting

combine -M FitDiagnostics -n .Asimov_ele_2016 datacard_ele_2016.root --seed=314159 --redefineSignalPOIs=r,nonPromptSF \
--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
--expectSignal=1 -t -1 -v0 --skipBOnlyFit


combine -M FitDiagnostics -n .Asimov_mu_2016 datacard_mu_2016.root --seed=314159 --redefineSignalPOIs=r,nonPromptSF \
--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
--expectSignal=1 -t -1 -v0 --skipBOnlyFit


combine -M FitDiagnostics -n .Asimov_both_2016 datacard_both_2016.root --seed=314159 --redefineSignalPOIs=r,nonPromptSF \
--saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 \
--expectSignal=1 -t -1 -v0 --skipBOnlyFit


exit 1

##### old way. It keeps crashing after 300 toys. and # checking with --trackParameters r,Others_norm



declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "prefireEcal" "TTbarSF" "WGSF" "ZGSF" "OtherSF")
for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_ele_2016.root -s 314159 -t -1 --expectSignal=1 --algo grid --points=100 -n .Asimov_Main_"$parameter" --rMin=-5 --rMax=5 --redefineSignalPOIs r,nonPromptSF -P $parameter --floatOtherPOIs 1 &
done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Asimov_Main_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_Asimov_"$parameter"&
done
echo "Done"

wait

for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_ele_2016.root -s 314159 --algo grid --points=100 -n .Data_Main_"$parameter" --rMin=-5 --rMax=5 --redefineSignalPOIs r,nonPromptSF -P $parameter --floatOtherPOIs 1 &

done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Data_Main_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_data_"$parameter"&
done
echo "Done"

exit 1


# Generate toy data and do fit diagnostics:
combine -M GenerateOnly -n .Gen_ele_2016 datacard_ele_2016.root --toys=1000 --toysFrequentist --expectSignal=1 --seed=314159 --redefineSignalPOIs r,nonPromptSF --rMin=-5 --rMax=5 -v0 --setParameterRanges nonPromptSF=-10,10 --saveToys 

combine -M FitDiagnostics -n .TOY_ele_2016 datacard_ele_2016.root --seed=314159 --redefineSignalPOIs r,nonPromptSF --saveWithUncertainties --saveNormalizations --saveToys  --plots --saveNLL --rMin=-5 --rMax=5 --setParameterRanges nonPromptSF=-10,10 --toysFile=higgsCombine.Gen_ele_2016.GenerateOnly.mH120.314159.root --expectSignal=1 -t 200 -v0


exit 1


# I think we can not do  NLL for toy.
combine -M MultiDimFit datacard_ele_2016.root -s 314159 --expectSignal=1 -t 50  --algo grid --points=100 -n .Main_PU --rMin=-5 --rMax=5 --redefineSignalPOIs r,nonPromptSF -P PU --floatOtherPOIs 1 -v3 > /dev/null 2>&1
python plot1DScan.py higgsCombine.Main_PU.MultiDimFit.mH120.314159.root --POI PU -o single_scan_PU

exit 1


# Generating Toys Only to study Bias

#combine -M GenerateOnly -n .TOY_ele_2016 datacard_ele_2016.txt --toys=1000 --toysFrequentist \
#--expectSignal=1 --seed=314159 --redefineSignalPOIs r,nonPromptSF \
#--rMin=-5 --rMax=5 -v0 --setParameterRanges nonPromptSF=-10,10 --saveToys 


#declare -a PARAMETERS=("PhoEff" "Q2" "misIDE" "PU" "isr" "fsr" "BTagSF_b" "lumi" "BTagSF_l" "EleEff" "TTbarSF" "WGSF" "ZGSF" "OtherSF" "Other_norm" "MuEff")
declare -a PARAMETERS=("PhoEff" "misIDE" "BTagSF_b" "lumi" "BTagSF_l" "MuEff" "EleEff" "prefireEcal" "TTbarSF" "WGSF" "ZGSF" "OtherSF")
#declare -a PARAMETERS=("PU")
for parameter in ${PARAMETERS[@]}; do
	combine -M MultiDimFit datacard_ele_2016.root -s 314159  --algo grid --points=100 -n .Main_"$parameter" --rMin=-5 --rMax=5 --redefineSignalPOIs r,nonPromptSF -P $parameter --floatOtherPOIs 1 --toysFile higgsCombine.TOY_ele_2016.GenerateOnly.mH120.314159.root &
	# freez other parameters for now or sth else or check it in impact plot too.
	#python plot1DScan.py higgsCombine.Main.MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_"$parameter"
	echo ""
done

wait 

for parameter in ${PARAMETERS[@]}; do
	python plot1DScan.py higgsCombine.Main_"$parameter".MultiDimFit.mH120.314159.root --POI $parameter -o single_scan_"$parameter"&
done
echo "Done"
#combine -M MultiDimFit datacard_ele_2016.root -s 314159  -t 100 --expectSignal=0 --algo grid --points=30 -n .Main_"$parameter" --rMin=-20 --rMax=20 --redefineSignalPOIs $parameter --setParameterRanges nonPromptSF=-20,20
exit 1

combine -M GenerateOnly -n .TOY_ele_2016 datacard_ele_2016.txt --toys=1000 --toysFrequentist \
--expectSignal=1 --seed=314159 --redefineSignalPOIs r,nonPromptSF \
--rMin=-5 --rMax=5 -v0 --setParameterRanges nonPromptSF=-10,10 --saveToys 

combine -M MultiDimFit datacard_ele_2016.txt -s 314159 \
--algo grid --points=100 -n .Main_PU --rMin=-5 --rMax=5 \
--redefineSignalPOIs r,nonPromptSF -P PU --floatOtherPOIs 1 \
--toysFile higgsCombine.TOY_ele_2016.GenerateOnly.mH120.314159.root

python plot1DScan.py higgsCombine.Main_PU.MultiDimFit.mH120.314159.root --POI PU -o single_scan_PU

exit 1
>> combine -M MultiDimFit -n _paramFit_Test_BTagSF_b --algo impact --redefineSignalPOIs r -P BTagSF_b --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --robustFit=1 --rMin=-5 --rMax=5 -m 125 -d datacard_ele_2016.root


combine datacard_ele_2016.root -M FitDiagnostics -n .datacard_ele_2016 \
--toys=-1 --expectSignal=1 --seed=314159 \
--redefineSignalPOIs=r,nonPromptSF --saveNormalizations \
--rMin=-5 --rMax=5 \
-v1 \
#--freezeParameters Q2,misIDE,PU,isr,lumi,BTagSF_l,EleEff \

#python make2016ttGammaSS_Asimov.py

python plot1DScan.py higgsCombine.Main_PU.MultiDimFit.mH120.314159.root --POI PU -o single_scan_PU
	
exit 1
#--saveShapes --saveWithUncertainties --saveNormalizations --plots \

 --rMin=-5 --rMax=5
 
--freezeParameters PhoEff,Q2,misIDE,PU,isr,fsr,BTagSF_b,lumi,BTagSF_l,MuEff,EleEff,OtherSF,Other_norm \
combine -M FitDiagnostics -n el_2016 datacard_ele_2016.root \
--plots --saveNLL --robustFit=1 -s 314159 --redefineSignalPOIs r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations -v1 \
--rMin=-2 --rMax=5

python mlfitNormsToText.py fitDiagnosticsel_2016.root --uncertainties

exit 1

Best fit r: 1  -0.0322271/+0.0314951  (68% CL)
INFO: (function: anyParameterAtBoundaries) utils.cc: 982 -- Found parameter ZGSF at boundary (within ~1sigma): 1.70249+/-0.200274
INFO: (function: anyParameterAtBoundaries) utils.cc: 982 -- Found parameter WGSF at boundary (within ~1sigma): 1.76+/-0.00567501

INFO: (function: anyParameterAtBoundaries) utils.cc: 982 -- Found parameter ZGSF at boundary (within ~1sigma): 1.84+/-0.210871
INFO: (function: anyParameterAtBoundaries) utils.cc: 982 -- Found parameter TTbarSF at boundary (within ~1sigma): 0.800001+/-0.0128573
INFO: (function: anyParameterAtBoundaries) utils.cc: 982 -- Found parameter WGSF at boundary (within ~1sigma): 1.76+/-0.00439749
 
--freezeParameters PhoEff,Q2,misIDE,PU,isr,fsr,BTagSF_b,lumi,BTagSF_l,MuEff,EleEff,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm \

python make2016ttGammaSS_Toy.py
