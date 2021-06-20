# CR1_TTGamma_Dilepton_2016_AnalysisNtuple.root
# CR1_TTGamma_SingleLept_2016_AnalysisNtuple.root
# CR2_TTGamma_Dilepton_2016_AnalysisNtuple.root
# CR2_TTGamma_SingleLept_2016_AnalysisNtuple.root

# TuneDown_TTGamma_Dilepton_2016_AnalysisNtuple.root
# TuneDown_TTGamma_SingleLept_2016_AnalysisNtuple.root
# TuneUp_TTGamma_Dilepton_2016_AnalysisNtuple.root
# TuneUp_TTGamma_SingleLept_2016_AnalysisNtuple.root

# erdOn_TTGamma_Dilepton_2016_AnalysisNtuple.root
# erdOn_TTGamma_SingleLept_2016_AnalysisNtuple.root
# --moreSyst CR1

from ROOT import TList, kFullCircle, Double, TFile, TLegend, TCanvas,gPad, TPad, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory,kCyan,kViolet
#from ROOT import *
import os

import numpy
import sys
import argparse
from optparse import OptionParser
from sampleInformation import sampleList
import sampleInformation
from numpy import log10,sqrt
from array import array

#from getFullYearMisIDEleSF import getFullYearMisIDEleSF
from getMisIDEleSF import getMisIDEleSF
from getZJetsSF import getZJetsSF
from getWJetsSF import getWJetsSF

#from TTGamma_nonPrompt_values_separateChannelYear import *
#from TTGamma_nonPrompt_values_bothChannelSeparateYear import *
#from TTGamma_nonPrompt_values_all import *

# from TTGamma_nonPrompt_2016 import *

from colorama import Fore, Back, Style 

padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
parser = OptionParser()
parser.add_option("-y", "--year", dest="Year", default="",type='str',help="Specify which year 2016, 2017 or 2018?" )
parser.add_option("-c", "--channel", dest="channel", default="",type='str',help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--datadriven", dest="datadriven", default=False,action="store_true",help="data driven plots" )
parser.add_option("--M3Plot", dest="M3Plot",default=False,action="store_true",help="Specify M3 or ChIso" )
parser.add_option("--ChIsoPlot", dest="ChIsoPlot",default=False,action="store_true",help="Specify M3 or ChIso" )
parser.add_option("--btag0", dest="btag0",default=False,action="store_true",help="0 btag " )
parser.add_option("--zeroPhoton", dest="zeroPhoton",default=False,action="store_true",help="0 photon " )
parser.add_option("--tight", dest="tight", default=False,action="store_true",help="draw photon Category for tight selection" )
parser.add_option("--level", dest="level", default="",type='str',help="Specify which level Up or Down" )
parser.add_option("--looseCRge4e0", dest="looseCRge4e0", default=False,action="store_true",help="Use >=4 jets + ==0 bjets selection" ) 
parser.add_option("--useQCDMC","--qcdMC",dest="useQCDMC", default=False, action="store_true",help="")
parser.add_option("--ratioPlot",dest="ratioPlot", default=False, action="store_true",help="")
parser.add_option("--xsecPlot",dest="xsecPlot", default=False, action="store_true",help="")

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()

finalState    = options.channel

ratioPlot     = options.ratioPlot
xsecPlot      = options.xsecPlot

level         = options.level

tight         = options.tight
looseCRge4e0  = options.looseCRge4e0
useQCDMC      = options.useQCDMC

M3Plot        = options.M3Plot
ChIsoPlot     = options.ChIsoPlot
btag0         = options.btag0
zeroPhoton    = options.zeroPhoton

datadriven    = options.datadriven

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"


if level=='up':   mylevel='Up'
if level=='down': mylevel='Down'


# moremodel = ["CR1","CR2","erdOn"]

eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
if M3Plot or ChIsoPlot or zeroPhoton:      #SR8 
	fileDirNom    = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	fileDirCR1         = "histograms_%s/%s/hists_CR1_tight/"%(selYear, channel)
	fileDirCR2         = "histograms_%s/%s/hists_CR2_tight/"%(selYear, channel)
	fileDirCR3         = "histograms_%s/%s/hists_erdOn_tight/"%(selYear, channel)
	plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"
	
elif btag0:      #CR3 >=4jet 0 btag
	fileDirNom    = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	fileDirCR1         = "histograms_%s/%s/hists_CR1_looseCRge4e0/"%(selYear, channel)
	fileDirCR2         = "histograms_%s/%s/hists_CR2_looseCRge4e0/"%(selYear, channel)
	fileDirCR3         = "histograms_%s/%s/hists_erdOn_looseCRge4e0/"%(selYear, channel)
	plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)

# elif zeroPhoton:      #CR3 >=4jet 0 btag
# 	fileDirNom         = "histograms_%s/%s/hists_tight/"%(selYear, channel)
# 	fileDirCR1         = "histograms_%s/%s/hists_CR1_tight/"%(selYear, channel)
# 	fileDirCR2         = "histograms_%s/%s/hists_CR2_tight/"%(selYear, channel)
# 	fileDirCR3         = "histograms_%s/%s/hists_erdOn_tight/"%(selYear, channel)
# 	plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)

