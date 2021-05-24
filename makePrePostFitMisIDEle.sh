#!/bin/bash

declare -a CONTROLREGION=("--looseCRge2e0" "--looseCRe2e0" "--looseCRe3e0" "--looseCRge4e0" "--looseCRe2e1")
declare -a YEAR=("2016" "2017" "2018")

# declare -a YEAR=("2016")
# declare -a CONTROLREGION=("--looseCRge2e0" "--looseCRe2e0" "--looseCRe3e0" "--looseCRge4e0" "--looseCRe2e1")

set -x 

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
        python makePlots_MisIDE.py -y $year  -c Ele $controlregion  --prefitPlots
        python makePlots_MisIDE.py -y $year  -c Mu  $controlregion  --prefitPlots
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



exit 1

# python makePlots_MisIDE.py -y 2016 -c Ele --looseCRge2e0  --prefitPlots
# python makePlots_MisIDE.py -y 2016 -c Mu  --looseCRge2e0  --prefitPlots
# python makePlots_MisIDE.py -y 2016 -c Ele --looseCRge2e0  --postfitPlots
# python makePlots_MisIDE.py -y 2016 -c Mu  --looseCRge2e0  --postfitPlots
