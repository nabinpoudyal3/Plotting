
declare -a CHANNEL=("ele" "mu" "both")

year=$1
myAsimovFit=" -t -1 --expectSignal 1 "

for channel in ${CHANNEL[@]}; do
	plotImpacts.py -i impacts_toy_"$channel"_"$1".json  -t rename.json -o impacts_toy_"$channel"_"$1"  --label-size 0.035 --left-margin 0.45
	plotImpacts.py -i impacts_data_"$channel"_"$1".json -t rename.json -o impacts_data_"$channel"_"$1" --label-size 0.035 --left-margin 0.45
done


exit 1
