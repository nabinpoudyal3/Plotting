from __future__ import print_function
import ROOT
import numpy
import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

ListOfFiles = [
               "higgsCombinedatacard_CR123_2016_ZG_0.4.MultiDimFit.mH120.123440.root",
               "higgsCombinedatacard_CR123_2016_ZG_0.6.MultiDimFit.mH120.123460.root",
               "higgsCombinedatacard_CR123_2016_ZG_0.8.MultiDimFit.mH120.123480.root",
               "higgsCombinedatacard_CR123_2016_ZG_1.0.MultiDimFit.mH120.1234100.root",
               "higgsCombinedatacard_CR123_2016_ZG_1.2.MultiDimFit.mH120.1234120.root",
               "higgsCombinedatacard_CR123_2016_ZG_1.4.MultiDimFit.mH120.1234140.root",
               "higgsCombinedatacard_CR123_2016_ZG_1.6.MultiDimFit.mH120.1234160.root",
               "higgsCombinedatacard_CR123_2016_ZG_1.8.MultiDimFit.mH120.1234180.root",
               "higgsCombinedatacard_CR123_2016_ZG_2.0.MultiDimFit.mH120.1234200.root",                                                                                          
               "higgsCombinedatacard_CR123_2016_ZG_2.2.MultiDimFit.mH120.1234220.root",
               "higgsCombinedatacard_CR123_2016_ZG_2.4.MultiDimFit.mH120.1234240.root",
               "higgsCombinedatacard_CR123_2016_ZG_2.6.MultiDimFit.mH120.1234260.root",                                            
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
     mytree.Draw("ZGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting for ZGamma SF ')
gr.GetXaxis().SetTitle("Expected ZGamma SF");
gr.GetYaxis().SetTitle("Toy Data ZGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("ZGamma_closure_2016.pdf")



ListOfFiles = [
               "higgsCombinedatacard_CR123_2017_ZG_0.4.MultiDimFit.mH120.123440.root",
               "higgsCombinedatacard_CR123_2017_ZG_0.6.MultiDimFit.mH120.123460.root",
               "higgsCombinedatacard_CR123_2017_ZG_0.8.MultiDimFit.mH120.123480.root",
               "higgsCombinedatacard_CR123_2017_ZG_1.0.MultiDimFit.mH120.1234100.root",
               "higgsCombinedatacard_CR123_2017_ZG_1.2.MultiDimFit.mH120.1234120.root",
               "higgsCombinedatacard_CR123_2017_ZG_1.4.MultiDimFit.mH120.1234140.root",
               "higgsCombinedatacard_CR123_2017_ZG_1.6.MultiDimFit.mH120.1234160.root",
               "higgsCombinedatacard_CR123_2017_ZG_1.8.MultiDimFit.mH120.1234180.root",
               "higgsCombinedatacard_CR123_2017_ZG_2.0.MultiDimFit.mH120.1234200.root",                                                                                          
               "higgsCombinedatacard_CR123_2017_ZG_2.2.MultiDimFit.mH120.1234220.root",
               "higgsCombinedatacard_CR123_2017_ZG_2.4.MultiDimFit.mH120.1234240.root",
               "higgsCombinedatacard_CR123_2017_ZG_2.6.MultiDimFit.mH120.1234260.root",                                            
              ]
c1 = ROOT.TCanvas( 'c1', 'Toy Data vs expected signal strength', 800, 800 )
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
     mytree.Draw("ZGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting for ZGamma SF ')
gr.GetXaxis().SetTitle("Expected ZGamma SF");
gr.GetYaxis().SetTitle("Toy ZGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("ZGamma_closure_2017.pdf")


ListOfFiles = [
               "higgsCombinedatacard_CR123_2018_ZG_0.4.MultiDimFit.mH120.123440.root",
               "higgsCombinedatacard_CR123_2018_ZG_0.6.MultiDimFit.mH120.123460.root",
               "higgsCombinedatacard_CR123_2018_ZG_0.8.MultiDimFit.mH120.123480.root",
               "higgsCombinedatacard_CR123_2018_ZG_1.0.MultiDimFit.mH120.1234100.root",
               "higgsCombinedatacard_CR123_2018_ZG_1.2.MultiDimFit.mH120.1234120.root",
               "higgsCombinedatacard_CR123_2018_ZG_1.4.MultiDimFit.mH120.1234140.root",
               "higgsCombinedatacard_CR123_2018_ZG_1.6.MultiDimFit.mH120.1234160.root",
               "higgsCombinedatacard_CR123_2018_ZG_1.8.MultiDimFit.mH120.1234180.root",
               "higgsCombinedatacard_CR123_2018_ZG_2.0.MultiDimFit.mH120.1234200.root",                                                                                          
               "higgsCombinedatacard_CR123_2018_ZG_2.2.MultiDimFit.mH120.1234220.root",
               "higgsCombinedatacard_CR123_2018_ZG_2.4.MultiDimFit.mH120.1234240.root",
               "higgsCombinedatacard_CR123_2018_ZG_2.6.MultiDimFit.mH120.1234260.root",                                            
              ]
c1 = ROOT.TCanvas( 'c1', 'Toy Data vs expected signal strength', 800, 800 )
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
     mytree.Draw("ZGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting for ZGamma SF ')
gr.GetXaxis().SetTitle("Expected ZGamma SF");
gr.GetYaxis().SetTitle("Toy Data ZGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("ZGamma_closure_2018.pdf")


