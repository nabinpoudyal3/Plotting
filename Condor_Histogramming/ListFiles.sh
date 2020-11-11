#!/bin/bash 

declare -a YEAR=("2016" "2017" "2018")
declare -a SYSTEMATICS=("BTagSF_b" "BTagSF_l" "PU" "MuEff" "EleEff" "PhoEff" "Q2" "isr" "fsr" "Pdf" "prefireEcal")
declare -a LEVEL=("up" "down")
declare -a CHANNEL=("ele" "mu")
declare -a CONTROLREGION=("tight" "looseCRge2e0" "looseCRge2ge0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1")
eosls='eos root://cmseos.fnal.gov ls -lh' 
for year in ${YEAR[@]}; do
	for channel in ${CHANNEL[@]}; do	
		for systematics in ${SYSTEMATICS[@]}; do
			for level in ${LEVEL[@]}; do
				for controlregion in ${CONTROLREGION[@]}; do
					echo $eosls /store/user/npoudyal/histograms_"$year"/"$channel"/hists_"$systematics"_"$level"_"$controlregion"/ 
					$eosls /store/user/npoudyal/histograms_"$year"/"$channel"/hists_"$systematics"_"$level"_"$controlregion"/ 
				done
			done
		done
	done
done

exit 1



echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_isr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_fsr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/ele/hists_Pdf_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_isr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_fsr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/ele/hists_Pdf_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_isr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_fsr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/ele/hists_Pdf_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_isr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_fsr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2016/mu/hists_Pdf_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_isr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_fsr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2017/mu/hists_Pdf_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_tight/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_tight/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRge2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_looseCRge2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRge2ge0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_looseCRge2ge0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe3ge2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_looseCRe3ge2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRge4e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_looseCRge4e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe3e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_looseCRe3e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe2e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_looseCRe2e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe2e0/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_looseCRe2e0/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe2e2/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_looseCRe2e2/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_isr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_fsr_down_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe3e1/ 
echo $eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_up_looseCRe3e1/ 
$eosls /store/user/npoudyal/histograms_2018/mu/hists_Pdf_down_looseCRe3e1/ 
