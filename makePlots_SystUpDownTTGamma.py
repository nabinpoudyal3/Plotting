from ROOT import kWarning, TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory,kViolet
#from ROOT import *
import os, PyPDF2

import numpy
import sys
from optparse import OptionParser
from sampleInformation import sampleList
import sampleInformation
from numpy import log10
from array import array

padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
parser = OptionParser()
parser.add_option("-y", "--year", dest="Year", default="",type='str',
					help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-c", "--channel", dest="channel", default="",type='str',
                 help="Specify which channel Mu or Ele? default is Mu" )

parser.add_option("--tight", dest="tight", default=False,action="store_true",
					help="draw photon Category for tight selection" )

parser.add_option("--plotVariable", dest="plotVariable",default="",type="str",
					help="Specify M3 or ChIso" )

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print(Fore.RED + "Specify which year 2016, 2017 or 2018?")
	sys.exit()

finalState = options.channel

tight          =options.tight
plotVariable   =options.plotVariable

# gSystem.RedirectOutput("/dev/null")
gErrorIgnoreLevel = kWarning

print plotVariable

if finalState=='Ele':
 	channel = 'ele'
 	channelText = "e+jets"

if finalState=='Mu':
 	channel = 'mu'
 	channelText = "#mu+jets"
#######
########

#allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","Pdf","fsr","isr"]
#allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","fsr","isr"]
#if systematics in allsystematics: print "running on systematics"
#else: print(Fore.RED + "systematics is not in list. Add the systematics in the list if you are running for systematics.")

#print(Style.RESET_ALL) 
# %jsroot
# import ROOT
# filename = "../../M3ChIso_tightplots_2016/misIDEle_syst_Prefit.root"
# systematicList = ["BTagSF_b","BTagSF_l","MuEff","EleEff","PhoEff","PU","Q2"] # keep adding more systematics 
# myfile = ROOT.TFile(filename,"READ")
# myDir = {"ele/MisIDEleSixteen":"ele_MisIDEleSixteen","ele/WgammaBkgPhoton":"ele_WgammaBkgPhoton","ele/ZgammaBkgPhoton":"ele_ZgammaBkgPhoton","ele/OtherSampleBkgPhoton":"ele_OtherSampleBkgPhoton",
#          "mu/MisIDEleSixteen":"mu_MisIDEleSixteen","mu/WgammaBkgPhoton":"mu_WgammaBkgPhoton","mu/ZgammaBkgPhoton":"mu_ZgammaBkgPhoton","mu/OtherSampleBkgPhoton":"mu_OtherSampleBkgPhoton"}

# # myfile.ls()
# #Note: PhoEff doesn't seem to be normalized.
# for idir in myDir.keys():
#     myfile.cd(idir)
#     for item in systematicList:
#         h_nominal = myfile.Get(idir+"/nominal");h_nominal.SetTitle(";M_{e,#gamma}(GeV);Events")
#         h_nominal.SetLineColor(ROOT.kBlack);h_nominal.SetFillColor(ROOT.kBlack);h_nominal.SetLineWidth(2);h_nominal.SetMarkerStyle(8);
        
#         h_Up = myfile.Get(idir+"/%sUp"%item);h_Up.SetTitle("")
#         h_Up.SetLineColor(ROOT.kRed);h_Up.SetFillColor(ROOT.kRed);h_Up.SetLineWidth(2);h_Up.SetMarkerStyle(4);
        
#         h_Down = myfile.Get(idir+"/%sDown"%item);h_Down.SetTitle("")
#         h_Down.SetLineColor(ROOT.kBlue);h_Down.SetFillColor(ROOT.kBlue);h_Down.SetLineWidth(2);h_Down.SetMarkerStyle(5);
        
#         print item, " :: ",h_nominal.Integral(),"==>", h_Up.Integral(),"==>", h_Down.Integral()
#         c = ROOT.TCanvas('c','',800,600)
#         legend = ROOT.TLegend(0.7,0.7,0.88,0.88)
#         legend.SetBorderSize(0)
#         legend.SetFillColor(0)
#         legend.AddEntry(h_nominal,"nominal","f")
#         legend.AddEntry(h_Up,"%s_Up"%item,"f")
#         legend.AddEntry(h_Down,"%s_Down"%item,"f")
#         # print dir(c)
        
