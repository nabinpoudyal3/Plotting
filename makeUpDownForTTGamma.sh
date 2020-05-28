#!/bin/bash

#declare -a YEAR=("2016" "2017" "2018")

#for year in ${YEAR[@]}; do
	# rm -rf M3ChIso_tightplots_"$yr"/*.pdf # delete old pdf files before merging new ones
#	python makePlots_SystUpDownNominal_ttg.py -y $year -c Ele --tight --M3Plot 
#	python makePlots_SystUpDownNominal_ttg.py -y $year -c Ele --tight --ChIsoPlot
	
#	python makePlots_SystUpDownNominal_ttg.py -y $year -c Mu  --tight --M3Plot 
#	python makePlots_SystUpDownNominal_ttg.py -y $year -c Mu  --tight --ChIsoPlot
#done


python makePlots_SystUpDownNominal_ttg.py -y 2016 -c Ele --tight --plotVariable M3 
python makePlots_SystUpDownNominal_ttg.py -y 2016 -c Ele --tight --plotVariable ChIso 

python makePlots_SystUpDownNominal_ttg.py -y 2016 -c Ele --tight --plotVariable M30btag
python makePlots_SystUpDownNominal_ttg.py -y 2016 -c Ele --tight --plotVariable M30photon
