


for i in $(seq 0.4 0.2 2.6)
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
        combine -M MultiDimFit -n el_2016_nonPrompt_$i datacard_M3ChIso_ele_2016.txt --setParameters nonPromptSF=$i -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2   >& outputFiles/file16.txt 
        combine -M MultiDimFit -n mu_2016_nonPrompt_$i datacard_M3ChIso_mu_2016.txt  --setParameters nonPromptSF=$i -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2   >& outputFiles/file15.txt 
       
        combine -M MultiDimFit -n el_2017_nonPrompt_$i datacard_M3ChIso_ele_2017.txt --setParameters nonPromptSF=$i -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2   >& outputFiles/file14.txt 
        combine -M MultiDimFit -n mu_2017_nonPrompt_$i datacard_M3ChIso_mu_2017.txt  --setParameters nonPromptSF=$i -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2   >& outputFiles/file13.txt 
        
        combine -M MultiDimFit -n el_2018_nonPrompt_$i datacard_M3ChIso_ele_2018.txt --setParameters nonPromptSF=$i -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2   >& outputFiles/file12.txt 
        combine -M MultiDimFit -n mu_2018_nonPrompt_$i datacard_M3ChIso_mu_2018.txt  --setParameters nonPromptSF=$i -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2   >& outputFiles/file11.txt   


done

wait

for i in $(seq 0.4 0.2 2.6)
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
        combine -M MultiDimFit -n el_2016_$i datacard_M3ChIso_ele_2016.txt -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file17.txt   
        combine -M MultiDimFit -n mu_2016_$i datacard_M3ChIso_mu_2016.txt  -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file18.txt 
        
        combine -M MultiDimFit -n el_2017_$i datacard_M3ChIso_ele_2017.txt -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file19.txt 
        combine -M MultiDimFit -n mu_2017_$i datacard_M3ChIso_mu_2017.txt  -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file20.txt 
       
        combine -M MultiDimFit -n el_2018_$i datacard_M3ChIso_ele_2018.txt -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file21.txt 
        combine -M MultiDimFit -n mu_2018_$i datacard_M3ChIso_mu_2018.txt  -s $x -t 5000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2  >& outputFiles/file22.txt 

        
done

#wait

