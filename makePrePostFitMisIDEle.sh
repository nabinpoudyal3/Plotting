#!/bin/bash


python makePlots_MisIDE.py -c Mu   -y 2016 --looseCRge2e0  --useQCDMC
python makePlots_MisIDE.py -c Ele  -y 2016 --looseCRge2e0  --useQCDMC

python makePlots_MisIDE.py -c Mu   -y 2017 --looseCRge2e0  --useQCDMC
python makePlots_MisIDE.py -c Ele  -y 2017 --looseCRge2e0  --useQCDMC

python makePlots_MisIDE.py -c Mu   -y 2018 --looseCRge2e0  --useQCDMC
python makePlots_MisIDE.py -c Ele  -y 2018 --looseCRge2e0  --useQCDMC

echo "Done prefit for MisIDEle plots!" 


wait

python makePlots_MisIDE.py -c Mu   -y 2016 --looseCRge2e0  --postfitPlots --useQCDMC
python makePlots_MisIDE.py -c Ele  -y 2016 --looseCRge2e0  --postfitPlots --useQCDMC

python makePlots_MisIDE.py -c Mu   -y 2017 --looseCRge2e0  --postfitPlots --useQCDMC
python makePlots_MisIDE.py -c Ele  -y 2017 --looseCRge2e0  --postfitPlots --useQCDMC

python makePlots_MisIDE.py -c Mu   -y 2018 --looseCRge2e0  --postfitPlots --useQCDMC
python makePlots_MisIDE.py -c Ele  -y 2018 --looseCRge2e0  --postfitPlots --useQCDMC

echo "Done postfit for MisIDEle plots!" 




wait

python makePlots_MisIDE.py -c Mu   -y 2016 --looseCRge2e0  
python makePlots_MisIDE.py -c Ele  -y 2016 --looseCRge2e0  

python makePlots_MisIDE.py -c Mu   -y 2017 --looseCRge2e0  
python makePlots_MisIDE.py -c Ele  -y 2017 --looseCRge2e0  

python makePlots_MisIDE.py -c Mu   -y 2018 --looseCRge2e0  
python makePlots_MisIDE.py -c Ele  -y 2018 --looseCRge2e0  

echo "Done prefit for MisIDEle plots!" 


wait

python makePlots_MisIDE.py -c Mu   -y 2016 --looseCRge2e0  --postfitPlots 
python makePlots_MisIDE.py -c Ele  -y 2016 --looseCRge2e0  --postfitPlots 

python makePlots_MisIDE.py -c Mu   -y 2017 --looseCRge2e0  --postfitPlots 
python makePlots_MisIDE.py -c Ele  -y 2017 --looseCRge2e0  --postfitPlots 

python makePlots_MisIDE.py -c Mu   -y 2018 --looseCRge2e0  --postfitPlots 
python makePlots_MisIDE.py -c Ele  -y 2018 --looseCRge2e0  --postfitPlots 

echo "Done postfit for MisIDEle plots!"

#declare -a StringArray=("looseCRge2e0" "looseCRge4e0" "looseCRe2e1" "looseCRe2e0" "looseCRe3e0" )
