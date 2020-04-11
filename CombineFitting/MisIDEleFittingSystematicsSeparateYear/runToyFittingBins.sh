#!/bin/bash


for i in `seq 0.4 0.2 2.6`; do
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
	combine -M MultiDimFit -n datacard_CR123_2016_$i datacard_CR123_2016.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_$i datacard_CR123_2017.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_$i datacard_CR123_2018.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR1_2016_$i datacard_CR1_2016.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR1_2017_$i datacard_CR1_2017.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR1_2018_$i datacard_CR1_2018.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR2_2016_$i datacard_CR2_2016.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR2_2017_$i datacard_CR2_2017.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR2_2018_$i datacard_CR2_2018.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR3_2016_$i datacard_CR3_2016.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR3_2017_$i datacard_CR3_2017.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR3_2018_$i datacard_CR3_2018.txt --expectSignal=$i -t 1000  -s $x --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &

done

wait



#--redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF --setParameters ZGammaBkgPhotonSF=1

for i in `seq 0.4 .2 2.6`; do 

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
	combine -M MultiDimFit -n datacard_CR123_2016_ZG_$i datacard_CR123_2016.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_ZG_$i datacard_CR123_2017.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_ZG_$i datacard_CR123_2018.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR1_2016_ZG_$i datacard_CR1_2016.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR1_2017_ZG_$i datacard_CR1_2017.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR1_2018_ZG_$i datacard_CR1_2018.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR2_2016_ZG_$i datacard_CR2_2016.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR2_2017_ZG_$i datacard_CR2_2017.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR2_2018_ZG_$i datacard_CR2_2018.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR3_2016_ZG_$i datacard_CR3_2016.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR3_2017_ZG_$i datacard_CR3_2017.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR3_2018_ZG_$i datacard_CR3_2018.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	
	#combine -M MultiDimFit -n datacard_CR123_2016_nbins6_ZG_$i datacard_CR123_2016_nbins6.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	#combine -M MultiDimFit -n datacard_CR123_2017_nbins6_ZG_$i datacard_CR123_2017_nbins6.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	#combine -M MultiDimFit -n datacard_CR123_2018_nbins6_ZG_$i datacard_CR123_2018_nbins6.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &

	#combine -M MultiDimFit -n datacard_CR123_2016_nbins9_ZG_$i datacard_CR123_2016_nbins9.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	#combine -M MultiDimFit -n datacard_CR123_2017_nbins9_ZG_$i datacard_CR123_2017_nbins9.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	#combine -M MultiDimFit -n datacard_CR123_2018_nbins9_ZG_$i datacard_CR123_2018_nbins9.txt --setParameters ZGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
done

wait

for i in `seq 0.4 .2 2.6`; do 
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
	combine -M MultiDimFit -n datacard_CR123_2016_WG_$i datacard_CR123_2016.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2017_WG_$i datacard_CR123_2017.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR123_2018_WG_$i datacard_CR123_2018.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR1_2016_WG_$i datacard_CR123_2016.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR1_2017_WG_$i datacard_CR123_2017.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR1_2018_WG_$i datacard_CR123_2018.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR2_2016_WG_$i datacard_CR123_2016.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR2_2017_WG_$i datacard_CR123_2017.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR2_2018_WG_$i datacard_CR123_2018.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	combine -M MultiDimFit -n datacard_CR3_2016_WG_$i datacard_CR123_2016.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhoton&
	combine -M MultiDimFit -n datacard_CR3_2017_WG_$i datacard_CR123_2017.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	combine -M MultiDimFit -n datacard_CR3_2018_WG_$i datacard_CR123_2018.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
	
	#combine -M MultiDimFit -n datacard_CR123_2016_nbins6_WG_$i datacard_CR123_2016_nbins6.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	#combine -M MultiDimFit -n datacard_CR123_2017_nbins6_WG_$i datacard_CR123_2017_nbins6.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	#combine -M MultiDimFit -n datacard_CR123_2018_nbins6_WG_$i datacard_CR123_2018_nbins6.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &

	#combine -M MultiDimFit -n datacard_CR123_2016_nbins9_WG_$i datacard_CR123_2016_nbins9.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	#combine -M MultiDimFit -n datacard_CR123_2017_nbins9_WG_$i datacard_CR123_2017_nbins9.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	#combine -M MultiDimFit -n datacard_CR123_2018_nbins9_WG_$i datacard_CR123_2018_nbins9.txt --setParameters WGammaBkgPhotonSF=$i -t 1000 -s $x  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF &
	
done

wait

echo "Done"
