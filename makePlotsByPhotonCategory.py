from ROOT import Double, TFile, TLegend, TCanvas,gPad, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory,kCyan,kViolet
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
parser.add_option("--postfitPlots", dest="postfitPlots", default=False,action="store_true",help="post fit plots" )
parser.add_option("--prefitPlots", dest="prefitPlots", default=False,action="store_true",help="pre fit plots" )
parser.add_option("--template", dest="template", default=False,action="store_true",help="post fit plots" )
parser.add_option("--datadriven", dest="datadriven", default=False,action="store_true",help="data driven plots" )
parser.add_option("--photonEt", dest="photonEt",default=False,action="store_true",help="Specify M3 or ChIso" )
parser.add_option("--photonAntiChIso", dest="photonAntiChIso",default=False,action="store_true",help="Specify M3 or ChIso" )
parser.add_option("--photonChIso", dest="photonChIso",default=False,action="store_true",help="Specify M3 or ChIso" )
parser.add_option("--SIEIEPlot", dest="SIEIEPlot",default=False,action="store_true",help="Specify M3 or ChIso" )
parser.add_option("--SIEIEnoChIsoPlot", dest="SIEIEnoChIsoPlot",default=False,action="store_true",help="0 btag " )
parser.add_option("--SIEIEnoChIsoFocusPlot", dest="SIEIEnoChIsoFocusPlot",default=False,action="store_true",help="0 btag " )
parser.add_option("--zeroPhoton", dest="zeroPhoton",default=False,action="store_true",help="0 photon " )						
parser.add_option("--tight", dest="tight", default=False,action="store_true",help="draw photon Category for tight selection" )
parser.add_option("--syst", "--systematics", dest="systematics", default="",type='str',help="Specify which systematic plots" )
parser.add_option("--level", dest="level", default="",type='str',help="Specify which level Up or Down" )	
parser.add_option("--looseCRge2ge0", dest="looseCRge2ge0", default=False,action="store_true",help="draw photon Category for loose CR ge2 ge0" )
parser.add_option("--looseCRge2e0", dest="looseCRge2e0", default=False,action="store_true",help="draw photon Category for loose CR ge2 =0" )
parser.add_option("--LooseCRe2e0","--looseCRe2e0", dest="looseCRe2e0", default=False,action="store_true",help="Use ==2 jets + ==0 bjets selection" )  
parser.add_option("--LooseCRe2e1","--looseCRe2e1", dest="looseCRe2e1", default=False,action="store_true",help="Use ==2 jets + ==1 bjets selection" ) 
parser.add_option("--LooseCRe3e0","--looseCRe3e0", dest="looseCRe3e0", default=False,action="store_true",help="Use ==3 jets + ==0 bjets selection" ) 
parser.add_option("--LooseCRge4e0","--looseCRge4e0", dest="looseCRge4e0", default=False,action="store_true",help="Use >=4 jets + ==0 bjets selection" ) 
parser.add_option("--LooseCRe3e1","--looseCRe3e1", dest="looseCRe3e1", default=False,action="store_true",help="Use ==3 jets + ==1 bjets selection" ) 
parser.add_option("--LooseCRe2e2","--looseCRe2e2", dest="looseCRe2e2", default=False,action="store_true",help="Use ==2 jets + ==2 bjets selection" ) 
parser.add_option("--LooseCRe3ge2","--looseCRe3ge2", dest="looseCRe3ge2", default=False,action="store_true",help="Use ==3 jets + >=2 bjets selection" )  
parser.add_option("--useQCDMC","--qcdMC",dest="useQCDMC", default=False, action="store_true",help="")
parser.add_option("--useQCDCR",dest="useQCDCR", default=False, action="store_true",help="to make plots in QCDCR region")
parser.add_option("--noQCD",dest="noQCD", default=False, action="store_true",help="")
parser.add_option("--noData",dest="noData", default=False, action="store_true",help="")
parser.add_option("--ratioPlot",dest="ratioPlot", default=False, action="store_true",help="")

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()

finalState    = options.channel
postfitPlots  = options.postfitPlots
prefitPlots   = options.prefitPlots

ratioPlot     = options.ratioPlot
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
template        = options.template
datadriven      = options.datadriven

