#!/bin/bash

# declare -a YEAR=("2016" "2017" "2018")
declare -a YEAR=("2016")

for year in ${YEAR[@]}; do

	python makePlots_SystUpDownTTGamma.py -y $year -c Ele --tight --plotVariable M3 
	python makePlots_SystUpDownTTGamma.py -y $year -c Ele --tight --plotVariable ChIso 
	python makePlots_SystUpDownTTGamma.py -y $year -c Ele --tight --plotVariable zerobtag
	python makePlots_SystUpDownTTGamma.py -y $year -c Ele --tight --plotVariable M30photon
		
	python makePlots_SystUpDownTTGamma.py -y $year -c Mu --tight --plotVariable M3 
	python makePlots_SystUpDownTTGamma.py -y $year -c Mu --tight --plotVariable ChIso 
	python makePlots_SystUpDownTTGamma.py -y $year -c Mu --tight --plotVariable zerobtag
	python makePlots_SystUpDownTTGamma.py -y $year -c Mu --tight --plotVariable M30photon

done 

exit 1

test
	python makePlots_SystUpDownTTGamma.py -y 2016 -c Mu --tight --plotVariable M3 
	python makePlots_SystUpDownTTGamma.py -y 2016 -c Mu --tight --plotVariable ChIso 
	python makePlots_SystUpDownTTGamma.py -y 2016 -c Mu --tight --plotVariable zerobtag
	python makePlots_SystUpDownTTGamma.py -y 2016 -c Mu --tight --plotVariable M30photon


	combine --skipBOnlyFit -M FitDiagnostics -n .Asimov_ele_2017 datacard_ele_2017.root --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --setParameterRanges nonPromptSF=-5,5:WGSF=-5,5:OtherSF=-5,5:Other_norm=-5,5:ZGSF=-5,5 -t -1 --expectSignal 1 -v1 --freezeParameters fsr

		combine --skipBOnlyFit -M FitDiagnostics -n .Asimov_ele_2018 datacard_ele_2018.root --seed=314159 --saveOverallShapes --plots --saveNLL --redefineSignalPOIs=r,nonPromptSF,TTbarSF --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 --setParameterRanges nonPromptSF=-5,5:WGSF=-5,5:OtherSF=-5,5:Other_norm=-5,5:ZGSF=-5,5 -t -1 --expectSignal 1 -v1 --freezeParameters fsr
