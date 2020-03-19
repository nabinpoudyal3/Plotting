from __future__ import print_function
import ROOT
import numpy
import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

ListOfFiles = [
               "higgsCombinedatacard_CR123_2016_nbins3_WG_0.4.MultiDimFit.mH120.40.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_0.6.MultiDimFit.mH120.60.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_0.8.MultiDimFit.mH120.80.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_1.0.MultiDimFit.mH120.100.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_1.2.MultiDimFit.mH120.120.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_1.4.MultiDimFit.mH120.140.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_1.6.MultiDimFit.mH120.160.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_1.8.MultiDimFit.mH120.180.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_2.0.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombinedatacard_CR123_2016_nbins3_WG_2.2.MultiDimFit.mH120.220.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_2.4.MultiDimFit.mH120.240.root",
               "higgsCombinedatacard_CR123_2016_nbins3_WG_2.6.MultiDimFit.mH120.260.root",                                            
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
     mytree.Draw("WGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting for WGamma SF ')
gr.GetXaxis().SetTitle("Expected WGamma SF");
gr.GetYaxis().SetTitle("Toy Data WGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("WGamma_closure_2016_3.pdf")

ListOfFiles = [
               "higgsCombinedatacard_CR123_2016_nbins6_WG_0.4.MultiDimFit.mH120.40.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_0.6.MultiDimFit.mH120.60.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_0.8.MultiDimFit.mH120.80.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_1.0.MultiDimFit.mH120.100.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_1.2.MultiDimFit.mH120.120.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_1.4.MultiDimFit.mH120.140.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_1.6.MultiDimFit.mH120.160.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_1.8.MultiDimFit.mH120.180.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_2.0.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombinedatacard_CR123_2016_nbins6_WG_2.2.MultiDimFit.mH120.220.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_2.4.MultiDimFit.mH120.240.root",
               "higgsCombinedatacard_CR123_2016_nbins6_WG_2.6.MultiDimFit.mH120.260.root",                                            
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
     mytree.Draw("WGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting for WGamma SF ')
gr.GetXaxis().SetTitle("Expected WGamma SF");
gr.GetYaxis().SetTitle("Toy Data WGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("WGamma_closure_2016_6.pdf")

ListOfFiles = [
               "higgsCombinedatacard_CR123_2016_nbins9_WG_0.4.MultiDimFit.mH120.40.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_0.6.MultiDimFit.mH120.60.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_0.8.MultiDimFit.mH120.80.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_1.0.MultiDimFit.mH120.100.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_1.2.MultiDimFit.mH120.120.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_1.4.MultiDimFit.mH120.140.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_1.6.MultiDimFit.mH120.160.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_1.8.MultiDimFit.mH120.180.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_2.0.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombinedatacard_CR123_2016_nbins9_WG_2.2.MultiDimFit.mH120.220.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_2.4.MultiDimFit.mH120.240.root",
               "higgsCombinedatacard_CR123_2016_nbins9_WG_2.6.MultiDimFit.mH120.260.root",                                            
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
     mytree.Draw("WGammaBkgPhotonSF>>hist1")
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

gr = ROOT.TGraphAsymmErrors( n, x, y,zeros,zeros,errMinus, errPlus)
gr.SetTitle('Toy fitting for WGamma SF ')
gr.GetXaxis().SetTitle("Expected WGamma SF");
gr.GetYaxis().SetTitle("Toy Data WGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("WGamma_closure_2016_9.pdf")


ListOfFiles = [
               "higgsCombinedatacard_CR123_2017_nbins3_WG_0.4.MultiDimFit.mH120.40.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_0.6.MultiDimFit.mH120.60.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_0.8.MultiDimFit.mH120.80.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_1.0.MultiDimFit.mH120.100.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_1.2.MultiDimFit.mH120.120.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_1.4.MultiDimFit.mH120.140.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_1.6.MultiDimFit.mH120.160.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_1.8.MultiDimFit.mH120.180.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_2.0.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombinedatacard_CR123_2017_nbins3_WG_2.2.MultiDimFit.mH120.220.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_2.4.MultiDimFit.mH120.240.root",
               "higgsCombinedatacard_CR123_2017_nbins3_WG_2.6.MultiDimFit.mH120.260.root",                                            
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
     mytree.Draw("WGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting for WGamma SF ')
gr.GetXaxis().SetTitle("Expected WGamma SF");
gr.GetYaxis().SetTitle("Toy WGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("WGamma_closure_2017_3.pdf")

ListOfFiles = [
               "higgsCombinedatacard_CR123_2017_nbins6_WG_0.4.MultiDimFit.mH120.40.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_0.6.MultiDimFit.mH120.60.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_0.8.MultiDimFit.mH120.80.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_1.0.MultiDimFit.mH120.100.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_1.2.MultiDimFit.mH120.120.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_1.4.MultiDimFit.mH120.140.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_1.6.MultiDimFit.mH120.160.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_1.8.MultiDimFit.mH120.180.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_2.0.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombinedatacard_CR123_2017_nbins6_WG_2.2.MultiDimFit.mH120.220.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_2.4.MultiDimFit.mH120.240.root",
               "higgsCombinedatacard_CR123_2017_nbins6_WG_2.6.MultiDimFit.mH120.260.root",                                            
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
     mytree.Draw("WGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting for WGamma SF ')
gr.GetXaxis().SetTitle("Expected WGamma SF");
gr.GetYaxis().SetTitle("Toy WGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("WGamma_closure_2017_6.pdf")


ListOfFiles = [
               "higgsCombinedatacard_CR123_2017_nbins9_WG_0.4.MultiDimFit.mH120.40.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_0.6.MultiDimFit.mH120.60.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_0.8.MultiDimFit.mH120.80.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_1.0.MultiDimFit.mH120.100.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_1.2.MultiDimFit.mH120.120.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_1.4.MultiDimFit.mH120.140.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_1.6.MultiDimFit.mH120.160.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_1.8.MultiDimFit.mH120.180.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_2.0.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombinedatacard_CR123_2017_nbins9_WG_2.2.MultiDimFit.mH120.220.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_2.4.MultiDimFit.mH120.240.root",
               "higgsCombinedatacard_CR123_2017_nbins9_WG_2.6.MultiDimFit.mH120.260.root",                                            
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
     mytree.Draw("WGammaBkgPhotonSF>>hist1")
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


gr = ROOT.TGraphAsymmErrors( n, x, y,zeros,zeros,errMinus, errPlus)
gr.SetTitle('Toy fitting for WGamma SF ')
gr.GetXaxis().SetTitle("Expected WGamma SF");
gr.GetYaxis().SetTitle("Toy WGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("WGamma_closure_2017_9.pdf")

ListOfFiles = [
               "higgsCombinedatacard_CR123_2018_nbins3_WG_0.4.MultiDimFit.mH120.40.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_0.6.MultiDimFit.mH120.60.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_0.8.MultiDimFit.mH120.80.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_1.0.MultiDimFit.mH120.100.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_1.2.MultiDimFit.mH120.120.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_1.4.MultiDimFit.mH120.140.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_1.6.MultiDimFit.mH120.160.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_1.8.MultiDimFit.mH120.180.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_2.0.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombinedatacard_CR123_2018_nbins3_WG_2.2.MultiDimFit.mH120.220.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_2.4.MultiDimFit.mH120.240.root",
               "higgsCombinedatacard_CR123_2018_nbins3_WG_2.6.MultiDimFit.mH120.260.root",                                            
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
     mytree.Draw("WGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting for WGamma SF ')
gr.GetXaxis().SetTitle("Expected WGamma SF");
gr.GetYaxis().SetTitle("Toy Data WGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("WGamma_closure_2018_3.pdf")


ListOfFiles = [
               "higgsCombinedatacard_CR123_2018_nbins6_WG_0.4.MultiDimFit.mH120.40.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_0.6.MultiDimFit.mH120.60.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_0.8.MultiDimFit.mH120.80.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_1.0.MultiDimFit.mH120.100.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_1.2.MultiDimFit.mH120.120.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_1.4.MultiDimFit.mH120.140.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_1.6.MultiDimFit.mH120.160.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_1.8.MultiDimFit.mH120.180.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_2.0.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombinedatacard_CR123_2018_nbins6_WG_2.2.MultiDimFit.mH120.220.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_2.4.MultiDimFit.mH120.240.root",
               "higgsCombinedatacard_CR123_2018_nbins6_WG_2.6.MultiDimFit.mH120.260.root",                                            
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
     mytree.Draw("WGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting of for WGamma SF ')
gr.GetXaxis().SetTitle("Expected WGamma SF");
gr.GetYaxis().SetTitle("Toy Data WGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("WGamma_closure_2018_6.pdf")


ListOfFiles = [
               "higgsCombinedatacard_CR123_2018_nbins9_WG_0.4.MultiDimFit.mH120.40.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_0.6.MultiDimFit.mH120.60.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_0.8.MultiDimFit.mH120.80.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_1.0.MultiDimFit.mH120.100.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_1.2.MultiDimFit.mH120.120.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_1.4.MultiDimFit.mH120.140.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_1.6.MultiDimFit.mH120.160.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_1.8.MultiDimFit.mH120.180.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_2.0.MultiDimFit.mH120.200.root",                                                                                          
               "higgsCombinedatacard_CR123_2018_nbins9_WG_2.2.MultiDimFit.mH120.220.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_2.4.MultiDimFit.mH120.240.root",
               "higgsCombinedatacard_CR123_2018_nbins9_WG_2.6.MultiDimFit.mH120.260.root",                                            
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
     mytree.Draw("WGammaBkgPhotonSF>>hist1")
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
gr.SetTitle('Toy fitting of for WGamma SF ')
gr.GetXaxis().SetTitle("Expected WGamma SF");
gr.GetYaxis().SetTitle("Toy Data WGamma SF");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("WGamma_closure_2018_9.pdf")
