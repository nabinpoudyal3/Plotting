from ROOT import TFile, Double, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory
#from ROOT import *
import os

import numpy
import sys
from optparse import OptionParser
from sampleInformation import sampleList
import sampleInformation
from numpy import log10, sqrt
from array import array

#from getFullYearMisIDEleSF import getFullYearMisIDEleSF
from getMisIDEleSF import getMisIDEleSF
from getZJetsSF import getZJetsSF

from colorama import Fore, Back, Style 

padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
parser = OptionParser()
parser.add_option("-y", "--year", dest="Year", default="",type='str',
					help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-c", "--channel", dest="channel", default="",type='str',
					help="Specify which channel Mu or Ele? default is Mu" )

parser.add_option("--nBinss", dest="nBinss", default="",type='str',
					help="Number of bins in template plot" )

parser.add_option("--template", dest="template", default=False,action="store_true",
					help="post fit plots" )
	
parser.add_option("--postfitPlots", dest="postfitPlots", default=False,action="store_true",
					help="post fit plots" )

parser.add_option("--prefitPlots", dest="prefitPlots", default=False,action="store_true",
					help="pre fit plots" )

parser.add_option("--syst", "--systematics", dest="systematics", default="",type='str',
					help="Specify which systematic plots" )

parser.add_option("--level", dest="level", default="",type='str',
					help="Specify which level Up or Down" )
								
parser.add_option("--tight", dest="tight", default=False,action="store_true",
					help="draw photon Category for tight selection" )

