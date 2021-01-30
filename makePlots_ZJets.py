from ROOT import TFile, TLegend, TCanvas,gPad, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory
#from ROOT import *
import os

import numpy
import sys
from optparse import OptionParser
from sampleInformation import sampleList
import sampleInformation
from numpy import log10
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
					
parser.add_option("--prefitPlots", dest="prefitPlots", default=False,action="store_true",
					help="pre fit plots" )
					
parser.add_option("--postfitPlots", dest="postfitPlots", default=False,action="store_true",
					help="post fit plots" )

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

nBinss = options.nBinss # this is a test

template = options.template

if finalState=='DiMu':
	channel = 'mu'
	channelText = "#mu#mu+jets"
if finalState=='DiEle':
	channel = 'ele'
	channelText = "ee+jets"
#######
########

allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","Pdf","fsr","isr", "prefireEcal","JER", "JECTotal"]
#allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2"]#,"fsr","isr","Pdf"]
if systematics in allsystematics: print "running on systematics", systematics
else: print(Fore.RED + "systematics is not in list. Add the systematics in the list if you are running for systematics.")

print(Style.RESET_ALL) 

if level=='up': mylevel='Up'
if level=='down': mylevel='Down'

isSelectionDir = ""
crName=""
if tight:      #SR8 
	crName="SR8"
	isSelectionDir = "tight"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/Dilep_hists_tight/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/Dilep_hists_%s_%s_tight/"%(selYear, channel,systematics,level)
		plotDirectory = "ZJets_syst_tightplots_%s/"%(selYear)
		plotDirectoryTemplate = "ZJets_syst_tightplots_%s/"%(selYear)		
		regionText = "N_{j}#geq4, N_{b}#geq1"

	else:
		fileDir     = "histograms_%s/%s/Dilep_hists_tight/"%(selYear, channel)
		plotDirectory = "ZJets_syst_tightplots_%s/"%(selYear)
		plotDirectoryTemplate = "ZJets_syst_tightplots_%s/"%(selYear)		
		regionText = "N_{j}#geq4, N_{b}#geq1"

if looseCRge2e0:  #CR1+CR2+CR3 ZJetSF = getZJetsSF(selYear,isSelectionDir)
	crName="CR123"
	isSelectionDir = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/Dilep_hists_looseCRge2e0/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/Dilep_hists_%s_%s_looseCRge2e0/"%(selYear, channel,systematics,level)
		plotDirectory = "ZJets_syst_looseCRge2e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRge2e0plots_%s/"%(selYear)		
	else:
		fileDir     = "histograms_%s/%s/Dilep_hists_looseCRge2e0/"%(selYear, channel)
		plotDirectory = "ZJets_syst_looseCRge2e0plots_%s_%s/"%(channel,selYear)
		plotDirectoryTemplate = "ZJets_syst_looseCRge2e0plots_%s/"%(selYear)		
		regionText = "N_{j}#geq2, N_{b}=0"

###
if looseCRe2e0:  #CR1
	crName="CR1"
	isSelectionDir = "looseCRe2e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 			
	fileDirQCD  = "histograms_%s/%s/Dilep_hists_looseCRe2e0/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/Dilep_hists_%s_%s_looseCRe2e0/"%(selYear, channel,systematics,level)
		plotDirectory = "ZJets_syst_looseCRe2e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe2e0plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/Dilep_hists_looseCRe2e0/"%(selYear, channel)
		plotDirectory = "ZJets_syst_looseCRe2e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe2e0plots_%s/"%(selYear)		
		regionText = "N_{j}=2, N_{b}=0"

if looseCRe3e0:  #CR2
	crName="CR2"
	isSelectionDir = "looseCRe3e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/Dilep_hists_looseCRe3e0/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/Dilep_hists_%s_%s_looseCRe3e0/"%(selYear, channel,systematics,level)
		plotDirectory = "ZJets_syst_looseCRe3e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe3e0plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/Dilep_hists_looseCRe3e0/"%(selYear, channel)
		plotDirectory = "ZJets_syst_looseCRe3e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe3e0plots_%s/"%(selYear)		
		regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0:  #CR3
	isSelectionDir = "looseCRge4e0"
	crName="CR3"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/Dilep_hists_looseCRge4e0/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/Dilep_hists_%s_%s_looseCRge4e0/"%(selYear, channel,systematics,level)
		plotDirectory = "ZJets_syst_looseCRge4e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRge4e0plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/Dilep_hists_looseCRge4e0/"%(selYear, channel)
		plotDirectory = "ZJets_syst_looseCRge4e0plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRge4e0plots_%s/"%(selYear)		
		regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe2e1:  #CR4
	crName="CR4"
	isSelectionDir = "looseCRe2e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/Dilep_hists_looseCRe2e1/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/Dilep_hists_%s_%s_looseCRe2e1/"%(selYear, channel,systematics,level)
		plotDirectory = "ZJets_syst_looseCRe2e1plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe2e1plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/Dilep_hists_looseCRe2e1/"%(selYear, channel)
		plotDirectory = "ZJets_syst_looseCRe2e1plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe2e1plots_%s/"%(selYear)	
		regionText = "N_{j}=2, N_{b}=1"
	
