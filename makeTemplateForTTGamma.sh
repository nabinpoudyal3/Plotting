#!/bin/bash

###IMPORTANT:
# always keep misIDE at last in array

# declare -a YEAR=("2016" "2017" "2018")
declare -a YEAR=("2017")
declare -a SYSTEMATICS1=("prefireEcal" "BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Pdf" "isr" "fsr" "JECTotal1" "JER1" "Q2" "elesmear" "phosmear" "elescale" "phoscale" "misIDE")
declare -a SYSTEMATICS0=("prefireEcal" "BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Pdf" "isr" "fsr" "JECTotal0" "JER0" "Q2" "elesmear" "phosmear" "elescale" "phoscale")
# declare -a SYSTEMATICS=(              "BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Pdf" "isr" "fsr" "JECTotal" "JER" "Q2" "misIDE")

# declare -a SYSTEMATICS1=("misIDE")
declare -a LEVEL=("up" "down")

set -x 
################################################

for year in ${YEAR[@]}; do   
	python makePlots_TTGamma.py  -y $year   -c Ele   --ChIsoPlot  --template  --datadriven
	python makePlots_TTGamma.py  -y $year   -c Mu    --ChIsoPlot  --template  --datadriven
done

for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS1[@]}; do
		for level in ${LEVEL[@]}; do
			python makePlots_TTGamma.py  -y $year   -c Ele   --ChIsoPlot --syst $systematics --level $level --template --datadriven
			python makePlots_TTGamma.py  -y $year   -c Mu    --ChIsoPlot --syst $systematics --level $level --template --datadriven
		done
	done
done

####################################### JUST THE DD SHAPE SYSTEMATICS

for year in ${YEAR[@]}; do   
	python makePlots_TTGamma_DD_template.py  -y $year   -c Ele   --ChIsoPlot  --datadriven
	python makePlots_TTGamma_DD_template.py  -y $year   -c Mu    --ChIsoPlot  --datadriven
done

# ###################################

for year in ${YEAR[@]}; do   
	python makePlots_TTGamma.py  -y $year   -c Ele   --M3Plot  --template 
	python makePlots_TTGamma.py  -y $year   -c Mu    --M3Plot  --template 
done
for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS1[@]}; do
		for level in ${LEVEL[@]}; do
			python makePlots_TTGamma.py  -y $year   -c Ele   --M3Plot --syst $systematics --level $level --template 
			python makePlots_TTGamma.py  -y $year   -c Mu    --M3Plot --syst $systematics --level $level --template 
		done
	done
done

###################################

for year in ${YEAR[@]}; do   
	python makePlots_TTGamma.py  -y $year   -c Ele   --btag0  --template 
	python makePlots_TTGamma.py  -y $year   -c Mu    --btag0  --template 
done
for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS1[@]}; do
		for level in ${LEVEL[@]}; do
			python makePlots_TTGamma.py  -y $year   -c Ele   --btag0 --syst $systematics --level $level --template 
			python makePlots_TTGamma.py  -y $year   -c Mu    --btag0 --syst $systematics --level $level --template 
		done
	done
done

######################################

for year in ${YEAR[@]}; do    
	python makePlot_M3Control.py  -y $year   -c Ele   --zeroPhoton  --template 
	python makePlot_M3Control.py  -y $year   -c Mu    --zeroPhoton  --template 
done
unset 'SYSTEMATICS[${#SYSTEMATICS[@]}-1]'
for year in ${YEAR[@]}; do
	for systematics in ${SYSTEMATICS0[@]}; do
		for level in ${LEVEL[@]}; do
			python makePlot_M3Control.py  -y $year   -c Ele   --zeroPhoton --syst $systematics --level $level --template 
			python makePlot_M3Control.py  -y $year   -c Mu    --zeroPhoton --syst $systematics --level $level --template 
		done
	done
done
echo "Done"

#########CHECK THIS ONE


### To create shape distribution in different ChIso cuts for ChIso DD template uncertainty
python makePlots_TTGamma_DD.py -y 2016 -c Ele --ChIsoPlot --datadriven
python makePlots_TTGamma_DD.py -y 2016 -c Mu  --ChIsoPlot --datadriven
python makePlots_TTGamma_DD.py -y 2017 -c Ele --ChIsoPlot --datadriven
python makePlots_TTGamma_DD.py -y 2017 -c Mu  --ChIsoPlot --datadriven
python makePlots_TTGamma_DD.py -y 2018 -c Ele --ChIsoPlot --datadriven
python makePlots_TTGamma_DD.py -y 2018 -c Mu  --ChIsoPlot --datadriven


