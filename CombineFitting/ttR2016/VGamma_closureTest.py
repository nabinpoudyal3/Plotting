
import ROOT
import numpy
import array
import sys
import argparse
from optparse import OptionParser

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

parser = OptionParser()

parser.add_option("-poi",             dest="poi",            default="",   type='str',         help="")
# parser.add_option("--with0btagCR",    dest="with0btagCR",    default=False,action="store_true",help="")
parser.add_option("--without0btagCR", dest="without0btagCR", default=False,action="store_true",help="")   

(options, args) = parser.parse_args()

poi            = options.poi
# with0btagCR    = options.with0btagCR
without0btagCR = options.without0btagCR
print poi

if without0btagCR:
     ListOfFiles = [
               "higgsCombineel_2016_%s_no0BtagCR_0.4.MultiDimFit.mH120.123440.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_0.6.MultiDimFit.mH120.123460.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_0.8.MultiDimFit.mH120.123480.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_1.0.MultiDimFit.mH120.1234100.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_1.2.MultiDimFit.mH120.1234120.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_1.4.MultiDimFit.mH120.1234140.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_1.6.MultiDimFit.mH120.1234160.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_1.8.MultiDimFit.mH120.1234180.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_2.0.MultiDimFit.mH120.1234200.root"%poi,                                                                                          
               "higgsCombineel_2016_%s_no0BtagCR_2.2.MultiDimFit.mH120.1234220.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_2.4.MultiDimFit.mH120.1234240.root"%poi,
               "higgsCombineel_2016_%s_no0BtagCR_2.6.MultiDimFit.mH120.1234260.root"%poi,                                            
              ]
              
else:
     ListOfFiles = [
               "higgsCombineel_2016_%s_0.4.MultiDimFit.mH120.123440.root"%poi,
               "higgsCombineel_2016_%s_0.6.MultiDimFit.mH120.123460.root"%poi,
               "higgsCombineel_2016_%s_0.8.MultiDimFit.mH120.123480.root"%poi,
               "higgsCombineel_2016_%s_1.0.MultiDimFit.mH120.1234100.root"%poi,
               "higgsCombineel_2016_%s_1.2.MultiDimFit.mH120.1234120.root"%poi,
               "higgsCombineel_2016_%s_1.4.MultiDimFit.mH120.1234140.root"%poi,
               "higgsCombineel_2016_%s_1.6.MultiDimFit.mH120.1234160.root"%poi,
               "higgsCombineel_2016_%s_1.8.MultiDimFit.mH120.1234180.root"%poi,
               "higgsCombineel_2016_%s_2.0.MultiDimFit.mH120.1234200.root"%poi,                                                                                          
               "higgsCombineel_2016_%s_2.2.MultiDimFit.mH120.1234220.root"%poi,
               "higgsCombineel_2016_%s_2.4.MultiDimFit.mH120.1234240.root"%poi,
               "higgsCombineel_2016_%s_2.6.MultiDimFit.mH120.1234260.root"%poi,                                            
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
	mytree.Draw("%s>>hist1"%poi)
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
gr.SetTitle('Bias test for %s for tt/tt#gamma fitting'%poi)
gr.GetXaxis().SetTitle("Expected %s values"%poi);
gr.GetYaxis().SetTitle("Measured %s values"%poi);
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
if without0btagCR:c1.Print("%s_no0BtagCR_closure_ele_2016.pdf"%poi) #####
else:c1.Print("%s_closure_ele_2016.pdf"%poi) #####


if without0btagCR:
     ListOfFiles = [
               "higgsCombinemu_2016_%s_no0BtagCR_0.4.MultiDimFit.mH120.123440.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_0.6.MultiDimFit.mH120.123460.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_0.8.MultiDimFit.mH120.123480.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_1.0.MultiDimFit.mH120.1234100.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_1.2.MultiDimFit.mH120.1234120.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_1.4.MultiDimFit.mH120.1234140.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_1.6.MultiDimFit.mH120.1234160.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_1.8.MultiDimFit.mH120.1234180.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_2.0.MultiDimFit.mH120.1234200.root"%poi,                                                                                          
               "higgsCombinemu_2016_%s_no0BtagCR_2.2.MultiDimFit.mH120.1234220.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_2.4.MultiDimFit.mH120.1234240.root"%poi,
               "higgsCombinemu_2016_%s_no0BtagCR_2.6.MultiDimFit.mH120.1234260.root"%poi,                                            
              ]
              
else:
     ListOfFiles = [
               "higgsCombinemu_2016_%s_0.4.MultiDimFit.mH120.123440.root"%poi,
               "higgsCombinemu_2016_%s_0.6.MultiDimFit.mH120.123460.root"%poi,
               "higgsCombinemu_2016_%s_0.8.MultiDimFit.mH120.123480.root"%poi,
               "higgsCombinemu_2016_%s_1.0.MultiDimFit.mH120.1234100.root"%poi,
               "higgsCombinemu_2016_%s_1.2.MultiDimFit.mH120.1234120.root"%poi,
               "higgsCombinemu_2016_%s_1.4.MultiDimFit.mH120.1234140.root"%poi,
               "higgsCombinemu_2016_%s_1.6.MultiDimFit.mH120.1234160.root"%poi,
               "higgsCombinemu_2016_%s_1.8.MultiDimFit.mH120.1234180.root"%poi,
               "higgsCombinemu_2016_%s_2.0.MultiDimFit.mH120.1234200.root"%poi,                                                                                          
               "higgsCombinemu_2016_%s_2.2.MultiDimFit.mH120.1234220.root"%poi,
               "higgsCombinemu_2016_%s_2.4.MultiDimFit.mH120.1234240.root"%poi,
               "higgsCombinemu_2016_%s_2.6.MultiDimFit.mH120.1234260.root"%poi,                                            
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
	mytree.Draw("%s>>hist1"%poi)
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
gr.SetTitle('Bias test for %s for tt/tt#gamma fitting'%poi)
gr.GetXaxis().SetTitle("Expected %s values"%poi);
gr.GetYaxis().SetTitle("Measured %s values"%poi);
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
if without0btagCR: c1.Print("%s_no0BtagCR_closure_mu_2016.pdf"%poi) #####
else: c1.Print("%s_closure_mu_2016.pdf"%poi) #####