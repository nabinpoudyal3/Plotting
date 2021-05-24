#!/bin/bash

callTrain()
{
for i in {1..2}; do
echo "***************************************************************************"
echo " $(tput setaf 1) (@@) (  ) (@)  ( )  @@    ()    @     O     @
                     (   )
                 (@@@@)
              (    )

            (@@@)
         ====        ________                ___________
     _D _|  |_______/        \__I_I_____===__|_________|
      |(_)---  |   H\________/ |   |        =|___ ___|      ________________
      /     |  |   H  |  |     |   |         ||_| |_||     _|
     |      |  |   H  |__--------------------| [___] |   =|
     | ________|___H__/__|_____/[][]~\_______|       |   -|
     |/ |   |-----------I_____I [][] []  D   |=======|____|_________________
   __/ =| o |=-O=====O=====O=====O \ ____Y___________|__|___________________
    |/-=|___|=    ||    ||    ||    |_____/~\___/          |_D__D__D_|  |_D_
     \_/      \__/  \__/  \__/  \__/      \_/               \_/   \_/    \_/ $(tput sgr 0)" 
echo "***************************************************************************"
done
}

declare -a YEAR=("2016" "2017" "2018")
declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" )

for controlregion in ${CONTROLREGION[@]}; do
	for year in ${YEAR[@]}; do
		callTrain
		echo "=====>" python makePlots.py -y $year -c Ele --$controlregion  --allPlots     
	    	          python makePlots.py -y $year -c Ele --$controlregion  --allPlots  
		echo "=====>" python makePlots.py -y $year -c Mu  --$controlregion  --allPlots  
		    	      python makePlots.py -y $year -c Mu  --$controlregion  --allPlots  

	done
done
echo ""
exit 1


for year in ${YEAR[@]}; do
	callTrain
	python makePlots.py -y $year -c Ele --tight            --noQCD --allPlots     
	python makePlots.py -y $year -c Mu  --tight            --noQCD --allPlots  
	python makePlots.py -y $year -c Ele --looseCRge4e0     --noQCD --allPlots  
	python makePlots.py -y $year -c Mu  --looseCRge4e0     --noQCD --allPlots  

	python makePlots.py -y $year -c Ele  --looseCRge2e0    --plot phosel_MassEGamma 
	python makePlots.py -y $year -c Mu   --looseCRge2e0    --plot phosel_MassEGamma 
	python makePlots.py -y $year -c Ele  --looseCRge2e0    --plot phosel_MassEGamma --postfitPlots
	python makePlots.py -y $year -c Mu   --looseCRge2e0    --plot phosel_MassEGamma --postfitPlots 

	# python makePlots.py -y $year -c Ele  --looseCRge4e0    --plot phosel_MassEGamma 
	# python makePlots.py -y $year -c Mu   --looseCRge4e0    --plot phosel_MassEGamma 

	# python makePlots.py -y $year -c Ele  --looseCRge4e0    --plot phosel_MassEGamma --postfitPlots
	# python makePlots.py -y $year -c Mu   --looseCRge4e0    --plot phosel_MassEGamma --postfitPlots 
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


