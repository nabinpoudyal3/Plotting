
text2workspace.py  datacard_ele_2016.txt 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_ele_2016.json
plotImpacts.py -i impacts_toy_ele_2016.json -o impacts_toy_ele_2016
##
##
text2workspace.py  datacard_mu_2016.txt 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_mu_2016.json
plotImpacts.py -i impacts_toy_mu_2016.json -o impacts_toy_mu_2016
##
#####################
text2workspace.py  datacard_ele_2017.txt 
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125 -t -1 --expectSignal 1  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_ele_2017.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_ele_2017.json
plotImpacts.py -i impacts_toy_ele_2017.json -o impacts_toy_ele_2017
##
##
text2workspace.py  datacard_mu_2017.txt 
combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -t -1 --expectSignal 1  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_mu_2017.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_mu_2017.json
plotImpacts.py -i impacts_toy_mu_2017.json -o impacts_toy_mu_2017
##
#######################
text2workspace.py  datacard_ele_2018.txt 
combineTool.py -M Impacts -d datacard_ele_2018.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_ele_2018.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_ele_2018.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_ele_2018.json
plotImpacts.py -i impacts_toy_ele_2018.json -o impacts_toy_ele_2018
##
##
text2workspace.py  datacard_mu_2018.txt 
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_mu_2018.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_mu_2018.json
plotImpacts.py -i impacts_toy_mu_2018.json -o impacts_toy_mu_2018
##
##
##
text2workspace.py  datacard_ele_2016.txt 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125   --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125   --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_ele_2016.root -m 125   -o impacts_data_ele_2016.json
plotImpacts.py -i impacts_data_ele_2016.json -o impacts_data_ele_2016
##
##
text2workspace.py  datacard_mu_2016.txt 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_mu_2016.root -m 125  -o impacts_data_mu_2016.json
plotImpacts.py -i impacts_data_mu_2016.json -o impacts_data_mu_2016
##


###########################
text2workspace.py  datacard_both_2016.txt 
combineTool.py -M Impacts -d datacard_both_2016.root -m 125 -t -1 --expectSignal 1  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_both_2016.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_both_2016.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_both_2016.json
plotImpacts.py -i impacts_toy_both_2016.json -o impacts_toy_both_2016
###########################
text2workspace.py  datacard_both_2017.txt 
combineTool.py -M Impacts -d datacard_both_2017.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_both_2017.root -m 125 -t -1 --expectSignal 1  --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_both_2017.root -m 125 -t -1 --expectSignal 1  -o impacts_toy_both_2017.json
plotImpacts.py -i impacts_toy_both_2017.json -o impacts_toy_both_2017
###########################
text2workspace.py  datacard_both_2018.txt 
combineTool.py -M Impacts -d datacard_both_2018.root -m 125 -t -1 --expectSignal 1 --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_both_2018.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_both_2018.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_both_2018.json
plotImpacts.py -i impacts_toy_both_2018.json -o impacts_toy_both_2018
###########################
###########################

text2workspace.py  datacard_both_2016.txt 
combineTool.py -M Impacts -d datacard_both_2016.root -m 125   --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_both_2016.root -m 125   --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_both_2016.root -m 125   -o impacts_data_both_2016.json
plotImpacts.py -i impacts_data_both_2016.json -o impacts_data_both_2016

text2workspace.py  datacard_both_allyear.txt
combineTool.py -M Impacts -d datacard_both_allyear.root -m 125 -t -1 --expectSignal 1  --doInitialFit --robustFit 1 
combineTool.py -M Impacts -d datacard_both_allyear.root -m 125 -t -1 --expectSignal 1 --robustFit 1 --doFits 
combineTool.py -M Impacts -d datacard_both_allyear.root -m 125 -t -1 --expectSignal 1 -o impacts_toy_both_allyear.json
plotImpacts.py -i impacts_toy_both_allyear.json -o impacts_toy_both_allyear

