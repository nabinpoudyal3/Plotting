#!/bin/bash

declare -a SAMPLEEle=("TTGamma" "TTbar" "TGJets" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCDEle" "DataEle" )
declare -a SAMPLEMu=("TTGamma" "TTbar" "TGJets" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCDMu" "DataMu" )
declare -a YEAR=("2016" "2017" "2018")
declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRge2ge0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Q2" "isr" "fsr" "Pdf" "prefireEcal")
declare -a LEVEL=("up" "down")


fileDir="root://cmseos.fnal.gov//store/user/npoudyal"
localDir="/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming"

for year in ${YEAR[@]}; do
	for controlregion in ${CONTROLREGION[@]}; do
		for sample in ${SAMPLEEle[@]}; do
			xrdcp -f $fileDir/histograms_$year/ele/Dilep_hists_$controlregion/$sample.root $localDir/histograms_$year/ele/Dilep_hists_$controlregion/
			xrdcp -f $fileDir/histograms_$year/ele/hists_$controlregion/$sample.root $localDir/histograms_$year/ele/hists_$controlregion/
		done
	done
done


for year in ${YEAR[@]}; do
	for controlregion in ${CONTROLREGION[@]}; do
		for sample in ${SAMPLEMu[@]}; do
			xrdcp -f $fileDir/histograms_$year/mu/Dilep_hists_$controlregion/$sample.root $localDir/histograms_$year/mu/Dilep_hists_$controlregion/
			xrdcp -f $fileDir/histograms_$year/mu/hists_$controlregion/$sample.root $localDir/histograms_$year/mu/hists_$controlregion/
		done
	done
done

for year in ${YEAR[@]}; do
	for controlregion in ${CONTROLREGION[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				for sample in ${SAMPLEEle[@]}; do
			    	xrdcp -f $fileDir/histograms_$year/ele/Dilep_hists_"$systematics"_"$level"_"$controlregion"/$sample.root $localDir/histograms_$year/ele/Dilep_hists_"$systematics"_"$level"_"$controlregion"/
			    	xrdcp -f $fileDir/histograms_$year/ele/hists_"$systematics"_"$level"_"$controlregion"/$sample.root $localDir/histograms_$year/ele/hists_"$systematics"_"$level"_"$controlregion"/
				done
			done
		done
	done
done


for year in ${YEAR[@]}; do
	for controlregion in ${CONTROLREGION[@]}; do
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				for sample in ${SAMPLEMu[@]}; do
			    	xrdcp -f $fileDir/histograms_$year/mu/Dilep_hists_"$systematics"_"$level"_"$controlregion"/$sample.root $localDir/histograms_$year/mu/Dilep_hists_"$systematics"_"$level"_"$controlregion"/
			    	xrdcp -f $fileDir/histograms_$year/mu/hists_"$systematics"_"$level"_"$controlregion"/$sample.root $localDir/histograms_$year/mu/hists_"$systematics"_"$level"_"$controlregion"/
				done
			done
		done
	done
done

	
