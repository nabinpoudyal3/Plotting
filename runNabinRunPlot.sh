#!/bin/bash

declare -a YEAR=("2016" "2017" "2018")

for year in ${YEAR[@]}; do

	python makePlots.py -y $year -c Ele --tight            --useQCDMC --makePlotsForSF      
	python makePlots.py -y $year -c Mu  --tight            --useQCDMC --makePlotsForSF

	python makePlots.py -y $year -c Ele --looseCRge4e0     --useQCDMC --makePlotsForSF
	python makePlots.py -y $year -c Mu  --looseCRge4e0     --useQCDMC --makePlotsForSF

done
echo ""
exit 1


for year in ${YEAR[@]}; do

	python makePlots.py -y $year -c Ele --tight            --useQCDMC --makePlotsForSF      
	python makePlots.py -y $year -c Mu  --tight            --useQCDMC --makePlotsForSF

	python makePlots.py -y $year -c Ele --looseCRge2e0     --useQCDMC --makePlotsForSF
	python makePlots.py -y $year -c Mu  --looseCRge2e0     --useQCDMC --makePlotsForSF

	python makePlots.py -y $year -c Ele --looseCRe2e0      --useQCDMC --makePlotsForSF
	python makePlots.py -y $year -c Mu  --looseCRe2e0      --useQCDMC --makePlotsForSF

	python makePlots.py -y $year -c Ele --looseCRe3e0      --useQCDMC --makePlotsForSF
	python makePlots.py -y $year -c Mu  --looseCRe3e0      --useQCDMC --makePlotsForSF

	python makePlots.py -y $year -c Ele --looseCRge4e0     --useQCDMC --makePlotsForSF
	python makePlots.py -y $year -c Mu  --looseCRge4e0     --useQCDMC --makePlotsForSF

	python makePlots.py -y $year -c Ele --looseCRe2e1      --useQCDMC --makePlotsForSF
	python makePlots.py -y $year -c Mu  --looseCRe2e1      --useQCDMC --makePlotsForSF

	python makePlots.py -y $year -c Ele --looseCRe3e1      --useQCDMC --makePlotsForSF
	python makePlots.py -y $year -c Mu  --looseCRe3e1      --useQCDMC --makePlotsForSF

	python makePlots.py -y $year -c Ele --looseCRe2e2      --useQCDMC --makePlotsForSF
	python makePlots.py -y $year -c Mu  --looseCRe2e2      --useQCDMC --makePlotsForSF

	python makePlots.py -y $year -c Ele --looseCRe3ge2     --useQCDMC --makePlotsForSF
	python makePlots.py -y $year -c Mu  --looseCRe3ge2     --useQCDMC --makePlotsForSF
done
wait
echo "All processes done!"