parser.add_option("--looseCRge2ge0", dest="looseCRge2ge0", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 ge0" )

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

parser.add_option("--LooseCRe3e1","--looseCRe3e1", dest="looseCRe3e1", default=False,action="store_true",
                     help="Use ==3 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe2e2","--looseCRe2e2", dest="looseCRe2e2", default=False,action="store_true",
                     help="Use ==2 jets + ==2 bjets selection" ) 

parser.add_option("--LooseCRe3ge2","--looseCRe3ge2", dest="looseCRe3ge2", default=False,action="store_true",
                     help="Use ==3 jets + >=2 bjets selection" )  

parser.add_option("--useQCDMC","--qcdMC",dest="useQCDMC", default=False, action="store_true",
		  			 help="")

parser.add_option("--useQCDCR",dest="useQCDCR", default=False, action="store_true",
                     help="to make plots in QCDCR region")

parser.add_option("--noQCD",dest="noQCD", default=False, action="store_true",
		help="")
		
(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print(Fore.RED + "Specify which year 2016, 2017 or 2018?")
	sys.exit()
	
systematics = options.systematics
level=options.level
finalState = options.channel

postfitPlots = options.postfitPlots
prefitPlots   = options.prefitPlots

tight = options.tight
looseCRge2ge0=options.looseCRge2ge0
looseCRge2e0 =options.looseCRge2e0
looseCRe2e0  =options.looseCRe2e0
looseCRe2e1  =options.looseCRe2e1
looseCRe3e0  =options.looseCRe3e0
looseCRge4e0 =options.looseCRge4e0
looseCRe3e1  =options.looseCRe3e1
looseCRe2e2  =options.looseCRe2e2
looseCRe3ge2 =options.looseCRe3ge2
useQCDMC = options.useQCDMC
useQCDCR = options.useQCDCR
noQCD = options.noQCD

nBinss = options.nBinss

template = options.template

if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
#######
########

#allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","Pdf","fsr","isr"]
allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","fsr","isr","prefireEcal","JER","JECTotal"]
if systematics in allsystematics: print "running on systematics", systematics
else: print(Fore.RED + "systematics is not in the list. Add the systematic in the list, if you are running for systematics.")

print(Style.RESET_ALL) 

if level=='up': mylevel='Up'
if level=='down': mylevel='Down'

crName=""

if tight:      #SR8 
	isSelectionDir = "tight"
	crName = "SR8"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_tightplots_%s/"%(selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"

	else:
		fileDir     = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_tightplots_%s/"%(selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"

if looseCRge2ge0:  #AR
	isSelectionDir = "looseCRge2ge0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge2ge0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRge2ge0plots_%s/"%(selYear)

	else:
		fileDir     = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRge2ge0plots_%s/"%(selYear)
		regionText = "N_{j}#geq2, N_{b}#geq0"

if looseCRge2e0:  #CR1+CR2+CR3 ZJetSF = getZJetsSF(selYear,isSelectionDir)
	isSelectionDir = "looseCRge2e0"
	crName="CR123"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge2e0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRge2e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "misIDEle_syst_looseCRge2e0plots_%s/"%(selYear)		
	else:
		fileDir     = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRge2e0plots_%s_%s/"%(channel,selYear)
		plotDirectoryTemplate = "misIDEle_syst_looseCRge2e0plots_%s/"%(selYear)		
		regionText = "N_{j}#geq2, N_{b}=0"

###
if looseCRe2e0:  #CR1
	isSelectionDir = "looseCRge2e0"
	crName="CR1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 			
	fileDirQCD  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe2e0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe2e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "misIDEle_syst_looseCRe2e0plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe2e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "misIDEle_syst_looseCRe2e0plots_%s/"%(selYear)		

		regionText = "N_{j}=2, N_{b}=0"

if looseCRe3e0:  #CR2
	isSelectionDir = "looseCRge2e0"
	crName="CR2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe3e0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe3e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "misIDEle_syst_looseCRe3e0plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe3e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "misIDEle_syst_looseCRe3e0plots_%s/"%(selYear)		

		regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0:  #CR3
	isSelectionDir = "looseCRge2e0"
	crName="CR3"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge4e0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRge4e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "misIDEle_syst_looseCRge4e0plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRge4e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "misIDEle_syst_looseCRge4e0plots_%s/"%(selYear)		

		regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe2e1:  #CR4
	isSelectionDir = "looseCRe2e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe2e1/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe2e1plots_%s/"%(selYear)

	else:
		fileDir  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe2e1plots_%s/"%(selYear)
		regionText = "N_{j}=2, N_{b}=1"
	
if looseCRe3e1:  #CR5
	isSelectionDir = "looseCRe3e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe3e1/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe3e1plots_%s/"%(selYear)

	else:	
		fileDir     = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe3e1plots_%s/"%(selYear)
		regionText = "N_{j}=3, N_{b}=1"

if looseCRe2e2:  #CR6
	isSelectionDir = "looseCRe2e2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe2e2/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe2e2plots_%s/"%(selYear)

	else:	
		fileDir     = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe2e2plots_%s/"%(selYear)
		regionText = "N_{j}=2, N_{b}=2"

if looseCRe3ge2:  #CR7
	isSelectionDir = "looseCRe3ge2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe3ge2/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe3ge2plots_%s/"%(selYear)
	else:
		fileDir     = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe3ge2plots_%s/"%(selYear)
		regionText = "N_{j}=3, N_{b}#geq2"

###
####

eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
localFolder="/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/"

fileDir = eosFolder+fileDir
fileDirQCD = eosFolder+fileDirQCD
print fileDir

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)
	
if not os.path.exists(plotDirectoryTemplate):
	os.mkdir(plotDirectoryTemplate)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
from Style import *
gROOT.ForceStyle()
if selYear=='2016': myMisIDEle="MisIDEleSixteen"
elif selYear=='2017': myMisIDEle="MisIDEleSeventeen"
else: myMisIDEle="MisIDEleEighteen"

sampleList = ['TTGamma', 'TTbar','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
# template_category = {"myWGamma":kRed, "myZGamma":kOrange, "myBackground":kBlue, "myTotal":kGreen+1 }
template_category = {myMisIDEle:kRed, "ZgammaBkgPhoton":kOrange, "WgammaBkgPhoton":kBlue, "OtherSampleBkgPhoton":kGreen+1 }
hist_category = {"GenuinePhoton":kOrange, "MisIDEle":kRed, "HadronicPhoton":kBlue, "HadronicFake":kGreen+1 }
template_categoryName = {myMisIDEle:"misID ele", "ZgammaBkgPhoton":"Z#gamma", "WgammaBkgPhoton":"W#gamma", "OtherSampleBkgPhoton":"other","Total":"total" }

_file = {}

import CMS_lumi

if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"

if useQCDMC:
	if channel=="mu":	sampleList[-1] = "QCDMu"
	if channel=="ele":	sampleList[-1] = "QCDEle"
elif noQCD:
	sampleList.remove("QCD")
	sampleList.remove("GJets") 
else:
	sampleList[-1] = "QCD_DD"
	sampleList.remove("GJets") 
	#samples["QCD_DD"] = [[],kGreen+3,"Multijet",isMC]

print sampleList

H = 600;
W = 800;
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

legendHeightPer = 0.04

legendStart = 0.6
legendEnd = 0.97-(R/W)

legend = TLegend(legendStart, 1-T/H-0.01 - legendHeightPer*(len(template_category)+4), legendEnd, 0.99-(T/H)-0.01)
legend.SetBorderSize(0)
legend.SetFillColor(0)

TGaxis.SetMaxDigits(3)
# histName    = "phosel_LeadingPhotonEt_%s_%s"
# histNameData= "phosel_LeadingPhotonEt_%s"

# histName    = "phosel_noCut_SIEIE_%s_%s"
# histNameData= "phosel_noCut_SIEIE_%s"

histName    = "phosel_MassEGamma_%s_%s"
histNameData= "phosel_MassEGamma_%s"

mydistributionName = histNameData[7:-3]

myfilename = "misIDEle_syst_Prefit"

templateHist ={}

for sample in sampleList:
	if sample=="QCD_DD": 
		#print "==>",sample, fileDirQCD
		_file[sample] = TFile.Open('%s%s.root'%(fileDirQCD,sample),'read')
	else:
		#print sample, fileDir
		_file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')

#print _file["QCD_DD"]	

templateHist[myMisIDEle]        = None
templateHist["ZgammaBkgPhoton"] = None
templateHist["WgammaBkgPhoton"] = None
templateHist["OtherSampleBkgPhoton"] = None 

for sample in sampleList:
	if sample == "QCD_DD": continue
	item = "MisIDEle"
	tempHist = _file[sample].Get(histName%(item,sample))
	# scale the ZJetSF
	if sample=="ZJets": 
		tempHist.Scale(ZJetSF)  #ZJetSF for misIDEle
		print "%s; ZJetSF==%s"%(sample,ZJetSF)
	if templateHist[myMisIDEle] is None:
		templateHist[myMisIDEle] = tempHist.Clone(myMisIDEle)
		templateHist[myMisIDEle].SetDirectory(0)
	else:
		templateHist[myMisIDEle].Add(tempHist)


for sample in sampleList:
	if sample=='WGamma':
		for item in ["GenuinePhoton","HadronicPhoton","HadronicFake"]:
			tempHist = _file[sample].Get(histName%(item,sample))
			if templateHist["WgammaBkgPhoton"] is None:
				templateHist["WgammaBkgPhoton"] = tempHist.Clone("WgammaBkgPhoton")
				templateHist["WgammaBkgPhoton"].SetDirectory(0)
			else:
				templateHist["WgammaBkgPhoton"].Add(tempHist)
	elif sample=='ZGamma':
		for item in ["GenuinePhoton","HadronicPhoton","HadronicFake"]:
			tempHist = _file[sample].Get(histName%(item,sample))
			if templateHist["ZgammaBkgPhoton"] is None:
				templateHist["ZgammaBkgPhoton"] = tempHist.Clone("ZgammaBkgPhoton")
				templateHist["ZgammaBkgPhoton"].SetDirectory(0)
			else:
				templateHist["ZgammaBkgPhoton"].Add(tempHist)
	elif sample=="QCD_DD":
		tempHist = _file[sample].Get(histNameData%(sample))
		if templateHist["OtherSampleBkgPhoton"] is None:
			templateHist["OtherSampleBkgPhoton"] = tempHist.Clone("OtherSampleBkgPhoton")
			templateHist["OtherSampleBkgPhoton"].SetDirectory(0)
		else:
			templateHist["OtherSampleBkgPhoton"].Add(tempHist)
	else:
		for item in ["GenuinePhoton","HadronicPhoton","HadronicFake"]:
			tempHist = _file[sample].Get(histName%(item,sample))
			if sample=="ZJets": tempHist.Scale(ZJetSF)  #ZJetSF for rest
			if templateHist["OtherSampleBkgPhoton"] is None:
				templateHist["OtherSampleBkgPhoton"] = tempHist.Clone("OtherSampleBkgPhoton")
				templateHist["OtherSampleBkgPhoton"].SetDirectory(0)
			else:
				templateHist["OtherSampleBkgPhoton"].Add(tempHist)

if systematics=='':
	if finalState=='Ele':
		sample = "DataEle"
		_file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
		dataHist = _file[sample].Get(histNameData%(sample))
		dataHist.SetLineColor(kBlack)
		dataHist.SetMarkerStyle(8)
			
	elif finalState=='Mu':
		sample = "DataMu"
		_file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
		dataHist = _file[sample].Get(histNameData%(sample))
		dataHist.SetLineColor(kBlack)
		dataHist.SetMarkerStyle(8)
	else:
		print "Select the channel !!!"
		sys.exit()	
	
	data_obs = dataHist.Clone("data_obs")

## input to combine , open root file


#for event yield purpose:

	lastbin = 0
	totalMC = 0
	totalMCerror = 0
	line = ""
	line += "\\begin{tabular} {|l|l|} \n"
	line += "\\hline \n"
	nEventData = data_obs.Integral(-1,-1,"width")
	if prefitPlots:
		for ih in templateHist:
			error = Double(0.)
			nEvents = templateHist[ih].IntegralAndError(-1,-1,error,"width")
			totalMC += nEvents
			totalMCerror += error*error
			line += "%s & $%.2f \\pm %.2f$  \\\\ \n"%(ih, nEvents, error) 
			line += "\\hline \n"

		#print "prefit==>",nEventData, totalMC, sqrt(totalMCerror)
		line += "Data = %.2f & MC = $%.2f \\pm %.2f$  \\\\ \n"%(nEventData, totalMC, sqrt(totalMCerror)) 
		line += "\\end{tabular}\n"
		print line



if channel =='ele':
	binning = numpy.array([0,80,84,88,92,96,100,180.])
else:
	binning = numpy.array([0,91.,180.])
	

binWidth = numpy.diff(binning)

rebinnedHist ={} 
for ih in templateHist:
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])

