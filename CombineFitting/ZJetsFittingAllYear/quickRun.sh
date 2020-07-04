#!/bin/bash
declare -a CONTROLREGION=("CR123" "CR1" "CR2" "CR3" "CR4" "CR5" "CR6" "CR7" "SR8" )
declare -a YEAR=("2016" "2017" "2018")
#declare -a CONTROLREGION=("CR1")
#declare -a YEAR=("2016")

for year in ${YEAR[@]}; do
	for controlregion in ${CONTROLREGION[@]}; do
		text2workspace.py datacard_"$controlregion"_"$year".txt
		combine -M FitDiagnostics -n "$controlregion"_"$year" datacard_"$controlregion"_"$year".root --plots --saveNLL --robustFit=1 -s 314159 \
		--saveShapes --saveWithUncertainties --saveNormalizations --rMin=-1 --rMax=5 --skipBOnlyFit \
		-v0
	done
done
