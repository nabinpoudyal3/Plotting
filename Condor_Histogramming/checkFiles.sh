#!/bin/bash

eosls="eos root://cmseos.fnal.gov ls"

declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRge4e0" "looseCRe3e0" "looseCRe2e0")
declare -a YEAR=("2016" "2017" "2018")

# "PU", "JER", "prefireEcal", "fsr", "isr", "Pdf", "Q2", "EleEff", "BTagSF_l", "BTagSF_b", "PhoEff", "MuEff", "JECTotal"

declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "prefireEcal" "Pdf" "isr" "fsr" "JECTotal" "JER" "Q2")
declare -a LEVEL=("up" "down")
# For nominal template

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		echo         /store/user/npoudyal/histograms_"$year"/ele/hists_"$controlregion" 
		$eosls -lth  /store/user/npoudyal/histograms_"$year"/ele/hists_"$controlregion"    
		echo         /store/user/npoudyal/histograms_"$year"/mu/hists_"$controlregion"    
		$eosls -lth  /store/user/npoudyal/histograms_"$year"/mu/hists_"$controlregion"    
	done
done

# For systematics templates

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				echo         /store/user/npoudyal/histograms_"$year"/ele/hists_"$systematics"_"$level"_"$controlregion" 
				$eosls -lth  /store/user/npoudyal/histograms_"$year"/ele/hists_"$systematics"_"$level"_"$controlregion"    
				echo          /store/user/npoudyal/histograms_"$year"/mu/hists_"$systematics"_"$level"_"$controlregion"    
				$eosls -lth   /store/user/npoudyal/histograms_"$year"/mu/hists_"$systematics"_"$level"_"$controlregion"   
			done
		done
	done
done

wait
echo "Done "

exit 1

