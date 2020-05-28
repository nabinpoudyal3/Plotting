#!/bin/bash

#declare -a YEAR=("2016")
declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Q2" "isr" "fsr" "misIDE")
#declare -a SYSTEMATICS=("misIDE")
declare -a LEVEL=("up" "down")
declare -a PLOT=("M3Plot" "ChIsoPlot" "btag0")
#declare -a PLOT=("btag0")
# "zeroPhoton")

for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do      
		python makePlots_TTGamma.py -y $year   -c Ele   --$plot  --template
		python makePlots_TTGamma.py -y $year   -c Mu    --$plot  --template
	done
done
##
for plot in ${PLOT[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				python makePlots_TTGamma.py -y $year   -c Ele   --$plot --syst $systematics --level $level --template
				python makePlots_TTGamma.py -y $year   -c Mu    --$plot --syst $systematics --level $level --template
			done
		done
	done
done
###
##
echo "Done making templates for M3 and ChIso"
##
wait

echo "Making M3 control template"

for year in ${YEAR[@]}; do      
	python makePlot_M3Control.py -y $year   -c Ele   --zeroPhoton  --template 
	python makePlot_M3Control.py -y $year   -c Mu    --zeroPhoton  --template 
done

unset 'SYSTEMATICS[${#SYSTEMATICS[@]}-1]'
for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS[@]}; do
		for level in ${LEVEL[@]}; do
			python makePlot_M3Control.py -y $year   -c Ele   --zeroPhoton --syst $systematics --level $level --template 
			python makePlot_M3Control.py -y $year   -c Mu    --zeroPhoton --syst $systematics --level $level --template 
		done
	done
done



echo "Done making M3 control templates"

#to remove QCD and GJets,  and to use data driven use --useQCDCR for now. 
