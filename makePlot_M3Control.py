from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kViolet,kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,kYellow,kCyan,kSpring
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

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()
finalState = options.channel
postfitPlots = options.postfitPlots
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

M3Plot = options.M3Plot
ChIsoPlot=options.ChIsoPlot
M3pho0Plot=options.M3pho0Plot

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

rebinCenter = 2
rebinLeftRight = 10
eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"

#######
########
if tight:      #SR8 
	isSelection = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	if channel=='ele':
		isoTTGammaSF = 0.871212  #-0.0421535/+0.0423445 # WGamma non prompt came out empty so fitting failed.
		nonPromptTTGammaSF = 0.88642  # +/-  1.36e+00
	else:
		isoTTGammaSF = 0.916049  #-0.022929/+0.0230016 ; 0.970489  #-0.0275155/+0.0275579
		nonPromptTTGammaSF = 3.9909 #         +/-  6.48e-01# 3.1048    # +/-  8.47e-01 
	fileDir  = "%shistograms_%s/%s/hists_tight/"%(eosFolder,selYear, channel)
	#fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	plotDirectory = "M3ChIso_tightplots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"
	print fileDir


if looseCRge2ge0:  #AR
	isSelection = "looseCRge2ge0"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear, channel)
	plotDirectory = "M3ChIso_looseCRge2ge0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}#geq0"

if looseCRge2e0:  #CR1+CR2+CR3
	isSelection = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
	plotDirectory = "M3ChIso_looseCRge2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}=0"

###
if looseCRe2e0:  #CR1
	isSelection = "looseCRe2e0"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);		
	fileDir  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
	plotDirectory = "M3ChIso_looseCRe2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=0"

if looseCRe3e0:  #CR2
	isSelection = "looseCRe3e0"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
	plotDirectory = "M3ChIso_looseCRe3e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0:  #CR3
	isSelection = "looseCRge4e0"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	plotDirectory = "M3ChIso_looseCRge4e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe2e1:  #CR4
	isSelection = "looseCRe2e1"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	fileDir  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
	plotDirectory = "M3ChIso_looseCRe2e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=1"
	
if looseCRe3e1:  #CR5
	isSelection = "looseCRe3e1"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	fileDir  = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
	plotDirectory = "M3ChIso_looseCRe3e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=1"

if looseCRe2e2:  #
	isSelection = "looseCRe2e2" #
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	fileDir  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
	plotDirectory = "M3ChIso_looseCRe2e2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=2"

if looseCRe3ge2:  #CR7
	isSelection = "looseCRe3ge2"
	if selYear  =='2016': ZJetSF = 1.23; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = 1.30; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = 1.26; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	fileDir  = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
	plotDirectory = "M3ChIso_looseCRe3ge2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}#geq2"

###
####

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
					     "Other":  "Other"}
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
mydistributionName = histNameData[7:-3]+"_Pho0"

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
	if sample=='ZJets': 
		tempHist.Scale(ZJetSF)
		print "ZJetSF", ZJetSF
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
print "WGammaSF and ZGammaSF",  WGammaSF,"  ",ZGammaSF 

data_obs = dataHist.Clone("data_obs")

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




rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)
rebinnedHist ={} 

if postfitPlots:
 	print"no need save root file"
else:
 	myfile = TFile(plotDirectory+"promptTemplate_%s_%s_Prefit.root"%(channel,mydistributionName),"recreate")

for ih in templateHist:
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])
	rebinnedHist[ih].Write()

rebinnedData.Write()
# forget about plotting right now. Just make a template.

## purpose for plotting 
rebinnedData.Scale(1.,"width")
	
stack = THStack()
print rebinnedHist.keys()

for ih in rebinnedHist:
	rebinnedHist[ih].Scale(1.,"width")

stack.Add(rebinnedHist["Other"])
stack.Add(rebinnedHist["ZGamma"])
stack.Add(rebinnedHist["WGamma"])
stack.Add(rebinnedHist["TTbar"])
stack.Add(rebinnedHist["TTGamma"])


if postfitPlots:
	MC = stack.GetStack().Last().Clone("MC")
	x = rebinnedData.Chi2Test(MC,"UW CHI2/NDF") 
	chi2Text = "#chi^{2}/NDF=%.2f"%x

	
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

minVal = 1
# minVal = max(stack.GetStack()[0].GetMinimum(),1)
stack.SetMaximum(1.25*maxVal)
stack.SetMinimum(minVal)

errorband=stack.GetStack().Last().Clone("error")
errorband.Sumw2()
errorband.SetLineColor(kBlack)
errorband.SetFillColor(kBlack)
errorband.SetFillStyle(3245)
errorband.SetMarkerSize(0)

legend.AddEntry(rebinnedData,"Data", 'pe')
legend.AddEntry(errorband,"Uncertainty","f")

for ih in rebinnedHist:
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

canvasRatio.Update()
canvasRatio.RedrawAxis()
if postfitPlots:
	canvasRatio.SaveAs("%s%s_%s_postfit.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
	canvasRatio.Print("%s%s_%s_postfit.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
else:
	canvasRatio.SaveAs("%s%s_%s.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
	canvasRatio.Print("%s%s_%s.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
	myfile.Close()
canvasRatio.Close()


    
