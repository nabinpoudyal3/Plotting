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
parser.add_option("-y", "--year", dest="Year", default="",type='str',
					help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-c", "--channel", dest="channel", default="",type='str',
					help="Specify which channel Mu or Ele? default is Mu" )

parser.add_option("--postfitPlots", dest="postfitPlots", default=False,action="store_true",
					help="post fit plots" )

parser.add_option("--prefitPlots", dest="prefitPlots", default=False,action="store_true",
					help="pre fit plots" )
					
parser.add_option("--template", dest="template", default=False,action="store_true",
					help="post fit plots" )
					
parser.add_option("--datadriven", dest="datadriven", default=False,action="store_true",
					help="data driven plots" )

parser.add_option("--M3Plot", dest="M3Plot",default=False,action="store_true",
					help="Specify M3 or ChIso" )

parser.add_option("--ChIsoPlot", dest="ChIsoPlot",default=False,action="store_true",
					help="Specify M3 or ChIso" )

parser.add_option("--btag0", dest="btag0",default=False,action="store_true",
					help="0 btag " )

parser.add_option("--btag0_3j", dest="btag0_3j",default=False,action="store_true",
					help="0 btag with 3jets " )

parser.add_option("--zeroPhoton", dest="zeroPhoton",default=False,action="store_true",
					help="0 photon " )
					
								
parser.add_option("--tight", dest="tight", default=False,action="store_true",
					help="draw photon Category for tight selection" )

parser.add_option("--syst", "--systematics", dest="systematics", default="",type='str',
					help="Specify which systematic plots" )

parser.add_option("--level", dest="level", default="",type='str',
					help="Specify which level Up or Down" )
				
					
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

parser.add_option("--noData",dest="noData", default=False, action="store_true",
		help="")

parser.add_option("--ratioPlot",dest="ratioPlot", default=False, action="store_true",
		help="")

parser.add_option("--xsecPlot",dest="xsecPlot", default=False, action="store_true",
		help="")

############
#parser=argparse.ArgumentParser(
#    description='''How to run this script? ''',
#    epilog=""" python makePlot_signal_prompt.py -c Ele -y 2016 --tight --useQCDMC --M3Plot --posfitPlots""")

#args=parser.parse_args()

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()

finalState    = options.channel
postfitPlots  = options.postfitPlots
prefitPlots   = options.prefitPlots

ratioPlot     = options.ratioPlot
xsecPlot      = options.xsecPlot

systematics   = options.systematics
level         = options.level

tight         = options.tight
looseCRge2ge0 = options.looseCRge2ge0
looseCRge2e0  = options.looseCRge2e0
looseCRe2e0   = options.looseCRe2e0
looseCRe2e1   = options.looseCRe2e1
looseCRe3e0   = options.looseCRe3e0
looseCRge4e0  = options.looseCRge4e0
looseCRe3e1   = options.looseCRe3e1
looseCRe2e2   = options.looseCRe2e2
looseCRe3ge2  = options.looseCRe3ge2
useQCDMC      = options.useQCDMC
useQCDCR      = options.useQCDCR
noQCD         = options.noQCD
noData        = options.noData

ChIsoPlot     = options.ChIsoPlot
datadriven      = options.datadriven
template      = options.template

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"


if level=='up':   mylevel='Up'
if level=='down': mylevel='Down'

eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
crName = ""
if ChIsoPlot:      #SR8 
	# isSelection = "looseCRge2e0"
	isSelection = "looseCRge4e0"
	crName = "signal"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDirNom  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"

else:
	print "wrong plot variable"		

eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
# localFolder="/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/"

fileDirNom = eosFolder + fileDirNom
print fileDirNom

fileDir = eosFolder + fileDir
print fileDir

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

from Style import *

gROOT.ForceStyle()