####### make template for Tune
for year in ${YEAR[@]}; do
python makePlots_TTGamma_1photon_Tune.py -y $year -c Ele --ChIsoPlot --syst Tune --level down --template --datadriven
python makePlots_TTGamma_1photon_Tune.py -y $year -c Ele --ChIsoPlot --syst Tune --level up   --template --datadriven
python makePlots_TTGamma_1photon_Tune.py -y $year -c Mu  --ChIsoPlot --syst Tune --level down --template --datadriven
python makePlots_TTGamma_1photon_Tune.py -y $year -c Mu  --ChIsoPlot --syst Tune --level up   --template --datadriven
done

for year in ${YEAR[@]}; do
for p in M3Plot; do
python makePlots_TTGamma_1photon_Tune.py -y $year -c Ele --$p --syst Tune --level down --template 
python makePlots_TTGamma_1photon_Tune.py -y $year -c Ele --$p --syst Tune --level up   --template 
python makePlots_TTGamma_1photon_Tune.py -y $year -c Mu  --$p --syst Tune --level down --template 
python makePlots_TTGamma_1photon_Tune.py -y $year -c Mu  --$p --syst Tune --level up   --template 
done
done

for year in ${YEAR[@]}; do
for p in btag0; do
python makePlots_TTGamma_1photon_Tune.py -y $year -c Ele --$p --syst Tune --level down --template 
python makePlots_TTGamma_1photon_Tune.py -y $year -c Ele --$p --syst Tune --level up   --template 
python makePlots_TTGamma_1photon_Tune.py -y $year -c Mu  --$p --syst Tune --level down --template 
python makePlots_TTGamma_1photon_Tune.py -y $year -c Mu  --$p --syst Tune --level up   --template 
done
done


for year in ${YEAR[@]}; do
python makePlots_TTGamma_0photon_Tune.py -y $year -c Ele --zeroPhoton --syst Tune --level down --template 
python makePlots_TTGamma_0photon_Tune.py -y $year -c Ele --zeroPhoton --syst Tune --level up   --template 
python makePlots_TTGamma_0photon_Tune.py -y $year -c Mu  --zeroPhoton --syst Tune --level down --template 
python makePlots_TTGamma_0photon_Tune.py -y $year -c Mu  --zeroPhoton --syst Tune --level up   --template 
done

# # make template for CR1, CR2. erdOn

for year in 2016 2017 2018; do
# for year in 2016; do
for channel in Ele Mu; do
python makePlots_SystematicTemplate.py -y $year -c $channel --M3Plot
python makePlots_SystematicTemplate.py -y $year -c $channel --ChIsoPlot
python makePlots_SystematicTemplate.py -y $year -c $channel --btag0
python makePlots_SystematicTemplate.py -y $year -c $channel --zeroPhoton
done
done






exit 1

# ./makeTemplateForTTGamma.sh > /dev/null; ./makeTemplateForTTGamma_Additional.sh >/dev/null



# rootprint -D hist ttgamma_tightplots_ele_2016/ttgamma_Prefit.root:M3/isolatedTTGamma/nominal
# rootprint -D hist ttgamma_tightplots_ele_2016/ttgamma_Prefit.root:M3/isolatedTTGamma/elescaleUp
# rootprint -D hist ttgamma_tightplots_ele_2016/ttgamma_Prefit.root:M3/isolatedTTGamma/phoscaleUp
# rootprint -D hist ttgamma_tightplots_ele_2016/ttgamma_Prefit.root:M3/isolatedTTGamma/phosmearUp
# rootprint -D hist ttgamma_tightplots_ele_2016/ttgamma_Prefit.root:M3/isolatedTTGamma/elesmearUp

# rootprint -D hist ttgamma_tightplots_ele_2016/ttgamma_Prefit.root:M3/isolatedTTGamma/JER0Up
# rootprint -D hist ttgamma_tightplots_ele_2016/ttgamma_Prefit.root:M3/isolatedTTGamma/JER1Up

# rootprint -D hist ttgamma_tightplots_ele_2016/ttgamma_Prefit.root:M3/isolatedTTGamma/JECTotal0Up
# rootprint -D hist ttgamma_tightplots_ele_2016/ttgamma_Prefit.root:M3/isolatedTTGamma/JECTotal1Up


# subl -n \
# makePlots_TTGamma.py \
# makePlots_TTGamma_DD_template.py \
# makePlot_M3Control.py \
# makePlots_TTGamma_DD.py \
# makePlots_TTGamma_1photon_Tune.py \
# makePlots_TTGamma_0photon_Tune.py \
# makePlots_SystematicTemplate.py


# rm -rf ttgamma_tightplots_ele_2016/*
# rm -rf ttgamma_tightplots_ele_2017/*
# rm -rf ttgamma_tightplots_ele_2018/*
# rm -rf ttgamma_tightplots_mu_2016/*
# rm -rf ttgamma_tightplots_mu_2017/*
# rm -rf ttgamma_tightplots_mu_2018/*

