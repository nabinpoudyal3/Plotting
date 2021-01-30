
import ROOT
import numpy
import array
import sys

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

ListOfFiles = [
               "higgsCombineel_2016_0.4.MultiDimFit.mH120.123440.root",
               "higgsCombineel_2016_0.6.MultiDimFit.mH120.123460.root",
               "higgsCombineel_2016_0.8.MultiDimFit.mH120.123480.root",
               "higgsCombineel_2016_1.0.MultiDimFit.mH120.1234100.root",
               "higgsCombineel_2016_1.2.MultiDimFit.mH120.1234120.root",
               "higgsCombineel_2016_1.4.MultiDimFit.mH120.1234140.root",
               "higgsCombineel_2016_1.6.MultiDimFit.mH120.1234160.root",
               "higgsCombineel_2016_1.8.MultiDimFit.mH120.1234180.root",
               "higgsCombineel_2016_2.0.MultiDimFit.mH120.1234200.root",                                                                                          
               "higgsCombineel_2016_2.2.MultiDimFit.mH120.1234220.root",
               "higgsCombineel_2016_2.4.MultiDimFit.mH120.1234240.root",
               "higgsCombineel_2016_2.6.MultiDimFit.mH120.1234260.root",                                            
              ]
              

c1 = ROOT.TCanvas( 'c1', '', 800,800 )
c1.SetFixedAspectRatio()
c1.Draw()
c1.SetGrid()
# c1.DrawFrame(0,0,20,20);
# pad = ROOT.TPad()
# ROOT.gPad.DrawFrame(0.,0.,3.,3.);
# f(x) = p0 + p1*x 
# p0 = offset = 0
# p1 = slope =1
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
# oneLine = ROOT.TF1("oneline","x",0,3)

gr = ROOT.TGraphAsymmErrors( n, x, y, zeros,zeros,errMinus, errPlus)
gr.SetTitle('Closure test for signal strength modifier')
gr.GetXaxis().SetTitle("Expected tt#gamma values");
gr.GetYaxis().SetTitle("Measured tt#gamma values");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# gr.SetMarkerSize(3)
gr.Draw()
gr.Fit("pol1")
slope     = gr.GetFunction("pol1").GetParameter(1)
offset    = gr.GetFunction("pol1").GetParameter(0)
slopeErr  = gr.GetFunction("pol1").GetParError(1)
offsetErr = gr.GetFunction("pol1").GetParError(0)

myText = ROOT.TPaveText(0.3,0.7,0.5,0.8,"NDC")
myText.AddText("slope  = %.2f #pm %.2f"%(slope,slopeErr) )
myText.AddText("offset = %.2f #pm %.2f"%(offset,offsetErr) )
myText.SetTextColor(ROOT.kBlack)
myText.SetFillColor(ROOT.kWhite)
myText.SetTextSize(0.038)
myText.SetTextFont(42)
myText.Draw("same")

c1.Print("ttgamma_closure_ele_2016.pdf") #####

ListOfFiles = [
               "higgsCombinemu_2016_0.4.MultiDimFit.mH120.123440.root",
               "higgsCombinemu_2016_0.6.MultiDimFit.mH120.123460.root",
               "higgsCombinemu_2016_0.8.MultiDimFit.mH120.123480.root",
               "higgsCombinemu_2016_1.0.MultiDimFit.mH120.1234100.root",
               "higgsCombinemu_2016_1.2.MultiDimFit.mH120.1234120.root",
               "higgsCombinemu_2016_1.4.MultiDimFit.mH120.1234140.root",
               "higgsCombinemu_2016_1.6.MultiDimFit.mH120.1234160.root",
               "higgsCombinemu_2016_1.8.MultiDimFit.mH120.1234180.root",
               "higgsCombinemu_2016_2.0.MultiDimFit.mH120.1234200.root",                                                                                          
               "higgsCombinemu_2016_2.2.MultiDimFit.mH120.1234220.root",
               "higgsCombinemu_2016_2.4.MultiDimFit.mH120.1234240.root",
               "higgsCombinemu_2016_2.6.MultiDimFit.mH120.1234260.root",                                            
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
gr.SetTitle('Closure test for signal strength modifier')
gr.GetXaxis().SetTitle("Expected tt#gamma values");
gr.GetYaxis().SetTitle("Measured tt#gamma values");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,3)
gr.GetYaxis().SetRangeUser(0,3)
# print "offset error ", fit.GetParameter(0), "slope error", fit.GetParameter(1)
# gr.SetMarkerSize(3)
gr.Draw()
gr.Fit("pol1")
slope     = gr.GetFunction("pol1").GetParameter(1)
offset    = gr.GetFunction("pol1").GetParameter(0)
slopeErr  = gr.GetFunction("pol1").GetParError(1)
offsetErr = gr.GetFunction("pol1").GetParError(0)

myText = ROOT.TPaveText(0.3,0.7,0.5,0.8,"NDC")
myText.AddText("slope  = %.2f #pm %.2f"%(slope,slopeErr) )
myText.AddText("offset = %.2f #pm %.2f"%(offset,offsetErr) )
myText.SetTextColor(ROOT.kBlack)
myText.SetFillColor(ROOT.kWhite)
myText.SetTextSize(0.038)
myText.SetTextFont(42)
myText.Draw("same")
c1.Print("ttgamma_closure_mu_2016.pdf")  ################################################################################################################
