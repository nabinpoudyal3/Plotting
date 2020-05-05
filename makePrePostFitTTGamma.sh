#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")
declare -a PLOT=("M3Plot" "ChIsoPlot" "btag0")
# "zeroPhoton")

for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Ele   --$plot &
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Mu    --$plot &
	done
done

wait


for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Ele   --$plot --postfitPlots &
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Mu    --$plot --postfitPlots &
	done
done

echo "Done making pre-post fit M3 and ChIso"
