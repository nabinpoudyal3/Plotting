
declare -a CONTROLREGION=("CR123" "CR1" "CR2" "CR3" )
declare -a YEAR=("2016" "2017" "2018")

myAsimovFit=" -t -1 --expectSignal 1 "

for year in ${YEAR[@]}; do
for controlregion in ${CONTROLREGION[@]}; do

# plotImpacts.py -i impacts_toy_"$controlregion"_"$year".json  -t rename.json -o impacts_toy_"$controlregion"_"$year"  --label-size 0.035
# plotImpacts.py -i impacts_data_"$controlregion"_"$year".json -t rename.json -o impacts_data_"$controlregion"_"$year" --label-size 0.035 

python plot1DScan.py --translate rename.json higgsCombine.Asimov_Main_"$controlregion"_"$year"_ZGammaBkgPhotonSF.MultiDimFit.mH120.314159.root --POI ZGammaBkgPhotonSF -o single_scan__"$controlregion"_"$year"_ZGammaBkgPhotonSF
python plot1DScan.py --translate rename.json higgsCombine.Asimov_Main_"$controlregion"_"$year"_WGammaBkgPhotonSF.MultiDimFit.mH120.314159.root --POI WGammaBkgPhotonSF -o single_scan__"$controlregion"_"$year"_WGammaBkgPhotonSF
python plot1DScan.py --translate rename.json higgsCombine.Asimov_Main_"$controlregion"_"$year".MultiDimFit.mH120.314159.root -o single_scan__"$controlregion"_"$year"_r
python plot1DScan.py --translate rename.json higgsCombine.total_Toy.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll_Toy.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_toy_"$controlregion"_"$year" 
python plot1DScan.py --translate rename.json higgsCombine.total_Data.MultiDimFit.mH120.314159.root --others 'higgsCombine.freezeAll_Data.MultiDimFit.mH120.314159.root:Stat:2' --breakdown Syst,Stat -o freeze_data_"$controlregion"_"$year" 

done
done


exit 1





