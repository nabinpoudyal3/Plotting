#!/bin/bash

declare -a CONTROLREGION=("--looseCRge2e0" "--looseCRe2e0" "--looseCRe3e0" "--looseCRge4e0")
declare -a YEAR=("2016" "2017" "2018")

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		echo "===> " python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --prefitPlots
		             python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --prefitPlots
		echo "===> " python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --prefitPlots
		             python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --prefitPlots
	done
done
wait

echo "Done prefit for MisIDEle plots!" 

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		echo "===> " python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --postfitPlots
		             python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --postfitPlots
		echo "===> " python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --postfitPlots
		             python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --postfitPlots
	done
done
wait
 
echo "Done prefit for MisIDEle plots!" 


