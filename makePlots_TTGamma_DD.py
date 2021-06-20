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
	isSelection = "looseCRge2e0"
	# isSelection = "looseCRge4e0"
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
# binning = numpy.array([1.141,20.]) # without first bin, removing last bin

binWidth = numpy.diff(binning)

rebinnedHist ={} 	

sample = ""
if finalState=='Ele' and datadriven: sample = "DataEle"
elif finalState=='Mu' and datadriven: sample = "DataMu"

histo_sieie_MC  = None
histo_ChIso_MC  = None
for i in sampleList:
	if i =="QCD_DD": continue
	histoFile = TFile.Open("%s%s.root"%(fileDir,i),"read")
	histo = histoFile.Get("phosel_AntiSIEIE_ChIso_%s"%i).Clone("histo")
	histoChIsoHad = histoFile.Get("phosel_mediumID_ChIso_HadronicPhoton_%s"%i).Clone("histoChIsoHad")
	histoChIsoFake = histoFile.Get("phosel_mediumID_ChIso_HadronicFake_%s"%i).Clone("histoChIsoFake")
	histoChIso =  histoChIsoHad.Clone("histo_ChIso")
	histoChIso.Add(histoChIsoFake)
	histo_sieie = histo.Rebin(len(binning)-1,"",binning)
	histo_ChIso = histoChIso.Rebin(len(binning)-1,"",binning)
	print i, histo_sieie.Integral()
	if histo_ChIso_MC is None:
		histo_ChIso_MC = histo_ChIso.Clone("histo_sieie_MC")
		histo_ChIso_MC.SetDirectory(0)
	else:
		histo_ChIso_MC.Add(histo_ChIso)

	if histo_sieie_MC is None:
		histo_sieie_MC = histo_sieie.Clone("histo_sieie_MC")
		histo_sieie_MC.SetDirectory(0)
	else:
		histo_sieie_MC.Add(histo_sieie)
		# print ""

histoFile = TFile.Open("%s%s.root"%(fileDirNom,sample),"read")
print fileDirNom
histo = histoFile.Get("phosel_AntiSIEIE_ChIso_%s"%sample).Clone("histo")
myCanvas1 = TCanvas()
myCanvas1.SetGrid()
histo_sieie1 = histo.Rebin(len(binning)-1,"",binning)
print "datadriven binning == >", binning
#print histo_sieie.GetBinContent(1)
# totalEvt = histo_sieie.Integral(-1,-1)
totalEvt1 = histo_sieie1.Integral()
print "number of data events used to estimate the shape", totalEvt1
#print "total # of events in Ele Channel antisiesie data:", totalEvt, mydistributionName
histo_sieie1.Scale(1.0/totalEvt1)
histo_sieie1.Scale(1.,"width")
histo_sieie1.SetLineColor(kBlue)
histo_sieie1.SetLineWidth(2)
histo_sieie1.SetMaximum(0.1)
histo_sieie1.SetMinimum(0)
histo_sieie1.SetMarkerStyle(21)
histo_sieie1.SetTitle(";ChIso;Normalized events")
# myCanvas1.Print("histo_sieie_ele.pdf")
totalEvtChIso = histo_ChIso_MC.Integral()
histo_ChIso_MC.Scale(1.0/totalEvtChIso)
histo_ChIso_MC.Scale(1.,"width")
histo_ChIso_MC.SetLineColor(kGreen+3)
histo_ChIso_MC.SetLineWidth(2)
histo_ChIso_MC.SetMarkerStyle(kFullCircle)
# myCanvas2 = TCanvas()
totalEvt = histo_sieie_MC.Integral()
histo_sieie_MC.Scale(1.0/totalEvt)
histo_sieie_MC.Scale(1.,"width")
histo_sieie1.Draw()
histo_sieie_MC.Draw("SAME")
histo_ChIso_MC.Draw("SAME")
histo_sieie_MC.SetLineColor(kRed)
histo_sieie_MC.SetMaximum(0.1)
histo_sieie_MC.SetMinimum(0)
histo_sieie_MC.SetLineWidth(2)
histo_sieie_MC.SetMarkerStyle(22)

# myCanvas2.SetGrid()
myCanvas1.Print("histo_sieie_%s.pdf"%("Compare"))

myCanvas2 = TCanvas()
myCanvas2.SetGrid()

ratio = histo_sieie1.Clone("ratio")
ratio.Divide(histo_sieie_MC)
print histo_sieie_MC.GetBinContent(1)
ratio.Draw()
ratio.SetMaximum(1.2)
ratio.SetMinimum(0.8)
ratio.SetLineWidth(2)
ratio.SetMarkerStyle(kFullCircle)

