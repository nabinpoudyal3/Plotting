#!/bin/bash

###IMPORTANT:
# isr, fsr, q2, JECTotal are wrong.
# always keep misIDE at last in array

declare -a YEAR=("2016" "2017" "2018")
# declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "prefireEcal" "JER" "misIDE")
declare -a SYSTEMATICS=("JECTotal")

declare -a LEVEL=("up" "down")

declare -a PLOT1=("ChIsoPlot")
declare -a PLOT2=("M3Plot" "btag0")

# for plot in ${PLOT1[@]}; do
# 	for year in ${YEAR[@]}; do   
# 		echo "===> python makePlots_TTGamma.py  -y $year   -c Ele   --$plot  --template --datadriven "    
# 		           python makePlots_TTGamma.py  -y $year   -c Ele   --$plot  --template --datadriven  
# 		echo "===> python makePlots_TTGamma.py  -y $year   -c Mu    --$plot  --template --datadriven " 
# 		           python makePlots_TTGamma.py  -y $year   -c Mu    --$plot  --template --datadriven  
# 	done
# done

for plot in ${PLOT1[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				echo "===> python makePlots_TTGamma.py  -y $year   -c Ele   --$plot --syst $systematics --level $level --template --datadriven " 
				           python makePlots_TTGamma.py  -y $year   -c Ele   --$plot --syst $systematics --level $level --template --datadriven 
				echo "===> python makePlots_TTGamma.py  -y $year   -c Mu    --$plot --syst $systematics --level $level --template --datadriven " 
				           python makePlots_TTGamma.py  -y $year   -c Mu    --$plot --syst $systematics --level $level --template --datadriven  
			done
		done
	done
done

# for plot in ${PLOT2[@]}; do
# 	for year in ${YEAR[@]}; do   
# 		echo "===> python makePlots_TTGamma.py  -y $year   -c Ele   --$plot  --template"    
# 		           python makePlots_TTGamma.py  -y $year   -c Ele   --$plot  --template 
# 		echo "===> python makePlots_TTGamma.py  -y $year   -c Mu    --$plot  --template" 
# 		           python makePlots_TTGamma.py  -y $year   -c Mu    --$plot  --template 
# 	done
# done

for plot in ${PLOT2[@]}; do
	for year in ${YEAR[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				echo "===> python makePlots_TTGamma.py  -y $year   -c Ele   --$plot --syst $systematics --level $level --template" 
				           python makePlots_TTGamma.py  -y $year   -c Ele   --$plot --syst $systematics --level $level --template 
				echo "===> python makePlots_TTGamma.py  -y $year   -c Mu    --$plot --syst $systematics --level $level --template" 
				           python makePlots_TTGamma.py  -y $year   -c Mu    --$plot --syst $systematics --level $level --template 
			done
		done
	done
done

# for year in ${YEAR[@]}; do    
# 	echo "===> python makePlot_M3Control.py  -y $year   -c Ele   --zeroPhoton  --template "  #no QCDMC means using DD QCD
# 	           python makePlot_M3Control.py  -y $year   -c Ele   --zeroPhoton  --template 
# 	echo "===> python makePlot_M3Control.py  -y $year   -c Mu    --zeroPhoton  --template "
# 	           python makePlot_M3Control.py  -y $year   -c Mu    --zeroPhoton  --template 
# done

# unset 'SYSTEMATICS[${#SYSTEMATICS[@]}-1]'
for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS[@]}; do
		for level in ${LEVEL[@]}; do
			echo "===> python makePlot_M3Control.py  -y $year   -c Ele   --zeroPhoton --syst $systematics --level $level --template" 
			           python makePlot_M3Control.py  -y $year   -c Ele   --zeroPhoton --syst $systematics --level $level --template 
			echo "===> python makePlot_M3Control.py  -y $year   -c Mu    --zeroPhoton --syst $systematics --level $level --template" 
			           python makePlot_M3Control.py  -y $year   -c Mu    --zeroPhoton --syst $systematics --level $level --template 
		done
	done
done
echo "Done"
