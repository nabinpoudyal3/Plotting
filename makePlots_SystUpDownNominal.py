from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory
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

# parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
#                 help="Specify which channel Mu or Ele? default is Mu" )

parser.add_option("--tight", dest="tight", default=False,action="store_true",
					help="draw photon Category for tight selection" )

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

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print(Fore.RED + "Specify which year 2016, 2017 or 2018?")
	sys.exit()

# finalState = options.channel

looseCRge2e0 =options.looseCRge2e0 #cr123
looseCRe2e0  =options.looseCRe2e0 #cr1
looseCRe3e0  =options.looseCRe3e0 
looseCRge4e0 =options.looseCRge4e0
looseCRe2e1  =options.looseCRe2e1
looseCRe2e2  =options.looseCRe2e2
looseCRe3e1  =options.looseCRe3e1
looseCRe3ge2 =options.looseCRe3ge2
tight        =options.tight

# if finalState=='Ele':
# 	channel = 'ele'
# 	channelText = "e+jets"

# if finalState=='Mu':
# 	channel = 'mu'
# 	channelText = "#mu+jets"
#######
########

#allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","Pdf","fsr","isr"]
#allsystematics = ["PU","MuEff","BTagSF_l","PhoEff", "BTagSF_b","EleEff","Q2","fsr","isr"]
#if systematics in allsystematics: print "running on systematics"
#else: print(Fore.RED + "systematics is not in list. Add the systematics in the list if you are running for systematics.")

#print(Style.RESET_ALL) 
# %jsroot
# import ROOT
# filename = "../../misIDEle_syst_looseCRge2e0plots_2016/misIDEle_syst_Prefit.root"
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
	plotDirectory  = "misIDEle_syst_looseCRge2e0plots_%s"%(selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"

if looseCRge2e0:  #CR1+CR2+CR3
	plotDirectory = "misIDEle_syst_looseCRge2e0plots_%s/"%(selYear)
	regionText = "N_{j}#geq2, N_{b}=0"

if looseCRe2e0:  #CR1     
	plotDirectory = "misIDEle_syst_looseCRe2e0plots_%s/"%(selYear)
	regionText = "N_{j}=2, N_{b}=0"

if looseCRe3e0:  #CR2
	plotDirectory = "misIDEle_syst_looseCRe3e0plots_%s/"%(selYear)
	regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0:  #CR3
	plotDirectory = "misIDEle_syst_looseCRge4e0plots_%s/"%(selYear)
	regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe2e1:  #CR4
	plotDirectory = "misIDEle_syst_looseCRe2e1plots_%s/"%(selYear)
	regionText = "N_{j}=2, N_{b}=1"

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
gROOT.ForceStyle()

if selYear=='2016': 
	myDir = {"ele/MisIDEleSixteen":"ele_MisIDEleSixteen","ele/WgammaBkgPhoton":"ele_WgammaBkgPhoton","ele/ZgammaBkgPhoton":"ele_ZgammaBkgPhoton","ele/OtherSampleBkgPhoton":"ele_OtherSampleBkgPhoton",
             "mu/MisIDEleSixteen":"mu_MisIDEleSixteen","mu/WgammaBkgPhoton":"mu_WgammaBkgPhoton","mu/ZgammaBkgPhoton":"mu_ZgammaBkgPhoton","mu/OtherSampleBkgPhoton":"mu_OtherSampleBkgPhoton"}

elif selYear=='2017':
	myDir = {"ele/MisIDEleSeventeen":"ele_MisIDEleSeventeen","ele/WgammaBkgPhoton":"ele_WgammaBkgPhoton","ele/ZgammaBkgPhoton":"ele_ZgammaBkgPhoton","ele/OtherSampleBkgPhoton":"ele_OtherSampleBkgPhoton",
             "mu/MisIDEleSeventeen":"mu_MisIDEleSeventeen","mu/WgammaBkgPhoton":"mu_WgammaBkgPhoton","mu/ZgammaBkgPhoton":"mu_ZgammaBkgPhoton","mu/OtherSampleBkgPhoton":"mu_OtherSampleBkgPhoton"}

else: 
	myDir = {"ele/MisIDEleEighteen":"ele_MisIDEleEighteen","ele/WgammaBkgPhoton":"ele_WgammaBkgPhoton","ele/ZgammaBkgPhoton":"ele_ZgammaBkgPhoton","ele/OtherSampleBkgPhoton":"ele_OtherSampleBkgPhoton",
             "mu/MisIDEleEighteen":"mu_MisIDEleEighteen","mu/WgammaBkgPhoton":"mu_WgammaBkgPhoton","mu/ZgammaBkgPhoton":"mu_ZgammaBkgPhoton","mu/OtherSampleBkgPhoton":"mu_OtherSampleBkgPhoton"}

import CMS_lumi

if selYear == '2016':	CMS_lumi.lumi_13TeV = "[2016] 35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "[2017] 41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "[2018] 59.74 fb^{-1}"

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)
	

