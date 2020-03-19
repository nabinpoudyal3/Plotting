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

parser.add_option("--LooseCRe2e2","--looseCRe2e2", dest="isLooseCRe2e2Selection", default=False,action="store_true",
                     help="Use ==2 jets + ==2 bjets selection" ) 

parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
		  			 help="Use 4j1t selection" )
##

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()

finalState = options.channel

isLooseCRe2e2Selection = options.isLooseCRe2e2Selection
isTightSelection       = options.isTightSelection

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

if isLooseCRe2e2Selection:  #CR6
	fileDir  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
	plotDirectory = "PhoCatYield_looseCRe2e2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=2"

if isTightSelection: #SR
	plotDirectory = "tightplots_%s_%s/"%(channel, selYear)
	fileDir = "histograms_%s/%s/hists_tight/"%(selYear,channel)
	regionText = ", N_{j}#geq4, N_{b}#geq1"
      
ZJetSF = 1.23  
if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)


eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
fileDir = eosFolder+fileDir

sampleList = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]

Photon_category = ["GenuinePhoton","MisIDEle","HadronicPhoton","HadronicFake"]

GenuinePhotonDict  = {'TTGamma':(0,0), 'TTbar':(0,0), 'TGJets':(0,0),'SingleTop':(0,0), 'WJets':(0,0), 'ZJets':(0,0), 'WGamma':(0,0),'ZGamma':(0,0),'Diboson':(0,0),'TTV':(0,0),'GJets':(0,0),"QCD":(0,0)}
MisIDEleDict       = {'TTGamma':(0,0), 'TTbar':(0,0), 'TGJets':(0,0),'SingleTop':(0,0), 'WJets':(0,0), 'ZJets':(0,0), 'WGamma':(0,0),'ZGamma':(0,0),'Diboson':(0,0),'TTV':(0,0),'GJets':(0,0),"QCD":(0,0)}
HadronicPhotonDict = {'TTGamma':(0,0), 'TTbar':(0,0), 'TGJets':(0,0),'SingleTop':(0,0), 'WJets':(0,0), 'ZJets':(0,0), 'WGamma':(0,0),'ZGamma':(0,0),'Diboson':(0,0),'TTV':(0,0),'GJets':(0,0),"QCD":(0,0)}
HadronicFakeDict   = {'TTGamma':(0,0), 'TTbar':(0,0), 'TGJets':(0,0),'SingleTop':(0,0), 'WJets':(0,0), 'ZJets':(0,0), 'WGamma':(0,0),'ZGamma':(0,0),'Diboson':(0,0),'TTV':(0,0),'GJets':(0,0),"QCD":(0,0)}


import CMS_lumi

if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"

histName    = "phosel_M3_%s_%s"
histNameData= "phosel_M3_%s" 
mydistributionName = histNameData[7:-3]

#histName    = "phosel_mediumID_ChIso_%s_%s"
#histNameData= "phosel_mediumID_ChIso_%s" 
#mydistributionName = histNameData[16:-3]

file = {}

if finalState=='Ele':
	sample = "DataEle"
	file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
	dataHist = file[sample].Get(histNameData%(sample))
	nPhotonData = dataHist.Integral(-1,-1)
	
elif finalState=='Mu':
	sample = "DataMu"
	file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
	dataHist = file[sample].Get(histNameData%(sample))
	nPhotonData = dataHist.Integral(-1,-1)

else:
	print "Select the channel !!!"
	sys.exit()	

if selYear == '2017' or selYear == '2018': nPhotonData = 0

totalGen, totalMis, totalHad, totalFak = 0,0,0,0
totalGenErr, totalMisErr, totalHadErr, totalFakErr = 0,0,0,0
for phocat in Photon_category:
	for sample in sampleList:  
		if finalState == 'Ele' and sample == 'QCD': sample = 'QCDEle'
		if finalState == 'Mu'  and sample == 'QCD': sample = 'QCDMu'
		file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')
		sampleHist = file[sample].Get(histName%(phocat,sample))
		if sample=="ZJets": sampleHist.Scale(ZJetSF)
		error = Double(0.)
		nPhotons = sampleHist.IntegralAndError(-1,-1,error)
		
		if   phocat == "GenuinePhoton":  
			GenuinePhotonDict[sample] =(nPhotons,error)
			totalGen += nPhotons; totalGenErr += error*error;
		elif phocat == "MisIDEle":       
			MisIDEleDict[sample]      =(nPhotons,error)
			totalMis += nPhotons; totalMisErr += error*error;
			
		elif phocat == "HadronicPhoton": 
			HadronicPhotonDict[sample]=(nPhotons,error)
			totalHad += nPhotons; totalHadErr += error*error;
			
		elif phocat == "HadronicFake":   
			HadronicFakeDict[sample]  =(nPhotons,error)
			totalFak += nPhotons; totalFakErr += error*error;
			
		else: sys.exit()


line = ""
line += "\\begin{frame} \n" 
line += "\\frametitle{Photon category Table for \\srEight ~%s: channel=%s; year=%s} \n"%(mydistributionName,channel,selYear)
line += "\\tiny{ \n"
line += "\\begin{tabular} {|l||l|l|l|l||l|} \n"
line += "\\hline \n" 
line += "sample & GenuinePhoton & MisIDEle & Hadronic & HadronicFake & Total \\\\ \n"
totalMCErr = 0
for sample in sampleList:
	totalEachSample    = GenuinePhotonDict[sample][0]+ MisIDEleDict[sample][0] + HadronicPhotonDict[sample][0] + HadronicFakeDict[sample][0]
	totalEachSampleErr = sqrt(GenuinePhotonDict[sample][1]**2+ MisIDEleDict[sample][1]**2 + HadronicPhotonDict[sample][1]**2 + HadronicFakeDict[sample][1]**2)
	totalMCErr += totalEachSampleErr**2
	line += "\\hline \n"
	line += "%s & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ \\\\ \n"%(sample, GenuinePhotonDict[sample][0], GenuinePhotonDict[sample][1],MisIDEleDict[sample][0], MisIDEleDict[sample][1],HadronicPhotonDict[sample][0], HadronicPhotonDict[sample][1],HadronicFakeDict[sample][0], HadronicFakeDict[sample][1],totalEachSample,totalEachSampleErr) 

line += "\\hline \n"
line += "\\hline \n"
line += "MC & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ \\\\ \n"%(totalGen,sqrt(totalGenErr),totalMis,sqrt(totalMisErr),totalHad,sqrt(totalHadErr),totalFak,sqrt(totalFakErr), totalGen+totalMis+totalHad+totalFak,sqrt(totalMCErr)) # calculate error propagate
line += "\\hline \n"
line += "Data &  &  &  &  & $%i $ \\\\ \n"%(nPhotonData) 
line += "\\hline \n"

line += "\\end{tabular} \n"
line += "} \n"
line += "\\end{frame} \n"

with open("photonCategoryYield_%s_%s_%s.tex"%(channel,selYear,mydistributionName),"w") as _file:
    _file.write(line)

_file.close()

#shutil.copy("photonCategoryYield_%s_%s_%s.tex"%(channel,selYear,mydistributionName),"CombineFitting/AllTexFiles")

#os.remove("photonCategoryYield_%s_%s_%s.tex"%(channel,selYear,mydistributionName))