if systematics=='': rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)


if template:
	myfile = TFile("%s%s.root"%(plotDirectoryTemplate,myfilename),"update")
	# i have to get the nominal histogram from root file first and get the integration value
	if systematics=='':
		myDatahist = rebinnedData.Clone("nominal")
		mydataDir  = "%s/data_obs/"%channel

		if myfile.GetDirectory(mydataDir):
			gDirectory.cd(mydataDir)
			gDirectory.Delete("*;*")
			myDatahist.Write()
		else:
			gDirectory.mkdir(mydataDir)
			gDirectory.cd(mydataDir)
			gDirectory.Delete("*;*")
			myDatahist.Write()
	# create directory only if it does not exist
	### ele channel
	for iprocess in template_category.keys():
		print "process:", iprocess
		print "----------------"
		myfile.cd()
		mydir =  "%s/%s/"%(channel,iprocess) 
		#print "%s/%s/"%(channel,iprocess) 

		if systematics=='':
			myhist = rebinnedHist[iprocess].Clone("nominal")
		else:
			myhist = rebinnedHist[iprocess].Clone("%s%s"%(systematics,mylevel))
			if systematics in ["Q2","Pdf","isr","fsr"]:
				myNominalHist = myfile.Get(mydir+"nominal")
				valNominal = myNominalHist.Integral()
				val = myhist.Integral()
				print "nominal", valNominal, " ==> ", "syst %s"%systematics,val
				myhist.Scale(valNominal/val)
				print "normalized", myhist.Integral()
		
		if myfile.GetDirectory(mydir):
			gDirectory.cd(mydir)
			if systematics=='':
				gDirectory.Delete("nominal;*")
			else:
				gDirectory.Delete("%s%s;*"%(systematics,mylevel))
			myhist.Write()
		else:
			gDirectory.mkdir(mydir)
			gDirectory.cd(mydir)
			if systematics=='':
				gDirectory.Delete("nominal;*")
			else:
				gDirectory.Delete("%s%s;*"%(systematics,mylevel))
			myhist.Write()
	print "rootbrowse %s%s.root"%(plotDirectoryTemplate,myfilename)
	print "---------------------------------------------------------------------------"
	myfile.Close()
