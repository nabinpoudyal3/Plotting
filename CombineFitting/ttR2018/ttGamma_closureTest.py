
import ROOT
import numpy
import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

ListOfFiles = [
               "higgsCombineel_2018_0.4.MultiDimFit.mH120.123440.root",
               "higgsCombineel_2018_0.6.MultiDimFit.mH120.123460.root",
               "higgsCombineel_2018_0.8.MultiDimFit.mH120.123480.root",
               "higgsCombineel_2018_1.0.MultiDimFit.mH120.1234100.root",
               "higgsCombineel_2018_1.2.MultiDimFit.mH120.1234120.root",
               "higgsCombineel_2018_1.4.MultiDimFit.mH120.1234140.root",
               "higgsCombineel_2018_1.6.MultiDimFit.mH120.1234160.root",
               "higgsCombineel_2018_1.8.MultiDimFit.mH120.1234180.root",
               "higgsCombineel_2018_2.0.MultiDimFit.mH120.1234200.root",                                                                                          
               "higgsCombineel_2018_2.2.MultiDimFit.mH120.1234220.root",
               "higgsCombineel_2018_2.4.MultiDimFit.mH120.1234240.root",
               "higgsCombineel_2018_2.6.MultiDimFit.mH120.1234260.root",                                            
              ]
              

c1 = ROOT.TCanvas( 'c1', '', 800,800 )
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
gr.SetTitle('Closure test for ratio signal strength modifier for tt/tt#gamma fitting')
gr.GetXaxis().SetTitle("Expected tt#gamma values");
gr.GetYaxis().SetTitle("Measured tt#gamma values");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("ttgamma_closure_ele_2018.pdf") #####

ListOfFiles = [
               "higgsCombinemu_2018_0.4.MultiDimFit.mH120.123440.root",
               "higgsCombinemu_2018_0.6.MultiDimFit.mH120.123460.root",
               "higgsCombinemu_2018_0.8.MultiDimFit.mH120.123480.root",
               "higgsCombinemu_2018_1.0.MultiDimFit.mH120.1234100.root",
               "higgsCombinemu_2018_1.2.MultiDimFit.mH120.1234120.root",
               "higgsCombinemu_2018_1.4.MultiDimFit.mH120.1234140.root",
               "higgsCombinemu_2018_1.6.MultiDimFit.mH120.1234160.root",
               "higgsCombinemu_2018_1.8.MultiDimFit.mH120.1234180.root",
               "higgsCombinemu_2018_2.0.MultiDimFit.mH120.1234200.root",                                                                                          
               "higgsCombinemu_2018_2.2.MultiDimFit.mH120.1234220.root",
               "higgsCombinemu_2018_2.4.MultiDimFit.mH120.1234240.root",
               "higgsCombinemu_2018_2.6.MultiDimFit.mH120.1234260.root",                                            
              ]
c1 = ROOT.TCanvas( 'c1', '', 800,800 )
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
gr.SetTitle('Closure test for ratio signal strength modifier for tt/tt#gamma fitting')
gr.GetXaxis().SetTitle("Expected tt#gamma values");
gr.GetYaxis().SetTitle("Measured tt#gamma values");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("ttgamma_closure_mu_2018.pdf")  ################################################################################################################
