declare -a StringArray=("tight" "looseCRge2e0" "looseCRge2ge0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )

for val in ${StringArray[@]}; do
    python makePlots_ZJets.py -c DiMu   -y 2016 --useQCDMC --postfitPlots --$val &
    python makePlots_ZJets.py -c DiEle  -y 2016 --useQCDMC --postfitPlots --$val &

    python makePlots_ZJets.py -c DiMu   -y 2017 --useQCDMC --postfitPlots --$val &
    python makePlots_ZJets.py -c DiEle  -y 2017 --useQCDMC --postfitPlots --$val &

    python makePlots_ZJets.py -c DiMu   -y 2018 --useQCDMC --postfitPlots --$val &
    python makePlots_ZJets.py -c DiEle  -y 2018 --useQCDMC --postfitPlots --$val &
    
done
wait 
echo "Done postfit"
