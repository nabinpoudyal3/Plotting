#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")

for year in ${YEAR[@]}; do

	python makePlots.py -y $year -c Ele --tight           --useQCDMC  --makePhotonSplitplots      #eight
	python makePlots.py -y $year -c Mu  --tight           --useQCDMC  --makePhotonSplitplots

	python makePlots.py -y $year -c Ele --looseCRge2e0    --useQCDMC  --makePhotonSplitplots     #all
	python makePlots.py -y $year -c Mu  --looseCRge2e0    --useQCDMC  --makePhotonSplitplots

	python makePlots.py -y $year -c Ele --looseCRe2e0     --useQCDMC  --makePhotonSplitplots    #one
	python makePlots.py -y $year -c Mu  --looseCRe2e0     --useQCDMC  --makePhotonSplitplots

	python makePlots.py -y $year -c Ele --looseCRe3e0     --useQCDMC  --makePhotonSplitplots    #two
	python makePlots.py -y $year -c Mu  --looseCRe3e0     --useQCDMC  --makePhotonSplitplots

	python makePlots.py -y $year -c Ele --looseCRge4e0    --useQCDMC  --makePhotonSplitplots   #three
	python makePlots.py -y $year -c Mu  --looseCRge4e0    --useQCDMC  --makePhotonSplitplots

	python makePlots.py -y $year -c Ele --looseCRe2e1     --useQCDMC  --makePhotonSplitplots   #four
	python makePlots.py -y $year -c Mu  --looseCRe2e1     --useQCDMC  --makePhotonSplitplots

	python makePlots.py -y $year -c Ele --looseCRe3e1     --useQCDMC  --makePhotonSplitplots  #five 
	python makePlots.py -y $year -c Mu  --looseCRe3e1     --useQCDMC  --makePhotonSplitplots

	python makePlots.py -y $year -c Ele --looseCRe2e2     --useQCDMC  --makePhotonSplitplots  #six
	python makePlots.py -y $year -c Mu  --looseCRe2e2     --useQCDMC  --makePhotonSplitplots

	python makePlots.py -y $year -c Ele --looseCRe3ge2    --useQCDMC  --makePhotonSplitplots  #seven
	python makePlots.py -y $year -c Mu  --looseCRe3ge2    --useQCDMC  --makePhotonSplitplots
done
wait
echo "All processes done!"


