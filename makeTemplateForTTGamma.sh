#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Q2")
declare -a LEVEL=("up" "down")
declare -a PLOT=("M3Plot" "ChIsoPlot" "btag0")

for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do      
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Ele --tight  --$plot  --template
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Mu --tight  --$plot  --template
	done
done

for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				python makePlots_TTGamma.py -y $year  --useQCDMC -c Ele --tight  --$plot --syst $systematics --level $level --template
				python makePlots_TTGamma.py -y $year  --useQCDMC -c Mu  --tight  --$plot --syst $systematics --level $level --template
			done
		done
	done
done


echo "Done making templates for M3 and ChIso"
