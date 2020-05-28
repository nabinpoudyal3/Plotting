
#!/bin/bash

declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Q2" "isr" "fsr")
declare -a LEVEL=("up" "down")

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		python makePlots_ZJets.py -y $year  -c DiEle --$controlregion  --useQCDMC --template
		python makePlots_ZJets.py -y $year  -c DiMu  --$controlregion  --useQCDMC --template
	done
done

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				echo python makePlots_ZJets.py -y $year  -c DiEle --$controlregion  --syst $systematics --level $level --template --useQCDMC
				python makePlots_ZJets.py -y $year  -c DiEle --$controlregion  --syst $systematics --level $level --template --useQCDMC
				echo python makePlots_ZJets.py -y $year  -c DiMu  --$controlregion  --syst $systematics --level $level --template --useQCDMC
				python makePlots_ZJets.py -y $year  -c DiMu  --$controlregion  --syst $systematics --level $level --template --useQCDMC
				
			done
		done
	done
done

wait
echo "Done making templates for ZJets. "
