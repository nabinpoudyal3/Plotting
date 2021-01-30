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

myParameterRange=" --setParameterRanges nonPromptSF=0,5:TTbarSF=0,4:WGSF=0,4:OtherSF=0,4:Other_norm=0,4:ZGSF=0,4 "
mySignalParamters=" --redefineSignalPOIs=r,nonPromptSF "
mySignalModifierRange=" --rMin=-1 --rMax=5 "
myAsimovFit=" -t -1 --expectSignal 1 "
myFakeDataFit=" -t 1 --expectSignal 1 "
myToyFit=" -t 300 --expectSignal 1 "
verbose=" -v1 "
myTrackParameters=" --trackParameters r,BTagSF_b,BTagSF_l,EleEff,MuEff,PhoEff,lumi,misIDE,ZGSF,TTbarSF,OtherSF,WGSF,Other_norm,nonPromptSF "
mySeed=" --seed=314159 "
myPoints=" --points=100 "



if [[ $btag == "no0BtagCR" ]]; then 
        combineCards.py -S M3=datacard_ele_2016_M3_DD.txt ChIso=datacard_ele_2016_ChIso_DD.txt  M30photon=datacard_ele_2016_M30photon_DD.txt >  datacard_ele_2016.txt
        combineCards.py -S M3=datacard_mu_2016_M3_DD.txt  ChIso=datacard_mu_2016_ChIso_DD.txt   M30photon=datacard_mu_2016_M30photon_DD.txt  >  datacard_mu_2016.txt
        combineCards.py -S ele=datacard_ele_2016.txt      mu=datacard_mu_2016.txt                                                            >  datacard_both_2016.txt    
else
        ./allCombine.sh

fi 

echo "Just check the following:"

text2workspace.py  datacard_ele_2016.txt 
ValidateDatacards.py datacard_ele_2016.txt  --printLevel 3 --checkUncertOver 0.1 

text2workspace.py  datacard_mu_2016.txt 
ValidateDatacards.py datacard_mu_2016.txt   --printLevel 3 --checkUncertOver 0.1 

text2workspace.py  datacard_both_2016.txt 
ValidateDatacards.py datacard_both_2016.txt --printLevel 3 --checkUncertOver 0.1 


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
                combine -M MultiDimFit -n el_2016_WGSF_no0BtagCR_$i datacard_ele_2016.root  -P WGSF --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF -v0&
                combine -M MultiDimFit -n mu_2016_WGSF_no0BtagCR_$i datacard_mu_2016.root   -P WGSF --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF -v0&
                combine -M MultiDimFit -n el_2016_ZGSF_no0BtagCR_$i datacard_ele_2016.root  -P ZGSF --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF -v0&
                combine -M MultiDimFit -n mu_2016_ZGSF_no0BtagCR_$i datacard_mu_2016.root   -P ZGSF --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF -v0&      
        else
                combine -M MultiDimFit -n el_2016_WGSF_$i           datacard_ele_2016.root  -P WGSF --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF -v0&
                combine -M MultiDimFit -n mu_2016_WGSF_$i           datacard_mu_2016.root   -P WGSF --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF -v0&
                combine -M MultiDimFit -n el_2016_ZGSF_$i           datacard_ele_2016.root  -P ZGSF --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF -v0&
                combine -M MultiDimFit -n mu_2016_ZGSF_$i           datacard_mu_2016.root   -P ZGSF --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF -v0&   

        fi 
done

wait

exit 1

#Below is 4 variable
python VGamma_closureTest.py --poi WGSF
python VGamma_closureTest.py --poi ZGSF
python VGamma_closureTest.py --poi WGSF --without0btagCR
python VGamma_closureTest.py --poi ZGSF --without0btagCR

exit 1

combine -M MultiDimFit datacard_"$channel"_2016.root $mySeed --algo grid $myFakeDataFit $myPoints -n .Data_Main_"$channel"_"$parameter" $mySignalModifierRange -P $parameter --floatOtherPOIs 1  $myParameterRange
combine -M MultiDimFit -t %i --setParameters %s=%.2f --redefineSignalPOIs r,%s --expectSignal 1"%(nToys,fitParam,scale,fitParam,seed,datacard)
combine -M MultiDimFit -t 10 --setParameters %s=%.2f --expectSignal 1 -s %i %s"%(fitParam,scale,seed,datacard)
combine -M MultiDimFit -t %i --expectSignal %.2f -s %i %s"%(nToys,scale,seed,datacard)



                combine -M MultiDimFit -n el_2016_WGSF_no0BtagCR_$i datacard_ele_2016.root  -P WGSF --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,WGSF -v0&
                combine -M MultiDimFit -n mu_2016_WGSF_no0BtagCR_$i datacard_mu_2016.root   -P WGSF --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,WGSF -v0&
                combine -M MultiDimFit -n el_2016_ZGSF_no0BtagCR_$i datacard_ele_2016.root  -P ZGSF --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,ZGSF -v0&
                combine -M MultiDimFit -n mu_2016_ZGSF_no0BtagCR_$i datacard_mu_2016.root   -P ZGSF --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,ZGSF -v0&      
        else
                combine -M MultiDimFit -n el_2016_WGSF_$i           datacard_ele_2016.root  -P WGSF --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,WGSF -v0&
                combine -M MultiDimFit -n mu_2016_WGSF_$i           datacard_mu_2016.root   -P WGSF --setParameters WGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,WGSF -v0&
                combine -M MultiDimFit -n el_2016_ZGSF_$i           datacard_ele_2016.root  -P ZGSF --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,ZGSF -v0&
                combine -M MultiDimFit -n mu_2016_ZGSF_$i           datacard_mu_2016.root   -P ZGSF --setParameters ZGSF=$i -s $x -t 300 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,ZGSF -v0&   