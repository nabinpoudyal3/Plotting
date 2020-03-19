from __future__ import print_function
import ROOT
import numpy
import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

ListOfFiles = [
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.40.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.60.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.80.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.100.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.120.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.140.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.160.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.180.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.220.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.240.root",
               "higgsCombineCR123_2016_nbins3.MultiDimFit.mH120.260.root",                                            
              ]
c1 = ROOT.TCanvas( 'c1', 'Toy Data vs expected signal strength', 800,800 )
c1.SetGrid()


xData = list(numpy.arange(0.4,2.8,0.2))
yData = []
n = len(xData)
errMinusData = []
errPlusData = []
zerosData = []
for ifile in ListOfFiles:
	zerosData.append(0)
	myfile = ROOT.TFile(ifile,"read")
	mytree=myfile.limit
	mytree.Draw("r>>hist1")
	hist1 = ROOT.gDirectory.Get('hist1')
	yData.append(hist1.GetMean())
	errMinusData.append(hist1.GetRMS())
	errPlusData.append(hist1.GetRMS())

x = array.array( 'f', xData )
y = array.array( 'f', yData )
errMinus = array.array( 'f', errMinusData )
errPlus  = array.array( 'f', errPlusData )
zeros = array.array('f',zerosData)
oneLine = ROOT.TF1("oneline","x",0,3)

gr = ROOT.TGraphAsymmErrors( n, x, y, zeros,zeros,errMinus, errPlus)
gr.SetTitle('Toy fitting for misIDEle SF with 200 iteration')
gr.GetXaxis().SetTitle("Expected misIDEle SF");
gr.GetYaxis().SetTitle("Toy Data misIDEle SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("misID_closure_2016_3.pdf")

