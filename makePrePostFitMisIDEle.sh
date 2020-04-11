#!/bin/bash


#python makePlots_MisIDE.py -c Mu   -y 2016 --looseCRge2e0  --useQCDMC
#python makePlots_MisIDE.py -c Ele  -y 2016 --looseCRge2e0  --useQCDMC

#python makePlots_MisIDE.py -c Mu   -y 2017 --looseCRge2e0  --useQCDMC
#python makePlots_MisIDE.py -c Ele  -y 2017 --looseCRge2e0  --useQCDMC

#python makePlots_MisIDE.py -c Mu   -y 2018 --looseCRge2e0  --useQCDMC
#python makePlots_MisIDE.py -c Ele  -y 2018 --looseCRge2e0  --useQCDMC

#echo "Done prefit for MisIDEle plots!" 


#wait

#python makePlots_MisIDE.py -c Mu   -y 2016 --looseCRge2e0  --postfitPlots --useQCDMC
#python makePlots_MisIDE.py -c Ele  -y 2016 --looseCRge2e0  --postfitPlots --useQCDMC

#python makePlots_MisIDE.py -c Mu   -y 2017 --looseCRge2e0  --postfitPlots --useQCDMC
#python makePlots_MisIDE.py -c Ele  -y 2017 --looseCRge2e0  --postfitPlots --useQCDMC

#python makePlots_MisIDE.py -c Mu   -y 2018 --looseCRge2e0  --postfitPlots --useQCDMC
#python makePlots_MisIDE.py -c Ele  -y 2018 --looseCRge2e0  --postfitPlots --useQCDMC

#echo "Done postfit for MisIDEle plots!" 


declare -a CONTROLREGION=("--looseCRge2e0" "--looseCRe2e0" "--looseCRe3e0" "--looseCRge4e0")
declare -a YEAR=("2016" "2017" "2018")

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		python makePlots_MisIDE.py -y $year  -c Ele $controlregion  
		python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  
	done
done
wait

echo "Done prefit for MisIDEle plots!" 

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --postfitPlots
		python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --postfitPlots
	done
done
wait
 
echo "Done prefit for MisIDEle plots!" 


