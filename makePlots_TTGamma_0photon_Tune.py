from ROOT import kFullCircle,TFile, TLegend, Double,TCanvas,gPad, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory,kCyan,kViolet
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

from colorama import Fore, Back, Style 

# from TTGamma_nonPrompt_2016 import *

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

parser.add_option("--verytight","--verytight", dest="verytight", default=False,action="store_true",
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


# python makePlot_M3Control.py -y 2016 -c Ele   --zeroPhoton --prefitPlots 

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
verytight     = options.verytight
useQCDMC      = options.useQCDMC
useQCDCR      = options.useQCDCR
noQCD         = options.noQCD
noData        = options.noData
zeroPhoton    = options.zeroPhoton

template        = options.template

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

RunIISytematics = ["BTagSF_b16","BTagSF_l16","JER16","BTagSF_b17","BTagSF_l17","JER17","BTagSF_b18","BTagSF_l18","JER18"]
commonSystematics= ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","Pdf","fsr","isr", "prefireEcal","Tune"]
separateSytematics =  ["JER0", "JECTotal0","JER1", "JECTotal1"]
allsystematics = RunIISytematics+commonSystematics+separateSytematics

print RunIISytematics
print commonSystematics
print separateSytematics
print allsystematics


if systematics in allsystematics: print "running on systematics"
else: print(Fore.RED + "systematics is not in list. Add the systematics in the list if you are running for systematics.")

print(Style.RESET_ALL) 

if level=='up': mylevel='Up'
if level=='down': mylevel='Down'

#eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"

#######
########

if zeroPhoton:      #tight but 0 photon
	crName = "zeroPhoton"
	isSelection = "looseCRge2e0"
	# isSelection = "looseCRge4e0"
	# isSelection = "looseCRe2e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDirQCD = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	if systematics in allsystematics:
		if systematics in RunIISytematics: 
			print systematics, " For full RunII"
			fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics[:-2],level)
			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
			regionText = "N_{j}#geq4, N_{b}#geq1"
		
		# elif systematics=="JECTotal0" or systematics=="JER0" or systematics=="JECTotal1" or systematics=="JER1": 
		elif systematics in separateSytematics:
			print "JECTotal and JER stuffs."
			fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics[:-1],level)
			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
			regionText = "N_{j}#geq4, N_{b}#geq1"

		elif systematics in commonSystematics:
			print "Common systematics"
			fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics,level)
			plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
			regionText = "N_{j}#geq4, N_{b}#geq1"		
	else:
		fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
		
print ZJetSF,"==>",WJetSF,"==>",MisIDEleSF,"==>",ZGammaSF,"==>",WGammaSF
# 1.09 ==> 1.14 ==> 2.24 ==> 0.82 ==> 1.15
# 1.0  ==> 1.14 ==> 2.42 ==> 1.17 ==> 1.25
# 1.14 ==> 1.32 ==> 2.69 ==> 1.12 ==> 0.36

# python makePlots.py -y 2016 -c Ele --tight --plot presel_M3
# python makePlots.py -y 2016 -c Mu --tight  --plot presel_M3

# if zeroPhoton:      #tight but 0 photon
# 	crName = "zeroPhoton"
# 	isSelection = "looseCRge2e0"
# 	# isSelection = "looseCRge4e0"
# 	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
# 	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
# 	else :                ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
# 	fileDirQCD = "histograms_%s/%s/hists_verytight/"%(selYear, channel)
# 	if systematics in allsystematics:
# 		if "1" in systematics:
# 			fileDir  = "histograms_%s/%s/hists_%s_%s_verytight/"%(selYear, channel,systematics[:-2],level)
# 			plotDirectory = "ttgamma_verytightplots_%s_%s/"%(channel,selYear)
# 			regionText = "N_{j}#geq4, N_{b}#geq2"
# 		else:
# 			fileDir  = "histograms_%s/%s/hists_%s_%s_verytight/"%(selYear, channel,systematics,level)
# 			plotDirectory = "ttgamma_verytightplots_%s_%s/"%(channel,selYear)
# 			regionText = "N_{j}#geq4, N_{b}#geq2"			
# 	else:
# 		fileDir  = "histograms_%s/%s/hists_verytight/"%(selYear, channel)
# 		#fileDir  = "histograms_%s/%s/hists_verytight/"%(selYear, channel)
# 		plotDirectory = "ttgamma_verytightplots_%s_%s/"%(channel,selYear)
# 		regionText = "N_{j}#geq4, N_{b}#geq2"
		
eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
localFolder="/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/"

fileDirQCD = eosFolder + fileDirQCD
print fileDirQCD

fileDir = eosFolder + fileDir

print fileDir

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

from Style import *

gROOT.ForceStyle()

if systematics=="Tune":
	sampleList=['TTGamma']
else:
	sampleList = ['TTGamma', 'TTbar', 'SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
# sampleList = ['TTGamma', 'TTbar', 'SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
# sampleList = ['TTGamma', 'TTbar', 'SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
# sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'SingleTop':kOrange-3, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7,'GJets':kGreen+1,"QCD":kGreen+3}
sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7,'GJets':kGreen+1,"QCD":kGreen+3}

#sampleList = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV']
#sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'TGJets':kGray,'SingleTop':kOrange-3, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7}


template_category = {"TTGamma":kOrange,  
					 "TTbar":  kRed+1,    
					 "WGamma": kBlue-4, 
					 "ZGamma": kBlue-2,   
					 "SingleTop": 228,   
					 "Other":  kGreen+3}
template_categoryName = {"TTGamma":"t#bar{t}#gamma", 
					     "TTbar":  "t#bart",    
					     "WGamma": "W#gamma", 
					     "ZGamma": "Z#gamma",   
					     "SingleTop": "t",   
					     "Other":  "Other_0#gamma"}
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
	print ""
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
legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((7+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legend.SetNColumns(2)

#legendR = TLegend(0.71, 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*(len(legList)+1), 0.99-(R/W), 0.99-(T/H)/(1.-padRatio+padOverlap))


legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((7+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))

legendR.SetNColumns(2)

legendR.SetBorderSize(0)
legendR.SetFillColor(0)

legend.SetBorderSize(0)
legend.SetFillColor(0)

histName  	= "presel_M3_%s"
histNameData= "presel_M3_%s" 
mydistributionName = histNameData[7:-3]+"0photon"
print mydistributionName

templateHist ={}
	
for sample in sampleList:
	if sample=="QCD_DD": 
		#print "==>",sample, fileDirQCD
		_file[sample] = TFile.Open('%s%s.root'%(fileDirQCD,sample),'read')
		qcdhistName = histNameData.replace("mediumID_","noCut_")
		qcdHist = _file[sample].Get(qcdhistName%(sample))
		print "qcdHist data driven ==>",qcdHist.Integral(-1,-1)
		errorQCD = Double(0.)
		nQCDEvents = qcdHist.IntegralAndError(1,qcdHist.GetNbinsX(),errorQCD,"width")

	else:
		#print sample, fileDir
		_file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')
	
templateHist = {}

templateHist["TTGamma" ] = None 
# templateHist["TTbar"   ] = None
# templateHist["WGamma"  ] = None 
# templateHist["ZGamma"  ] = None  
# templateHist["SingleTop"  ] = None  
# templateHist["Other"   ] = None 

print sampleList

mystack = THStack()
for sample in sampleList:
	if sample=='QCD_DD': continue 

	tempHist = _file[sample].Get(histName%(sample))
	print tempHist
	
	if sample=='ZJets': tempHist.Scale(ZJetSF)
	if sample=='WJets': tempHist.Scale(WJetSF)
		#print "ZJetSF", ZJetSF
    # addd WJetsSF here. IMP
	print sample, "==>", tempHist.Integral()	

	if   sample=='TTGamma': templateHist["TTGamma"]= tempHist.Clone("TTGamma")
	elif sample=='TTbar'  : templateHist["TTbar"]  = tempHist.Clone("TTbar")
	elif sample=='WGamma' :	templateHist["WGamma"] = tempHist.Clone("WGamma")
	elif sample=='ZGamma' : templateHist["ZGamma"] = tempHist.Clone("ZGamma")
	elif sample=='SingleTop' : templateHist["SingleTop"] = tempHist.Clone("SingleTop")
	# elif sample=='TTV':
	else:

		if  templateHist["Other"] is None:
			templateHist["Other"] = tempHist.Clone("Other")
			templateHist["Other"].SetDirectory(0)
		else:
			templateHist["Other"].Add(tempHist)
		
		print ""
		
binning = numpy.array([60., 100., 140., 160., 180., 200., 240., 280.,340., 420.,500.1]) # best one
# binning = numpy.array([60.,140.,200., 500.1]) # 3bins
# binning = numpy.array([60.,500.1]) # 1bins

print binning
binWidth = numpy.diff(binning)

rebinnedHist ={} 

for ih in templateHist:
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])

