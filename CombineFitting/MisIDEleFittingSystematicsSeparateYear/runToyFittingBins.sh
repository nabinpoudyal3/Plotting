
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
	combine -M MultiDimFit -n datacard_CR123_2016_nbins3_$i datacard_CR123_2016_nbins3.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_nbins3_$i datacard_CR123_2017_nbins3.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_nbins3_$i datacard_CR123_2018_nbins3.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR123_2016_nbins6_$i datacard_CR123_2016_nbins6.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_nbins6_$i datacard_CR123_2017_nbins6.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_nbins6_$i datacard_CR123_2018_nbins6.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &

	combine -M MultiDimFit -n datacard_CR123_2016_nbins9_$i datacard_CR123_2016_nbins9.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_nbins9_$i datacard_CR123_2017_nbins9.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_nbins9_$i datacard_CR123_2018_nbins9.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
done

wait



#--redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1

for i in `seq 0.4 .2 2.6`; do 
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
	combine -M MultiDimFit -n datacard_CR123_2016_nbins3_ZG_$i datacard_CR123_2016_nbins3.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_nbins3_ZG_$i datacard_CR123_2017_nbins3.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_nbins3_ZG_$i datacard_CR123_2018_nbins3.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR123_2016_nbins6_ZG_$i datacard_CR123_2016_nbins6.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_nbins6_ZG_$i datacard_CR123_2017_nbins6.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_nbins6_ZG_$i datacard_CR123_2018_nbins6.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &

	combine -M MultiDimFit -n datacard_CR123_2016_nbins9_ZG_$i datacard_CR123_2016_nbins9.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_nbins9_ZG_$i datacard_CR123_2017_nbins9.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_nbins9_ZG_$i datacard_CR123_2018_nbins9.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
done

wait

for i in `seq 0.4 .2 2.6`; do 
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
	combine -M MultiDimFit -n datacard_CR123_2016_nbins3_WG_$i datacard_CR123_2016_nbins3.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_nbins3_WG_$i datacard_CR123_2017_nbins3.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_nbins3_WG_$i datacard_CR123_2018_nbins3.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR123_2016_nbins6_WG_$i datacard_CR123_2016_nbins6.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_nbins6_WG_$i datacard_CR123_2017_nbins6.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_nbins6_WG_$i datacard_CR123_2018_nbins6.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &

	combine -M MultiDimFit -n datacard_CR123_2016_nbins9_WG_$i datacard_CR123_2016_nbins9.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_nbins9_WG_$i datacard_CR123_2017_nbins9.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_nbins9_WG_$i datacard_CR123_2018_nbins9.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
done

wait

echo "Done"
