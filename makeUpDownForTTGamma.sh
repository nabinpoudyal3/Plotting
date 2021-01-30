#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")

for year in ${YEAR[@]}; do

	python makePlots_SystUpDownTTGamma.py -y $year -c Ele --tight --plotVariable M3 
	python makePlots_SystUpDownTTGamma.py -y $year -c Ele --tight --plotVariable ChIso 
	python makePlots_SystUpDownTTGamma.py -y $year -c Ele --tight --plotVariable zerobtag
	python makePlots_SystUpDownTTGamma.py -y $year -c Ele --tight --plotVariable M30photon
		
	python makePlots_SystUpDownTTGamma.py -y $year -c Mu --tight --plotVariable M3 
	python makePlots_SystUpDownTTGamma.py -y $year -c Mu --tight --plotVariable ChIso 
	python makePlots_SystUpDownTTGamma.py -y $year -c Mu --tight --plotVariable zerobtag
	python makePlots_SystUpDownTTGamma.py -y $year -c Mu --tight --plotVariable M30photon

done 
