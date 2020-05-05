#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")
declare -a CONTROLREGION=("looseCRge2e0" "looseCRe2e0" "looseCRe3e0" "looseCRge4e0")

for year in ${YEAR[@]}; do
	# rm -rf M3ChIso_tightplots_"$yr"/*.pdf # delete old pdf files before merging new ones

	python makePlots_SystUpDownNominal.py -y $year  --looseCRge2e0
	python makePlots_SystUpDownNominal.py -y $year  --looseCRge2e0

done

