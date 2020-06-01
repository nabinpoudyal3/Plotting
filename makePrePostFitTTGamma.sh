#!/bin/bash

declare -a YEAR=("2016")
#declare -a YEAR=("2016" "2017" "2018")
declare -a PLOT=("M3Plot" "ChIsoPlot" "btag0")

#for plot in ${PLOT[@]}; do
#	for year in ${YEAR[@]}; do
		#python makePlots_TTGamma_temp.py -y $year   -c Ele   --$plot --prefitPlots
		#python makePlots_TTGamma_temp.py -y $year   -c Mu    --$plot --prefitPlots
#	done
#done

#wait


for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do
		python makePlots_TTGamma_temp.py -y $year   -c Ele   --$plot --postfitPlots
		python makePlots_TTGamma_temp.py -y $year   -c Mu    --$plot --postfitPlots
	done
done

echo "Done making pre-post fit M3 and ChIso"


echo "Making plot for 0 photon control region"
#for year in ${YEAR[@]}; do

	#python makePlot_M3Control.py -y $year --zeroPhoton  -c Ele --prefitPlots
	#python makePlot_M3Control.py -y $year --zeroPhoton  -c Mu  --prefitPlots

#done

#for year in ${YEAR[@]}; do

	#python makePlot_M3Control.py -y $year --zeroPhoton  -c Ele --postfitPlots
	#python makePlot_M3Control.py -y $year --zeroPhoton  -c Mu  --postfitPlots 

#done
