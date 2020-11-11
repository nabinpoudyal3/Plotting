#!/bin/bash

declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
declare -a YEAR=("2016" "2017" "2018")

for year in ${YEAR[@]}; do
	for controlregion in ${CONTROLREGION[@]}; do
		echo "DiEle" $year $controlregion  
		./makeHistograms_Dilep_nominal.sh "DiEle" $year $controlregion &
		echo "DiMu " $year $controlregion
		./makeHistograms_Dilep_nominal.sh "DiMu" $year $controlregion  &
   done
   wait
   echo "waiting for each year"
done
