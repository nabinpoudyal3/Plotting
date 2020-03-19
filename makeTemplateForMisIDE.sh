#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Q2")
declare -a LEVEL=("up" "down")



for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS[@]}; do
		for level in ${LEVEL[@]}; do
			python makePlots_MisIDE.py -y $year  --useQCDMC -c Ele --looseCRge2e0  --syst $systematics --level $level --template
			python makePlots_MisIDE.py -y $year  --useQCDMC -c Mu  --looseCRge2e0  --syst $systematics --level $level --template
		done
	done
done



echo "Done making templates with QCDMC for MisIDE. "

wait

for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS[@]}; do
		for level in ${LEVEL[@]}; do
			python makePlots_MisIDE.py -y $year  -c Ele --looseCRge2e0  --syst $systematics --level $level --template
			python makePlots_MisIDE.py -y $year  -c Mu  --looseCRge2e0  --syst $systematics --level $level --template
		done
	done
done



echo "Done making templates with QCD_DD for MisIDE. "
