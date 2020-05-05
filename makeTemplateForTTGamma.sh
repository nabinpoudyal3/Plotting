#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Q2")
declare -a LEVEL=("up" "down")
declare -a PLOT=("M3Plot" "ChIsoPlot" "btag0")
# "zeroPhoton")
#
for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do      
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Ele   --$plot  --template
		python makePlots_TTGamma.py -y $year  --useQCDMC -c Mu    --$plot  --template
	done
done

for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				python makePlots_TTGamma.py -y $year  --useQCDMC -c Ele   --$plot --syst $systematics --level $level --template
				python makePlots_TTGamma.py -y $year  --useQCDMC -c Mu    --$plot --syst $systematics --level $level --template
			done
		done
	done
done
#
#
echo "Done making templates for M3 and ChIso"
#
wait

echo "Making M3 control template"

for year in ${YEAR[@]}; do      
	python makePlot_M3Control.py -y $year  --useQCDMC -c Ele   --zeroPhoton  
	python makePlot_M3Control.py -y $year  --useQCDMC -c Mu    --zeroPhoton  
done

for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS[@]}; do
		for level in ${LEVEL[@]}; do
			python makePlot_M3Control.py -y $year  --useQCDMC -c Ele   --zeroPhoton --syst $systematics --level $level 
			python makePlot_M3Control.py -y $year  --useQCDMC -c Mu    --zeroPhoton --syst $systematics --level $level 
		done
	done
done



echo "Done making M3 control templates"