print noData
# sys.exit()
photonAntiChIso      = options.photonAntiChIso
photonChIso      = options.photonChIso
photonEt         = options.photonEt
SIEIEPlot        = options.SIEIEPlot
SIEIEnoChIsoPlot = options.SIEIEnoChIsoPlot
SIEIEnoChIsoFocusPlot = options.SIEIEnoChIsoFocusPlot

rebinX =1

if photonEt:
	histName    = "phosel_LeadingPhotonEt_%s_%s"
	histNameData= "phosel_LeadingPhotonEt_%s"
	mydistributionName = histNameData[7:-3]
	rebinX=5
	binning = numpy.array(list(numpy.arange(15.,105.,rebinX)))
	xtitle='Photon Et (GeV)'

elif photonChIso:
	histName    = "phosel_mediumID_ChIso_%s_%s"
	histNameData= "phosel_mediumID_ChIso_%s"
	mydistributionName = histNameData[16:-3]
	rebinX=0.5
	# binning = numpy.array(list(numpy.arange(1.14,20.,rebinX)))
	binning = numpy.array([1.141,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.]) # without first bin, removing last bin

	xtitle='Photon ChIso'

elif SIEIEPlot:
	histName    = "phosel_noCut_SIEIE_%s_%s"
	histNameData= "phosel_noCut_SIEIE_%s"
	mydistributionName = histNameData[7:-3]
	rebinX=0.0003
	binning = numpy.array(list(numpy.arange(0.006,0.024,rebinX)))
	xtitle='Sigma Ieta Ieta)'


elif SIEIEnoChIsoPlot:
	histName    = "phosel_noCut_SIEIE_noChIso_%s_%s"
	histNameData= "phosel_noCut_SIEIE_noChIso_%s"
	mydistributionName = histNameData[7:-3]
	rebinX=0.0003
	binning = numpy.array(list(numpy.arange(0.006,0.024,rebinX)))
	xtitle='Sigma Ieta Ieta)'


elif SIEIEnoChIsoFocusPlot:
	histName    = "phosel_noCut_SIEIE_noChIso_%s_%s"
	histNameData= "phosel_noCut_SIEIE_noChIso_%s"
	mydistributionName = histNameData[7:-3]+"_Focus"
	rebinX=0.0003
	binning = numpy.array(list(numpy.arange(0.01,0.024,rebinX)))
	xtitle='Sigma Ieta Ieta)'

elif photonAntiChIso:
	histName    = "phosel_AntiSIEIE_ChIso_%s_%s"
	histNameData= "phosel_AntiSIEIE_ChIso_%s"
	mydistributionName = histNameData[16:-3]
	# rebinX=2
	# binning = numpy.array(list(numpy.arange(1.143,20.,rebinX)))
	binning = numpy.array([1.141,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.,20.]) # without first bin, removing last bin

	xtitle='Photon ChIso in SB'
else:
	print "either M3 or ChIso!!"

print binning
if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

