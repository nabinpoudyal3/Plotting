
import ROOT

# import numpy
# import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(1111)
ROOT.gStyle.SetOptFit(111)

ListOfFiles = [

               "fitDiagnostics.TOY_mu_2016.root",
]              

c1 = ROOT.TCanvas( 'c1', 'toy histogram', 800,800 )
# hist1 = ROOT.TH1F("hist1","",50,-5,5)
for ifile in ListOfFiles:
	myfile = ROOT.TFile(ifile,"read")
	mytree=myfile.tree_fit_sb
	mytree.Draw("ZGSF>>hist1(50,0,2)")
	hist1 = ROOT.gDirectory.Get('hist1')
	# hist1.Fit("gaus")
c1.Draw()
c1.Print("ZGSF_ele_2016.pdf") #####


# for ifile in ListOfFiles:
# 	myfile = ROOT.TFile(ifile,"read")
# 	mytree=myfile.limit
# 	mytree.Draw("nonPromptSF>>hist2")
# 	hist2 = ROOT.gDirectory.Get('hist2')
# 	hist2.Fit("gaus")
# c1.Draw()
# c1.Print("nonPrompt_histogram_ele_2016.pdf") #####
