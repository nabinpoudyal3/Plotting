from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory,kCyan,kViolet
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

parser.add_option("--template", dest="template", default=False,action="store_true",
					help="post fit plots" )
					
					
parser.add_option("--M3Plot", dest="M3Plot",default=False,action="store_true",
					help="Specify M3 or ChIso" )

parser.add_option("--ChIsoPlot", dest="ChIsoPlot",default=False,action="store_true",
					help="Specify M3 or ChIso" )

parser.add_option("--btag0", dest="btag0",default=False,action="store_true",
					help="0 btag " )
					
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

M3Plot        = options.M3Plot
ChIsoPlot     = options.ChIsoPlot
btag0         = options.btag0

template        = options.template

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

#allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","Pdf","fsr","isr"]
allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","fsr","isr","Pdf"]
if systematics in allsystematics: print "running on systematics"
else: print(Fore.RED + "systematics is not in list. Add the systematics in the list if you are running for systematics.")

print(Style.RESET_ALL) 

if level=='up': mylevel='Up'
if level=='down': mylevel='Down'

#eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"

#######
########
if tight:      #SR8 
	isSelection = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics,level)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
	else:
		fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
	
	
if btag0:      #CR3 4jet 0 btag
	isSelection = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);

	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge4e0/"%(selYear, channel,systematics,level)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
	else:
		fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
		#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"



eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"

fileDir = eosFolder + fileDir
print fileDir

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

from Style import *

gROOT.ForceStyle()


sampleList = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'TGJets':kGray,'SingleTop':kOrange-3, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7,'GJets':kGreen+1,"QCD":kGreen+3}

#sampleList = ['TTGamma', 'TTbar', 'TGJets', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
#sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'TGJets':kGray, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7,'GJets':kGreen+1,"QCD":kGreen+3}

template_category = {"isolatedTTGamma":kOrange,  "nonPromptTTGamma":kOrange-3,  
					 "isolatedTTbar":  kRed+1,   "nonPromptTTbar":  kRed+3,   
					 "isolatedWGamma": kBlue-4,  "nonPromptWGamma": kViolet-1,  
					 "isolatedZGamma": kBlue-2,  "nonPromptZGamma": kViolet+8,  
					 "isolatedOther":  kGreen+3, "nonPromptOther":  kGreen+4, 
					}