crName = ""
if tight:      #SR8 
	isSelection = "looseCRge2e0"
	crName = "signal"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection); # use misIDEl for each year but same V sf for all year.
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	else :                ZJetSF = getZJetsSF(selYear,isSelection); WJetSF = getWJetsSF(selYear,isSelection); MisIDEleSF,ZGammaSF,WGammaSF = getMisIDEleSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	plotDirectory = "ByPhotonCategory_tightplots_%s_%s/"%(channel,selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"
else:
	print "which control region"		

eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
# localFolder="/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/Local_histogramming/"

fileDir = eosFolder+fileDir
print fileDir

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

from Style import *

from Style import *
thestyle = Style()

HasCMSStyle = False
style = None
if os.path.isfile('tdrstyle.C'):
	ROOT.gROOT.ProcessLine('.L tdrstyle.C')
	ROOT.setTDRStyle()
	print "Found tdrstyle.C file, using this style."
	HasCMSStyle = True
	if os.path.isfile('CMSTopStyle.cc'):
		gROOT.ProcessLine('.L CMSTopStyle.cc+')
		style = CMSTopStyle()
		style.setupICHEPv1()
		print "Found CMSTopStyle.cc file, use TOP style if requested in xml file."
if not HasCMSStyle:
	print "Using default style defined in cuy package."
	thestyle.SetStyle()

ROOT.gROOT.ForceStyle()


sampleList = ['TTGamma', 'TTbar', 'SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
sampleListColor = {'TTGamma':kOrange, 'TTbar':kRed+1, 'SingleTop':kOrange-3, 'WJets':kCyan-3, 'ZJets':kCyan-5, 'WGamma':kBlue-4,'ZGamma':kBlue-2,'Diboson':kCyan-7,'TTV':kRed-7,'GJets':kGreen+1,"QCD":kGreen+3}

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
	# sampleList["QCD_DD"] = [[],kGreen+3,"Multijet",isMC]

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

legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((10+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legend.SetNColumns(2)

legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((10+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))

legendR.SetNColumns(2)
legendR.SetBorderSize(0)
legendR.SetFillColor(0)
legend.SetBorderSize(0)
legend.SetFillColor(0)


if finalState=='Ele':
	sample = "DataEle"
	_file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
	dataHist = _file[sample].Get(histNameData%(sample))
	print dataHist
	dataHist.SetLineColor(kBlack)
	dataHist.SetMarkerStyle(8)
	dataHist = dataHist.Rebin(len(binning)-1,"",binning)
	print binning

elif finalState=='Mu':
	sample = "DataMu"
	_file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
	dataHist = _file[sample].Get(histNameData%(sample))
	dataHist.SetLineColor(kBlack)
	dataHist.SetMarkerStyle(8)
	dataHist = dataHist.Rebin(len(binning)-1,"",binning)
	print binning

else:
	print "Select the channel !!!"
	sys.exit()	

summedHist ={}

for item in hist_category.keys():
	summedHist[item] = None
	# print item
	for sample in sampleList:
		if sample=="QCD_DD": continue
		_file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')
		# print item, sample
		tempHist = _file[sample].Get(histName%(item,sample))
		print tempHist
		if tempHist is None: continue
		if   sample=="ZJets":  tempHist.Scale(ZJetSF)
		elif sample=="WJets":  tempHist.Scale(WJetSF)
		elif sample=="ZGamma": tempHist.Scale(ZGammaSF)
		elif sample=="WGamma": tempHist.Scale(WGammaSF)
		if summedHist[item] is None:
			summedHist[item] = tempHist.Clone(item)
			summedHist[item].SetDirectory(0)
		else:
			summedHist[item].Add(tempHist)


if "QCD_DD" in sampleList:  
	sample = "QCD_DD"
	print sample
	print "Yes using QCD DD "
	_file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')
	qcdHist = _file[sample].Get(histNameData%(sample))
	print qcdHist
	summedHist["HadronicPhoton"].Add(qcdHist)

for ih in summedHist:
	print ih, summedHist[ih]
	summedHist[ih] = summedHist[ih].Rebin(len(binning)-1,"",binning)
	summedHist[ih].SetLineColor(hist_category[ih])
	summedHist[ih].SetFillColor(hist_category[ih])

#IMP
summedHist['MisIDEle'].Scale(MisIDEleSF)


summedHist['HadronicPhoton'].Scale(1.,"width")
summedHist['HadronicFake'].Scale(1.,"width")
summedHist['GenuinePhoton'].Scale(1.,"width")
summedHist['MisIDEle'].Scale(1.,"width")

stack = THStack()
stack.Add(summedHist['HadronicPhoton'])
stack.Add(summedHist['HadronicFake'])
stack.Add(summedHist['GenuinePhoton'])
stack.Add(summedHist['MisIDEle'])

myhist = stack.GetStack().Last().Clone("myhist") # 5335.18 < 5370.67
print myhist.Integral(-1,-1)
print dataHist.Integral(-1,-1)

TGaxis.SetMaxDigits(3)

canvas = TCanvas('c1','c1',W,H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(0)

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

canvasRatio.cd()
pad1.Draw()
pad2.Draw()

canvas.cd()	
canvas.ResetDrawn()	

oneLine = TF1("oneline","1",-9e9,9e9)
oneLine.SetLineColor(kBlack)
oneLine.SetLineWidth(1)
oneLine.SetLineStyle(2)

maxVal = stack.GetMaximum()
if not noData: 
    maxVal = max(dataHist.GetMaximum(),maxVal)

minVal = 0.01

if photonEt:
	minVal = max(stack.GetStack()[0].GetMinimum(),1)
	stack.SetMaximum(10**(1.5*log10(2.5*maxVal) - 0.5*log10(minVal)))
	stack.SetMinimum(minVal)
else:
	stack.SetMaximum(1.5*maxVal) # 1.5 to 2.5
	# stack.SetMaximum(maxVal) # 1.5 to 2.5
	stack.SetMinimum(minVal)

# stack.SetMaximum(5500) # 1.5 to 2.5

errorband=stack.GetStack().Last().Clone("errorband")
errorband.Sumw2()
errorband.SetLineColor(kBlack)
errorband.SetFillColor(kBlack)
errorband.SetFillStyle(3245)
errorband.SetMarkerSize(0)

legend.AddEntry(dataHist,                    'Data',          'pe')
legend.AddEntry(summedHist['MisIDEle'],      'MisID e',      'f')
legend.AddEntry(summedHist['GenuinePhoton'], 'Genuine #gamma', 'f')
legend.AddEntry(summedHist['HadronicFake'],  'Fake #gamma',  'f')
legend.AddEntry(summedHist['HadronicPhoton'],'Hadronic #gamma','f')
legend.AddEntry(errorband,                   'Uncertainty',   'f')
legend.SetTextSize(0.043)
pad1.cd()

# if photonEt: 
# pad1.SetLogy()

stack.Draw('HIST')
if not noData == True:
	dataHist.Scale(1.,"width")
	dataHist.Draw('E,X0,SAME')
legend.Draw("same")
stack.GetXaxis().SetTitle('')
stack.GetXaxis().SetLabelSize(0)
stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
# stack.GetYaxis().SetTitleSize(.049)
stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
stack.SetTitle(';;<Events/GeV>')# '%rebin)
# stack.SetTitle(';;Events/%sGeV '%(rebinX))

CMS_lumi.channelText = channelText+", "+regionText
#if postfitPlots: CMS_lumi.channelText =channelText+"\\n "+regionText+"\\n "+chi2Text
# CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText,regionText)
#if postfitPlots: CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText+";"+regionText,chi2Text)s
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True
CMS_lumi.CMS_lumi(pad1, 4, 11)

if not noData:
	ratio = dataHist.Clone("ratio")
	temp = stack.GetStack().Last().Clone("temp")
	for i_bin in range(1,temp.GetNbinsX()+1):
		temp.SetBinError(i_bin,0.)
	ratio.Divide(temp)
else:
	ratio = dataHist.Clone("ratio")
	temp = stack.GetStack().Last().Clone("temp")

ratio.SetTitle('')
ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))





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
ratio.GetYaxis().SetTitle("Data/MC")
ratio.GetXaxis().SetTitle("%s"%xtitle)
# ratio.GetYaxis().SetTitleOffset(.4)
# ratio.GetYaxis().SetTitleSize(.1)
# ratio.GetXaxis().SetTitleSize(.1)
ratio.GetYaxis().SetNdivisions(-402)


CMS_lumi.CMS_lumi(pad2, 4, 11)
pad2.cd()
maxRatio = 1.5
minRatio = 0.5
ratio.SetMarkerStyle(dataHist.GetMarkerStyle())
ratio.SetMarkerSize(dataHist.GetMarkerSize())
ratio.SetLineColor(dataHist.GetLineColor())
ratio.SetLineWidth(dataHist.GetLineWidth())
ratio.Draw('e,x0')
errorbandRatio = errorband.Clone("errorbandRatio")
errorbandRatio.Divide(temp)
errorbandRatio.Draw('e2,same')
oneLine.Draw("same")

canvasRatio.Update()
canvasRatio.RedrawAxis()
canvasRatio.SaveAs("%s%s_%s.root"%(plotDirectory,plotDirectory[:-1],mydistributionName))
canvasRatio.Print("%s%s_%s.pdf" %(plotDirectory,plotDirectory[:-1],mydistributionName))
#myfile.Close()
canvasRatio.Close()

	
	
	
	
	
	
	
	
	

