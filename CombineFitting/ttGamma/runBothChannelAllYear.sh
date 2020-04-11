

combine -M MultiDimFit -n   both_allyear datacard_M3ChIso_both_allyear.txt  -s 314159 -t 1000 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF

#combine -M MultiDimFit -n   both_allyear datacard_M3ChIso_both_allyear.txt  -s 314159 -t 1000 --expectSignal 1 --trackParameters PhoEff,Q2,PU,EleEff,BTagSF_b,lumi,BTagSF_l,MuEff,nonPromptSF --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file10.txt

wait

#while [ true ] ; do
#	read -t 60 -n 1
#	if [ $? = 0 ] ; then
#	echo "got all SFs ??? "
#	break;	
#	else
#	echo "waiting to finish the MultiDimFit."
#	fi
#done


###########################
text2workspace.py  datacard_M3ChIso_both_allyear.txt
combineTool.py -M Impacts -d datacard_M3ChIso_both_allyear.root -m 125 -t -1 --expectSignal 1  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_M3ChIso_both_allyear.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_M3ChIso_both_allyear.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_both_allyear.json
plotImpacts.py -i impacts_toy_both_allyear.json -o impacts_toy_both_allyear



