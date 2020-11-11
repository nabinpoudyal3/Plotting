#!/bin/bash

CONTROLREGION = ["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]
SYSTEMATICS   = ["PU","Q2","Pdf","MuEff","EleEff","PhoEff","BTagSF_b","BTagSF_l","prefireEcal","isr","fsr"] 
LEVEL         = ["up", "down"]
YEAR          = ["2016", "2017", "2018"]
CHANNEL       = ["ele","mu"]

line =""
for year in YEAR:
	for channel in CHANNEL:
		for controlregion in CONTROLREGION:
			line+= "mkdir /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/histograms_%s/%s/hists_%s\n"%(year,channel,controlregion)
			line+= "mkdir /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/histograms_%s/%s/Dilep_hists_%s\n"%(year,channel,controlregion)
	
with open("nominalDirList.sh","w") as myfile1:
    myfile1.write(line)
   

lineSyst =""
for year in YEAR:
	for channel in CHANNEL:
		for controlregion in CONTROLREGION:
			for systematics in SYSTEMATICS:
				for level in LEVEL:
					lineSyst+= "mkdir /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/histograms_%s/%s/hists_%s_%s_%s\n"%(year,channel,systematics,level,controlregion)
					lineSyst+= "mkdir /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/histograms_%s/%s/Dilep_hists_%s_%s_%s\n"%(year,channel,systematics,level,controlregion)
					
with open("systematicsDirList.sh","w") as myfile2:
    myfile2.write(lineSyst) 
    
