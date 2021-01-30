
import ROOT
import numpy
import array
import sys,os

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit(1)

ListOfFiles = [
               "fitDiagnostics.TOY_ele_2018.root",
               "fitDiagnostics.TOY_mu_2018.root",
               "fitDiagnostics.TOY_both_2018.root"                                    
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

outputDir = "NuisancePlots"

if not os.path.exists(outputDir):
	os.mkdir(outputDir)
	
	
#listOfParameters = ["r","BTagSF_b","BTagSF_l","EleEff","MuEff","PU","PhoEff","Q2","lumi","misIDE","ZGSF","TTbarSF","OtherSF","WGSF"]
listOfParameters = ["r","BTagSF_b","BTagSF_l","EleEff","MuEff","PhoEff","lumi","misIDE","ZGSF","TTbarSF","OtherSF","WGSF"]#,"nonPromptSF"]
for ifile in ListOfFiles:
	channel = ifile[19:-10]
	myfile = ROOT.TFile(ifile,"read")
	mytree=myfile.tree_fit_sb
	for param in listOfParameters:
		hist = ROOT.TH1F("hist","",100,-2,2)
		mytree.Draw("%s >> hist"%(param))
		hist.Fit("gaus")
		hist.SetTitle("%s;%s;"%(channel,param))
		hist.GetYaxis().SetLabelSize(0.03)
		hist.GetXaxis().SetLabelSize(0.03)
		ROOT.gPad.Update()
		mypal = hist.GetListOfFunctions().FindObject('stats')
		mypal.SetX1NDC(0.17)
		mypal.SetX2NDC(0.4)
		mypal.SetY1NDC(0.7)
		mypal.SetY2NDC(0.9)
		c1.Draw()
		c1.Modified()
		c1.Update()
		c1.Print("%s/%s_%s.pdf"%(outputDir,channel,param))
		hist.Delete()