else:
	print "wrong plot variable"		

eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
# localFolder="/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/"

fileDirNom = eosFolder + fileDirNom
print fileDirNom

fileDirCR1   = eosFolder + fileDirCR1
fileDirCR2   = eosFolder + fileDirCR2
fileDirCR3   = eosFolder + fileDirCR3

print fileDirCR1   
print fileDirCR2   
print fileDirCR3

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
from Style import *
gROOT.ForceStyle()
import CMS_lumi
if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"
H = 600;
W = 800;
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W
legendHeightPer = 0.04
legendStart = 0.69
legendEnd = 0.97-(R/W)
legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((10+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((10+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legendR.SetBorderSize(0)
legendR.SetFillColor(0)
legend.SetBorderSize(0)
legend.SetFillColor(0)

# binning = numpy.array([1.141,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.,20.]) # without first bin, removing last bin
# binWidth = numpy.diff(binning)
# rebinnedHist ={} 	
if M3Plot:
	histName  	= "phosel_M3_%s_%s"
	histNameData= "phosel_M3_%s" 
	mydistributionName = histNameData[7:-3]
elif ChIsoPlot:
	histName    = "phosel_mediumID_ChIso_%s_%s"
	histNameData= "phosel_mediumID_ChIso_%s" 
	mydistributionName = histNameData[16:-3]
elif btag0:
	histName  	= "phosel_MassEGamma_%s_%s"
	histNameData= "phosel_MassEGamma_%s" 
	mydistributionName = histNameData[7:-3]+"0btag"
elif zeroPhoton:
	histName  	= "presel_M3_%s_%s"
	histNameData= "presel_M3_%s" 
	mydistributionName = histNameData[7:-3]+"0photon"
else:
	print "either M3 or ChIso!!"

if mydistributionName == "M3":
	myfilename = "M3"
	binning = numpy.array([60., 100., 140., 160., 180., 200., 240., 280.,340., 420.,500.1]) #best one
	# binning = numpy.array([60., 500.1]) #best one
elif mydistributionName == "MassEGamma0btag":
	myfilename = "zerobtag"
	if channel =='ele':
		binning = numpy.array([0,80,100,180.])
	else:
		binning = numpy.array([0,91.,180.])

elif mydistributionName == "ChIso":
	myfilename = "ChIso"
	binning = numpy.array([1.141,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.]) # without first bin, removing last bin
elif mydistributionName=="M30photon":
	myfilename = "M30photon"
	binning = numpy.array([60., 100., 140., 160., 180., 200., 240., 280.,340., 420.,500.1]) # best one
	# binning = numpy.array([60.,140.,200., 500.1]) # best one
	# binning = numpy.array([60.,500.1]) # best one





binWidth = numpy.diff(binning)
myfile = TFile("%s%s.root"%(plotDirectory,"ttgamma_Prefit"),"update")

sample="TTGamma"
fileNom = TFile.Open("%s%s.root"%(fileDirNom,sample),"read")
fileCR1 = TFile.Open("%s%s.root"%(fileDirCR1,sample),"read")
fileCR2 = TFile.Open("%s%s.root"%(fileDirCR2,sample),"read")
fileCR3 = TFile.Open("%s%s.root"%(fileDirCR3,sample),"read")




if zeroPhoton:
	histNom = fileNom.Get(histNameData%sample).Clone("histNom")
	histCR1 = fileCR1.Get(histNameData%sample).Clone("histCR1")
	histCR2 = fileCR2.Get(histNameData%sample).Clone("histCR2")
	histCR3 = fileCR3.Get(histNameData%sample).Clone("histCR3")

	histNom = histNom.Rebin(len(binning)-1,"",binning)
	histCR1 = histCR1.Rebin(len(binning)-1,"",binning)
	histCR2 = histCR2.Rebin(len(binning)-1,"",binning)
	histCR3 = histCR3.Rebin(len(binning)-1,"",binning)
 
	colorUp   = TH1F("colorUp","",len(binWidth),binning)
	colorDown = TH1F("colorDown","",len(binWidth),binning)

	for ibin in range(1,histNom.GetNbinsX()+1):
			maxVal = max(histCR1.GetBinContent(ibin),histCR2.GetBinContent(ibin),histCR3.GetBinContent(ibin))
			minVal = min(histCR1.GetBinContent(ibin),histCR2.GetBinContent(ibin),histCR3.GetBinContent(ibin))
			NomVal = histNom.GetBinContent(ibin)
			print maxVal, NomVal, minVal
			colorUp.SetBinContent(ibin,maxVal)
			colorDown.SetBinContent(ibin,minVal) 

	canvas = ROOT.TCanvas()

	for iprocess in ["TTGamma"]:
		print myfilename
		mynominal = myfile.Get("%s/%s/nominal"%(myfilename,iprocess))
		mynominal.Draw()
		print mynominal.Integral()
		colorUp.Scale(mynominal.Integral()/colorUp.Integral())
		colorDown.Scale(mynominal.Integral()/colorDown.Integral())
		colorUp.Draw("same,E0")
		colorDown.Draw("same,E0")
		canvas.Print("modelTest.pdf")
		myfile.cd()
		mydir =  "%s/%s/"%(myfilename,iprocess) 
		if myfile.GetDirectory(mydir):
			gDirectory.cd(mydir)
			gDirectory.Delete("%s%s;*"%("color","Up"))
			gDirectory.Delete("%s%s;*"%("color","Down"))
			colorUp.Write()
			colorDown.Write()
		else:
			gDirectory.mkdir(mydir)
			gDirectory.cd(mydir)
			gDirectory.Delete("%s%s;*"%("color","Up"))
			gDirectory.Delete("%s%s;*"%("color","Down"))
			colorUp.Write()
			colorDown.Write()
	print "%s%s.root"%(plotDirectory,"ttgamma_Prefit")
	sys.exit()

else:

	canvas = TCanvas()
	for iprocess in ["nonPromptTTGamma","isolatedTTGamma"]:
	# for iprocess in ["isolatedTTGamma","nonPromptTTGamma"]:
		print myfilename
		histNom = myfile.Get("%s/%s/nominal"%(myfilename,iprocess))
		if iprocess=="isolatedTTGamma":
			histCR1 = fileCR1.Get(histName%("GenuinePhoton",sample,)).Clone("histCR1")
			histCR1a = fileCR1.Get(histName%("MisIDEle",sample,)).Clone("histCR1a")
			histCR1.Add(histCR1a)

			histCR2 = fileCR2.Get(histName%("GenuinePhoton",sample,)).Clone("histCR2")
			histCR2a = fileCR2.Get(histName%("MisIDEle",sample,)).Clone("histCR2a")
			histCR2.Add(histCR2a)

			histCR3 = fileCR3.Get(histName%("GenuinePhoton",sample,)).Clone("histCR3")
			histCR3a = fileCR3.Get(histName%("MisIDEle",sample,)).Clone("histCR3a")
			histCR3.Add(histCR3a)
		else:
			histCR1 = fileCR1.Get(histName%("HadronicPhoton",sample,)).Clone("histCR1")
			histCR1a = fileCR1.Get(histName%("HadronicFake",sample,)).Clone("histCR1a")
			histCR1.Add(histCR1a)

			histCR2 = fileCR2.Get(histName%("HadronicPhoton",sample,)).Clone("histCR2")
			histCR2a = fileCR2.Get(histName%("HadronicFake",sample,)).Clone("histCR2a")
			histCR2.Add(histCR2a)

			histCR3 = fileCR3.Get(histName%("HadronicPhoton",sample,)).Clone("histCR3")
			histCR3a = fileCR3.Get(histName%("HadronicFake",sample,)).Clone("histCR3a")
			histCR3.Add(histCR3a)

		# histNom = histNom.Rebin(len(binning)-1,"",binning)
		histCR1 = histCR1.Rebin(len(binning)-1,"",binning)
		histCR2 = histCR2.Rebin(len(binning)-1,"",binning)
		histCR3 = histCR3.Rebin(len(binning)-1,"",binning)

		colorUp   = TH1F("colorUp","",len(binWidth),binning)
		colorDown = TH1F("colorDown","",len(binWidth),binning)
		for ibin in range(1,histCR1.GetNbinsX()+1):
			maxVal = max(histCR1.GetBinContent(ibin),histCR2.GetBinContent(ibin),histCR3.GetBinContent(ibin))
			minVal = min(histCR1.GetBinContent(ibin),histCR2.GetBinContent(ibin),histCR3.GetBinContent(ibin))
			NomVal = histNom.GetBinContent(ibin)
			print maxVal, NomVal, minVal
			colorUp.SetBinContent(ibin,maxVal)
			colorDown.SetBinContent(ibin,minVal) 
		colorUp.Scale(histNom.Integral()/colorUp.Integral())
		colorDown.Scale(histNom.Integral()/colorDown.Integral())
		histNom.Draw()
		colorUp.Draw("same,E0")
		colorDown.Draw("same,E0")
		# histNom.SetMaximum(200)
		# histNom.SetMinimum(0)
		canvas.Print("modelTest.pdf")
		myfile.cd()
		mydir =  "%s/%s/"%(myfilename,iprocess) 
		if myfile.GetDirectory(mydir):
			gDirectory.cd(mydir)
			gDirectory.Delete("%s%s;*"%("color","Up"))
			gDirectory.Delete("%s%s;*"%("color","Down"))
			colorUp.Write()
			colorDown.Write()
		else:
			gDirectory.mkdir(mydir)
			gDirectory.cd(mydir)
			gDirectory.Delete("%s%s;*"%("color","Up"))
			gDirectory.Delete("%s%s;*"%("color","Down"))
			colorUp.Write()
			colorDown.Write()
	print "%s%s.root"%(plotDirectory,"ttgamma_Prefit")
	sys.exit()