#         h_nominal.Draw()
#         h_Up.Draw("same")
#         h_Down.Draw("same")
        
#         legend.Draw("same")
#         c.Draw()
#         c.SetTitle("")
#         c.Print("%s_%s.pdf"%(myDir[idir],item))
#         del c

# systematicList = ["BTagSF_b","BTagSF_l","MuEff","EleEff","PhoEff","PU","Q2"] # keep adding more systematics 

if tight:      #SR8 
	plotDirectory  = "ttgamma_tightplots_%s_%s/"%(channel,selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"


# if looseCRe3e1:  #CR5
# 	isSelectionDir = "looseCRe3e1"
# 	if selYear  =='2016': ZJetSF = 1.22;; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
# 	elif selYear=='2017': ZJetSF = 1.22;; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
# 	else :                ZJetSF = 1.22;; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
# 	fileDir  = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
# 	plotDirectory = "misIDEle_syst_looseCRe3e1plots_%s_%s/"%(channel,selYear)
# 	regionText = "N_{j}=3, N_{b}=1"

# if looseCRe2e2:  #CR6
# 	isSelectionDir = "looseCRe2e2"
# 	if selYear  =='2016': ZJetSF = 1.22;; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
# 	elif selYear=='2017': ZJetSF = 1.22;; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
# 	else :                ZJetSF = 1.22;; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
# 	fileDir  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
# 	plotDirectory = "misIDEle_syst_looseCRe2e2plots_%s_%s/"%(channel,selYear)
# 	regionText = "N_{j}=2, N_{b}=2"

# if looseCRe3ge2:  #CR7
# 	isSelectionDir = "looseCRe3ge2"
# 	if selYear  =='2016': ZJetSF = 1.22;; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
# 	elif selYear=='2017': ZJetSF = 1.22;; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
# 	else :                ZJetSF = 1.22;; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
# 	fileDir  = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
# 	plotDirectory = "misIDEle_syst_looseCRe3ge2plots_%s_%s/"%(channel,selYear)
# 	regionText = "N_{j}=3, N_{b}#geq2"

###
####

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

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


template_category = {"isolatedTTGamma":kOrange,  "nonPromptTTGamma":kOrange-3,  
					 "isolatedTTbar":  kRed+1,   "nonPromptTTbar":  kRed+3,   
					 "isolatedWGamma": kBlue-4,  "nonPromptWGamma": kViolet-1,  
					 "isolatedZGamma": kBlue-2,  "nonPromptZGamma": kViolet+8,  
					 "isolatedOther":  kGreen+3, "nonPromptOther":  kGreen+4, 
					 "TTGamma":kOrange,
					 "TTbar":  kRed+1, 
					 "WGamma": kBlue-4,
					 "ZGamma": kBlue-2,
					 "Other":  kGreen+3
					}

template_categoryName = {"isolatedTTGamma":"t#bar{t}#gamma iso", "nonPromptTTGamma":"t#bar{t}#gamma non prompt",  
					     "isolatedTTbar":  "t#bar{t} iso",        "nonPromptTTbar":  "t#bar{t} non prompt",   
					     "isolatedWGamma": "W#gamma iso",  "nonPromptWGamma": "W#gamma non prompt",  
					     "isolatedZGamma": "Z#gamma iso",  "nonPromptZGamma": "Z#gamma non prompt",  
					     "isolatedOther":  "other_1 #gamma iso",    "nonPromptOther":  "other_1 #gamma non prompt", 
					     "TTGamma":"t#bart#gamma",
						 "TTbar":  "t#bart",      
						 "WGamma": "W#gamma",     
						 "ZGamma": "Z#gamma",     
						 "Other":  "Other_0#gamma"
					    }
					

# if selYear=='2016': 
# 	myDir = {"ele/MisIDEleSixteen":"ele_MisIDEleSixteen","ele/WgammaBkgPhoton":"ele_WgammaBkgPhoton","ele/ZgammaBkgPhoton":"ele_ZgammaBkgPhoton","ele/OtherSampleBkgPhoton":"ele_OtherSampleBkgPhoton",
#              "mu/MisIDEleSixteen":"mu_MisIDEleSixteen","mu/WgammaBkgPhoton":"mu_WgammaBkgPhoton","mu/ZgammaBkgPhoton":"mu_ZgammaBkgPhoton","mu/OtherSampleBkgPhoton":"mu_OtherSampleBkgPhoton"}

# elif selYear=='2017':
# 	myDir = {"ele/MisIDEleSeventeen":"ele_MisIDEleSeventeen","ele/WgammaBkgPhoton":"ele_WgammaBkgPhoton","ele/ZgammaBkgPhoton":"ele_ZgammaBkgPhoton","ele/OtherSampleBkgPhoton":"ele_OtherSampleBkgPhoton",
#              "mu/MisIDEleSeventeen":"mu_MisIDEleSeventeen","mu/WgammaBkgPhoton":"mu_WgammaBkgPhoton","mu/ZgammaBkgPhoton":"mu_ZgammaBkgPhoton","mu/OtherSampleBkgPhoton":"mu_OtherSampleBkgPhoton"}

# else: 
# 	myDir = {"ele/MisIDEleEighteen":"ele_MisIDEleEighteen","ele/WgammaBkgPhoton":"ele_WgammaBkgPhoton","ele/ZgammaBkgPhoton":"ele_ZgammaBkgPhoton","ele/OtherSampleBkgPhoton":"ele_OtherSampleBkgPhoton",
#              "mu/MisIDEleEighteen":"mu_MisIDEleEighteen","mu/WgammaBkgPhoton":"mu_WgammaBkgPhoton","mu/ZgammaBkgPhoton":"mu_ZgammaBkgPhoton","mu/OtherSampleBkgPhoton":"mu_OtherSampleBkgPhoton"}
if plotVariable=="M30photon":
	systematicList = ["JECTotal0","JER0"]
	# systematicList = ["fsr"] #,"BTagSF_l","MuEff","EleEff","PU","JECTotal","JER","isr","fsr","Q2","Pdf"]
	myDir= {"%s/ZGamma"%plotVariable:  "%s_ZGamma"%plotVariable,
	 		"%s/TTGamma"%plotVariable: "%s_TTGamma"%plotVariable,
	 		"%s/TTbar"%plotVariable:   "%s_TTbar"%plotVariable,
	 		"%s/Other"%plotVariable:   "%s_Other"%plotVariable,
	 		"%s/WGamma"%plotVariable:  "%s_WGamma"%plotVariable,
	 		"%s/SingleTop"%plotVariable:  "%s_t"%plotVariable,
	}
	myDirName = {

			"%s/ZGamma"%plotVariable:  "%s %s "%(plotVariable,template_categoryName["ZGamma"]),
	 		"%s/TTGamma"%plotVariable: "%s %s "%(plotVariable,template_categoryName["TTGamma"]),
	 		"%s/TTbar"%plotVariable:   "%s %s "%(plotVariable,template_categoryName["TTbar"]),
	 		"%s/Other"%plotVariable:   "%s %s "%(plotVariable,template_categoryName["Other"]),
	 		"%s/WGamma"%plotVariable:  "%s %s "%(plotVariable,template_categoryName["WGamma"]),
	 		"%s/SingleTop"%plotVariable:  "%s %s "%(plotVariable,template_categoryName["SingleTop"]),



	}
else:
	systematicList = ["PhoEff"]

	# systematicList = ["PhoEff","misIDE","BTagSF_b","BTagSF_l","MuEff","EleEff","PU","JECTotal","JER","isr","fsr","Q2","Pdf"]
	# systematicList = ["fsr"] #,"BTagSF_l","MuEff","EleEff","PU","JECTotal","JER","isr","fsr","Q2","Pdf"]
	myDir= {"%s/nonPromptZGamma"%plotVariable:  "%s_nonPromptZGamma"%plotVariable,
	 		"%s/nonPromptTTGamma"%plotVariable: "%s_nonPromptTTGamma"%plotVariable,
	 		"%s/nonPromptTTbar"%plotVariable:   "%s_nonPromptTTbar"%plotVariable,
	 		"%s/nonPromptOther"%plotVariable:   "%s_nonPromptOther"%plotVariable,
	 		"%s/nonPromptWGamma"%plotVariable:  "%s_nonPromptWGamma"%plotVariable,
	 		"%s/isolatedTTGamma"%plotVariable:  "%s_isolatedTTGamma"%plotVariable,
	 		"%s/isolatedOther"%plotVariable:    "%s_isolatedOther"%plotVariable,
	 		"%s/isolatedZGamma"%plotVariable:   "%s_isolatedZGamma"%plotVariable,
	 		"%s/isolatedTTbar"%plotVariable:    "%s_isolatedTTbar"%plotVariable,
	 		"%s/isolatedWGamma"%plotVariable:   "%s_isolatedWGamma"%plotVariable,
	}

	myDirName= {"%s/nonPromptZGamma"%plotVariable:  "%s %s "%(plotVariable,template_categoryName["nonPromptZGamma"]),
	 		    "%s/nonPromptTTGamma"%plotVariable: "%s %s "%(plotVariable,template_categoryName["nonPromptTTGamma"]),
	 		    "%s/nonPromptTTbar"%plotVariable:   "%s %s "%(plotVariable,template_categoryName["nonPromptTTbar"]),
	 		    "%s/nonPromptOther"%plotVariable:   "%s %s "%(plotVariable,template_categoryName["nonPromptOther"]),
	 		    "%s/nonPromptWGamma"%plotVariable:  "%s %s "%(plotVariable,template_categoryName["nonPromptWGamma"]),
	 		    "%s/isolatedTTGamma"%plotVariable:  "%s %s "%(plotVariable,template_categoryName["isolatedTTGamma"]),
	 		    "%s/isolatedOther"%plotVariable:    "%s %s "%(plotVariable,template_categoryName["isolatedOther"]),
	 		    "%s/isolatedZGamma"%plotVariable:   "%s %s "%(plotVariable,template_categoryName["isolatedZGamma"]),
	 		    "%s/isolatedTTbar"%plotVariable:    "%s %s "%(plotVariable,template_categoryName["isolatedTTbar"]),
	 		    "%s/isolatedWGamma"%plotVariable:   "%s %s "%(plotVariable,template_categoryName["isolatedWGamma"])
	}
systematicsDictionary = {
"lumi"       : "Luminosity",
"PU"         : "Pile Up",
"PhoEff"     : "Photon Efficiency",
"MuEff"      : "Muon Efficiency",
"Q2"         : "Renorm/Fact Scale",
"BTagSF_b"   : "b tagging ",
"BTagSF_l"   : "l tagging ",
"EleEff"     : "Electron Efficiency",
"prefireEcal": "L1 prefire Efficiency",
"JECTotal1"   : "Jet Energy Correction 1",
"JECTotal0"   : "Jet Energy Correction 0",
"JER1"        : "Jet Energy Resolution 1",
"JER0"        : "Jet Energy Resolution 0",
"OtherSF"    : "1#gamma other bkg norm",
"Other_norm" : "0#gamma other bkg norm",
"TTbarSF"    : "tt norm",
"WGSF"       : "W#gamma norm",
"ZGSF"       : "Z#gamma norm",
"misIDE"     : "MisID ele",
"Pdf"  : "PDF ",
"erd"  : "Color Reconnection",
"hdamp": "ME/PS matching",
"UE"   : "Underlying Events",
"fsr"  : "FSR",
"isr"  : "ISR",
"phoscale" : "Photon Energy Scale",
"phosmear" : "Photon Energy Smearing",
"elescale" : "Electron Energy Scale",
"elesmear" : "Electron Energy Smearing",
"shapeDD"  : "Shape of DataDriven templates"
}

import CMS_lumi

if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"


if not os.path.exists("upDownTemplateTTGamma/"+plotDirectory):
	os.mkdir("upDownTemplateTTGamma/"+plotDirectory)
		
inputfilename = "ttgamma_tightplots_%s_%s/ttgamma_Prefit.root"%(channel,selYear)

myfile = ROOT.TFile(inputfilename,"READ")

# # myfile.ls()
# #Note: PhoEff doesn't seem to be normalized.
line = ""
eline = ""



for idir in myDir.keys():
	myfile.cd(idir)
	for item in systematicList:
		h_nominal = myfile.Get(idir+"/nominal");h_nominal.SetTitle(";%s;Events"%inputfilename[:-12])
		h_nominal.SetLineColor(ROOT.kBlack);h_nominal.SetFillColor(ROOT.kBlack);h_nominal.SetLineWidth(2);h_nominal.SetMarkerStyle(8);

		h_Up = myfile.Get(idir+"/%sUp"%item);h_Up.SetTitle("")
		h_Up.SetLineColor(ROOT.kRed);h_Up.SetFillColor(ROOT.kRed);h_Up.SetLineWidth(2);h_Up.SetMarkerStyle(4);

		h_Down = myfile.Get(idir+"/%sDown"%item);h_Down.SetTitle("")
		h_Down.SetLineColor(ROOT.kBlue);h_Down.SetFillColor(ROOT.kBlue);h_Down.SetLineWidth(2);h_Down.SetMarkerStyle(5);

		# print item, " :: ",h_nominal.Integral(),"==>", h_Up.Integral(),"==>", h_Down.Integral()
		# print item, " :: ",h_nominal.Integral(-1,-1),"==>", h_Up.Integral(-1,-1),"==>", h_Down.Integral(-1,-1)	
        
		line += " %s --> %s :: nominal ==> %.3f Up-nominal ==>  %.3f  Dn-nominal ==> %.3f \n"%(idir,item, h_nominal.Integral(),      h_Up.Integral()-h_nominal.Integral(),           h_Down.Integral()-h_nominal.Integral())
		line += " %s --> %s :: nominal ==> %.3f Up-nominal ==>  %.3f  Dn-nominal ==> %.3f \n"%(idir,item, h_nominal.Integral(-1,-1), h_Up.Integral(-1,-1)-h_nominal.Integral(-1,-1), h_Down.Integral(-1,-1)-h_nominal.Integral(-1,-1))
      
		if h_nominal.Integral() <= 0: eline += " %s --> %s :: nominal ==> %.3f \n"%(idir,item,h_nominal.Integral())

		print item, systematicsDictionary[item]
        # c = ROOT.TCanvas('c','',800,600)
        # legend = ROOT.TLegend(0.7,0.7,0.88,0.88)
        # legend.SetBorderSize(0)
        # legend.SetFillColor(0)
        # legend.AddEntry(h_nominal,"nominal","f")
        # legend.AddEntry(h_Up,"%s_Up"%item,"f")
        # legend.AddEntry(h_Down,"%s_Down"%item,"f")
        # # print dir(c)
        
        # h_nominal.Draw()
        # h_Up.Draw("same")
        # h_Down.Draw("same")
        
        # legend.Draw("same")
        # c.Draw()
        # c.SetTitle("")
        # c.Print("%s%s_%s.pdf"%(plotDirectory,myDir[idir],item))
        # del c

		H = 600;
		W = 800;
		T = 0.08*H
		B = 0.12*H
		L = 0.12*W
		R = 0.1*W

		legendHeightPer = 0.04

		legendStart = 0.6
		legendEnd = 0.97-(R/W)
		# legend = TLegend(0.7,0.7,0.88,0.88)
		legend = TLegend(legendStart, 1-T/H-0.01 - legendHeightPer*(6), legendEnd, 0.99-(T/H)-0.01)
		legend.SetBorderSize(0)
		legend.SetFillColor(0)
		print idir
		legend.SetHeader(myDirName[idir],"L")
		TGaxis.SetMaxDigits(3)

		c = TCanvas('c','',W,H)
		c.SetFillColor(0)
		c.SetBorderMode(0)
		c.SetFrameFillStyle(0)
		c.SetFrameBorderMode(0)
		c.SetLeftMargin( L/W )
		c.SetRightMargin( R/W )
		c.SetTopMargin( T/H )
		c.SetBottomMargin( B/H )
		c.SetTickx(0)
		c.SetTicky(0)
		c.Draw()
		c.cd()

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


		# errorband=stack.GetStack().Last().Clone("error")
		# errorband.Sumw2()
		# errorband.SetLineColor(kBlack)
		# errorband.SetFillColor(kBlack)
		# errorband.SetFillStyle(3245)
		# errorband.SetMarkerSize(0)

		pad1.cd()
		

		print "==>",item
		legend.AddEntry(h_nominal,"nominal","f")
		legend.AddEntry(h_Up,"%s Up"%systematicsDictionary[item],"f")
		legend.AddEntry(h_Down,"%s Down"%systematicsDictionary[item],"f")
		
		h_nominal.Draw()
		h_Up.Draw("same")
		h_Down.Draw("same")

		legend.Draw("same")

		h_nominal.GetXaxis().SetTitle('')
		h_nominal.GetXaxis().SetLabelSize(0)
		h_nominal.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
		h_nominal.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
		h_nominal.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
		h_nominal.SetTitle(';;Events')# '%rebin)


		maxVal = max(h_nominal.GetMaximum(),h_Up.GetMaximum(),h_Down.GetMaximum())
		#minVal = 1
		minVal = min(h_nominal.GetMinimum(),h_Up.GetMinimum(),h_Down.GetMinimum())
		# minVal = min(0,minVal)*2
		minVal = 0.001
		h_nominal.SetMaximum(1.3*maxVal)
		h_nominal.SetMinimum(minVal)
		
		print maxVal, minVal
		#CMS_lumi.channelText = (channelText+"\\n"+regionText)
		#if postfitPlots: CMS_lumi.channelText =channel

		CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText,regionText)
		# CMS_lumi.channelText = regionText
		CMS_lumi.cmsText="CMS"
		CMS_lumi.writeChannelText = True
		CMS_lumi.writeExtraText = True
		CMS_lumi.CMS_lumi(pad1, 4, 11)


		ratioUp   =   h_Up.Clone("ratioUp") #data, UP or down
		ratioDown = h_Down.Clone("ratioDown") #data, UP or down

		temp = h_nominal.Clone("temp") # MC or nominal
		for i_bin in range(1,temp.GetNbinsX()+1):
			temp.SetBinError(i_bin,0.)
		ratioUp.Divide(temp)
		ratioDown.Divide(temp)

		    
		ratioUp.SetTitle('')



		maxRatio = 1.8 #ratioUp.GetMaximum()
		minRatio = 0.2 #ratioDown.GetMinimum()

		for i_bin in range(1,ratioUp.GetNbinsX()):
			if ratioUp.GetBinError(i_bin)<1:
				if ratioUp.GetBinContent(i_bin)>maxRatio:
					maxRatio = ratioUp.GetBinContent(i_bin)
				if ratioUp.GetBinContent(i_bin)<minRatio:
					minRatio = ratioUp.GetBinContent(i_bin)

		if maxRatio > 1.8:
			ratioUp.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
		elif maxRatio < 1:
			ratioUp.GetYaxis().SetRangeUser(0,1.2)
		elif maxRatio-1 < 1-minRatio:
			ratioUp.GetYaxis().SetRangeUser((1-(1-minRatio)*1.2),1.1*maxRatio)		
		else:
			ratioUp.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)

		ratioUp.GetYaxis().SetRangeUser(0.95,1.05)

		# ratioUp.GetYaxis().SetNdivisions(504)
		#ratioUp.GetXaxis().SetTitle(inputfilename[:-12])
		ratioUp.GetXaxis().SetTitle(plotVariable+" "+systematicsDictionary[item])
		ratioUp.GetYaxis().SetTitle("Data/MC")
		# ratioUp.GetYaxis().SetTitleOffset(.38)
		# ratioUp.GetYaxis().SetTitleSize(.1)
		# ratioUp.GetXaxis().SetTitleSize(.1)
		ratioUp.GetYaxis().SetNdivisions(-402)
		ratioUp.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
		ratioUp.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
		ratioUp.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
		ratioUp.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
		ratioUp.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
		CMS_lumi.CMS_lumi(pad2, 4, 11)
		pad2.cd()

		ratioUp.SetMarkerStyle(1)
		ratioUp.SetLineColor(2)
		ratioUp.SetFillColor(0)
		ratioUp.SetLineWidth(2)
		ratioUp.Draw("hist")

		ratioDown.SetMarkerStyle(1)
		ratioDown.SetLineColor(4)
		ratioDown.SetFillColor(0)
		ratioDown.SetLineWidth(2)
		ratioDown.Draw("hist, same")
		# errorbandRatio = errorband.Clone("errorRatio")
		# errorbandRatio.Divide(temp)
		# errorbandRatio.Draw('e2,same')
		oneLine.Draw("same")

		c.Update()
		c.RedrawAxis()

		c.Print("upDownTemplateTTGamma/%s%s_%s.pdf"%(plotDirectory,myDir[idir],item))
		c.Close()

