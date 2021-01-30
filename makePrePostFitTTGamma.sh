#!/bin/bash

declare -a YEAR2016=("2016") #"2017" "2018")
declare -a YEAR=("2017" "2018")

######################################
######################################
##### I won't have postfit plots yet. 
######################################
######################################
#### These prefit below contains all the SFs applied such as misID,Wgamma,Zgamma,ZJets
######################################
######################################

for year in ${YEAR2016[@]}; do
	echo "==>" python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot  --prefitPlots --datadriven 
	           python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot  --prefitPlots --datadriven 
	echo "==>" python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot  --prefitPlots --datadriven 
	           python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot  --prefitPlots --datadriven 

	echo "==>" python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot     --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot     --prefitPlots 
	echo "==>" python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot     --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot     --prefitPlots 

	echo "==>" python makePlots_TTGamma.py  -y $year -c Ele   --btag0      --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Ele   --btag0      --prefitPlots 
	echo "==>" python makePlots_TTGamma.py  -y $year -c Mu    --btag0      --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --btag0      --prefitPlots 

	echo "==>" python makePlots_TTGamma.py  -y $year -c Ele   --btag0_3j      --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Ele   --btag0_3j      --prefitPlots 
	echo "==>" python makePlots_TTGamma.py  -y $year -c Mu    --btag0_3j      --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --btag0_3j      --prefitPlots 	           

	echo "==>" python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton --prefitPlots 
	           python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton --prefitPlots 
	echo "==>" python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton --prefitPlots 
	           python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton --prefitPlots 
 
done


for year in ${YEAR[@]}; do
	echo "==>" python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot  --prefitPlots --datadriven --noData
	           python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot  --prefitPlots --datadriven --noData
	echo "==>" python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot  --prefitPlots --datadriven --noData
	           python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot  --prefitPlots --datadriven --noData

	echo "==>" python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot     --prefitPlots  --noData
	           python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot     --prefitPlots  --noData
	echo "==>" python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot     --prefitPlots  --noData
	           python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot     --prefitPlots  --noData

	echo "==>" python makePlots_TTGamma.py  -y $year -c Ele   --btag0      --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Ele   --btag0      --prefitPlots 
	echo "==>" python makePlots_TTGamma.py  -y $year -c Mu    --btag0      --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --btag0      --prefitPlots 

	echo "==>" python makePlots_TTGamma.py  -y $year -c Ele   --btag0_3j      --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Ele   --btag0_3j      --prefitPlots 
	echo "==>" python makePlots_TTGamma.py  -y $year -c Mu    --btag0_3j      --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --btag0_3j      --prefitPlots 	           

	echo "==>" python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton --prefitPlots 
	           python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton --prefitPlots 
	echo "==>" python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton --prefitPlots 
	           python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton --prefitPlots 
 
done


exit 1