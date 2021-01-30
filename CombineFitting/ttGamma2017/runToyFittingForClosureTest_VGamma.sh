#!/bin/bash

btag=$1

# rm *el_201?_?GammaSF_*.root
# rm *mu_201?_?GammaSF_*.root

# rm WGammaSF_closure_ele_201?.pdf
# rm WGammaSF_closure_mu_201?.pdf
# rm ZGammaSF_closure_ele_201?.pdf
# rm ZGammaSF_closure_mu_201?.pdf

# rm WGammaSF_no0BtagCR_closure_ele_201?.pdf
# rm WGammaSF_no0BtagCR_closure_mu_201?.pdf
# rm ZGammaSF_no0BtagCR_closure_ele_201?.pdf
# rm ZGammaSF_no0BtagCR_closure_mu_201?.pdf

if [[ $btag == "no0BtagCR" ]]; then 
        combineCards.py -S M3=datacard_ele_2017_M3_DD.txt ChIso=datacard_ele_2017_ChIso_DD.txt  M30photon=datacard_ele_2017_M30photon_DD.txt >  datacard_ele_2017.txt
        combineCards.py -S M3=datacard_mu_2017_M3_DD.txt  ChIso=datacard_mu_2017_ChIso_DD.txt   M30photon=datacard_mu_2017_M30photon_DD.txt  >  datacard_mu_2017.txt
        combineCards.py -S ele=datacard_ele_2017.txt      mu=datacard_mu_2017.txt                                                            >  datacard_both_2017.txt    
else
        ./allCombine.sh

fi 

echo "Just check the following:"

text2workspace.py  datacard_ele_2017.txt 
ValidateDatacards.py datacard_ele_2017.txt  --printLevel 3 --checkUncertOver 0.1 

text2workspace.py  datacard_mu_2017.txt 
ValidateDatacards.py datacard_mu_2017.txt   --printLevel 3 --checkUncertOver 0.1 

text2workspace.py  datacard_both_2017.txt 
ValidateDatacards.py datacard_both_2017.txt --printLevel 3 --checkUncertOver 0.1 


for i in $(seq 0.4 0.2 2.6)
do

if [[ $i == "0.4" ]]; then 
        x=123440
elif [[ $i == "0.6" ]]; then 
        x=123460
elif [[ $i == "0.8" ]]; then 
        x=123480
elif [[ $i == "1.0" ]]; then 
        x=1234100
elif [[ $i == "1.2" ]]; then 
        x=1234120
elif [[ $i == "1.4" ]]; then 
        x=1234140
elif [[ $i == "1.6" ]]; then 
        x=1234160
elif [[ $i == "1.8" ]]; then 
        x=1234180
elif [[ $i == "2.0" ]]; then 
        x=1234200
elif [[ $i == "2.2" ]]; then 
        x=1234220
elif [[ $i == "2.4" ]]; then 
        x=1234240
else  
        x=1234260
fi
        echo $x
        if [[ $btag == "no0BtagCR" ]]; then 
                combine -M MultiDimFit -n el_2017_WGSF_no0BtagCR_$i datacard_ele_2017.root  --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,WGSF -v3&
                combine -M MultiDimFit -n mu_2017_WGSF_no0BtagCR_$i datacard_mu_2017.root   --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,WGSF -v3&
                combine -M MultiDimFit -n el_2017_ZGSF_no0BtagCR_$i datacard_ele_2017.root  --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,ZGSF -v3&
                combine -M MultiDimFit -n mu_2017_ZGSF_no0BtagCR_$i datacard_mu_2017.root   --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,ZGSF -v3&      
        else
                combine -M MultiDimFit -n el_2017_WGSF_$i           datacard_ele_2017.root  --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,WGSF -v3&
                combine -M MultiDimFit -n mu_2017_WGSF_$i           datacard_mu_2017.root   --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,WGSF -v3&
                combine -M MultiDimFit -n el_2017_ZGSF_$i           datacard_ele_2017.root  --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,ZGSF -v3&
                combine -M MultiDimFit -n mu_2017_ZGSF_$i           datacard_mu_2017.root   --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,ZGSF -v3&   

        fi 
done

wait

exit 1

#Below is 4 variable
python VGamma_closureTest.py --poi WGSF
python VGamma_closureTest.py --poi ZGSF

#Below is 3 variable
python VGamma_closureTest.py --poi WGSF --without0btagCR
python VGamma_closureTest.py --poi ZGSF --without0btagCR

exit 1