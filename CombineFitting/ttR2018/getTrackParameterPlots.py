
import ROOT
import numpy
import array
import sys,os

ROOT.gROOT.SetBatch(True)
#ROOT.gStyle.SetOptStat(0)
#ROOT.gStyle.SetOptFit(1)
#ROOT.gStyle.SetOptStat("nemr")

ListOfFiles = [
               "higgsCombine.TOY_ele_2018.FitDiagnostics.mH120.314159.root",
               "higgsCombine.TOY_mu_2018.FitDiagnostics.mH120.314159.root",
               "higgsCombine.TOY_both_2018.FitDiagnostics.mH120.314159.root",                                    
              ]
              

c1 = ROOT.TCanvas( 'c1', '', 800,800 )
c1.SetFillColor(10)
c1.SetBorderMode(0)
c1.SetBorderSize(0)
c1.SetTickx()
c1.SetTicky()
c1.SetLeftMargin(0.15)
c1.SetRightMargin(0.15)
c1.SetTopMargin(0.15)
c1.SetBottomMargin(0.15)
c1.SetFrameFillColor(0)
c1.SetFrameBorderMode(0)
c1.SetGrid()

outputDir = "TrackParameterPlots"

if not os.path.exists(outputDir):
	os.mkdir(outputDir)
	
listOfParameters = ["r","nonPromptSF","BTagSF_b","BTagSF_l","EleEff","MuEff","PU","PhoEff","lumi","misIDE","ZGSF","TTbarSF","OtherSF","WGSF"]	
#listOfTrackedParameters = ["trackedParam_r","trackedParam_nonPromptSF","trackedParam_BTagSF_b","trackedParam_BTagSF_l","trackedParam_EleEff","trackedParam_MuEff","trackedParam_PU","trackedParam_PhoEff","trackedParam_Q2",
#"trackedParam_lumi","trackedParam_misIDE","trackedParam_ZGSF","trackedParam_TTbarSF","trackedParam_OtherSF","trackedParam_WGSF"]
listOfTrackedParameters = ["trackedParam_r","trackedParam_nonPromptSF","trackedParam_BTagSF_b","trackedParam_BTagSF_l","trackedParam_EleEff","trackedParam_MuEff","trackedParam_PhoEff",
"trackedParam_lumi","trackedParam_misIDE","trackedParam_ZGSF","trackedParam_TTbarSF","trackedParam_OtherSF","trackedParam_WGSF"]
for ifile in ListOfFiles:
	channel = ifile[17:-38]
	myfile = ROOT.TFile(ifile,"read")
	mytree=myfile.limit
	for param in listOfTrackedParameters:
		hist = ROOT.TH2F("hist","",60,-1,2,60,-1,2)
		mytree.Draw("%s:%s >> hist"%(param,"trackedParam_r"),"quantileExpected>=-1","colz")#y,x=r
		#hist.Fit("gaus")
		#hist = ROOT.gDirectory.Get('hist')
		hist.SetTitle("%s;%s;%s;"%(channel,"r",param[13:]))
		hist.GetYaxis().SetLabelSize(0.03)
		hist.GetXaxis().SetLabelSize(0.03)
		ROOT.gPad.Update() # without this we get null pointer to stats box
		mypal = hist.GetListOfFunctions().FindObject('stats')
		mypal.SetX1NDC(0.17)
		mypal.SetX2NDC(0.4)
		mypal.SetY1NDC(0.79)
		mypal.SetY2NDC(0.99)
		c1.Draw()
		c1.Modified()
		c1.Update()
		c1.Print("%s/%s_%s.pdf"%(outputDir,channel,param[13:]))
		hist.Delete()