sampleList = ['TTGamma', 'TTbar', 'SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD_DD"]

_file = {}

import CMS_lumi

if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"


print sampleList

H = 600;
W = 800;
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

legendHeightPer = 0.04


legendStart = 0.69
legendEnd = 0.97-(R/W)

#legend = TLegend(2*legendStart - legendEnd, 1-T/H-0.01 - legendHeightPer*(len(legList)+1), legendEnd, 0.99-(T/H)-0.01)
legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((10+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
# legend.SetNColumns(2)

#legendR = TLegend(0.71, 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*(len(legList)+1), 0.99-(R/W), 0.99-(T/H)/(1.-padRatio+padOverlap))


legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((10+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))

# legendR.SetNColumns(2)

legendR.SetBorderSize(0)
legendR.SetFillColor(0)


legend.SetBorderSize(0)
legend.SetFillColor(0)

binning = numpy.array([1.141,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.]) # without first bin, removing last bin

binWidth = numpy.diff(binning)

rebinnedHist ={} 	

sample = ""
if finalState=='Ele' and datadriven: sample = "DataEle"
elif finalState=='Mu' and datadriven: sample = "DataMu"
histo_sieie_MC  = None
histo_ChIso_MC  = None
print fileDir
print fileDirNom
for i in sampleList:
	if i =="QCD_DD": continue
	histoFileChI = TFile.Open("%s%s.root"%(fileDir,i),"read")
	histo1 = histoFileChI.Get("phosel_AntiSIEIE_ChIso_%s"%i).Clone("histo1") # sideband MC
	histoChIsoHad = histoFileChI.Get("phosel_mediumID_ChIso_HadronicPhoton_%s"%i).Clone("histoChIsoHad") # signal MC
	histoChIsoFake = histoFileChI.Get("phosel_mediumID_ChIso_HadronicFake_%s"%i).Clone("histoChIsoFake")
	histoChIso =  histoChIsoHad.Clone("histoChIso")
	histoChIso.Add(histoChIsoFake)
	histo_sieie = histo1.Rebin(len(binning)-1,"",binning)
	histo_ChIso = histoChIso.Rebin(len(binning)-1,"",binning)
	print i, histo_sieie.Integral()
	if histo_ChIso_MC is None:
		histo_ChIso_MC = histo_ChIso.Clone("histo_ChIso_MC")
		histo_ChIso_MC.SetDirectory(0)
	else:
		histo_ChIso_MC.Add(histo_ChIso)

	if histo_sieie_MC is None:
		histo_sieie_MC = histo_sieie.Clone("histo_sieie_MC")
		histo_sieie_MC.SetDirectory(0)
	else:
		histo_sieie_MC.Add(histo_sieie)

histoFile = TFile.Open("%s%s.root"%(fileDirNom,sample),"read")
histo = histoFile.Get("phosel_AntiSIEIE_ChIso_%s"%sample).Clone("histo")
histo_sieie_Data = histo.Rebin(len(binning)-1,"",binning)

print binWidth
print len(binWidth)
plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
myfilename = "ChIso"
template_category = {"nonPromptTTGamma":kOrange-3,  
					 "nonPromptTTbar":  kRed+3,   
					 "nonPromptWGamma": kViolet-1,  
					 "nonPromptZGamma": kViolet+8,  
					 "nonPromptOther":  kGreen+4, 
					}


myfile = TFile("%s%s.root"%(plotDirectory,"ttgamma_Prefit"),"update")

# histo_ChIso_MC.Scale(1/histo_ChIso_MC.Integral())
# histo_sieie_MC.Scale(1/histo_sieie_MC.Integral())

for iprocess in template_category.keys():
	mynominal = myfile.Get("%s/%s/nominal"%(myfilename,iprocess))
	shapeDDUp = TH1F("shapeDDUp","",len(binWidth),binning)
	shapeDDDown = TH1F("shapeDDDown","",len(binWidth),binning)
	print "************************************"
	print iprocess
	for ibin in range(1,histo_sieie_MC.GetNbinsX()+1):
		correctionFactor = histo_ChIso_MC.GetBinContent(ibin)/histo_sieie_MC.GetBinContent(ibin)
		up = histo_sieie_Data.GetBinContent(ibin)
		down = histo_sieie_Data.GetBinContent(ibin)* (correctionFactor*correctionFactor) #*binWidth[ibin-1] 
		print ">>>>>",mynominal.GetBinContent(ibin), up, down
		shapeDDUp.SetBinContent(ibin,up)
		shapeDDDown.SetBinContent(ibin,down)

	shapeDDDown.Scale(mynominal.Integral()/shapeDDDown.Integral())
	shapeDDUp.Scale(mynominal.Integral()/shapeDDUp.Integral())


	if iprocess == "nonPromptTTbar":
		mycanvas = TCanvas()
		shapeDDDown.Draw("E")	
		shapeDDUp.Draw("same,E")	
		mynominal.Draw("same,E")
		shapeDDDown.SetLineColor(kBlue)	
		shapeDDUp.SetLineColor(kRed)	
		mynominal.SetLineColor(kBlack)
		shapeDDDown.SetLineWidth(3)	
		shapeDDUp.SetLineWidth(3)	
		mynominal.SetLineWidth(3)
		shapeDDDown.SetMaximum(3000)
		shapeDDDown.SetMinimum(0)
		mycanvas.Print("ddtest.pdf")
		print iprocess, mynominal.Integral(),shapeDDUp.Integral(), shapeDDDown.Integral()

	myfile.cd()
	mydir =  "%s/%s/"%(myfilename,iprocess) 
	if myfile.GetDirectory(mydir):
		gDirectory.cd(mydir)
		gDirectory.Delete("%s%s;*"%("shapeDD","Up"))
		gDirectory.Delete("%s%s;*"%("shapeDD","Down"))
		shapeDDDown.Write()
		shapeDDUp.Write()
	else:
		gDirectory.mkdir(mydir)
		gDirectory.cd(mydir)
		gDirectory.Delete("%s%s;*"%("shapeDD","Up"))
		gDirectory.Delete("%s%s;*"%("shapeDD","Down"))
		shapeDDDown.Write()
		shapeDDUp.Write()
print "%s%s.root"%(plotDirectory,"ttgamma_Prefit")

myfile.Close()
sys.exit()