if looseCRe3e1:  #CR5
	crName="CR5"
	isSelectionDir = "looseCRe3e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/Dilep_hists_looseCRe3e1/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/Dilep_hists_%s_%s_looseCRe3e1/"%(selYear, channel,systematics,level)
		plotDirectory = "ZJets_syst_looseCRe3e1plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe3e1plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/Dilep_hists_looseCRe3e1/"%(selYear, channel)
		plotDirectory = "ZJets_syst_looseCRe3e1plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe3e1plots_%s/"%(selYear)	
		regionText = "N_{j}=3, N_{b}=1"

if looseCRe2e2:  #CR6
	crName="CR6"
	isSelectionDir = "looseCRe2e2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/Dilep_hists_looseCRe2e2/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/Dilep_hists_%s_%s_looseCRe2e2/"%(selYear, channel,systematics,level)
		plotDirectory = "ZJets_syst_looseCRe2e2plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe2e2plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/Dilep_hists_looseCRe2e2/"%(selYear, channel)
		plotDirectory = "ZJets_syst_looseCRe2e2plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe2e2plots_%s/"%(selYear)	
		regionText = "N_{j}=2, N_{b}=2"

if looseCRe3ge2:  #CR7
	crName="CR7"
	isSelectionDir = "looseCRe3ge2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); 
	fileDirQCD  = "histograms_%s/%s/Dilep_hists_looseCRe3ge2/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/Dilep_hists_%s_%s_looseCRe3ge2/"%(selYear, channel,systematics,level)
		plotDirectory = "ZJets_syst_looseCRe3ge2plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe3ge2plots_%s/"%(selYear)		


	else:
		fileDir     = "histograms_%s/%s/Dilep_hists_looseCRe3ge2/"%(selYear, channel)
		plotDirectory = "ZJets_syst_looseCRe3ge2plots_%s_%s/"%(channel,selYear)		
		plotDirectoryTemplate = "ZJets_syst_looseCRe3ge2plots_%s/"%(selYear)	
		regionText = "N_{j}=3, N_{b}#geq2"

###
####



eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
#localFolder="/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/"

fileDir = eosFolder + fileDir
fileDirQCD = eosFolder + fileDirQCD
print fileDir
#print fileDirQCD

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)
	
if not os.path.exists(plotDirectoryTemplate):
	os.mkdir(plotDirectoryTemplate)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
from Style import *
gROOT.ForceStyle()


sampleList = ['TTGamma','TTbar', 'SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]

template_category = {"myZJets":kGreen+1, "myBackground":kRed }
template_category_name = {"myZJets":"ZJets", "myBackground":"background" }

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

histName    = "presel_DilepMass_%s"
histNameData= "presel_DilepMass_%s"

myfilename = "ZJets_syst_Prefit"

templateHist ={}

for sample in sampleList:
	if useQCDMC:
		if finalState == 'DiEle' and sample == 'QCD': sample = 'QCDEle'
		if finalState == 'DiMu'  and sample == 'QCD': sample = 'QCDMu'

	if sample=="QCD_DD": 
		#print "==>",sample, fileDirQCD
		_file[sample] = TFile.Open('%s%s.root'%(fileDirQCD,sample),'read')
	else:
		#print sample, fileDir
		_file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')

#print _file["QCD_DD"]	

templateHist["myZJets"]      = None
templateHist["myBackground"] = None


for sample in sampleList:
	if sample=='ZJets':
		tempHist = _file[sample].Get(histName%(sample))
		if templateHist["myZJets"] is None:
			templateHist["myZJets"] = tempHist.Clone("ZJets")
			templateHist["myZJets"].SetDirectory(0)
		else:
			templateHist["myZJets"].Add(tempHist)
	else:
		tempHist = _file[sample].Get(histName%(sample))
		#print sample
		#tempHist.Print("All")
		if templateHist["myBackground"] is None:
			templateHist["myBackground"] = tempHist.Clone("myBackground")
			templateHist["myBackground"].SetDirectory(0)
		else:
			templateHist["myBackground"].Add(tempHist)
			

#rebin = 4
# binning = numpy.array([88.,94.]) # Z mass pm Z width
binning = numpy.array([81,84,86,88,90,92,94,96,102.])
# binning = numpy.array([82,88,92,98,102.])
# binning = numpy.array([82.,102.])
# binning = numpy.array([82.,88.,94.,102.])

binWidth = numpy.diff(binning)

#print binning
#binning = numpy.array([80,88,92,100.1])

rebinnedHist ={} 
for ih in templateHist:
	print ih, binning
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])


if systematics=='':
	if finalState=='DiEle':
		sample = "DataEle"
		_file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
    	#print sample
		dataHist = _file[sample].Get(histNameData%(sample))
		dataHist.SetLineColor(kBlack)
		dataHist.SetMarkerStyle(8)

	elif finalState=='DiMu':
		sample = "DataMu"
		_file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
		dataHist = _file[sample].Get(histNameData%(sample))
		dataHist.SetLineColor(kBlack)
		dataHist.SetMarkerStyle(8)
	else:
		print "Select the channel !!!"
		sys.exit()
	
	data_obs = dataHist.Clone("data_obs")
	rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)