# rebinnedqcdHist = qcdHist.Rebin(len(binning)-1,"",binning)
# rebinnedHist["Other"].Add(rebinnedqcdHist)

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
	dataError = Double(0.)
	nEventData = data_obs.IntegralAndError(1,data_obs.GetNbinsX(),dataError,"width")
	print "nEventsData ==>", nEventData
	rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)	


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
	newtemplateHist = ["TTGamma","TTbar","ZGamma","WGamma","Other"]
	latex_categoryName = {"TTGamma": "\\ttgamma ",        
					      "TTbar":   "\\ttbar ",          
					      "WGamma":  "\\Wgamma ",         
					      "ZGamma":  "\\Zgamma ",         
					      "SingleTop":  "\\SingleTop ",         
					      "Other":   "other"
					    }
	totalMCEvents = 0
	fullPercent = 0
	for ih in newtemplateHist:
		nEvents1 = templateHist[ih].Integral(1,templateHist[ih].GetNbinsX(),"width")
		# print nEvents
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
	line += "%s & $%.1f \\pm %.1f$ & %.2f \\\\ \n"%("QCD\\_DD", nQCDEvents, errorQCD, nQCDEvents/(totalMCEvents+nQCDEvents)*100) 
	line += "\\hline \n"
	line += "Data = $%.1f $ & MC = $%.1f \\pm %.1f$  & %.2f \\\\ \n"%(nEventData, totalMC+nQCDEvents, sqrt(totalMCerror),fullPercent+nQCDEvents/(totalMCEvents+nQCDEvents)*100 ) 
	# line += "Data = $%.2f \\pm %.2f$ & MC = $%.2f \\pm %.2f$  \\\\ \n"%(nEventData, dataError, totalMC, sqrt(totalMCerror)) 
	line += "\\hline \n"
	line += "\\end{tabular} \n"
	line += "\\end{table} \n"
	#print line

if template:	
	myfile = TFile("%s%s.root"%(plotDirectory,"ttgamma_Prefit"),"update")
		# i have to get the nominal histogram from root file first and get the integration value

	myfilename = mydistributionName

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
	for iprocess in ["TTGamma"]:

		myfile.cd()
		mydir =  "%s/%s/"%(myfilename,iprocess) 
		#print "%s/%s/"%(myfilename,iprocess) 

		if systematics=='':
			myhist = rebinnedHist[iprocess].Clone("nominal")
		else:
			myhist = rebinnedHist[iprocess].Clone("%s%s"%(systematics,mylevel))
			# if systematics in ["Q2","isr","fsr","Pdf","JECTotal0","JECTotal1","JER0","JER1","Tune"]:
			if systematics in ["Tune"]:
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
	print "%s%s.root"%(plotDirectory,"ttgamma_Prefit")

	myfile.Close()
	sys.exit()