template_categoryName = {"isolatedTTGamma":"TT#gamma iso", "nonPromptTTGamma":"TT#gamma nonPrompt",  
					     "isolatedTTbar":  "TT iso",       "nonPromptTTbar":  "TT nonPrompt",   
					     "isolatedWGamma": "W#gamma iso",  "nonPromptWGamma": "W#gamma nonPrompt",  
					     "isolatedZGamma": "Z#gamma iso",  "nonPromptZGamma": "Z#gamma nonPrompt",  
					     "isolatedOther":  "other iso",    "nonPromptOther":  "other nonPrompt", 
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
elif useQCDCR:
	sampleList[-1] = "QCD_DD"
	sampleList.remove("GJets") 
else:
	#sampleList[-1] = "QCD_DD"
	#sampleList.remove("GJets") 
	sampleList.remove("QCD") 
	sampleList.remove("GJets") 
	#samples["QCD_DD"] = [[],kGreen+3,"Multijet",isMC]

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
	histName  	= "phosel_M3_%s_%s"
	histNameData= "phosel_M3_%s" 
	mydistributionName = histNameData[7:-3]+"0btag"

else:
	print "either M3 or ChIso!!"


templateHist ={}


	
for sample in sampleList:
	if sample=="QCD_DD": 
		#print "==>",sample, fileDirQCD
		_file[sample] = TFile.Open('%s%s.root'%(fileDirQCD,sample),'read')
	else:
		#print sample, fileDir
		_file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')
	


templateHist = {}

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

for item in hist_category:
	if item == "MisIDEle" or item == "GenuinePhoton":
		for sample in sampleList:
			tempHist = _file[sample].Get(histName%(item,sample))
			if item=="MisIDEle":tempHist.Scale(MisIDEleSF)
			if sample=="ZJets": tempHist.Scale(ZJetSF) 
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
			tempHist = _file[sample].Get(histName%(item,sample))
			
			if sample=="ZJets": tempHist.Scale(ZJetSF) 
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
#sys.exit()
# apply SF before plotting or feeding into combine
templateHist["isolatedWGamma"].Scale(WGammaSF)
templateHist["isolatedZGamma"].Scale(ZGammaSF)
templateHist["nonPromptWGamma"].Scale(WGammaSF)
templateHist["nonPromptZGamma"].Scale(ZGammaSF)

print ZJetSF, MisIDEleSF, WGammaSF, ZGammaSF	
	
if mydistributionName == "M3":
	myfilename = "M3"
	binning = numpy.array([50,100,125,150,175,200,250,300,500.])
	
if mydistributionName == "M30btag":
	myfilename = "M30btag"
	binning = numpy.array([50,500.])

if mydistributionName == "ChIso":
	myfilename = "ChIso"
	binning = numpy.array([0,0.5,1.0,1.5,2.0,3.0,5.0,10.0,20.0])

rebinnedHist ={} 	

for ih in templateHist:
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])
	
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
		print "%s/%s/"%(myfilename,iprocess) 
	
		if systematics=='':
			myhist = rebinnedHist[iprocess].Clone("nominal")
		else:
			myhist = rebinnedHist[iprocess].Clone("%s%s"%(systematics,mylevel))
			if systematics in ["PU","Q2"]:
			 	myNominalHist = myfile.Get(mydir+"nominal")
			 	if myNominalHist != None:
			 		valNominal = myNominalHist.Integral()
			 		val = myhist.Integral()
			 		if valNominal != 0 and val != 0:
			 			print "nominal", valNominal, " ==> ", "syst",val
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
	print "%s%s.root"%(plotDirectory,"ttgamma_Prefit")

	myfile.Close()
	sys.exit()
### For plotting
else:
	if postfitPlots:
		rebinnedHist["isolatedTTGamma" ].Scale(TTGammaSF)
		rebinnedHist["nonPromptTTGamma"].Scale(nonPromptSF)
		rebinnedHist["nonPromptTTbar"  ].Scale(nonPromptSF)
		rebinnedHist["nonPromptWGamma" ].Scale(nonPromptSF)  
		rebinnedHist["nonPromptZGamma" ].Scale(nonPromptSF)  
		rebinnedHist["nonPromptOther"  ].Scale(nonPromptSF) 
	
	## purpose for plotting 
	rebinnedData.Scale(1.,"width")
	#print TTGammaSF, nonPromptSF
	stack = THStack()
	print rebinnedHist.keys()

	for ih in rebinnedHist:
		rebinnedHist[ih].Scale(1.,"width")

	stack.Add(rebinnedHist["nonPromptOther"  ])
	stack.Add(rebinnedHist["isolatedOther"   ])  
	stack.Add(rebinnedHist["nonPromptZGamma" ])   
	stack.Add(rebinnedHist["isolatedZGamma"  ])   
	stack.Add(rebinnedHist["nonPromptWGamma" ])   
	stack.Add(rebinnedHist["isolatedWGamma"  ])  
	stack.Add(rebinnedHist["nonPromptTTbar"  ]) 
	stack.Add(rebinnedHist["isolatedTTbar"   ]) 
	stack.Add(rebinnedHist["nonPromptTTGamma"])  
	stack.Add(rebinnedHist["isolatedTTGamma" ]) 	

	rebinnedMC = stack.GetStack().Last().Clone("rebinnedMC")
	print rebinnedMC.GetBinContent(8)

	if postfitPlots:
		rebinnedMC = stack.GetStack().Last().Clone("rebinnedMC")
		x = rebinnedData.Chi2Test(rebinnedMC,"WW CHI2/NDF") 
		chi2Text = "#chi^{2}/NDF=%.1f"%x

		
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
	print minVal
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
	if postfitPlots: CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText+";"+regionText,chi2Text)

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


    
	
	
	
	
	
	
	
	
	

