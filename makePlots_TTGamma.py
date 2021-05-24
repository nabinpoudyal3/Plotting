from ROOT import TList, kFullCircle, Double, TFile, TLegend, TCanvas,gPad, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory,kCyan,kViolet
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

print "Are we using MC only? ",noData
# sys.exit()

M3Plot        = options.M3Plot
ChIsoPlot     = options.ChIsoPlot
btag0         = options.btag0
btag0_3j      = options.btag0_3j
zeroPhoton    = options.zeroPhoton

template        = options.template
datadriven      = options.datadriven

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

commonSystematics= ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","Pdf","fsr","isr", "prefireEcal","phosmear","elesmear","phoscale" "elescale"]

RunIISytematics = [
"BTagSF_b16", "BTagSF_l16", "JER1_16", "JER0_16", "elescale_16", "phoscale_16",
"BTagSF_b17", "BTagSF_l17", "JER1_17", "JER0_17", "elescale_17", "phoscale_17",
"BTagSF_b18", "BTagSF_l18", "JER1_18", "JER0_18", "elescale_18", "phoscale_18"]

separateSytematics =  ["JER0", "JECTotal0","JER1", "JECTotal1"]


allsystematics = RunIISytematics+commonSystematics+separateSytematics

RunIISytematicsDict = {
"BTagSF_b16":"BTagSF_b",
"BTagSF_l16":"BTagSF_l", 
"JER1_16":"JER", 
"JER0_16":"JER", 
"elescale_16":"elescale", 
"phoscale_16":"phoscale",
"BTagSF_b17":"BTagSF_b", 
"BTagSF_l17":"BTagSF_l", 
"JER1_17":"JER", 
"JER0_17":"JER", 
"elescale_17":"elescale", 
"phoscale_17":"phoscale",
"BTagSF_b18":"BTagSF_b", 
"BTagSF_l18":"BTagSF_l", 
"JER1_18":"JER", 
"JER0_18":"JER", 
"elescale_18":"elescale", 
"phoscale_18":"phoscale"
}

print RunIISytematics
print commonSystematics
print separateSytematics
print allsystematics


if systematics in allsystematics: print "running on systematics"
else: print(Fore.RED + "systematics is not in list. Add the systematics in the list if you are running for systematics.")

print(Style.RESET_ALL) 


# [systematics=="BTagSF_b16",systematics=="BTagSF_l16",systematics=="JER16",systematics=="BTagSF_b17",systematics=="BTagSF_l17",systematics=="JER17",systematics=="BTagSF_b18",systematics=="BTagSF_l18",systematics=="JER18"]

if level=='up':   mylevel='Up'
if level=='down': mylevel='Down'

eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
crName = ""
if M3Plot or ChIsoPlot:      #SR8 
	# isSelection = "looseCRge2e0"
	isSelection = "looseCRge4e0"
	crName = "signal"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDirNom  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	if systematics in allsystematics:
		if systematics in RunIISytematics: 
			print systematics, " For full RunII ==>", RunIISytematicsDict[systematics]
			fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,RunIISytematicsDict[systematics],level)
			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
			regionText = "N_{j}#geq4, N_{b}#geq1"
		
		# elif systematics=="JECTotal0" or systematics=="JER0" or systematics=="JECTotal1" or systematics=="JER1": 
		elif systematics in separateSytematics:
			print "JECTotal and JER stuffs. ==>", systematics[:-1]
			fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics[:-1],level)
			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
			regionText = "N_{j}#geq4, N_{b}#geq1"

		elif systematics in commonSystematics:
			print "common systematics. ==>", systematics
			fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics,level)
			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
			regionText = "N_{j}#geq4, N_{b}#geq1"
	else:
		print "******** Caution********** this is nominal run"
		fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
	
	
elif btag0:      #CR3 >=4jet 0 btag
	# isSelection = "looseCRge2e0"
	isSelection = "looseCRge4e0"
	crName = "btag0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDirNom  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	if systematics in allsystematics:
		if systematics in RunIISytematics: 
			print systematics, "For full RunII",RunIISytematicsDict[systematics]
			fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge4e0/"%(selYear, channel,RunIISytematicsDict[systematics],level)
			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
			regionText = "N_{j}#geq4, N_{b}=0"
		
		# elif systematics=="JECTotal0" or systematics=="JER0" or systematics=="JECTotal1" or systematics=="JER1": 
		elif systematics in separateSytematics:
			print "JECTotal and JER stuffs."
			fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge4e0/"%(selYear, channel,systematics[:-1],level)
			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
			regionText = "N_{j}#geq4, N_{b}=0"

		elif systematics in commonSystematics:
			print "Common systematics"
			fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge4e0/"%(selYear, channel,systematics,level)
			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
			regionText = "N_{j}#geq4, N_{b}#geq1"	
	else:
		fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
		#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}=0"


# elif btag0:      #CR2 ==3jet 0 btag
# 	# isSelection = "looseCRge2e0"
# 	isSelection = "looseCRe3e0"
# 	crName = "btag0"
# 	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
# 	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
# 	else :                ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
# 	fileDirNom  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
# 	if systematics in allsystematics:
# 		if "1" in systematics:
# 			fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe3e0/"%(selYear, channel,systematics[:-2],level)
# 			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
# 			regionText = "N_{j}=3, N_{b}=0"
# 		else:
# 			fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe3e0/"%(selYear, channel,systematics,level)
# 			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
# 			regionText = "N_{j}=3, N_{b}=0"
# 	else:
# 		fileDir  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
# 		#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
# 		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
# 		regionText = "N_{j}=3, N_{b}=0"


