from ROOT import TFile, TLegend, TCanvas,gPad, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory,kCyan,kViolet
#from ROOT import *
import os

import numpy
import sys
import argparse
from optparse import OptionParser
from sampleInformation import sampleList
import sampleInformation
from numpy import log10
from array import array

#from getFullYearMisIDEleSF import getFullYearMisIDEleSF
from getMisIDEleSF import getMisIDEleSF
from getZJetsSF import getZJetsSF

from colorama import Fore, Back, Style 

from TTGamma_nonPrompt_2016 import *

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

parser.add_option("--LooseCRe3ge2","--looseCRe3ge2", dest="looseCRe3ge2", default=False,action="store_true",
                     help="Use ==3 jets + >=2 bjets selection" )  

parser.add_option("--useQCDMC","--qcdMC",dest="useQCDMC", default=False, action="store_true",
		  			 help="")

parser.add_option("--useQCDCR",dest="useQCDCR", default=False, action="store_true",
                     help="to make plots in QCDCR region")

parser.add_option("--noQCD",dest="noQCD", default=False, action="store_true",
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
noQCD = options.noQCD
zeroPhoton    = options.zeroPhoton

template        = options.template

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","Pdf","fsr","isr", "prefireEcal", "JER", "JEC"]
#allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2"]#,"fsr","isr","Pdf"]
if systematics in allsystematics: print "running on systematics"
else: print(Fore.RED + "systematics is not in list. Add the systematics in the list if you are running for systematics.")

print(Style.RESET_ALL) 

if level=='up': mylevel='Up'
if level=='down': mylevel='Down'

#eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"

#######
########

if zeroPhoton:      #tight but 0 photon
	isSelection = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = getZJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDirQCD = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics,level)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
	else:
		fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
		
		

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

sampleList = ['TTGamma', 'TTbar', 'SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'SingleTop':kOrange-3, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7,'GJets':kGreen+1,"QCD":kGreen+3}

#sampleList = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV']
#sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'TGJets':kGray,'SingleTop':kOrange-3, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7}


template_category = {"TTGamma":kOrange,  
					 "TTbar":  kRed+1,    
					 "WGamma": kBlue-4, 
					 "ZGamma": kBlue-2,   
					 "Other":  kGreen+3}
template_categoryName = {"TTGamma":"t#bart#gamma",  
					     "TTbar":  "t#bart",    
					     "WGamma": "W#gamma", 
					     "ZGamma": "Z#gamma",   
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
	else:
		#print sample, fileDir
		_file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')
	
templateHist = {}

templateHist["TTGamma" ] = None 
templateHist["TTbar"   ] = None
templateHist["WGamma"  ] = None 
templateHist["ZGamma"  ] = None  
templateHist["Other"   ] = None 

print sampleList

mystack = THStack()
for sample in sampleList:
	if sample=='QCD_DD': continue 
	tempHist = _file[sample].Get(histName%(sample))
	#print tempHist
	
	if sample=='ZJets': 
		tempHist.Scale(ZJetSF)
		#print "ZJetSF", ZJetSF
    # addd WJetsSF here. IMP
	print sample, "==>", tempHist.Integral()	

	if   sample=='TTGamma': templateHist["TTGamma"]= tempHist.Clone("TTGamma")
	elif sample=='TTbar'  : templateHist["TTbar"]  = tempHist.Clone("TTbar")
	elif sample=='WGamma' :	templateHist["WGamma"] = tempHist.Clone("WGamma")
	elif sample=='ZGamma' : templateHist["ZGamma"] = tempHist.Clone("ZGamma")

	else:


		if  templateHist["Other"] is None:
			templateHist["Other"] = tempHist.Clone("Other")
			templateHist["Other"].SetDirectory(0)
		else:
			templateHist["Other"].Add(tempHist)
		

		
#templateHist["Other"].Add(qcdHist)
#gApplication.Run()
#print "exited"
#sys.exit()
# apply SF before plotting or feeding into combine
templateHist["WGamma"].Scale(WGammaSF)
templateHist["ZGamma"].Scale(ZGammaSF)

#print "WGammaSF and ZGammaSF",  WGammaSF,"  ",ZGammaSF 

#binning = numpy.array([50,105,155,185,260,500.])
#binning = numpy.array([50,500.])
#binning = numpy.array([50,105,155,185,260,500.])

binning = numpy.array([50,100,125,150,175,200,250,300,500.])
print binning
binWidth = numpy.diff(binning)

rebinnedHist ={} 

for ih in templateHist:
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])

