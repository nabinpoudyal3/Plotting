

#!/bin/bash

declare -a StringArray=("tight" "looseCRge2e0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
# declare -a StringArray=("looseCRge2e0")

for val in ${StringArray[@]}; do
	echo "===>" python makePlots.py -c DiMu   -y 2016 --useQCDMC --dilepmassPlots  --prefitPlots --$val
    			python makePlots.py -c DiMu   -y 2016 --useQCDMC --dilepmassPlots  --prefitPlots --$val 
	echo "===>" python makePlots.py -c DiEle  -y 2016 --useQCDMC --dilepmassPlots  --prefitPlots --$val
    			python makePlots.py -c DiEle  -y 2016 --useQCDMC --dilepmassPlots  --prefitPlots --$val 
	echo "===>" python makePlots.py -c DiMu   -y 2017 --useQCDMC --dilepmassPlots  --prefitPlots --$val
    			python makePlots.py -c DiMu   -y 2017 --useQCDMC --dilepmassPlots  --prefitPlots --$val 
	echo "===>" python makePlots.py -c DiEle  -y 2017 --useQCDMC --dilepmassPlots  --prefitPlots --$val
    			python makePlots.py -c DiEle  -y 2017 --useQCDMC --dilepmassPlots  --prefitPlots --$val 
	echo "===>" python makePlots.py -c DiMu   -y 2018 --useQCDMC --dilepmassPlots  --prefitPlots --$val
    			python makePlots.py -c DiMu   -y 2018 --useQCDMC --dilepmassPlots  --prefitPlots --$val 
	echo "===>" python makePlots.py -c DiEle  -y 2018 --useQCDMC --dilepmassPlots  --prefitPlots --$val
    			python makePlots.py -c DiEle  -y 2018 --useQCDMC --dilepmassPlots  --prefitPlots --$val 
   
done
wait
echo "Done Prefit!" 

exit 1

for val in ${StringArray[@]}; do
	echo "===>" python makePlots.py -c DiMu   -y 2016 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
    			python makePlots.py -c DiMu   -y 2016 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
	echo "===>" python makePlots.py -c DiEle  -y 2016 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
   				python makePlots.py -c DiEle  -y 2016 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
	echo "===>" python makePlots.py -c DiMu   -y 2017 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
    			python makePlots.py -c DiMu   -y 2017 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
	echo "===>" python makePlots.py -c DiEle  -y 2017 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
    			python makePlots.py -c DiEle  -y 2017 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
	echo "===>" python makePlots.py -c DiMu   -y 2018 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
    			python makePlots.py -c DiMu   -y 2018 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
	echo "===>" python makePlots.py -c DiEle  -y 2018 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
    			python makePlots.py -c DiEle  -y 2018 --useQCDMC  --dilepmassPlots  --postfitPlots --$val 
    
done
wait 
echo "Done postfit"

exit 1















python makePlots.py -y $1 -c DiEle --tight           --useQCDMC  --dilepmassPlots &      
python makePlots.py -y $1 -c DiMu  --tight           --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRge2ge0   --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRge2ge0   --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRge2e0    --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRge2e0    --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe2e0     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe2e0     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe3e0     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe3e0     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRge4e0    --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRge4e0    --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe2e1     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe2e1     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe3e1     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe3e1     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe2e2     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe2e2     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe3ge2   --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe3ge2   --useQCDMC  --dilepmassPlots &
