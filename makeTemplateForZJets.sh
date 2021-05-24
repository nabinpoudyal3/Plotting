#!/bin/bash

declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
# declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
declare -a YEAR=("2016")
# declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "prefireEcal" "Pdf" "isr" "fsr" "JECTotal" "JER" "Q2")
# declare -a SYSTEMATICS=("JECTotal" "JER")
declare -a LEVEL=("up" "down")


# For nominal template
for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		python makePlots_ZJets.py -y $year  -c DiEle --$controlregion  --useQCDMC --template 
		python makePlots_ZJets.py -y $year  -c DiMu  --$controlregion  --useQCDMC --template 
	done
done
# For systematics templates
for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				python makePlots_ZJets.py -y $year  -c DiEle --$controlregion  --syst $systematics --level $level --template --useQCDMC 
				python makePlots_ZJets.py -y $year  -c DiMu  --$controlregion  --syst $systematics --level $level --template --useQCDMC              
			done
		done
	done
done

wait
echo "Done making templates for ZJets. "

exit 1


> /dev/null

python makePlots_ZJets.py -y 2016  -c DiEle --looseCRge2e0  --useQCDMC --template
for systematics in ${SYSTEMATICS[@]}; do
	python makePlots_ZJets.py -y 2016  -c DiEle --looseCRge2e0  --useQCDMC --template --syst $systematics --level up   
	python makePlots_ZJets.py -y 2016  -c DiEle --looseCRge2e0  --useQCDMC --template --syst $systematics --level down 

done

exit 1
