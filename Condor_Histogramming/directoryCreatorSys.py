import sys


## JEC correction JECTotoal
ControlRegion=["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]
#systematics=["isr","fsr","Pdf"] 
systematics=["JEC"] 
lineSyst ='#!/bin/bash \n'
lineSyst ="eosrename='eos root://cmseos.fnal.gov rename' \n"
for channel in ['ele', 'mu']:
	for year in ["2016", "2017", "2018"]:
		for cr in ControlRegion:
			for syst in systematics:
				#lineSyst+='echo eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s_up_%s/ \n'%(year,channel,syst,cr) 
				lineSyst+='$eosrename  /store/user/npoudyal/histograms_%s/%s/hists_%s_up_%s/ /store/user/npoudyal/histograms_%s/%s/hists_%s_up_%s/ \n'%(year,channel,syst,cr, year,channel,syst+"Total",cr) 
				#lineSyst+='echo eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s_down_%s/ \n'%(year,channel,syst,cr) 
				lineSyst+='$eosrename  /store/user/npoudyal/histograms_%s/%s/hists_%s_down_%s/ /store/user/npoudyal/histograms_%s/%s/hists_%s_down_%s/ \n'%(year,channel,syst,cr, year,channel,syst+"Total",cr) 

with open("JECNameCorrection.sh","w") as _file:
    _file.write(lineSyst)  
    
sys.exit()



#ControlRegion=["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]
#systematics=["isr","fsr"] 
#line ="eosmkdir='eos root://cmseos.fnal.gov mkdir' \n"
#for channel in ['ele', 'mu']:
#	for year in ["2016", "2017", "2018"]:
#		for cr in ControlRegion:
#			line+='eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s/ \n'%(year,channel,cr) 
#with open("nominalDirList.sh","w") as _file:
#    _file.write(line)
   
#systematics=["PU","Q2","Pdf","MuEff","EleEff","PhoEff","BTagSF_b","BTagSF_l"]    
#lineSyst ="eosmkdir='eos root://cmseos.fnal.gov mkdir' \n"
#for channel in ['ele', 'mu']:
#	for year in ["2016", "2017", "2018"]:
#		for cr in ControlRegion:
#			for syst in systematics:
#				lineSyst+='$eosmkdir -p /store/user/npoudyal/histograms_%s/%s/Dilep_hists_%s_up_%s/ \n'%(year,channel,syst,cr) 
#				lineSyst+='$eosmkdir -p /store/user/npoudyal/histograms_%s/%s/Dilep_hists_%s_down_%s/ \n'%(year,channel,syst,cr) 
#with open("systematicsDirListDilepton.sh","w") as _file:
#    _file.write(lineSyst) 
    
    
ControlRegion=["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]
#systematics=["isr","fsr","Pdf"] 
systematics=["JEC","JER"] 
lineSyst ='#!/bin/bash \n'
lineSyst ="eosmkdir='eos root://cmseos.fnal.gov mkdir' \n"
for channel in ['ele', 'mu']:
	for year in ["2016", "2017", "2018"]:
		for cr in ControlRegion:
			for syst in systematics:
				lineSyst+='echo eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s_up_%s/ \n'%(year,channel,syst,cr) 
				lineSyst+='$eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s_up_%s/ \n'%(year,channel,syst,cr) 
				lineSyst+='echo eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s_down_%s/ \n'%(year,channel,syst,cr) 
				lineSyst+='$eosmkdir -p /store/user/npoudyal/histograms_%s/%s/hists_%s_down_%s/ \n'%(year,channel,syst,cr) 

with open("makeDir_JECJER.sh","w") as _file:
    _file.write(lineSyst)  
    
sys.exit()


ControlRegion=["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]
#systematics=["isr","fsr","Pdf"] 
systematics=["JEC","JER"] 
lineSyst ='#!/bin/bash \n'
lineSyst +="eosls='eos root://cmseos.fnal.gov ls -lh' \n"
for channel in ['ele', 'mu']:
	for year in ["2016", "2017", "2018"]:
		for cr in ControlRegion:
			for syst in systematics:
				lineSyst+='echo $eosls /store/user/npoudyal/histograms_%s/%s/Dilep_hists_%s_up_%s/ \n'%(year,channel,syst,cr) 
				lineSyst+='$eosls /store/user/npoudyal/histograms_%s/%s/Dilep_hists_%s_up_%s/ \n'%(year,channel,syst,cr) 
				lineSyst+='echo $eosls /store/user/npoudyal/histograms_%s/%s/Dilep_hists_%s_down_%s/ \n'%(year,channel,syst,cr) 
				lineSyst+='$eosls /store/user/npoudyal/histograms_%s/%s/Dilep_hists_%s_down_%s/ \n'%(year,channel,syst,cr) 

with open("ListFilesDilepton_JECJER.sh","w") as _file:
    _file.write(lineSyst)
