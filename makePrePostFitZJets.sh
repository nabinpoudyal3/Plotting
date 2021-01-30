#!/bin/bash

# declare -a StringArray=("tight" "looseCRge2e0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
declare -a StringArray=("looseCRge2e0")

for val in ${StringArray[@]}; do
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2016 --useQCDMC --prefitPlots --$val
    			python makePlots_ZJets.py -c DiMu   -y 2016 --useQCDMC --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2016 --useQCDMC --prefitPlots --$val
    			python makePlots_ZJets.py -c DiEle  -y 2016 --useQCDMC --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2017 --useQCDMC --prefitPlots --$val
    			python makePlots_ZJets.py -c DiMu   -y 2017 --useQCDMC --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2017 --useQCDMC --prefitPlots --$val
    			python makePlots_ZJets.py -c DiEle  -y 2017 --useQCDMC --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2018 --useQCDMC --prefitPlots --$val
    			python makePlots_ZJets.py -c DiMu   -y 2018 --useQCDMC --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2018 --useQCDMC --prefitPlots --$val
    			python makePlots_ZJets.py -c DiEle  -y 2018 --useQCDMC --prefitPlots --$val 
   
done
wait
echo "Done Prefit!" 


for val in ${StringArray[@]}; do
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2016 --useQCDMC --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiMu   -y 2016 --useQCDMC --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2016 --useQCDMC --postfitPlots --$val 
   				python makePlots_ZJets.py -c DiEle  -y 2016 --useQCDMC --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2017 --useQCDMC --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiMu   -y 2017 --useQCDMC --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2017 --useQCDMC --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiEle  -y 2017 --useQCDMC --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2018 --useQCDMC --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiMu   -y 2018 --useQCDMC --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2018 --useQCDMC --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiEle  -y 2018 --useQCDMC --postfitPlots --$val 
    
done
wait 
echo "Done postfit"

exit 1

python makePlots_ZJets.py -c DiMu   -y 2016 --useQCDMC --prefitPlots  --looseCRge2e0 
python makePlots_ZJets.py -c DiMu   -y 2016 --useQCDMC --postfitPlots --looseCRge2e0 





exit 1