rebinnedqcdHist = qcdHist.Rebin(len(binning)-1,"",binning)
rebinnedHist["Other"].Add(rebinnedqcdHist)

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
	rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)	
	
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
	for iprocess in template_category.keys():

		myfile.cd()
		mydir =  "%s/%s/"%(myfilename,iprocess) 
		#print "%s/%s/"%(myfilename,iprocess) 

		if systematics=='':
			myhist = rebinnedHist[iprocess].Clone("nominal")
		else:
			myhist = rebinnedHist[iprocess].Clone("%s%s"%(systematics,mylevel))
			if systematics in ["Q2","isr","fsr"]:
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

	if prefitPlots:
		rebinnedData.Scale(1.,"width")
		for ih in rebinnedHist:
			rebinnedHist[ih].Scale(1.,"width")	

		stack = THStack()
		stack.Add(rebinnedHist["Other"  ])
		stack.Add(rebinnedHist["ZGamma" ])   
		stack.Add(rebinnedHist["WGamma" ])   
		stack.Add(rebinnedHist["TTbar"  ]) 
		stack.Add(rebinnedHist["TTGamma"])  
		#rebinnedMC = stack.GetStack().Last().Clone("rebinnedMC")

	if postfitPlots:
		rebinnedData.Scale(1.,"width")
		#if finalState=="Ele": filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma%s/fitDiagnostics%s_%s.root"%(selYear,channel[:-1],selYear)
		#if finalState=="Mu":  filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma%s/fitDiagnostics%s_%s.root"%(selYear,channel,selYear)
		if finalState=="Ele": filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma/fitDiagnostics%s_%s.root"%(channel[:-1],selYear)
		if finalState=="Mu":  filename = "/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/ttGamma/fitDiagnostics%s_%s.root"%(channel,selYear)
		Postfile = TFile(filename,"read")
		templatePostHist = {}
		# print len(binning),"==>",len(binWidth)
		templatePostHist["TTGamma" ] = TH1F("TTGamma" ,"",len(binWidth),binning)
		templatePostHist["TTbar"   ] = TH1F("TTbar"   ,"",len(binWidth),binning)   
		templatePostHist["WGamma"  ] = TH1F("WGamma"  ,"",len(binWidth),binning)   
		templatePostHist["ZGamma"  ] = TH1F("ZGamma"  ,"",len(binWidth),binning)    
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
		stack.Add(templatePostHist["ZGamma"  ])   
		stack.Add(templatePostHist["WGamma"  ])  
		stack.Add(templatePostHist["TTbar"   ]) 
		stack.Add(templatePostHist["TTGamma" ]) 

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

	legend.AddEntry(rebinnedHist["TTGamma" ],template_categoryName["TTGamma" ],'f')	
	legend.AddEntry(rebinnedHist["TTbar"   ],template_categoryName["TTbar"   ],'f') 
	legend.AddEntry(rebinnedHist["WGamma"  ],template_categoryName["WGamma"  ],'f')  
	legend.AddEntry(rebinnedHist["ZGamma"  ],template_categoryName["ZGamma"  ],'f')
	legend.AddEntry(rebinnedHist["Other"   ],template_categoryName["Other"   ],'f')  
	
	pad1.cd()

	stack.Draw('HIST')
	if not noData == True:
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
		canvasRatio.SaveAs("%s%s_%s_postfit.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
		canvasRatio.Print("%s%s_%s_postfit.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
	else:

		canvasRatio.SaveAs("%s%s_%s.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
		canvasRatio.Print("%s%s_%s.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
		#myfile.Close()
	canvasRatio.Close()


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
