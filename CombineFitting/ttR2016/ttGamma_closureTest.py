
import ROOT
import numpy
import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

ListOfFiles = [
               "higgsCombineel_2016_0.01.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_0.02.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_0.03.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_0.04.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_0.05.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_0.06.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_0.07.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_0.08.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_0.09.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_0.10.MultiDimFit.mH120.1234260.root",
              ]
              

# c1 = ROOT.TCanvas( 'c1', '', 800,800 )
c1 = ROOT.TCanvas()
c1.SetGrid()

xData = list(numpy.arange(0.01,0.1,0.01))
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
oneLine = ROOT.TF1("oneline","x",0,0.1)

gr = ROOT.TGraphAsymmErrors( n, x, y, zeros,zeros,errMinus, errPlus)
gr.SetTitle('Closure test for ratio signal strength modifier for t#bar{t}#gamma/t#bar{t} fitting')
gr.GetXaxis().SetTitle("Expected t#bar{t}#gamma/t#bar{t}");
gr.GetYaxis().SetTitle("Measured t#bar{t}#gamma/t#bar{t}");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,0.1)
gr.GetYaxis().SetRangeUser(0,0.1)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("ttgamma_closure_ele_2016.pdf") #####

ListOfFiles = [
               "higgsCombinemu_2016_0.01.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_0.02.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_0.03.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_0.04.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_0.05.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_0.06.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_0.07.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_0.08.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_0.09.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_0.10.MultiDimFit.mH120.1234260.root",
              ]
# c1 = ROOT.TCanvas( 'c1', '', 800,800 )
c1 = ROOT.TCanvas()
c1.SetGrid()

xData = list(numpy.arange(0.01,0.1,0.01))
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
oneLine = ROOT.TF1("oneline","x",0,0.1)

gr = ROOT.TGraphAsymmErrors( n, x, y, zeros,zeros,errMinus, errPlus)
gr.SetTitle('Closure test for ratio signal strength modifier for t#bar{t}#gamma/t#bar{t}  fitting')
gr.GetXaxis().SetTitle("Expected t#bar{t}#gamma/t#bar{t}");
gr.GetYaxis().SetTitle("Measured t#bar{t}#gamma/t#bar{t}");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,0.1)
gr.GetYaxis().SetRangeUser(0,0.1)
# gr.SetMarkerSize(3)
gr.Draw('AP')
oneLine.Draw('same')

c1.Draw()
c1.Print("ttgamma_closure_mu_2016.pdf")  ################################################################################################################