# elif btag0:      
# 	isSelection = "looseCRge2e0"
# 	crName = "btag0"
# 	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
# 	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
# 	else :                ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
# 	fileDirNom  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
# 	if systematics in allsystematics:
# 		if "1" in systematics: 
# 			fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge2e0/"%(selYear, channel,systematics[:-2],level)
# 			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
# 			regionText = "N_{j}#geq2, N_{b}=0"
# 		else:
# 			fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge2e0/"%(selYear, channel,systematics,level)
# 			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
# 			regionText = "N_{j}#geq2, N_{b}=0"		
# 	else:
# 		fileDir  = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
# 		#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
# 		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
# 		regionText = "N_{j}#geq2, N_{b}=0"


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


sampleList = ['TTGamma', 'TTbar', 'SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'SingleTop':kOrange-3, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7,'GJets':kGreen+1,"QCD":kGreen+3}

#sampleList = ['TTGamma', 'TTbar', 'TGJets', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV']
#sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'TGJets':kGray, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7}

template_category = {"isolatedTTGamma":kOrange,  "nonPromptTTGamma":kOrange-3,  
					 "isolatedTTbar":  kRed+1,   "nonPromptTTbar":  kRed+3,   
					 "isolatedWGamma": kBlue-4,  "nonPromptWGamma": kViolet-1,  
					 "isolatedZGamma": kBlue-2,  "nonPromptZGamma": kViolet+8,  
					 "isolatedOther":  kGreen+3, "nonPromptOther":  kGreen+4, 
					}

template_categoryName = {"isolatedTTGamma":"t#bar{t}#gamma iso", "nonPromptTTGamma":"t#bar{t}#gamma non prompt",  
					     "isolatedTTbar":  "t#bar{t} iso",        "nonPromptTTbar":  "t#bar{t} non prompt",   
					     "isolatedWGamma": "W#gamma iso",  "nonPromptWGamma": "W#gamma non prompt",  
					     "isolatedZGamma": "Z#gamma iso",  "nonPromptZGamma": "Z#gamma non prompt",  
					     "isolatedOther":  "other_1 #gamma iso",    "nonPromptOther":  "other_1 #gamma non prompt", 
					    }
					
hist_category = {"GenuinePhoton":kOrange, "MisIDEle":kRed, "HadronicPhoton":kBlue, "HadronicFake":kGreen+1 }

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


legendStart = 0.69
legendEnd = 0.97-(R/W)

#legend = TLegend(2*legendStart - legendEnd, 1-T/H-0.01 - legendHeightPer*(len(legList)+1), legendEnd, 0.99-(T/H)-0.01)
legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((10+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legend.SetNColumns(2)

#legendR = TLegend(0.71, 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*(len(legList)+1), 0.99-(R/W), 0.99-(T/H)/(1.-padRatio+padOverlap))


legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((10+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))

legendR.SetNColumns(2)

legendR.SetBorderSize(0)
legendR.SetFillColor(0)


legend.SetBorderSize(0)
legend.SetFillColor(0)

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
	
	# histName  	= "phosel_LeadingPhotonEt_%s_%s"
	# histNameData= "phosel_LeadingPhotonEt_%s" 
	# mydistributionName = histNameData[7:-3]+"0btag"
	
	# histName  	= "phosel_M3_%s_%s"
	# histNameData= "phosel_M3_%s" 
	# mydistributionName = histNameData[7:-3]+"0btag"

	# if channel == "ele":
	# 	histName  	= "phosel_elePt_%s_%s"
	# 	histNameData= "phosel_elePt_%s" 
	# 	mydistributionName = histNameData[7:-3]+"0btag"
	# else:
	# 	histName  	= "phosel_muPt_%s_%s"
	# 	histNameData= "phosel_muPt_%s" 
	# 	mydistributionName = histNameData[7:-3]+"0btag"

elif btag0_3j:
	histName  	= "phosel_M3_%s_%s"
	histNameData= "phosel_M3_%s" 
	mydistributionName = histNameData[7:-3]+"0btag"
else:
	print "either M3 or ChIso!!"


templateHist ={}

print mydistributionName

#print "==>",sampleList	
for sample in sampleList:
	if sample=="QCD_DD": 
		#print "==>",sample, fileDirQCD
		_file[sample] = TFile.Open('%s%s.root'%(fileDirNom,sample),'read')
		# tempHisttest  = _file[sample].Get(histNameData%(sample))
		# print sample, tempHisttest.Integral(1,tempHisttest.GetNbinsX(),"width")

	else:
		#print sample, fileDir
		_file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')
		# tempHisttest  = _file[sample].Get(histNameData%(sample))
		# print sample, tempHisttest.Integral(1,tempHisttest.GetNbinsX(),"width")

	
templateHist = {}

# sys.exit()

templateHist["isolatedTTGamma" ] = None 
templateHist["nonPromptTTGamma"] = None 
templateHist["isolatedTTbar"   ] = None
templateHist["nonPromptTTbar"  ] = None
templateHist["isolatedWGamma"  ] = None 
templateHist["nonPromptWGamma" ] = None  
templateHist["isolatedZGamma"  ] = None  
templateHist["nonPromptZGamma" ] = None  
templateHist["isolatedOther"   ] = None 
templateHist["nonPromptOther"  ] = None 

#templateHist["Total"] = None 
print sampleList

print "<==", MisIDEleSF

if systematics=='misIDE' and level=='up':
	if selYear=="2016":
		MisIDEleSF=MisIDEleSF+0.34
	elif selYear=="2017":
		MisIDEleSF=MisIDEleSF+0.4
	else:
		MisIDEleSF=MisIDEleSF+0.27
if systematics=='misIDE' and level=='down':
	if selYear=="2016":
		MisIDEleSF=MisIDEleSF-0.34
	elif selYear=="2017":
		MisIDEleSF=MisIDEleSF-0.4
	else:
		MisIDEleSF=MisIDEleSF-0.27

print "==>", MisIDEleSF

for item in hist_category:
	if item == "MisIDEle" or item == "GenuinePhoton":
		for sample in sampleList:
			if sample=="QCD_DD": continue
			tempHist = _file[sample].Get(histName%(item,sample))
			if sample=="ZJets": tempHist.Scale(ZJetSF) 
			if sample=="WJets": tempHist.Scale(WJetSF) 

			print "MC counts ==> ",sample,item, int(tempHist.Integral(-1,-1))

			if item=="MisIDEle":
				print MisIDEleSF
				tempHist.Scale(MisIDEleSF)
			#print sample,item, "==>", tempHist.Integral()	
			if sample=='TTGamma':	
				if  templateHist["isolatedTTGamma"] is None:
					templateHist["isolatedTTGamma"] = tempHist.Clone("isolatedTTGamma")
					templateHist["isolatedTTGamma"].SetDirectory(0)
				else:
					templateHist["isolatedTTGamma"].Add(tempHist)
			elif sample=='TTbar':	
				if  templateHist["isolatedTTbar"] is None:
					templateHist["isolatedTTbar"] = tempHist.Clone("isolatedTTbar")
					templateHist["isolatedTTbar"].SetDirectory(0)
				else:
					templateHist["isolatedTTbar"].Add(tempHist)
			elif sample=='WGamma':	
				if  templateHist["isolatedWGamma"] is None:
					templateHist["isolatedWGamma"] = tempHist.Clone("isolatedWGamma")
					templateHist["isolatedWGamma"].SetDirectory(0)
				else:
					templateHist["isolatedWGamma"].Add(tempHist)
			elif sample=='ZGamma':	
				if  templateHist["isolatedZGamma"] is None:
					templateHist["isolatedZGamma"] = tempHist.Clone("isolatedZGamma")
					templateHist["isolatedZGamma"].SetDirectory(0)
				else:
					templateHist["isolatedZGamma"].Add(tempHist)
			else:
				
				if  templateHist["isolatedOther"] is None:
					templateHist["isolatedOther"] = tempHist.Clone("isolatedOther")
					templateHist["isolatedOther"].SetDirectory(0)
				else:

					templateHist["isolatedOther"].Add(tempHist)

	else:
		for sample in sampleList:
			if sample=="QCD_DD": continue
			tempHist = _file[sample].Get(histName%(item,sample))
			if sample=="ZJets": tempHist.Scale(ZJetSF) 
			if sample=="WJets": tempHist.Scale(WJetSF) 
			#print sample,item, "==>", tempHist.Integral()	

			print "MC counts ==> ",sample,item, int(tempHist.Integral(-1,-1))

			if sample=='TTGamma':	
				if  templateHist["nonPromptTTGamma"] is None:
					templateHist["nonPromptTTGamma"] = tempHist.Clone("nonPromptTTGamma")
					templateHist["nonPromptTTGamma"].SetDirectory(0)
				else:
					templateHist["nonPromptTTGamma"].Add(tempHist)
			elif sample=='TTbar':	
				if  templateHist["nonPromptTTbar"] is None:
					templateHist["nonPromptTTbar"] = tempHist.Clone("nonPromptTTbar")
					templateHist["nonPromptTTbar"].SetDirectory(0)
				else:
					templateHist["nonPromptTTbar"].Add(tempHist)
			elif sample=='WGamma':	
				if  templateHist["nonPromptWGamma"] is None:
					templateHist["nonPromptWGamma"] = tempHist.Clone("nonPromptWGamma")
					templateHist["nonPromptWGamma"].SetDirectory(0)
				else:
					templateHist["nonPromptWGamma"].Add(tempHist)
			elif sample=='ZGamma':	
				if  templateHist["nonPromptZGamma"] is None:
					templateHist["nonPromptZGamma"] = tempHist.Clone("nonPromptZGamma")
					templateHist["nonPromptZGamma"].SetDirectory(0)
				else:
					templateHist["nonPromptZGamma"].Add(tempHist)
			else:
				if  templateHist["nonPromptOther"] is None:
					templateHist["nonPromptOther"] = tempHist.Clone("nonPromptOther")
					templateHist["nonPromptOther"].SetDirectory(0)
				else:

					templateHist["nonPromptOther"].Add(tempHist)
	
#gApplication.Run()
#print "exited"


# grep -r "Error in <TChain" *.* 
# grep -r "No such file or directory" *.*
# grep -r "Error in <TNet" *.*


# apply SF before plotting or feeding into combine
#print qcdHist.Print("All")
#print templateHist["nonPromptOther"].Print("All")

#sys.exit()

if _file["QCD_DD"] is not None: 
	print sample
	print "Yes using QCD DD "
	qcdHist = _file[sample].Get(histNameData%(sample))
	templateHist["nonPromptOther"].Add(qcdHist)
	print "qcdHist data driven ==>",qcdHist.Integral(-1,-1)
	errorQCD = Double(0.)
	nQCDEvents = qcdHist.IntegralAndError(1,qcdHist.GetNbinsX(),errorQCD,"width")

templateHist[ "isolatedWGamma"].Scale(WGammaSF)
templateHist["nonPromptWGamma"].Scale(WGammaSF)
templateHist[ "isolatedZGamma"].Scale(ZGammaSF)
templateHist["nonPromptZGamma"].Scale(ZGammaSF)

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
	#rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)
	dataError = Double(0.)
	nEventData = data_obs.IntegralAndError(1,data_obs.GetNbinsX(),dataError,"width")
	print "nEventsData ==>", nEventData
#for event yield purpose:

lastbin = 0
totalMC = 0
totalMCerror = 0
line = ""
line += "\\begin{table} \n"
line += "\\caption{} \n"
line += "\\label{tab:} \n"
line += "\\centering \n"
line += "\\begin{tabular} {|l|l|l|} \n"
line += "\\hline \n"
line += "Processes & Total Events & Percent \\\\ \n"
line += "\\hline \n"

if prefitPlots:

	newtemplateHist = ["isolatedTTGamma","nonPromptTTGamma","isolatedTTbar","nonPromptTTbar","isolatedZGamma","nonPromptZGamma","isolatedWGamma","nonPromptWGamma","isolatedOther","nonPromptOther"]
	
	latex_categoryName = {"isolatedTTGamma":"\\ttgamma iso",        "nonPromptTTGamma":"\\ttgamma non prompt",  
					     "isolatedTTbar":   "\\ttbar iso",          "nonPromptTTbar":  "\\ttbar non prompt",   
					     "isolatedWGamma":  "\\Wgamma iso",         "nonPromptWGamma": "\\Wgamma non prompt",  
					     "isolatedZGamma":  "\\Zgamma iso",         "nonPromptZGamma": "\\Zgamma non prompt",  
					     "isolatedOther":   "other\\_1 $\\gamma$ iso","nonPromptOther":  "other\\_1 $\\gamma$ non prompt"
					    }
	totalMCEvents = 0
	fullPercent = 0
	nEvents1 =0
	for ih in newtemplateHist:
		nEvents1 = templateHist[ih].Integral(1,templateHist[ih].GetNbinsX(),"width")
		print ih , nEvents1
		totalMCEvents += nEvents1
	print "just a check: totol number of MC events:",totalMCEvents

	for ih in newtemplateHist:
		error = Double(0.)
		nEvents = templateHist[ih].IntegralAndError(1,templateHist[ih].GetNbinsX(),error,"width")
		# print nEvents
		totalMC += nEvents
		totalMCerror += error*error
		percent = nEvents/(totalMCEvents+nQCDEvents)*100
		fullPercent += percent
		line += "%s & $%.1f \\pm %.1f$ & %.2f \\\\ \n"%(latex_categoryName[ih], nEvents, error, percent) 
		line += "\\hline \n"

	#print "prefit==>",nEventData, totalMC, sqrt(totalMCerror)
	# IMP: comment the line below when you have no QCD
	line += "%s & $%.1f \\pm %.1f$  & %.2f \\\\ \n"%("QCD\\_DD", nQCDEvents, errorQCD, nQCDEvents/(totalMCEvents+nQCDEvents)*100) 
	line += "\\hline \n"
	line += "Data = $%.1f $ & MC = $%.1f \\pm %.1f$ & %.2f \\\\ \n"%(nEventData, totalMC+nQCDEvents, sqrt(totalMCerror),fullPercent+ nQCDEvents/(totalMCEvents+nQCDEvents)*100) 
	# line += "Data = $%.2f \\pm %.2f$ & MC = $%.2f \\pm %.2f$  \\\\ \n"%(nEventData, dataError, totalMC, sqrt(totalMCerror)) 
	line += "\\hline \n"
	line += "\\end{tabular} \n"
	line += "\\end{table} \n"
	#print line



print "scale factors =======>",ZJetSF, WJetSF, MisIDEleSF, WGammaSF, ZGammaSF	
#print "WGamma ==>",(templateHist["isolatedWGamma"].Integral(-1,-1) + templateHist["nonPromptWGamma"].Integral(-1,-1))
#rint "ZGamma ==>",(templateHist["isolatedZGamma"].Integral(-1,-1) + templateHist["nonPromptZGamma"].Integral(-1,-1))

if mydistributionName == "M3":
	myfilename = "M3"
	# binning = numpy.array([50,500.])
	# binning = numpy.array([50,100,125,150,175,200,250,350,500.]) #good one
	binning = numpy.array([60., 100., 140., 160., 180., 200., 240., 280.,340., 420.,500.1]) #best one

	#binning = numpy.array([50,100,125,150,175,200,250,300,500.])
	#binning = numpy.array([50,100,120,140,160,180,200,220,240,260,280,300,340,400,500.])
# if mydistributionName == "M30btag":
if mydistributionName == "MassEGamma0btag":
	myfilename = "zerobtag"
	#binning = numpy.array([50,100,120,140,160,180,200,220,240,260,280,300,340,400,500.])
	# binning = numpy.array([0,500.]) # for M3 distribution
	if channel =='ele':
		# binning = numpy.array([0,80,100,180.])
		binning = numpy.array([0,80,84,88,92,96,100,180.])

	else:
		binning = numpy.array([0,91.,180.])
	#binning = numpy.array([50,100,125,150,175,200,250,350,500.])

if mydistributionName == "M30btag":
	myfilename = "zerobtag"
	# binning = numpy.array([60,500.1]) # for M3 distribution best one is yield only
	# binning = numpy.array([60., 100., 140., 160., 180., 200., 240., 280.,340., 420.,500.1]) # do not use shape
	# binning = numpy.array([60., 140., 200., 280., 500.1]) # do not use shape
	binning = numpy.array([60., 500.1]) # do not use shape

# if mydistributionName == "muPt0btag":
# 	myfilename = "zerobtag"
# 	binning = numpy.array([35,500.]) # for M3 distribution

# if mydistributionName == "elePt0btag":
# 	myfilename = "zerobtag"
# 	binning = numpy.array([25,500.]) # for M3 distribution

if mydistributionName == "LeadingPhotonEt0btag":
	myfilename = "zerobtag"
	mylist = [ 20.  ,30.,  40.,  50.,  60.,  70.,  80.,  90., 100., 110., 120., 130., 140.]
	# binning = numpy.array(mylist) # for photon pt distribution
	binning = numpy.array([20.,200.]) # for photon pt distribution

if mydistributionName == "ChIso":
	myfilename = "ChIso"
	# binning = numpy.array([0,0.5,1,2,5,12,20.])
	# binning = numpy.array([0.,1.141,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.,20.]) # include first bin
	# binning = numpy.array([1.141,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.,20.]) # without first bin
	binning = numpy.array([1.141,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.]) # without first bin, removing last bin
	# binning = numpy.array([1.141,20.]) # seems better with default plots.
	# binning = numpy.array([1.141,2,3,4,10,18.]) # seems better with default plots.

binWidth = numpy.diff(binning)
print binning
print "bin width",binWidth

rebinnedHist ={} 	

for ih in templateHist:
	print ih
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)

if systematics=='': 
	rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)

# if not useQCDMC:
# 	rebinnedqcdHist = qcdHist.Rebin(len(binning)-1,"",binning)
# 	#print rebinnedqcdHist.Print("All")
# 	rebinnedHist["nonPromptOther"].Add(rebinnedqcdHist)
	
sampleData = ""
if finalState=='Ele' and datadriven: sampleData = "DataEle"
elif finalState=='Mu' and datadriven: sampleData = "DataMu"
histo_sieie_MC  = None
histo_ChIso_MC  = None
print fileDir
print fileDirNom
if datadriven:
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

	histoFile = TFile.Open("%s%s.root"%(fileDirNom,sampleData),"read")
	histo = histoFile.Get("phosel_AntiSIEIE_ChIso_%s"%sampleData).Clone("histo")
	histo_sieie_Data1 = histo.Rebin(len(binning)-1,"",binning)
	histo_sieie_Data  = histo_sieie_Data1.Clone("histo_sieie_Data")
	# histo_ChIso_MC.Scale(1/histo_ChIso_MC.Integral())
	# histo_sieie_MC.Scale(1/histo_sieie_MC.Integral())
	for ibin in range(1,histo_sieie_MC.GetNbinsX()+1):
		# print              histo_ChIso_MC.GetBinContent(ibin), histo_sieie_MC.GetBinContent(ibin)	
		correctionFactor = histo_ChIso_MC.GetBinContent(ibin)/histo_sieie_MC.GetBinContent(ibin)
		newBinContent = (histo_sieie_Data1.GetBinContent(ibin) * correctionFactor )  #*binWidth[ibin-1]
		histo_sieie_Data.SetBinContent(ibin,newBinContent)

	print binWidth
	print len(binWidth)

	canvas = TCanvas()
	histo_sieie_Data.Scale(1/histo_sieie_Data.Integral())
	# histo_sieie_Data.Scale(1.,"width")
	histo_sieie_Data.Draw()
	canvas.Print("test.pdf")

	# sys.exit()

	for item in rebinnedHist.keys():
		if "nonPrompt" in item:
			#print item
			# nMCevents = rebinnedHist[item].Integral(-1,-1)
			nMCevents = rebinnedHist[item].Integral()
			print "==+>", item ,rebinnedHist[item].Integral()
			rebinnedHist[item] = histo_sieie_Data.Clone("rebinnedHist[%s]"%item)
			print "***>",item ,rebinnedHist[item].Integral()
			rebinnedHist[item].Scale(nMCevents)
			print "+++>",item, rebinnedHist[item].Integral()


for ih in templateHist:
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])
	if "nonPrompt" in ih:	rebinnedHist[ih].SetFillStyle( 3244);
	print "before feeding template/prefit ==>", ih, rebinnedHist[ih].Integral()