filename = "misIDEle_syst_Prefit.root"
systematicList = ["BTagSF_b","BTagSF_l","MuEff","EleEff","PhoEff","PU","Q2","isr", "fsr", "prefireEcal"] # keep adding more systematics 
myfile = ROOT.TFile(plotDirectory+filename,"READ")

# # myfile.ls()
# #Note: PhoEff doesn't seem to be normalized.
for idir in myDir.keys():
	myfile.cd(idir)
	for item in systematicList:
		h_nominal = myfile.Get(idir+"/nominal");h_nominal.SetTitle(";M_{l,#gamma}(GeV);Events")
		h_nominal.SetLineColor(ROOT.kBlack);h_nominal.SetFillColor(ROOT.kBlack);h_nominal.SetLineWidth(2);h_nominal.SetMarkerStyle(8);

		h_Up = myfile.Get(idir+"/%sUp"%item);h_Up.SetTitle("")
		h_Up.SetLineColor(ROOT.kRed);h_Up.SetFillColor(ROOT.kRed);h_Up.SetLineWidth(2);h_Up.SetMarkerStyle(4);

		h_Down = myfile.Get(idir+"/%sDown"%item);h_Down.SetTitle("")
		h_Down.SetLineColor(ROOT.kBlue);h_Down.SetFillColor(ROOT.kBlue);h_Down.SetLineWidth(2);h_Down.SetMarkerStyle(5);

		print item, " :: ",h_nominal.Integral(),"==>", h_Up.Integral(),"==>", h_Down.Integral()
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
		legend.SetHeader(myDir[idir],"L")
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

		legend.AddEntry(h_nominal,"nominal","f")
		legend.AddEntry(h_Up,"%s_Up"%item,"f")
		legend.AddEntry(h_Down,"%s_Down"%item,"f")
		
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
		h_nominal.SetMaximum(1.1*maxVal)
		h_nominal.SetMinimum(minVal)
		
		print maxVal, minVal
		#CMS_lumi.channelText = (channelText+"\\n"+regionText)
		#if postfitPlots: CMS_lumi.channelText =channelText+"\\n "+regionText+"\\n "+chi2Text

		CMS_lumi.channelText = regionText
		CMS_lumi.cmsText=''
		CMS_lumi.writeChannelText = True
		CMS_lumi.writeExtraText = False
		CMS_lumi.CMS_lumi(pad1, 4, 11)


		ratioUp   =   h_Up.Clone("ratioUp") #data, UP or down
		ratioDown = h_Down.Clone("ratioDown") #data, UP or down

		temp = h_nominal.Clone("temp") # MC or nominal
		for i_bin in range(1,temp.GetNbinsX()+1):
			temp.SetBinError(i_bin,0.)
		ratioUp.Divide(temp)
		ratioDown.Divide(temp)

		    
		ratioUp.SetTitle('')
		ratioUp.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
		ratioUp.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
		ratioUp.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
		ratioUp.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
		ratioUp.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap-padGap))

		maxRatio = ratioUp.GetMaximum()
		minRatio = ratioDown.GetMinimum()

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

		ratioUp.GetYaxis().SetRangeUser(0.8,1.2)
		ratioUp.GetYaxis().SetNdivisions(504)
		ratioUp.GetXaxis().SetTitle('m_{l,#gamma} GeV')
		ratioUp.GetYaxis().SetTitle("Data/MC")
		ratioUp.GetYaxis().SetTitleOffset(.4)
		ratioUp.GetYaxis().SetTitleSize(.09)
		ratioUp.GetYaxis().SetNdivisions(2)

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

		c.Print("%s%s_%s.pdf"%(plotDirectory,myDir[idir],item))
		c.Close()




from PyPDF2 import PdfFileMerger, PdfFileReader

pdflocation="/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/"+plotDirectory
os.chdir(pdflocation)

print plotDirectory[:-1]

pdf2merge =[]
for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdf2merge.append(filename)

merger = PdfFileMerger()
for filename in pdf2merge:
    merger.append(PdfFileReader(file(filename, 'rb')))

merger.write(plotDirectory[:-1]+'.pdf')



