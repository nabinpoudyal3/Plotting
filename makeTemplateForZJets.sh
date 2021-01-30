#!/bin/bash

###IMPORTANT:
# pdf, isr, fsr and q2 are wrong.

declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
declare -a YEAR=("2016" "2017" "2018")

## quick test for 2016, 2017 and 2018:
# declare -a CONTROLREGION=("looseCRge2e0")
# declare -a YEAR=("2016" "2017" "2018")

#82 to 102 bins
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "prefireEcal")
#declare -a SYSTEMATICS=("Pdf") I don't have systematics such as JEC and JER for dilepton 
declare -a LEVEL=("up" "down")
# For nominal template
for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		echo "=====>" python makePlots_ZJets.py -y $year  -c DiEle --$controlregion  --useQCDMC --template
		              python makePlots_ZJets.py -y $year  -c DiEle --$controlregion  --useQCDMC --template
		echo "=====>" python makePlots_ZJets.py -y $year  -c DiMu  --$controlregion  --useQCDMC --template
		              python makePlots_ZJets.py -y $year  -c DiMu  --$controlregion  --useQCDMC --template
	done
done
# For systematics templates
for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				echo "=====>" python makePlots_ZJets.py -y $year  -c DiEle --$controlregion  --syst $systematics --level $level --template --useQCDMC
				              python makePlots_ZJets.py -y $year  -c DiEle --$controlregion  --syst $systematics --level $level --template --useQCDMC
				echo "=====>" python makePlots_ZJets.py -y $year  -c DiMu  --$controlregion  --syst $systematics --level $level --template --useQCDMC
				              python makePlots_ZJets.py -y $year  -c DiMu  --$controlregion  --syst $systematics --level $level --template --useQCDMC               
			done
		done
	done
done

wait
echo "Done making templates for ZJets. "
