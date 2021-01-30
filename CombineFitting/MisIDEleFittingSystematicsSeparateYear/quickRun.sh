
#!/bin/bash

##$1= control region with year
declare -a CONTROLREGION=("CR123" "CR1" "CR2" "CR3")
declare -a YEAR=("2016" "2018")
#declare -a YEAR=("2018")
rMin=0
rMax=5
for year in ${YEAR[@]}; do
	for controlregion in ${CONTROLREGION[@]}; do
		text2workspace.py datacard_"$controlregion"_"$year".txt
		combine -M MultiDimFit datacard_"$controlregion"_"$year".root  -s 314159  --rMin $rMin --rMax $rMax --algo grid --points 300 -n .Main
#python plot1DScan.py higgsCombine.Main.MultiDimFit.mH120.314159.root -o single_scan
		combine -M MultiDimFit datacard_"$controlregion"_"$year".root -n .snapshot -s 314159  --rMin $rMin --rMax $rMax --saveWorkspace
		combine -M MultiDimFit higgsCombine.snapshot.MultiDimFit.mH120.314159.root -s 314159  -n .freezeAll --rMin $rMin --rMax $rMax --algo grid --points 300 --freezeNuisanceGroups mySyst --snapshotName MultiDimFit
		python plot1DScan.py  higgsCombine.Main.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_"$controlregion"_"$year"
##
#freezing nuisance parameter gives better result
	done
done

exit 1
--X-rtd MINIMIZER_analytic 