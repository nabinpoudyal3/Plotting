#!/bin/bash

declare -a StringArray=("tight" "looseCRge2e0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
for val in ${StringArray[@]}; do
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2016 --noQCD --prefitPlots --$val
    			python makePlots_ZJets.py -c DiMu   -y 2016 --noQCD --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2016 --noQCD --prefitPlots --$val
    			python makePlots_ZJets.py -c DiEle  -y 2016 --noQCD --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2017 --noQCD --prefitPlots --$val
    			python makePlots_ZJets.py -c DiMu   -y 2017 --noQCD --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2017 --noQCD --prefitPlots --$val
    			python makePlots_ZJets.py -c DiEle  -y 2017 --noQCD --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2018 --noQCD --prefitPlots --$val
    			python makePlots_ZJets.py -c DiMu   -y 2018 --noQCD --prefitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2018 --noQCD --prefitPlots --$val
    			python makePlots_ZJets.py -c DiEle  -y 2018 --noQCD --prefitPlots --$val 
   
done
wait
echo "Done Prefit!" 


for val in ${StringArray[@]}; do
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2016 --noQCD --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiMu   -y 2016 --noQCD --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2016 --noQCD --postfitPlots --$val 
   				python makePlots_ZJets.py -c DiEle  -y 2016 --noQCD --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2017 --noQCD --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiMu   -y 2017 --noQCD --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2017 --noQCD --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiEle  -y 2017 --noQCD --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiMu   -y 2018 --noQCD --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiMu   -y 2018 --noQCD --postfitPlots --$val 
	echo "===>" python makePlots_ZJets.py -c DiEle  -y 2018 --noQCD --postfitPlots --$val 
    			python makePlots_ZJets.py -c DiEle  -y 2018 --noQCD --postfitPlots --$val 
    
done
wait 
echo "Done postfit"
