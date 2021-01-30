#!/usr/bin/python

import string
import sys
import fileinput

fileList_ele_2018 = ["datacard_ele_2018_M3.txt","datacard_ele_2018_ChIso.txt","datacard_ele_2018_M30btag.txt","datacard_ele_2018_M30photon.txt"]
fileList_mu_2018  = ["datacard_mu_2018_M3.txt","datacard_mu_2018_ChIso.txt", "datacard_mu_2018_M30btag.txt","datacard_mu_2018_M30photon.txt"]
fileList_2018 =  fileList_ele_2018 + fileList_mu_2018

myinput = sys.argv[1]

for channel in fileList_2018:
	print channel
	for line in fileinput.FileInput(channel, inplace=1):
		if myinput[0]=="#":
			line = line.replace(myinput,myinput[1:])
		else:
			line = line.replace(myinput,"#%s"%myinput)
sys.exit()	





