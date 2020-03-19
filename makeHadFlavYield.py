from ROOT import TFile, Double
import os
import sys
from optparse import OptionParser
import CMS_lumi
import shutil
from math import sqrt

import uncertainties

parser = OptionParser()
parser.add_option("-y", "--year", dest="Year", default="",type='str',
					help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-c", "--channel", dest="channel", default="",type='str',
					help="Specify which channel Mu or Ele? default is Mu" )

parser.add_option("--looseCRge2e0", dest="looseCRge2e0", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 =0" )

parser.add_option("--LooseCRe2e0","--looseCRe2e0", dest="looseCRe2e0", default=False,action="store_true",
                     help="Use ==2 jets + ==0 bjets selection" )  

parser.add_option("--LooseCRe2e1","--looseCRe2e1", dest="looseCRe2e1", default=False,action="store_true",
                     help="Use ==2 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe3e0","--looseCRe3e0", dest="looseCRe3e0", default=False,action="store_true",
                     help="Use ==3 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRge4e0","--looseCRge4e0", dest="looseCRge4e0", default=False,action="store_true",
                     help="Use >=4 jets + ==0 bjets selection" ) 

##

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()

finalState = options.channel

looseCRge2e0 =options.looseCRge2e0
looseCRe2e0  =options.looseCRe2e0
looseCRe2e1  =options.looseCRe2e1
looseCRe3e0  =options.looseCRe3e0
looseCRge4e0 =options.looseCRge4e0

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

if looseCRge2e0:  #CR1+CR2+CR3
	name = "cr123"
	fileDir  = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
	#plotDirectory = "HadFlav_Yield_looseCRge2e0plots_%s_%s/"%(channel,selYear)
	regionText = "N_{j}#geq2, N_{b}=0"
###
if looseCRe2e0:  #CR1
	name = "cr1"
	fileDir  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
	#plotDirectory = "HadFlav_Yield_looseCRe2e0plots_%s_%s/"%(channel,selYear)
	regionText = "N_{j}=2, N_{b}=0"

if looseCRe3e0:  #CR2
	name = "cr2"
	fileDir  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
	#plotDirectory = "HadFlav_Yield_looseCRe3e0plots_%s_%s/"%(channel,selYear)
	regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0:  #CR3
	name = "cr3"
	fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	#plotDirectory = "HadFlav_Yield_looseCRge4e0plots_%s_%s/"%(channel,selYear)
	regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe2e1:  #CR4
	name = "cr4"
	fileDir  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
	#plotDirectory = "HadFlav_Yield_looseCRe2e1plots_%s_%s/"%(channel,selYear)
	regionText = "N_{j}=2, N_{b}=1"

             
#if not os.path.exists(plotDirectory):
	#os.mkdir(plotDirectory)

sampleList = ['WGamma','ZGamma']

Flavour_category = ["BTag","CTag","LightTag"]

BTagDict     = {'WGamma':(0,0),'ZGamma':(0,0)}
CTagDict     = {'WGamma':(0,0),'ZGamma':(0,0)}
LightTagDict = {'WGamma':(0,0),'ZGamma':(0,0)}

import CMS_lumi

if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"

#histName    = "phosel_M3_%s_%s"
#histNameData= "phosel_M3_%s" 
#mydistributionName = histNameData[7:-3]

histName    = "phosel_MassEGamma_%s_%s"
# histNameData= "phosel_MassEGamma_%s" 
#mydistributionName = histNameData[16:-6]

file = {}

# if finalState=='Ele':
# 	sample = "DataEle"
# 	file[sample] = TFile("%s%s.root"%(fileDir,sample),"read")
# 	dataHist = file[sample].Get(histNameData%(sample))
# 	nPhotonData = dataHist.Integral(-1,-1)
	
# elif finalState=='Mu':
# 	sample = "DataMu"
# 	file[sample] = TFile("%s%s.root"%(fileDir,sample),"read")
# 	dataHist = file[sample].Get(histNameData%(sample))
# 	nPhotonData = dataHist.Integral(-1,-1)

# else:
# 	print "Select the channel !!!"
# 	sys.exit()	

# if selYear == '2017' or selYear == '2018': nPhotonData = 0

for fl in Flavour_category:
	for sample in sampleList:  
		file[sample] = TFile('%s%s.root'%(fileDir,sample),'read')
		sampleHist = file[sample].Get(histName%(fl,sample))
		error = Double(0.)
		numbers = sampleHist.IntegralAndError(-1,-1,error)
		if   fl == "BTag":  
			BTagDict[sample] =(numbers,error)
		elif fl == "CTag":       
			CTagDict[sample] =(numbers,error)
		elif fl == "LightTag": 
			LightTagDict[sample]=(numbers,error)
		else: sys.exit()


line = ""
line += "\\begin{frame} \n" 
line += "\\frametitle{Flavour category Table for ~%s: channel=%s; year=%s} \n"%(name,channel,selYear)
line += "\\tiny{ \n"
line += "\\begin{tabular} {|l||l|l|l|} \n"
line += "\\hline \n" 
line += "sample & BTag & CTag & LightTag  \\\\ \n"

for sample in sampleList:
	line += "\\hline \n"
	line += "%s & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ \\\\ \n"%(sample, BTagDict[sample][0],BTagDict[sample][1],CTagDict[sample][0],CTagDict[sample][1],LightTagDict[sample][0],LightTagDict[sample][1])
line += "\\hline \n"
line += "\\end{tabular} \n"
line += "} \n"
line += "\\end{frame} \n"

with open("FlavCategoryYield_%s_%s_%s.tex"%(channel,selYear,name),"w") as _file:
    _file.write(line)

_file.close()

shutil.copy("FlavCategoryYield_%s_%s_%s.tex"%(channel,selYear,name),"CombineFitting/AllTexFiles")

os.remove("FlavCategoryYield_%s_%s_%s.tex"%(channel,selYear,name))









