for i in $(seq 0.4 0.2 2.6)
do
if [ $i == "0.4" ]; then 
        x=40
elif [ $i == "0.6" ]; then 
        x=60
elif [ $i == "0.8" ]; then 
        x=80
elif [ $i == "1.0" ]; then 
        x=100
elif [ $i == "1.2" ]; then 
        x=120
elif [ $i == "1.4" ]; then 
        x=140
elif [ $i == "1.6" ]; then 
        x=160
elif [ $i == "1.8" ]; then 
        x=180
elif [ $i == "2.0" ]; then 
        x=200
elif [ $i == "2.2" ]; then 
        x=220
elif [ $i == "2.4" ]; then 
        x=240
else  
        x=260
fi
        echo $x
        combine -M MultiDimFit -n el_2016_$i datacard_M3ChIso_ele_2016.txt -s $x -t 1000 --expectSignal=$i --redefineSignalPOIs r,nonPromptSF -v2


        
done

wait