if template:
	myfile = TFile("%s%s.root"%(plotDirectory,"ttgamma_Prefit"),"update")
	# i have to get the nominal histogram from root file first and get the integration value

	if systematics=='':
		myDatahist = rebinnedData.Clone("nominal")
		mydataDir  = "%s/data_obs/"%myfilename

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
		myfile.cd()
		mydir =  "%s/%s/"%(myfilename,iprocess) 
		#print "%s/%s/"%(myfilename,iprocess) 
	
		if systematics=='':
			myhist = rebinnedHist[iprocess].Clone("nominal")
			for i_bin in range(1,myhist.GetNbinsX()+1):
				if myhist.GetBinContent(i_bin)==0: 
					myhist.SetBinContent(i_bin,0.1)
				# print "TEST*** ",iprocess,i_bin, myhist.GetBinContent(i_bin)
		else:
			myhist = rebinnedHist[iprocess].Clone("%s%s"%(systematics,mylevel))
			## check if any bin is empty in the histogram, if empty then 
			for i_bin in range(1,myhist.GetNbinsX()+1):
				if myhist.GetBinContent(i_bin)==0: myhist.SetBinContent(i_bin,0.1)
			if systematics in ["Q2","isr","fsr","Pdf","JECTotal0","JECTotal1","JER0","JER1"]:
			 	myNominalHist = myfile.Get(mydir+"nominal")
				if myNominalHist != None:
			 		valNominal = myNominalHist.Integral()
			 		val = myhist.Integral()
			 		if valNominal != 0 and val != 0:
			 			#print "nominal", valNominal, " ==> ", "syst %s"%systematics,val
			 			myhist.Scale(valNominal/val)
			 			#print "normalized", myhist.Integral()
			 	else:
			 		print "either nominal histogram is empty, systematics histogram is empty."
	
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
	#print "%s%s.root"%(plotDirectory,"ttgamma_Prefit")

	myfile.Close()
	sys.exit()
