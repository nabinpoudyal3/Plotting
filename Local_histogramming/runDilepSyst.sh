#!/bin/bash

declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Q2" "isr" "fsr" "misIDE")
declare -a LEVEL=("up" "down")


for year in ${YEAR[@]}; do
	for controlregion in ${CONTROLREGION[@]}; do
    	for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				echo "DiEle" $year $controlregion  $systematics  $level
				./makeHistograms_Dilep_syst.sh "DiEle" $year $controlregion  $systematics  $level  &
				echo "DiMu " $year $controlregion  $systematics  $level
				./makeHistograms_Dilep_syst.sh "DiMu" $year $controlregion  $systematics  $level  &
            done
			wait
			echo "waiting to finish each systematics"
        done
		wait
		echo "waiting for each control region"
   done
   wait
   echo "waiting for each year"
done
