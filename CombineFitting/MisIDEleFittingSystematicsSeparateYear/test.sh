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
	
done

wait

