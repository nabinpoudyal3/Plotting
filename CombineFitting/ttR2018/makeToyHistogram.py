
import ROOT
import numpy
import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(1111)
ROOT.gStyle.SetOptFit(111)

ListOfFiles = [

               "higgsCombineel_2018_1.0.MultiDimFit.mH120.1234100.root",
]              

c1 = ROOT.TCanvas( 'c1', 'toy histogram', 800,800 )

for ifile in ListOfFiles:
	myfile = ROOT.TFile(ifile,"read")
	mytree=myfile.limit
	mytree.Draw("r>>hist1")
	hist1 = ROOT.gDirectory.Get('hist1')
	hist1.Fit("gaus")
c1.Draw()
c1.Print("ttgamma_histogram_ele_2018.pdf") #####


for ifile in ListOfFiles:
	myfile = ROOT.TFile(ifile,"read")
	mytree=myfile.limit
	mytree.Draw("nonPromptSF>>hist2")
	hist2 = ROOT.gDirectory.Get('hist2')
	hist2.Fit("gaus")
c1.Draw()
c1.Print("nonPrompt_histogram_ele_2018.pdf") #####
