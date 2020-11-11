#!/bin/bash

#declare -a YEAR=("2016")

declare -a YEAR=("2016" "2017" "2018")
declare -a PLOT1=("ChIsoPlot")
declare -a PLOT2=("M3Plot" "btag0")
#declare -a PLOT2=("btag0")


# test
for plot in ${PLOT2[@]}; do
	for year in ${YEAR[@]}; do
		echo "==>" python makePlots_TTGamma.py -y $year   -c Ele   --$plot --prefitPlots 
		           python makePlots_TTGamma.py -y $year   -c Ele   --$plot --prefitPlots 
		echo "==>" python makePlots_TTGamma.py -y $year   -c Mu    --$plot --prefitPlots 
		           python makePlots_TTGamma.py -y $year   -c Mu    --$plot --prefitPlots 
	done
done

#exit 1

for plot in ${PLOT1[@]}; do
	for year in ${YEAR[@]}; do
		echo "==>" python makePlots_TTGamma.py -y $year   -c Ele   --$plot --prefitPlots --datadriven
		           python makePlots_TTGamma.py -y $year   -c Ele   --$plot --prefitPlots 
		echo "==>" python makePlots_TTGamma.py -y $year   -c Mu    --$plot --prefitPlots --datadriven
		           python makePlots_TTGamma.py -y $year   -c Mu    --$plot --prefitPlots 
	done
done
#
wait
#
#
for plot in ${PLOT1[@]}; do
	for year in ${YEAR[@]}; do
		echo "==>" python makePlots_TTGamma.py -y $year   -c Ele   --$plot --postfitPlots 
		           python makePlots_TTGamma.py -y $year   -c Ele   --$plot --postfitPlots 
		echo "==>" python makePlots_TTGamma.py -y $year   -c Mu    --$plot --postfitPlots 
		           python makePlots_TTGamma.py -y $year   -c Mu    --$plot --postfitPlots 
	done
done


for plot in ${PLOT2[@]}; do
	for year in ${YEAR[@]}; do
		echo "==>" python makePlots_TTGamma.py -y $year   -c Ele   --$plot --prefitPlots 
		           python makePlots_TTGamma.py -y $year   -c Ele   --$plot --prefitPlots 
		echo "==>" python makePlots_TTGamma.py -y $year   -c Mu    --$plot --prefitPlots 
		           python makePlots_TTGamma.py -y $year   -c Mu    --$plot --prefitPlots 
	done
done
#
wait
#
#
for plot in ${PLOT2[@]}; do
	for year in ${YEAR[@]}; do
		echo "==>" python makePlots_TTGamma.py -y $year   -c Ele   --$plot --postfitPlots 
		           python makePlots_TTGamma.py -y $year   -c Ele   --$plot --postfitPlots 
		echo "==>" python makePlots_TTGamma.py -y $year   -c Mu    --$plot --postfitPlots 
		           python makePlots_TTGamma.py -y $year   -c Mu    --$plot --postfitPlots 
	done
done



echo "Done making pre-post fit M3 and ChIso"
exit 1
echo "Making plot for 0 photon control region"
for year in ${YEAR[@]}; do

	echo "==>" python makePlot_M3Control.py -y $year --zeroPhoton  -c Ele --prefitPlots 
	           python makePlot_M3Control.py -y $year --zeroPhoton  -c Ele --prefitPlots 
	echo "==>" python makePlot_M3Control.py -y $year --zeroPhoton  -c Mu  --prefitPlots 
	           python makePlot_M3Control.py -y $year --zeroPhoton  -c Mu  --prefitPlots 
 
done

for year in ${YEAR[@]}; do

	echo "==>" python makePlot_M3Control.py -y $year --zeroPhoton  -c Ele --postfitPlots 
	           python makePlot_M3Control.py -y $year --zeroPhoton  -c Ele --postfitPlots 
	echo "==>" python makePlot_M3Control.py -y $year --zeroPhoton  -c Mu  --postfitPlots 
	           python makePlot_M3Control.py -y $year --zeroPhoton  -c Mu  --postfitPlots 

done
