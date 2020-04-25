#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")
declare -a PLOT=("etPlot" "etaPlot" "phiPlot")

for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do

		python makePlots_photonCategory.py -y $year -c Ele --looseCRe2e0  --$plot   
		python makePlots_photonCategory.py -y $year -c Mu  --looseCRe2e0  --$plot  

	done
done
wait
echo "All processes done!"


