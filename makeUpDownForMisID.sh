#!/bin/bash

declare -a CONTROLREGION=("looseCRge2e0" "looseCRge4e0" "looseCRe3e0" "looseCRe2e0" )
declare -a YEAR=("2016" "2017" "2018")

#declare -a CONTROLREGION=("looseCRge2e0")
#declare -a YEAR=("2016")

for year in ${YEAR[@]}; do
        # rm -rf M3ChIso_tightplots_"$yr"/*.pdf # delete old pdf files before merging new ones
        for controlregion in ${CONTROLREGION[@]}; do
                echo "===> python makePlots_SystUpDownMisID.py -y $year --$controlregion" 
                python makePlots_SystUpDownMisID.py -y $year  --$controlregion

        done
done