myCanvas2.Print("histo_ratio.pdf")
## Make up and down template:
print binWidth
print len(binWidth)
shapeUp = TH1F("shapeUp","",len(binWidth),binning)
# shapeUp = TH1F("shapeUp","",len(binWidth),binning)
shapeDown = TH1F("shapeDown","",len(binWidth),binning)
# shapeDown = TH1F("shapeDown","",len(binWidth),binning)

for ibin in range(1,histo_sieie1.GetNbinsX()):
	difference = histo_sieie1.GetBinContent(ibin)-histo_sieie_MC.GetBinContent(ibin)
	print ibin
	up = (histo_sieie1.GetBinContent(ibin) + difference)*binWidth[ibin-1]
	down = (histo_sieie1.GetBinContent(ibin) - difference)*binWidth[ibin] 
	print ibin,up,down,binWidth[ibin]
	shapeUp.SetBinContent(ibin,up)
	shapeDown.SetBinContent(ibin,down)

s = TCanvas()
shapeUp.Draw()
shapeUp.SetMaximum(0.18)
shapeUp.SetMinimum(0)
shapeUp.SetLineColor(kRed)

shapeDown.Draw("SAME")
shapeDown.SetMaximum(0.18)
shapeDown.SetMinimum(0)
shapeDown.SetLineColor(kBlue)

s.Print("ShapeUp.pdf")



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
# pad2.Draw()

oneLine = TF1("oneline","1",-9e9,9e9)
oneLine.SetLineColor(kBlack)
oneLine.SetLineWidth(1)
oneLine.SetLineStyle(2)

histo_sieie1.SetMinimum(0.01)
histo_sieie1.SetMaximum(0.18)

errorband=histo_sieie1.Clone("errorband")
errorband.Sumw2()
errorband.SetLineColor(kBlack)
errorband.SetFillColor(kBlack)
errorband.SetFillStyle(3245)
errorband.SetMarkerSize(0)



legend.AddEntry(histo_ChIso_MC,"non Prompt MC: #sigma_{#eta#eta} < 0.011",'pl')
legend.AddEntry(histo_sieie_MC,"non Prompt MC: 0.11 < #sigma_{#eta#eta} < 0.2",'pl')
legend.AddEntry(histo_sieie1,"non Prompt SB: 0.11 < #sigma_{#eta#eta} < 0.2",'pl')
# legend.AddEntry(errorband,"Uncertainty","f")
# legend.SetTextSize(0.035)
pad1.cd()
histo_sieie1.Draw()
histo_sieie_MC.Draw("same")
histo_ChIso_MC.Draw("same")
legend.Draw("same")
histo_sieie1.GetXaxis().SetTitle('')
# histo_sieie1.GetXaxis().SetLabelSize(0)
histo_sieie1.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
histo_sieie1.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
histo_sieie1.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
histo_sieie1.GetYaxis().SetTitleSize(.049)
histo_sieie1.GetXaxis().SetTitleSize(.049)
histo_sieie1.GetXaxis().SetTitleOffset(1)

# histo_sieie1.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
histo_sieie1.SetTitle(';Photon ChIso;Normalized events')# '%rebin)

CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText,regionText)
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True
CMS_lumi.CMS_lumi(pad1, 4, 11)

ratio.SetTitle('')
ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap-padGap))

maxRatio = ratio.GetMaximum()
minRatio = ratio.GetMinimum()

ratio.GetYaxis().SetRangeUser(0.8,1.2)
ratio.GetYaxis().SetNdivisions(504)
ratio.GetXaxis().SetTitle("ChIso")

ratio.GetYaxis().SetTitle("SB/MC")
ratio.GetYaxis().SetTitleOffset(.4)
ratio.GetYaxis().SetTitleSize(.1)
ratio.GetXaxis().SetTitleSize(.1)
ratio.GetYaxis().SetNdivisions(-402)
CMS_lumi.CMS_lumi(pad2, 4, 11)

pad2.cd()
maxRatio = 1.5
minRatio = 0.5

# ratio.Draw('e,x0')
# errorbandRatio = errorband.Clone("errorbandRatio")
# errorbandRatio.Divide(histo_sieie_MC)
# errorbandRatio.Draw('e2,same')
# oneLine.Draw("same")

canvasRatio.Update()
canvasRatio.RedrawAxis()

canvasRatio.Print("all_histo_sieie_%s_%s.pdf"%(channel,selYear))
canvasRatio.Close()











