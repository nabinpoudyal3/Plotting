#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")


for year in ${YEAR[@]}; do
	# rm -rf M3ChIso_tightplots_"$yr"/*.pdf # delete old pdf files before merging new ones
	python makePlots_SystUpDownNominal.py -y $year -c Ele  
	python makePlots_SystUpDownNominal.py -y $year -c Ele  
	
	python makePlots_SystUpDownNominal.py -y $year -c Mu    
	python makePlots_SystUpDownNominal.py -y $year -c Mu  
done