else:
	print "Done"
	if prefitPlots:
		rebinnedData.Scale(1.,"width")
		for ih in rebinnedHist:
			rebinnedHist[ih].Scale(1.,"width")	

		stack = THStack()
		stack.Add(rebinnedHist["Other"  ])
		stack.Add(rebinnedHist["SingleTop" ])   
		stack.Add(rebinnedHist["ZGamma" ])   
		stack.Add(rebinnedHist["WGamma" ])   
		stack.Add(rebinnedHist["TTbar"  ]) 
		stack.Add(rebinnedHist["TTGamma"])  
		#rebinnedMC = stack.GetStack().Last().Clone("rebinnedMC")


		f = TFile("CombinedData/prefit_%s_%s_%s.root"%(channel,selYear,mydistributionName),"RECREATE")
		rebinnedData.Write("rebinnedData")
		rebinnedHist["TTGamma" ].Write()  
		rebinnedHist["TTbar"   ].Write()
		rebinnedHist["WGamma"  ].Write()		 
		rebinnedHist["ZGamma"  ].Write()		  
		rebinnedHist["SingleTop"  ].Write()		  
		rebinnedHist["Other"   ].Write()		 
		f.Close()


	elif postfitPlots:
		rebinnedData.Scale(1.,"width")

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
		# if finalState=="Ele": filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma/fitDiagnostics%s_%s.root"%(channel[:-1],selYear)
		# if finalState=="Mu":  filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma/fitDiagnostics%s_%s.root"%(channel,selYear)
		Postfile = TFile(filename,"read")
		templatePostHist = {}
		# print len(binning),"==>",len(binWidth)
		templatePostHist["TTGamma" ] = TH1F("TTGamma" ,"",len(binWidth),binning)
		templatePostHist["TTbar"   ] = TH1F("TTbar"   ,"",len(binWidth),binning)   
		templatePostHist["WGamma"  ] = TH1F("WGamma"  ,"",len(binWidth),binning)   
		templatePostHist["ZGamma"  ] = TH1F("ZGamma"  ,"",len(binWidth),binning)    
		templatePostHist["SingleTop"  ] = TH1F("SingleTop"  ,"",len(binWidth),binning)    
		templatePostHist["Other"   ] = TH1F("Other"   ,"",len(binWidth),binning)    

		for process in template_category.keys():
			#tempHist = None
			tempHist = Postfile.Get("shapes_fit_s/%s/%s"%(mydistributionName,process))
			for ibin in range(1,len(binning)):
				myBinContent = tempHist.GetBinContent(ibin)
				templatePostHist[process].SetBinContent(ibin,myBinContent)
			templatePostHist[process].SetLineColor(template_category[process])
			templatePostHist[process].SetFillColor(template_category[process])
			templatePostHist[process].Scale(1.,"width")

		stack = THStack()
		stack.Add(templatePostHist["Other"   ])  
		stack.Add(templatePostHist["SingleTop"  ])   
		stack.Add(templatePostHist["ZGamma"  ])   
		stack.Add(templatePostHist["WGamma"  ])  
		stack.Add(templatePostHist["TTbar"   ]) 
		stack.Add(templatePostHist["TTGamma" ]) 


		if noData:
			rebinnedData = TH1F("rebinnedData" ,"",len(binWidth),binning)
			fakeData = Postfile.Get("shapes_fit_s/%s/%s"%(mydistributionName,"data"))
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
		templatePostHist["TTGamma" ].Write()  
		templatePostHist["TTbar"   ].Write()
		templatePostHist["WGamma"  ].Write()		 
		templatePostHist["ZGamma"  ].Write()		  
		templatePostHist["SingleTop"  ].Write()		  
		templatePostHist["Other"   ].Write()		 
		f.Close()

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

	# noData = False

	oneLine = TF1("oneline","1",-9e9,9e9)
	oneLine.SetLineColor(kBlack)
	oneLine.SetLineWidth(1)
	oneLine.SetLineStyle(2)

	maxVal = stack.GetMaximum()
	if not noData: 
	    maxVal = max(rebinnedData.GetMaximum(),maxVal)

	minVal = 0
	if mydistributionName == "ChIso": minVal = 1
	#print minVal
	# minVal = max(stack.GetStack()[0].GetMinimum(),1)
	stack.SetMaximum(1.5*maxVal)
	if mydistributionName == "ChIso": stack.SetMaximum(20*maxVal)
	stack.SetMinimum(minVal)

	errorband=stack.GetStack().Last().Clone("error")
	errorband.Sumw2()
	errorband.SetLineColor(kBlack)
	errorband.SetFillColor(kBlack)
	errorband.SetFillStyle(3245)
	errorband.SetMarkerSize(0)

	if not noData == True:
		legend.AddEntry(rebinnedData,"Data", 'pe')

	legend.AddEntry(errorband,"Uncertainty","f")

	#for ih in rebinnedHist:
	#	legend.AddEntry(rebinnedHist[ih],template_categoryName[ih],'f')
	if noData:legend.AddEntry(rebinnedData,"Toy Data", 'pe')
	legend.AddEntry(rebinnedHist["TTGamma" ],template_categoryName["TTGamma" ],'f')	
	legend.AddEntry(rebinnedHist["TTbar"   ],template_categoryName["TTbar"   ],'f') 
	legend.AddEntry(rebinnedHist["WGamma"  ],template_categoryName["WGamma"  ],'f')  
	legend.AddEntry(rebinnedHist["ZGamma"  ],template_categoryName["ZGamma"  ],'f')
	legend.AddEntry(rebinnedHist["SingleTop"  ],template_categoryName["SingleTop"  ],'f')
	legend.AddEntry(rebinnedHist["Other"   ],template_categoryName["Other"   ],'f')  
	
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
	stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
	stack.SetTitle(';;<Events/GeV>')# '%rebin)
	if mydistributionName == "ChIso": gPad.SetLogy()

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

	ratio.GetXaxis().SetTitle('%s(GeV)'%mydistributionName)

	ratio.GetYaxis().SetTitle("Data/MC")
	ratio.GetYaxis().SetTitleOffset(.4)
	ratio.GetYaxis().SetTitleSize(.09)
	ratio.GetYaxis().SetNdivisions(2) 
	CMS_lumi.CMS_lumi(pad2, 4, 11)
	pad2.cd()
	maxRatio = 1.5
	minRatio = 0.5
	ratio.SetMarkerStyle(rebinnedData.GetMarkerStyle())
	ratio.SetMarkerSize(rebinnedData.GetMarkerSize())
	ratio.SetLineColor(rebinnedData.GetLineColor())
	ratio.SetLineWidth(rebinnedData.GetLineWidth())
	ratio.Draw('e,x0')
	errorbandRatio = errorband.Clone("errorRatio")
	errorbandRatio.Divide(temp)
	errorbandRatio.Draw('e2,same')
	oneLine.Draw("same")

	# canvasRatio.Update()
	canvasRatio.RedrawAxis()

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
	

