#!/bin/bash

###IMPORTANT:
# isr, fsr and q2 are wrong.
# always keep misIDE at last in array

#declare -a YEAR=("2016")
declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "prefireEcal" "JER" "JECTotal" "misIDE")
#declare -a SYSTEMATICS=("Q2") # "isr" "fsr") 
declare -a LEVEL=("up" "down")
declare -a PLOT2=("M3Plot" "btag0")
declare -a PLOT1=("ChIsoPlot")
# "zeroPhoton")

for plot in ${PLOT1[@]}; do
	for year in ${YEAR[@]}; do   
		echo "===> python makePlots_TTGamma.py --noQCD -y $year   -c Ele   --$plot  --template --datadriven "    
		           python makePlots_TTGamma.py --noQCD -y $year   -c Ele   --$plot  --template   
		echo "===> python makePlots_TTGamma.py --noQCD -y $year   -c Mu    --$plot  --template --datadriven " 
		           python makePlots_TTGamma.py --noQCD -y $year   -c Mu    --$plot  --template   
	done
done
###
for plot in ${PLOT1[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				echo "===> python makePlots_TTGamma.py --noQCD -y $year   -c Ele   --$plot --syst $systematics --level $level --template --datadriven " 
				           python makePlots_TTGamma.py --noQCD -y $year   -c Ele   --$plot --syst $systematics --level $level --template   
				echo "===> python makePlots_TTGamma.py --noQCD -y $year   -c Mu    --$plot --syst $systematics --level $level --template --datadriven " 
				           python makePlots_TTGamma.py --noQCD -y $year   -c Mu    --$plot --syst $systematics --level $level --template   
			done
		done
	done
done


for plot in ${PLOT2[@]}; do
	for year in ${YEAR[@]}; do   
		echo "===> python makePlots_TTGamma.py --noQCD -y $year   -c Ele   --$plot  --template"    
		           python makePlots_TTGamma.py --noQCD -y $year   -c Ele   --$plot  --template 
		echo "===> python makePlots_TTGamma.py --noQCD -y $year   -c Mu    --$plot  --template" 
		           python makePlots_TTGamma.py --noQCD -y $year   -c Mu    --$plot  --template 
	done
done
###
for plot in ${PLOT2[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				echo "===> python makePlots_TTGamma.py --noQCD -y $year   -c Ele   --$plot --syst $systematics --level $level --template" 
				           python makePlots_TTGamma.py --noQCD -y $year   -c Ele   --$plot --syst $systematics --level $level --template 
				echo "===> python makePlots_TTGamma.py --noQCD -y $year   -c Mu    --$plot --syst $systematics --level $level --template" 
				           python makePlots_TTGamma.py --noQCD -y $year   -c Mu    --$plot --syst $systematics --level $level --template 
			done
		done
	done
done
####
###
echo "Done making templates for M3, ChIso, and 0btag!!!!!!"
##
#wait

#exit 1

echo "exiting without making 0 photon templates(nominal and syst)!!!!!!!!"

echo "Making M3 control template"
for year in ${YEAR[@]}; do    
	echo "===> python makePlot_M3Control.py --noQCD -y $year   -c Ele   --zeroPhoton  --template "  #no QCDMC means using DD QCD
	           python makePlot_M3Control.py --noQCD -y $year   -c Ele   --zeroPhoton  --template 
	echo "===> python makePlot_M3Control.py --noQCD -y $year   -c Mu    --zeroPhoton  --template "
	           python makePlot_M3Control.py --noQCD -y $year   -c Mu    --zeroPhoton  --template 
done

unset 'SYSTEMATICS[${#SYSTEMATICS[@]}-1]'
for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS[@]}; do
		for level in ${LEVEL[@]}; do
			echo "===> python makePlot_M3Control.py --noQCD -y $year   -c Ele   --zeroPhoton --syst $systematics --level $level --template" 
			           python makePlot_M3Control.py --noQCD -y $year   -c Ele   --zeroPhoton --syst $systematics --level $level --template 
			echo "===> python makePlot_M3Control.py --noQCD -y $year   -c Mu    --zeroPhoton --syst $systematics --level $level --template" 
			           python makePlot_M3Control.py --noQCD -y $year   -c Mu    --zeroPhoton --syst $systematics --level $level --template 
		done
	done
done
echo "Done making M3 control templates"