### For plotting
else:

	if prefitPlots:
		rebinnedData.Scale(1.,"width")
		nEventData = rebinnedData.Integral("width")

		for ih in rebinnedHist:
			rebinnedHist[ih].Scale(1.,"width")	
		
		stack = THStack()
		stack.Add(rebinnedHist["nonPromptOther"  ])
		stack.Add(rebinnedHist["nonPromptZGamma" ])   
		stack.Add(rebinnedHist["nonPromptWGamma" ])   
		stack.Add(rebinnedHist["nonPromptTTbar"  ]) 
		stack.Add(rebinnedHist["nonPromptTTGamma"])  
		stack.Add(rebinnedHist["isolatedOther"   ])  
		stack.Add(rebinnedHist["isolatedZGamma"  ])   
		stack.Add(rebinnedHist["isolatedWGamma"  ])  
		stack.Add(rebinnedHist["isolatedTTbar"   ]) 
		stack.Add(rebinnedHist["isolatedTTGamma" ]) 
		print "prefit stuff"
		print "Total # of events in M3 distribution", stack.GetStack().Last().Integral("width")
		if M3Plot: print "Total # of events in M3 distribution", stack.GetStack().Last().Integral("width")
		if ChIsoPlot: print "Total # of events in 1st bin of ChIso distribution", stack.GetStack().Last().GetBinWidth(1)*stack.GetStack().Last().GetBinContent(1)
		

		f = TFile("CombinedData/prefit_%s_%s_%s.root"%(channel,selYear,mydistributionName),"RECREATE")
		rebinnedData.Write("rebinnedData")
		rebinnedHist["isolatedTTGamma" ].Write()  
		rebinnedHist["nonPromptTTGamma"].Write()  
		rebinnedHist["isolatedTTbar"   ].Write()
		rebinnedHist["nonPromptTTbar"  ].Write()
		rebinnedHist["isolatedWGamma"  ].Write()		 
		rebinnedHist["nonPromptWGamma" ].Write()		  
		rebinnedHist["isolatedZGamma"  ].Write()		  
		rebinnedHist["nonPromptZGamma" ].Write()		  
		rebinnedHist["isolatedOther"   ].Write()		 
		rebinnedHist["nonPromptOther"  ].Write() 
		f.Close()
	
	elif postfitPlots:
		if not noData: rebinnedData.Scale(1.,"width")
		if ratioPlot == True:
			if finalState=="Ele": filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttR%s/fitDiagnostics%s_%s.root"%(selYear,channel,selYear)
			if finalState=="Mu":  filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttR%s/fitDiagnostics%s_%s.root"%(selYear,channel,selYear)
		elif xsecPlot == True:
			if finalState=="Ele": filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttXsection%s/fitDiagnostics%s_%s.root"%(selYear,channel,selYear)
			if finalState=="Mu":  filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttXsection%s/fitDiagnostics%s_%s.root"%(selYear,channel,selYear)
		else:
			if finalState=="Ele": filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma%s/fitDiagnostics%s_%s.root"%(selYear,channel,selYear)
			if finalState=="Mu":  filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma%s/fitDiagnostics%s_%s.root"%(selYear,channel,selYear)
		print filename
		Postfile = TFile(filename,"read")
		
		templatePostHist = {}
		print "bin width",binWidth
		templatePostHist["isolatedTTGamma" ] = TH1F("isolatedTTGamma" ,"",len(binWidth),binning)
		templatePostHist["nonPromptTTGamma"] = TH1F("nonPromptTTGamma","",len(binWidth),binning)
		templatePostHist["isolatedTTbar"   ] = TH1F("isolatedTTbar"   ,"",len(binWidth),binning)   
		templatePostHist["nonPromptTTbar"  ] = TH1F("nonPromptTTbar"  ,"",len(binWidth),binning)  
		templatePostHist["isolatedWGamma"  ] = TH1F("isolatedWGamma"  ,"",len(binWidth),binning)   
		templatePostHist["nonPromptWGamma" ] = TH1F("nonPromptWGamma" ,"",len(binWidth),binning)   
		templatePostHist["isolatedZGamma"  ] = TH1F("isolatedZGamma"  ,"",len(binWidth),binning)    
		templatePostHist["nonPromptZGamma" ] = TH1F("nonPromptZGamma" ,"",len(binWidth),binning)   
		templatePostHist["isolatedOther"   ] = TH1F("isolatedOther"   ,"",len(binWidth),binning)    
		templatePostHist["nonPromptOther"  ] = TH1F("nonPromptOther"  ,"",len(binWidth),binning)   

		###IMP
		# How to with Null pointer
		for process in template_category.keys():
			# if process == "nonPromptWGamma" or process== "nonPromptZGamma": continue
			tempHist = None
			print "distribution name and file name", mydistributionName, myfilename
			if "0btag" in mydistributionName: tempHist = Postfile.Get("shapes_fit_s/%s/%s"%(myfilename,process))
			else:tempHist = Postfile.Get("shapes_fit_s/%s/%s"%(mydistributionName,process))
			print tempHist

			print process, tempHist
			if tempHist:
				for ibin in range(1,len(binning)):
					myBinContent = tempHist.GetBinContent(ibin)
					templatePostHist[process].SetBinContent(ibin,myBinContent)
			else:
				print "Null pointer"
			templatePostHist[process].SetLineColor(template_category[process])
			templatePostHist[process].SetFillColor(template_category[process])
			templatePostHist[process].Scale(1.,"width")
			if "nonPrompt" in process:	templatePostHist[process].SetFillStyle( 3244);

		stack = THStack()
		stack.Add(templatePostHist["nonPromptOther"  ])
		stack.Add(templatePostHist["nonPromptZGamma" ])   
		stack.Add(templatePostHist["nonPromptWGamma" ])   
		stack.Add(templatePostHist["nonPromptTTbar"  ]) 
		stack.Add(templatePostHist["nonPromptTTGamma"])  
		stack.Add(templatePostHist["isolatedOther"   ])  
		stack.Add(templatePostHist["isolatedZGamma"  ])   
		stack.Add(templatePostHist["isolatedWGamma"  ])  
		stack.Add(templatePostHist["isolatedTTbar"   ]) 
		stack.Add(templatePostHist["isolatedTTGamma" ]) 

		# stack.Add(templatePostHist["nonPromptOther"  ])
		# stack.Add(templatePostHist["isolatedOther"   ])  
		# stack.Add(templatePostHist["nonPromptZGamma" ])   
		# stack.Add(templatePostHist["nonPromptWGamma" ])   
		# stack.Add(templatePostHist["isolatedZGamma"  ])   
		# stack.Add(templatePostHist["isolatedWGamma"  ])  
		# stack.Add(templatePostHist["nonPromptTTbar"  ]) 
		# stack.Add(templatePostHist["isolatedTTbar"   ]) 
		# stack.Add(templatePostHist["nonPromptTTGamma"])  
		# stack.Add(templatePostHist["isolatedTTGamma" ]) 
		print "postfit stuff"


		if noData:
			rebinnedData = TH1F("rebinnedData" ,"",len(binWidth),binning)
			fakeData = Postfile.Get("shapes_fit_s/%s/%s"%(myfilename,"data"))
			nPoints = fakeData.GetN()
			x = Double(0.)
			y = Double(0.)
			for i in range(0,nPoints):
				# print i
				fakeData.GetPoint(i, x, y)
				# print x-0.5,y
				ey = fakeData.GetErrorY(i)
				rebinnedData.SetBinContent(i+1, y)
				rebinnedData.SetBinError(i+1, ey)
			
			rebinnedData.Scale(1.,"width")		
			rebinnedData.SetMarkerStyle(kFullCircle)


		f = TFile("CombinedData/postfit_%s_%s_%s.root"%(channel,selYear,mydistributionName),"RECREATE")
		rebinnedData.Write("rebinnedData")
		templatePostHist["isolatedTTGamma" ].Write()  
		templatePostHist["nonPromptTTGamma"].Write()  
		templatePostHist["isolatedTTbar"   ].Write()
		templatePostHist["nonPromptTTbar"  ].Write()
		templatePostHist["isolatedWGamma"  ].Write()		 
		templatePostHist["nonPromptWGamma" ].Write()		  
		templatePostHist["isolatedZGamma"  ].Write()		  
		templatePostHist["nonPromptZGamma" ].Write()		  
		templatePostHist["isolatedOther"   ].Write()		 
		templatePostHist["nonPromptOther"  ].Write() 
		f.Close()
			# sys.exit()
		#_file["Data%s"%finalState].cd()
		#rebinnedMC = stack.GetStack().Last().Clone("rebinnedMC")
		#x = rebinnedData.Chi2Test(rebinnedMC,"WW CHI2/NDF") 
		#chi2Text = "#chi^{2}/NDF=%.3f"%x
	# else: "prefit or postfit?"

	#rebinnedMC = stack.GetStack().Last().Clone("rebinnedMC")	
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

	oneLine = TF1("oneline","1",-9e9,9e9)
	oneLine.SetLineColor(kBlack)
	oneLine.SetLineWidth(1)
	oneLine.SetLineStyle(2)

	maxVal = stack.GetMaximum()
	if not noData: 
	    maxVal = max(rebinnedData.GetMaximum(),maxVal)

	minVal = 0.1
	# if mydistributionName == "ChIso": minVal = 60
	stack.SetMinimum(minVal)
	print minVal
	stack.SetMaximum(1.75*maxVal)
	if mydistributionName == "ChIso": stack.SetMaximum(2.5*maxVal)

	errorband=stack.GetStack().Last().Clone("errorband")
	errorband.Sumw2()
	errorband.SetLineColor(kBlack)
	errorband.SetFillColor(kBlack)
	errorband.SetFillStyle(3245)
	errorband.SetMarkerSize(0)
	


	if not noData == True:
		legend.AddEntry(rebinnedData,"Data", 'pe')
	if noData:legend.AddEntry(rebinnedData,"Toy Data", 'pe')
	legend.AddEntry(errorband,"Uncertainty","f")
	legend.AddEntry(rebinnedHist["isolatedTTGamma" ],template_categoryName["isolatedTTGamma" ],'f')	
	legend.AddEntry(rebinnedHist["nonPromptTTGamma"],template_categoryName["nonPromptTTGamma"],'f')  
	legend.AddEntry(rebinnedHist["isolatedTTbar"   ],template_categoryName["isolatedTTbar"   ],'f') 
	legend.AddEntry(rebinnedHist["nonPromptTTbar"  ],template_categoryName["nonPromptTTbar"  ],'f') 
	legend.AddEntry(rebinnedHist["isolatedWGamma"  ],template_categoryName["isolatedWGamma"  ],'f')  
	legend.AddEntry(rebinnedHist["nonPromptWGamma" ],template_categoryName["nonPromptWGamma" ],'f')  
	legend.AddEntry(rebinnedHist["isolatedZGamma"  ],template_categoryName["isolatedZGamma"  ],'f')
	legend.AddEntry(rebinnedHist["nonPromptZGamma" ],template_categoryName["nonPromptZGamma" ],'f')   
	legend.AddEntry(rebinnedHist["isolatedOther"   ],template_categoryName["isolatedOther"   ],'f')  
	legend.AddEntry(rebinnedHist["nonPromptOther"  ],template_categoryName["nonPromptOther"  ],'f')
	# legend.SetTextSize(0.035)
	pad1.cd()
	

	stack.Draw('HIST')
	if not noData == True:
		rebinnedData.Draw('E,X0,SAME')
	if noData:
		rebinnedData.Draw('E,X0,SAME')
	legend.Draw("same")
	stack.GetXaxis().SetTitle('')
	stack.GetXaxis().SetLabelSize(0)
	stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
	stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
	stack.GetYaxis().SetTitleSize(.049)
	stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
	stack.SetTitle(';;<Events/GeV>')# '%rebin)
	# if mydistributionName == "ChIso": gPad.SetLogy()

	#CMS_lumi.channelText = (channelText+"\\n"+regionText)
	#if postfitPlots: CMS_lumi.channelText =channelText+"\\n "+regionText+"\\n "+chi2Text
	CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText,regionText)
	#if postfitPlots: CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText+";"+regionText,chi2Text)s
	CMS_lumi.writeChannelText = True
	CMS_lumi.writeExtraText = True
	CMS_lumi.CMS_lumi(pad1, 4, 11)

	print "Test line"


	if not noData:
		ratio = rebinnedData.Clone("ratio")
		temp = stack.GetStack().Last().Clone("temp")
		for i_bin in range(1,temp.GetNbinsX()+1):
			temp.SetBinError(i_bin,0.)
		ratio.Divide(temp)
	else:
		ratio = rebinnedData.Clone("ratio")
		temp = stack.GetStack().Last().Clone("temp")
		ratio.Divide(temp)

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
	ratio.GetXaxis().SetTitle('%s(GeV)'%myfilename)

	ratio.GetYaxis().SetTitle("Data/MC")
	ratio.GetYaxis().SetTitleOffset(.4)
	ratio.GetYaxis().SetTitleSize(.1)
	ratio.GetXaxis().SetTitleSize(.1)
	ratio.GetYaxis().SetNdivisions(-402)
	CMS_lumi.CMS_lumi(pad2, 4, 11)
	pad2.cd()
	maxRatio = 1.5
	minRatio = 0.5
	print "==", rebinnedData.GetMarkerStyle()
	ratio.SetMarkerStyle(rebinnedData.GetMarkerStyle())
	ratio.SetMarkerSize(rebinnedData.GetMarkerSize())
	ratio.SetLineColor(rebinnedData.GetLineColor())
	ratio.SetLineWidth(rebinnedData.GetLineWidth())
	ratio.Draw('e,x0')
	errorbandRatio = errorband.Clone("errorbandRatio")
	errorbandRatio.Divide(temp)
	errorbandRatio.Draw('e2,same')
	oneLine.Draw("same")

	canvasRatio.Update()
	canvasRatio.RedrawAxis()

	if btag0_3j:mydistributionName=mydistributionName+"_3j"

	
	if postfitPlots:
		if ratioPlot == True:
			canvasRatio.SaveAs("%s%s_%s_postfit_ratioPlot.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
			canvasRatio.Print("%s%s_%s_postfit_ratioPlot.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
		elif xsecPlot == True:
			canvasRatio.SaveAs("%s%s_%s_postfit_xsectionPlot.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
			canvasRatio.Print("%s%s_%s_postfit_xsectionPlot.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
		else:
			canvasRatio.SaveAs("%s%s_%s_postfit.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
			canvasRatio.Print("%s%s_%s_postfit.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
	else:

		canvasRatio.SaveAs("%s%s_%s.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
		canvasRatio.Print("%s%s_%s.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
		#myfile.Close()
	canvasRatio.Close()

	print "EventYieldTables/EventsYield_%s_%s_%s_%s.tex"%(crName,channel,selYear,mydistributionName)
  	with open("EventYieldTables/EventsYield_%s_%s_%s_%s.tex"%(crName,channel,selYear,mydistributionName),"w") as _file:
	   		_file.write(line)
	_file.close()  
	
	
	
	
	
	
	
	
	

