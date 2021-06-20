#!/bin/bash

# rm *el_201?_nonPrompt_*.root
# rm *mu_201?_nonPrompt_*.root
# rm *el_201?_*.root
# rm *mu_201?_*.root

# rm ttgamma_closure_ele_201?.pdf
# rm ttgamma_closure_mu_201?.pdf
# rm nonPrompt_closure_ele_201?.pdf
# rm nonPrompt_closure_mu_201?.pdf

# ./allCombine.sh
# echo "Just check the following:"

# text2workspace.py  datacard_ele_2017.dat 
# ValidateDatacards.py datacard_ele_2017.dat --printLevel 3 --checkUncertOver 0.1 

# text2workspace.py  datacard_mu_2017.dat 
# ValidateDatacards.py datacard_mu_2017.dat --printLevel 3 --checkUncertOver 0.1 

# text2workspace.py  datacard_both_2017.dat 
# ValidateDatacards.py datacard_both_2017.dat --printLevel 3 --checkUncertOver 0.1 


for i in $(seq 0.01 0.01 0.1)
do

if [ $i == "0.4" ]; then 
        x=123440
elif [ $i == "0.6" ]; then 
        x=123460
elif [ $i == "0.8" ]; then 
        x=123480
elif [ $i == "1.0" ]; then 
        x=1234100
elif [ $i == "1.2" ]; then 
        x=1234120
elif [ $i == "1.4" ]; then 
        x=1234140
elif [ $i == "1.6" ]; then 
        x=1234160
elif [ $i == "1.8" ]; then 
        x=1234180
elif [ $i == "2.0" ]; then 
        x=1234200
elif [ $i == "2.2" ]; then 
        x=1234220
elif [ $i == "2.4" ]; then 
        x=1234240
else  
        x=1234260
fi
        echo $x
        combine -M MultiDimFit -n el_2017_nonPrompt_$i datacard_ele_2017.dat --setParameters nonPromptSF=$i -s $x -t 300 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2&
        combine -M MultiDimFit -n mu_2017_nonPrompt_$i datacard_mu_2017.dat  --setParameters nonPromptSF=$i -s $x -t 300 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2&
       
done

wait

for i in $(seq 0.01 0.01 0.1)
do

if [ $i == "0.4" ]; then 
        x=123440
elif [ $i == "0.6" ]; then 
        x=123460
elif [ $i == "0.8" ]; then 
        x=123480
elif [ $i == "1.0" ]; then 
        x=1234100
elif [ $i == "1.2" ]; then 
        x=1234120
elif [ $i == "1.4" ]; then 
        x=1234140
elif [ $i == "1.6" ]; then 
        x=1234160
elif [ $i == "1.8" ]; then 
        x=1234180
elif [ $i == "2.0" ]; then 
        x=1234200
elif [ $i == "2.2" ]; then 
        x=1234220
elif [ $i == "2.4" ]; then 
        x=1234240
else  
        x=1234260
fi
        echo $x
        combine -M MultiDimFit -n el_2017_$i datacard_ele_2017.dat -s $x -t 300 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2& 
        combine -M MultiDimFit -n mu_2017_$i datacard_mu_2017.dat  -s $x -t 300 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2&        
done


# echo "python ttGamma_closureTest.py"
# python ttGamma_closureTest.py
# echo "python ttGamma_closureTest_nonPrompt.py"
# python ttGamma_closureTest_nonPrompt.py