#
#if postfitPlots:
# 	print"no need save root file"
#else:
# 	myfile = TFile(plotDirectory+"promptTemplate_%s_%s_Prefit.root"%(channel,mydistributionName),"recreate")
#
#for ih in templateHist:
#	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
#	rebinnedHist[ih].SetLineColor(template_category[ih])
#	rebinnedHist[ih].SetFillColor(template_category[ih])
#	rebinnedHist[ih].Write()
#
#rebinnedData.Write()
## forget about plotting right now. Just make a template.
#
### purpose for plotting 
#rebinnedData.Scale(1.,"width")
#	
#stack = THStack()
#print rebinnedHist.keys()
#
#for ih in rebinnedHist:
#	rebinnedHist[ih].Scale(1.,"width")
#
#stack.Add(rebinnedHist["Other"])
#stack.Add(rebinnedHist["ZGamma"])
#stack.Add(rebinnedHist["WGamma"])
#stack.Add(rebinnedHist["TTbar"])
#stack.Add(rebinnedHist["TTGamma"])
#
#
#if postfitPlots:
#	MC = stack.GetStack().Last().Clone("MC")
#	x = rebinnedData.Chi2Test(MC,"UW CHI2/NDF") 
#	chi2Text = "#chi^{2}/NDF=%.2f"%x
#
#	
#canvasRatio = TCanvas('c1Ratio','c1Ratio',W,H)
#canvasRatio.SetFillColor(0)
#canvasRatio.SetBorderMode(0)
#canvasRatio.SetFrameFillStyle(0)
#canvasRatio.SetFrameBorderMode(0)
#canvasRatio.SetLeftMargin( L/W )
#canvasRatio.SetRightMargin( R/W )
#canvasRatio.SetTopMargin( T/H )
#canvasRatio.SetBottomMargin( B/H )
#canvasRatio.SetTickx(0)
#canvasRatio.SetTicky(0)
#canvasRatio.Draw()
#canvasRatio.cd()
#
#pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
#pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
#pad1.SetLeftMargin( L/W )
#pad1.SetRightMargin( R/W )
#pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
#pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
#pad1.SetFillColor(0)
#pad1.SetBorderMode(0)
#pad1.SetFrameFillStyle(0)
#pad1.SetFrameBorderMode(0)
#pad1.SetTickx(0)
#pad1.SetTicky(0)
#
#pad2.SetLeftMargin( L/W )
#pad2.SetRightMargin( R/W )
#pad2.SetTopMargin( (padOverlap)/(padRatio+padOverlap) )
#pad2.SetBottomMargin( B/H/(padRatio+padOverlap) )
#pad2.SetFillColor(0)
#pad2.SetFillStyle(4000)
#pad2.SetBorderMode(0)
#pad2.SetFrameFillStyle(0)
#pad2.SetFrameBorderMode(0)
#pad2.SetTickx(0)
#pad2.SetTicky(0)
#
#pad1.Draw()
#pad2.Draw()
#
#noData = False
#
#oneLine = TF1("oneline","1",-9e9,9e9)
#oneLine.SetLineColor(kBlack)
#oneLine.SetLineWidth(1)
#oneLine.SetLineStyle(2)
#
#maxVal = stack.GetMaximum()
#if not noData: 
#    maxVal = max(rebinnedData.GetMaximum(),maxVal)
#
#minVal = 1
## minVal = max(stack.GetStack()[0].GetMinimum(),1)
#stack.SetMaximum(1.25*maxVal)
#stack.SetMinimum(minVal)
#
#errorband=stack.GetStack().Last().Clone("error")
#errorband.Sumw2()
#errorband.SetLineColor(kBlack)
#errorband.SetFillColor(kBlack)
#errorband.SetFillStyle(3245)
#errorband.SetMarkerSize(0)
#
#legend.AddEntry(rebinnedData,"Data", 'pe')
#legend.AddEntry(errorband,"Uncertainty","f")
#
#for ih in rebinnedHist:
#	legend.AddEntry(rebinnedHist[ih],template_categoryName[ih],'f')
#
#pad1.cd()
#
#stack.Draw('HIST')
#rebinnedData.Draw('E,X0,SAME')
#legend.Draw("same")
#stack.GetXaxis().SetTitle('')
#stack.GetXaxis().SetLabelSize(0)
#stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
#stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
#stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
#stack.SetTitle(';;<Events/GeV>')# '%rebin)
#
##CMS_lumi.channelText = (channelText+"\\n"+regionText)
##if postfitPlots: CMS_lumi.channelText =channelText+"\\n "+regionText+"\\n "+chi2Text
#
#CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText,regionText)
#if postfitPlots: CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText+";"+regionText,chi2Text)
#
#CMS_lumi.writeChannelText = True
#CMS_lumi.writeExtraText = True
#CMS_lumi.CMS_lumi(pad1, 4, 11)
#
#if not noData:
#	ratio = rebinnedData.Clone("temp")
#	temp = stack.GetStack().Last().Clone("temp")
#	for i_bin in range(1,temp.GetNbinsX()+1):
#		temp.SetBinError(i_bin,0.)
#	ratio.Divide(temp)
#else:
#	ratio = rebinnedData.Clone("temp")
#	temp = stack.GetStack().Last().Clone("temp")
#    
#ratio.SetTitle('')
#ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
#ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
#ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
#ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
#ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap-padGap))
#
#maxRatio = ratio.GetMaximum()
#minRatio = ratio.GetMinimum()
#
#for i_bin in range(1,ratio.GetNbinsX()):
#	if ratio.GetBinError(i_bin)<1:
#		if ratio.GetBinContent(i_bin)>maxRatio:
#			maxRatio = ratio.GetBinContent(i_bin)
#		if ratio.GetBinContent(i_bin)<minRatio:
#			minRatio = ratio.GetBinContent(i_bin)
#
#if maxRatio > 1.8:
#	ratio.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
#elif maxRatio < 1:
#	ratio.GetYaxis().SetRangeUser(0,1.2)
#elif maxRatio-1 < 1-minRatio:
#	ratio.GetYaxis().SetRangeUser((1-(1-minRatio)*1.2),1.1*maxRatio)		
#else:
#	ratio.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)
#
#ratio.GetYaxis().SetRangeUser(0.8,1.2)
#ratio.GetYaxis().SetNdivisions(504)
#
#ratio.GetXaxis().SetTitle('%s(GeV)'%mydistributionName)
#
#ratio.GetYaxis().SetTitle("Data/MC")
#ratio.GetYaxis().SetTitleOffset(.4)
#ratio.GetYaxis().SetTitleSize(.09)
#ratio.GetYaxis().SetNdivisions(2) 
#CMS_lumi.CMS_lumi(pad2, 4, 11)
#pad2.cd()
#maxRatio = 1.5
#minRatio = 0.5
#ratio.SetMarkerStyle(rebinnedData.GetMarkerStyle())
#ratio.SetMarkerSize(rebinnedData.GetMarkerSize())
#ratio.SetLineColor(rebinnedData.GetLineColor())
#ratio.SetLineWidth(rebinnedData.GetLineWidth())
#ratio.Draw('e,x0')
#errorbandRatio = errorband.Clone("errorRatio")
#errorbandRatio.Divide(temp)
#errorbandRatio.Draw('e2,same')
#oneLine.Draw("same")
#
#canvasRatio.Update()
#canvasRatio.RedrawAxis()
#if postfitPlots:
#	canvasRatio.SaveAs("%s%s_%s_postfit.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
#	canvasRatio.Print("%s%s_%s_postfit.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
#else:
#	canvasRatio.SaveAs("%s%s_%s.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
#	canvasRatio.Print("%s%s_%s.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
#	myfile.Close()
#canvasRatio.Close()
#
#
#    