# c.Print("upDownTemplateTTGamma/%s%s.pdf"%(plotDirectory,myDir[idir]))
# c.Close()
with open("oneSigmaVariation/oneSigmaVariation_%s_%s_%s.py"%(plotVariable,channel,selYear),"w") as _file:
    _file.write(line)

with open("oneSigmaVariation/emptyTemplate_%s_%s_%s.py"%(plotVariable,channel,selYear),"w") as _file1:
    _file1.write(eline)


#from PyPDF2 import PdfFileMerger, PdfFileReader

#pdflocation="/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/"+plotDirectory
#os.chdir(pdflocation)

#print plotDirectory

#pdf2merge =[]
#for filename in os.listdir('.'):
#	if filename.endswith('.pdf'):
#		pdf2merge.append(filename)

#merger = PdfFileMerger()
#for filename in pdf2merge:
#    merger.append(PdfFileReader(file(filename, 'rb')))

#merger.write(plotDirectory[:-1]+'_%s.pdf'%plotVariable)

#print plotDirectory[:-1]+'/'+plotDirectory[:-1]+'_%s.pdf'%plotVariable


'''



mv all_ele_2016.pdf  all_ele_2016_3bin.pdf
mv all_mu_2016.pdf  all_mu_2016_3bin.pdf
mv all_ele_2017.pdf  all_ele_2017_3bin.pdf
mv all_mu_2017.pdf  all_mu_2017_3bin.pdf
mv all_ele_2018.pdf  all_ele_2018_3bin.pdf
mv all_mu_2018.pdf  all_mu_2018_3bin.pdf


/home/npoudyal/PlottingBackup_WorkingOne

cp /home/npoudyal/PlottingBackup_WorkingOne/ttgamma_tightplots_mu_2016/ttgamma_Prefit.root  ttgamma_tightplots_mu_2016
cp /home/npoudyal/PlottingBackup_WorkingOne/ttgamma_tightplots_ele_2016/ttgamma_Prefit.root  ttgamma_tightplots_ele_2016
cp /home/npoudyal/PlottingBackup_WorkingOne/ttgamma_tightplots_ele_2017/ttgamma_Prefit.root  ttgamma_tightplots_ele_2017
cp /home/npoudyal/PlottingBackup_WorkingOne/ttgamma_tightplots_ele_2018/ttgamma_Prefit.root  ttgamma_tightplots_ele_2018
cp /home/npoudyal/PlottingBackup_WorkingOne/ttgamma_tightplots_mu_2017/ttgamma_Prefit.root  ttgamma_tightplots_mu_2017
cp /home/npoudyal/PlottingBackup_WorkingOne/ttgamma_tightplots_mu_2018/ttgamma_Prefit.root  ttgamma_tightplots_mu_2018


cp -R ttgamma_tightplots_mu_2016  ttgamma_tightplots_mu_2016_backup  
cp -R ttgamma_tightplots_ele_2016  ttgamma_tightplots_ele_2016_backup  
cp -R ttgamma_tightplots_ele_2017  ttgamma_tightplots_ele_2017_backup  
cp -R ttgamma_tightplots_ele_2018  ttgamma_tightplots_ele_2018_backup  
cp -R ttgamma_tightplots_mu_2017  ttgamma_tightplots_mu_2017_backup  
cp -R ttgamma_tightplots_mu_2018  ttgamma_tightplots_mu_2018_backup  


rm -rf ttgamma_tightplots_mu_2016 
rm -rf ttgamma_tightplots_ele_2016
rm -rf ttgamma_tightplots_ele_2017
rm -rf ttgamma_tightplots_ele_2018
rm -rf ttgamma_tightplots_mu_2017 
rm -rf ttgamma_tightplots_mu_2018 


mv ttgamma_tightplots_mu_2016_backup   ttgamma_tightplots_mu_2016  
mv  ttgamma_tightplots_ele_2016_backup   ttgamma_tightplots_ele_2016 
mv  ttgamma_tightplots_ele_2017_backup   ttgamma_tightplots_ele_2017 
mv  ttgamma_tightplots_ele_2018_backup   ttgamma_tightplots_ele_2018 
mv ttgamma_tightplots_mu_2017_backup   ttgamma_tightplots_mu_2017  
mv ttgamma_tightplots_mu_2018_backup   ttgamma_tightplots_mu_2018  



'''