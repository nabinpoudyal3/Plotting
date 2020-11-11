#!/bin/bash

###IMPORTANT:
# isr, fsr and q2 are wrong.

declare -a CONTROLREGION=("--looseCRge2e0" "--looseCRe2e0" "--looseCRe3e0" "--looseCRge4e0")
declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "prefireEcal" "JER" "JECTotal")
declare -a LEVEL=("up" "down")



for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		echo "===>  python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --template"
		            python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --template 
		echo "===>  python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --template"
		            python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --template
	done
done



for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				echo "===>  python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --syst $systematics --level $level --template"
				            python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --syst $systematics --level $level --template
				echo "===>  python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --syst $systematics --level $level --template"
				            python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --syst $systematics --level $level --template
				
			done
		done
	done
done
echo "Done making templates with QCD_DD for MisIDE."