else:
	if prefitPlots:
		rebinnedData.Scale(1.,"width")
		nEventData = rebinnedData.Integral("width")

		for ih in rebinnedHist:
			rebinnedHist[ih].Scale(1.,"width")
					
		stack = THStack()
		stack.Add(rebinnedHist['OtherSampleBkgPhoton'])
		stack.Add(rebinnedHist['WgammaBkgPhoton'])
		stack.Add(rebinnedHist['ZgammaBkgPhoton'])
		stack.Add(rebinnedHist[myMisIDEle])


		
	if postfitPlots:
		rebinnedData.Scale(1.,"width")
		nEventData = rebinnedData.Integral("width")
		if finalState=="Ele": filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/MisIDEleFittingSystematicsSeparateYear/fitDiagnostics%s_%s.root"%(crName,selYear)
		if finalState=="Mu":  filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/MisIDEleFittingSystematicsSeparateYear/fitDiagnostics%s_%s.root"%(crName,selYear)

		Postfile = TFile(filename,"read")
		
		templatePostHist = {}
		# print len(binning),"==>",len(binWidth)
		templatePostHist["OtherSampleBkgPhoton"] = TH1F("OtherSampleBkgPhoton" ,"",len(binWidth),binning)
		templatePostHist["WgammaBkgPhoton"]      = TH1F("WgammaBkgPhoton"      ,"",len(binWidth),binning)
		templatePostHist["ZgammaBkgPhoton"]      = TH1F("ZgammaBkgPhoton"      ,"",len(binWidth),binning)   
		templatePostHist[myMisIDEle]             = TH1F( myMisIDEle            ,"",len(binWidth),binning)  
 

		for process in template_category.keys():
			tempHist = None
			tempHist = Postfile.Get("shapes_fit_s/%s/%s"%(channel,process))
			for ibin in range(1,len(binning)):
				myBinContent = tempHist.GetBinContent(ibin)
				templatePostHist[process].SetBinContent(ibin,myBinContent)
			templatePostHist[process].SetLineColor(template_category[process])
			templatePostHist[process].SetFillColor(template_category[process])
			templatePostHist[process].Scale(1.,"width")

			error = Double(0.)
			lastbin = templatePostHist[process].GetNbinsX()
			nEvents = templatePostHist[process].IntegralAndError(1,lastbin,error,"width")
			totalMC += nEvents
			totalMCerror += error*error
			line += "%s & $%.2f \\pm %.2f$  \\\\ \n"%(process, nEvents, error) 
			line += "\\hline \n"

		#print "prefit==>",nEventData, totalMC, sqrt(totalMCerror)
		line += "Data = %.2f & MC = $%.2f \\pm %.2f$  \\\\ \n"%(nEventData, totalMC, sqrt(totalMCerror)) 
		line += "\\end{tabular}\n"
			
			
		stack = THStack()
		stack.Add(templatePostHist['OtherSampleBkgPhoton'])
		stack.Add(templatePostHist['WgammaBkgPhoton'])
		stack.Add(templatePostHist['ZgammaBkgPhoton'])
		stack.Add(templatePostHist[myMisIDEle])
		
		mytestHistogram = stack.GetStack().Last().Clone("mytestHistogram")
		#x = rebinnedData.Chi2Test(rebinnedMC,"WW CHI2/NDF") 
		#chi2Text = "#chi^{2}/NDF=%.2f"%x

		
	canvasRatio = TCanvas('c1Ratio','c1Ratio',W,H)
	canvasRatio.SetFillColor(0)
	canvasRatio.SetBorderMode(0)
	canvasRatio.SetFrameFillStyle(0)
	canvasRatio.SetFrameBorderMode(0)
	canvasRatio.SetLeftMargin( L/W )
	canvasRatio.SetRightMargin( R/W )
	canvasRatio.SetTopMargin( T/H )
	canvasRatio.SetBottomMargin( B/H )
	canvasRatio.SetTickx(0)
	canvasRatio.SetTicky(0)
	canvasRatio.Draw()
	canvasRatio.cd()

	pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
	pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
	pad1.SetLeftMargin( L/W )
	pad1.SetRightMargin( R/W )
	pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
	pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
	pad1.SetFillColor(0)
	pad1.SetBorderMode(0)
	pad1.SetFrameFillStyle(0)
	pad1.SetFrameBorderMode(0)
	pad1.SetTickx(0)
	pad1.SetTicky(0)

	pad2.SetLeftMargin( L/W )
	pad2.SetRightMargin( R/W )
	pad2.SetTopMargin( (padOverlap)/(padRatio+padOverlap) )
	pad2.SetBottomMargin( B/H/(padRatio+padOverlap) )
	pad2.SetFillColor(0)
	pad2.SetFillStyle(4000)
	pad2.SetBorderMode(0)
	pad2.SetFrameFillStyle(0)
	pad2.SetFrameBorderMode(0)
	pad2.SetTickx(0)
	pad2.SetTicky(0)

	pad1.Draw()
	pad2.Draw()

	noData = False

	oneLine = TF1("oneline","1",-9e9,9e9)
	oneLine.SetLineColor(kBlack)
	oneLine.SetLineWidth(1)
	oneLine.SetLineStyle(2)

	maxVal = stack.GetMaximum()
	if not noData: 
	    maxVal = max(rebinnedData.GetMaximum(),maxVal)

	minVal = 0
	# minVal = max(stack.GetStack()[0].GetMinimum(),1)
	stack.SetMaximum(1.75*maxVal)
	stack.SetMinimum(minVal)

	errorband=stack.GetStack().Last().Clone("error")
	errorband.Sumw2()
	errorband.SetLineColor(kBlack)
	errorband.SetFillColor(kBlack)
	errorband.SetFillStyle(3245)
	errorband.SetMarkerSize(0)

	##### Uncertainty
	#h1_up={}
	#h1_do={}
	#for sample in stackList:
	#	h1_up[sample]={}
	#	h1_do[sample]={}
	#	for sys in systematics:		
	#		if sys=="Q2" or sys=="Pdf" or sys=="isr" or sys=="fsr":
	#			if sample not in ["TTbar","TTGamma"]:continue
	#
	#			print sample,sys
	#			
	#			if sample=="QCD_DD": 
	#				h1_up[sample][sys]=qcdHist.Clone("%s_%s_up"%(sys,sample))
	#				h1_do[sample][sys]=qcdHist.Clone("%s_%s_do"%(sys,sample))
	#		
	#			elif sample=="TTGamma" and (sys=="Pdf" or sys=="Q2"):
	#				#print sample,sys
	#				h1_up[sample][sys]=_filesys_up[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_up"%(sys,sample))
	#				h1_do[sample][sys]=_filesys_down[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_do"%(sys,sample))	
	#				total=_file[sample].Get("%s_%s"%(histName,sample)).Integral()
	#				h1_up[sample][sys].Scale(total/h1_up[sample][sys].Integral())
	#				h1_do[sample][sys].Scale(total/h1_do[sample][sys].Integral())
	#			elif sample=="TTbar" and sys=="Q2":
	#				#print sample, sys, _filesys_up[sample][sys], _filesys_down[sample][sys], "%s_%s"%(histName,sample) 	
	#				h1_up[sample][sys]=_filesys_up[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_up"%(sys,sample))
	#				h1_do[sample][sys]=_filesys_down[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_do"%(sys,sample))     
	#				total=_file[sample].Get("%s_%s"%(histName,sample)).Integral()
	#				h1_up[sample][sys].Scale(total/h1_up[sample][sys].Integral())
	#				h1_do[sample][sys].Scale(total/h1_do[sample][sys].Integral())
	#			
	#			else:
	#		#		print sample, sys, _filesys_down[sample][sys], histName
	#				h1_up[sample][sys]=_filesys_up[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_up"%(sys,sample))
	#				h1_do[sample][sys]=_filesys_down[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_do"%(sys,sample))
	#
	#			if type(plotInfo[2]) is type(list()):
	#			
	#			
	#				h1_up[sample][sys] = h1_up[sample][sys].Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
	#				h1_do[sample][sys] = h1_do[sample][sys].Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
	#				h1_do[sample][sys].Scale(1,"width")
	#				h1_up[sample][sys].Scale(1,"width")
	#
	#			else:
	#				h1_up[sample][sys].Rebin(plotInfo[2])
	#				h1_do[sample][sys].Rebin(plotInfo[2])
	#	error=0.
	#	diff={}		
	#	sum_={}
	#	for i_bin in range(1,errorband.GetNbinsX()+1):
	#		if isLooseCRe3g1Selection or Dilepmass:continue
	#		sum_[i_bin]=0.	
	#		diff[i_bin]=[]
	#		for sys in systematics:
	#			for sample in stackList:
	#				if "phosel_PhotonCategory" in histName:
	#					if sample=="QCD_DD":continue			
	#				if sys=="Q2" or sys=="Pdf" or sys=="isr" or sys=="fsr":
	#					if sample not in ["TTbar","TTGamma"]:continue
	#				if finalState=="Mu" and "ele" in histName:continue
	#				if finalState=="Ele" and "mu" in histName:continue
	#				if finalState=="Mu" and "MassEGamma" in histName:continue
	#				print "adding sys",sample,sys, ((h1_up[sample][sys].GetBinContent(i_bin)-h1_do[sample][sys].GetBinContent(i_bin))/2.)**2
	#				sum_[i_bin]+=((h1_up[sample][sys].GetBinContent(i_bin)-h1_do[sample][sys].GetBinContent(i_bin))/2.)**2
	#			#diff[i_bin].append(((h1_up[sample][sys].GetBinContent(i_bin)-h1_do[sample][sys].GetBinContent(i_bin))/2.)**2.)
	#			
	# 
	#		print (sum_[i_bin])**0.5		
	#		errorband.SetBinError(i_bin,(sum_[i_bin])**0.5)
	##### Uncertainty end

	legend.AddEntry(rebinnedData,"Data", 'pe')
	legend.AddEntry(errorband,"Uncertainty","f")

	for ih in rebinnedHist:
		if ih=='Total':continue
		legend.AddEntry(rebinnedHist[ih],template_categoryName[ih],'f')

	pad1.cd()

	stack.Draw('HIST')
	rebinnedData.Draw('E,X0,SAME')
	legend.Draw("same")
	stack.GetXaxis().SetTitle('')
	stack.GetXaxis().SetLabelSize(0)
	stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
	stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
	stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
	stack.SetTitle(';;<Events/GeV>')# '%rebin)

	#CMS_lumi.channelText = (channelText+"\\n"+regionText)
	#if postfitPlots: CMS_lumi.channelText =channelText+"\\n "+regionText+"\\n "+chi2Text

	CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText,regionText)
	#if postfitPlots: CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText+";"+regionText,chi2Text)

	CMS_lumi.writeChannelText = True
	CMS_lumi.writeExtraText = True
	CMS_lumi.CMS_lumi(pad1, 4, 11)

	if not noData:
		ratio = rebinnedData.Clone("temp")
		temp = stack.GetStack().Last().Clone("temp")
		for i_bin in range(1,temp.GetNbinsX()+1):
			temp.SetBinError(i_bin,0.)
		ratio.Divide(temp)
	else:
		ratio = rebinnedData.Clone("temp")
		temp = stack.GetStack().Last().Clone("temp")
	    
	ratio.SetTitle('')
	ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
	ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
	ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
	ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
	ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap-padGap))

	maxRatio = ratio.GetMaximum()
	minRatio = ratio.GetMinimum()

	for i_bin in range(1,ratio.GetNbinsX()):
		if ratio.GetBinError(i_bin)<1:
			if ratio.GetBinContent(i_bin)>maxRatio:
				maxRatio = ratio.GetBinContent(i_bin)
			if ratio.GetBinContent(i_bin)<minRatio:
				minRatio = ratio.GetBinContent(i_bin)

	if maxRatio > 1.8:
		ratio.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
	elif maxRatio < 1:
		ratio.GetYaxis().SetRangeUser(0,1.2)
	elif maxRatio-1 < 1-minRatio:
		ratio.GetYaxis().SetRangeUser((1-(1-minRatio)*1.2),1.1*maxRatio)		
	else:
		ratio.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)

	ratio.GetYaxis().SetRangeUser(0.8,1.2)
	ratio.GetYaxis().SetNdivisions(504)
	if channel == 'ele': ratio.GetXaxis().SetTitle('m_{e,#gamma} GeV')
	else: ratio.GetXaxis().SetTitle('m_{#mu,#gamma} GeV')
	ratio.GetYaxis().SetTitle("Data/MC")
	ratio.GetYaxis().SetTitleOffset(.4)
	ratio.GetYaxis().SetTitleSize(.09)
	ratio.GetYaxis().SetNdivisions(2)

	CMS_lumi.CMS_lumi(pad2, 4, 11)
	pad2.cd()
	ratio.SetMarkerStyle(rebinnedData.GetMarkerStyle())
	ratio.SetMarkerSize(rebinnedData.GetMarkerSize())
	ratio.SetLineColor(rebinnedData.GetLineColor())
	ratio.SetLineWidth(rebinnedData.GetLineWidth())
	ratio.Draw('e,x0')
	errorbandRatio = errorband.Clone("errorRatio")
	errorbandRatio.Divide(temp)
	errorbandRatio.Draw('e2,same')
	oneLine.Draw("same")

	canvasRatio.Update()
	canvasRatio.RedrawAxis()
	print plotDirectory
	if postfitPlots:
		canvasRatio.SaveAs("%s%s_massEG_Postfit.root"%(plotDirectory,plotDirectory[:-1]))
		canvasRatio.Print("%s%s_massEG_Postfit.pdf" %(plotDirectory,plotDirectory[:-1]))
	else:
		canvasRatio.SaveAs("%s%s_massEG.root"%(plotDirectory,plotDirectory[:-1]))
		canvasRatio.Print("%s%s_massEG.pdf" %(plotDirectory,plotDirectory[:-1]))
	canvasRatio.Close()

	if postfitPlots:
		with open("EventYieldTables/EventsYield_%s_%s_%s_%s_postfit.tex"%(crName,channel,selYear,mydistributionName),"w") as _file:
	   			_file.write(line)
		_file.close()
	else:
		with open("EventYieldTables/EventsYield_%s_%s_%s_%s_prefit.tex"%(crName,channel,selYear,mydistributionName),"w") as _file:
	   			_file.write(line)
		_file.close()
    


    