## input to combine , open root file

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
		#print "my templates:", iprocess
		myfile.cd()
		mydir =  "%s/%s/"%(channel,iprocess) 
		#print "%s/%s/"%(channel,iprocess) 

		if systematics=='':
			myhist = rebinnedHist[iprocess].Clone("nominal")
		else:
			myhist = rebinnedHist[iprocess].Clone("%s%s"%(systematics,mylevel))
			if systematics in ["Q2","isr","fsr"]:
				myNominalHist = myfile.Get(mydir+"nominal")
				valNominal = myNominalHist.Integral()
				val = myhist.Integral()
				#print "control region:", isSelectionDir
				#print "year:", selYear
				#print "channel:", channel
				print "nominal", valNominal, " ==> ", "syst %s %s"%(systematics,mylevel), val
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
	print "-------------------------------------------------------------"
	myfile.Close()
else:
	if prefitPlots:
		rebinnedData.Scale(1.,"width")

		for ih in rebinnedHist:
			rebinnedHist[ih].Scale(1.,"width")

		#if postfitPlots:
		#	rebinnedHist['myZJets'].Scale(ZJetSF)

		stack = THStack()
		stack.Add(rebinnedHist['myBackground'])
		stack.Add(rebinnedHist['myZJets'])
	
	if postfitPlots:
		rebinnedData.Scale(1.,"width")
		filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ZJetsFittingAllYear/fitDiagnostics%s_%s.root"%(crName,selYear) #BothChannel
		#if finalState=="Ele": filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ZJetsFittingAllYear/fitDiagnostics%s_%s.root"%(crName,selYear)
		#if finalState=="Mu":  filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ZJetsFittingAllYear/fitDiagnostics%s_%s.root"%(crName,selYear)

		Postfile = TFile(filename,"read")
		
		templatePostHist = {}
		# print len(binning),"==>",len(binWidth)
		templatePostHist["myZJets"]      = TH1F("myZJets" ,"",len(binWidth),binning)
		templatePostHist["myBackground"] = TH1F("myBackground"  ,"",len(binWidth),binning)
 
		for process in template_category.keys():
			tempHist = None
			tempHist = Postfile.Get("shapes_fit_s/%s/%s"%(channel,process))
			for ibin in range(1,len(binning)):
				myBinContent = tempHist.GetBinContent(ibin)
				templatePostHist[process].SetBinContent(ibin,myBinContent)
			templatePostHist[process].SetLineColor(template_category[process])
			templatePostHist[process].SetFillColor(template_category[process])
			templatePostHist[process].Scale(1.,"width")
			
			
		stack = THStack()
		stack.Add(templatePostHist['myBackground'])
		stack.Add(templatePostHist['myZJets'])

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

	minVal = 0.1
	# minVal = max(stack.GetStack()[0].GetMinimum(),1)
	stack.SetMaximum(1.75*maxVal)
	stack.SetMinimum(minVal)

	errorband=stack.GetStack().Last().Clone("error")
	errorband.Sumw2()
	errorband.SetLineColor(kBlack)
	errorband.SetFillColor(kBlack)
	errorband.SetFillStyle(3245)
	errorband.SetMarkerSize(0)

	legend.AddEntry(rebinnedData,"Data", 'pe')
	legend.AddEntry(errorband,"Uncertainty","f")
	legend.AddEntry(rebinnedHist["myZJets"],"ZJets",'f')
	legend.AddEntry(rebinnedHist["myBackground"],"Background",'f')

	pad1.cd()
	# gPad.SetLogy() # commment this out to remove the log scale
	stack.Draw('HIST')
	rebinnedData.Draw('E,X0,SAME')
	legend.Draw("same")
	stack.GetXaxis().SetTitle('')
	stack.GetXaxis().SetLabelSize(0)
	stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
	stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
	stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
	stack.SetTitle(';;<Events/GeV>')# '%rebin)
	#stack.SetTitle(';;Events/GeV')
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
	if channel == 'ele': ratio.GetXaxis().SetTitle('m_{e,e} GeV')
	else: ratio.GetXaxis().SetTitle('m_{#mu,#mu} GeV')
	ratio.GetYaxis().SetTitle("Data/MC")
	ratio.GetYaxis().SetTitleOffset(.4)
	ratio.GetYaxis().SetTitleSize(.09)
	ratio.GetYaxis().SetNdivisions(2)
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
		canvasRatio.SaveAs("%s%s_massDilep_Postfit.root"%(plotDirectory,plotDirectory[:-1]))
		canvasRatio.Print("%s%s_massDilep_Postfit.pdf" %(plotDirectory,plotDirectory[:-1]))
	else:
		canvasRatio.SaveAs("%s%s_massDilep.root"%(plotDirectory,plotDirectory[:-1]))
		canvasRatio.Print("%s%s_massDilep.pdf" %(plotDirectory,plotDirectory[:-1]))
	canvasRatio.Close()


    


    
