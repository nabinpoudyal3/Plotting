#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")
declare -a PLOT=("M3Plot" "ChIsoPlot" "btag0")

for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Ele --tight  --$plot 
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Mu  --tight  --$plot 
	done
done

wait


for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Ele --tight  --$plot --postfitPlots
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Mu  --tight  --$plot --postfitPlots
	done
done

echo "Done making pre-post fit M3 and ChIso"
