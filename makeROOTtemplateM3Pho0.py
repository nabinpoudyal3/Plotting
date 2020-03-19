
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

parser.add_option("--M3Plot", dest="M3Plot",default=False,action="store_true",
					help="Specify M3 or ChIso" )

parser.add_option("--ChIsoPlot", dest="ChIsoPlot",default=False,action="store_true",
					help="Specify M3 or ChIso" )

parser.add_option("--M3pho0Plot", dest="M3pho0Plot",default=False,action="store_true",
					help="M3 control region" )
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
M3pho0Plot    = options.M3pho0Plot

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


eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"

#######
########
if tight:      #SR8 
	isSelection = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	#if channel=='ele':
	#	TTGammaSF = 0.871212  #-0.0421535/+0.0423445 # WGamma non prompt came out empty so fitting failed.
	#	nonPromptSF = 0.88642  # +/-  1.36e+00
	#else:
	#	TTGammaSF = 0.906  #-0.022929/+0.0230016 ; 0.970489  #-0.0275155/+0.0275579
	#	nonPromptSF = 0.9214 #         +/-  6.48e-01# 3.1048    # +/-  8.47e-01 
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics,level)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
	else:
		fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		plotDirectory = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
	
	

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
template_category = {"TTGamma":kOrange,  
					 "TTbar":  kRed+1,    
					 "WGamma": kBlue-4, 
					 "ZGamma": kBlue-2,   
					 "Other":  kGreen+3}
template_categoryName = {"TTGamma":"TT#gamma",  
					     "TTbar":  "T#barT",    
					     "WGamma": "W#gamma", 
					     "ZGamma": "Z#gamma",   
					     "Other":  "MCOther"}
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
	stackList.remove("GJets") 
else:
	print "use --useQCDMC or --useQCDCR!"
	sys.exit()

histName  	= "presel_M3_%s"
histNameData= "presel_M3_%s" 
myfilename = histNameData[7:-3]+"Pho0"

	

templateHist ={}


for sample in sampleList:
	if finalState == 'Ele' and sample == 'QCD': sample = 'QCDEle'
	if finalState == 'Mu'  and sample == 'QCD': sample = 'QCDMu'
	_file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')
	
templateHist = {}

templateHist["TTGamma" ] = None 
templateHist["TTbar"   ] = None
templateHist["WGamma"  ] = None 
templateHist["ZGamma"  ] = None  
templateHist["Other"   ] = None 

for sample in sampleList:
	tempHist = _file[sample].Get(histName%(sample))
	if sample=='ZJets': tempHist.Scale(ZJetSF)
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
	
#gApplication.Run()
#print "exited"
#sys.exit()
# apply SF before plotting or feeding into combine
templateHist["WGamma"].Scale(WGammaSF)
templateHist["ZGamma"].Scale(ZGammaSF)
print "ZJetsSF, WGammaSF and ZGammaSF", ZJetSF,"   ", WGammaSF,"  ",ZGammaSF 

rebin=20
rebinCenter = 10 #2 #4
rebinLeftRight =20 # 10 #20
rebinLeftRightRight =40 # 10 #20
#binning  = numpy.arange(50,500.1,rebin)

binningLeft   = list(numpy.arange(50,90.1,rebinLeftRight)) # 40, 20 start
binningCenter = list(numpy.arange(100,200.1,rebinCenter))
binningRight  = list(numpy.arange(210,300.1,rebinLeftRight))
binningRightRight  = list(numpy.arange(310,500.1,rebinLeftRightRight))
binning = numpy.array(binningLeft + binningCenter + binningRight+binningRightRight)

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
		# if systematics in ["PU"]:
		# 	myNominalHist = myfile.Get(mydir+"nominal")
		# 	valNominal = myNominalHist.Integral()
		# 	val = myhist.Integral()
		# 	print "nominal", valNominal, " ==> ", "syst",val
		# 	myhist.Scale(valNominal/val)
		# 	print "normalized", myhist.Integral()
	
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


    
