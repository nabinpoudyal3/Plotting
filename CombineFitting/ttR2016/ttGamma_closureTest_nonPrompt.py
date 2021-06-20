
import ROOT
import numpy
import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

ListOfFiles = [
               "higgsCombineel_2016_nonPrompt_0.01.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_nonPrompt_0.02.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_nonPrompt_0.03.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_nonPrompt_0.04.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_nonPrompt_0.05.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_nonPrompt_0.06.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_nonPrompt_0.07.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_nonPrompt_0.08.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_nonPrompt_0.09.MultiDimFit.mH120.1234260.root",
               "higgsCombineel_2016_nonPrompt_0.10.MultiDimFit.mH120.1234260.root",
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
	mytree.Draw("nonPromptSF>>hist1")
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
gr.SetTitle('Bias test for  non prompt normalization for t#bar{t}#gamma/t#bar{t} fitting')
gr.GetXaxis().SetTitle("Expected non prompt norm");
gr.GetYaxis().SetTitle("Measured non prompt norm");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,0.1)
gr.GetYaxis().SetRangeUser(0,0.1)
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
c1.Print("nonPrompt_closure_ele_2016.pdf") #####

ListOfFiles = [
               "higgsCombinemu_2016_nonPrompt_0.01.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_nonPrompt_0.02.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_nonPrompt_0.03.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_nonPrompt_0.04.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_nonPrompt_0.05.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_nonPrompt_0.06.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_nonPrompt_0.07.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_nonPrompt_0.08.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_nonPrompt_0.09.MultiDimFit.mH120.1234260.root",
               "higgsCombinemu_2016_nonPrompt_0.10.MultiDimFit.mH120.1234260.root",
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
	mytree.Draw("nonPromptSF>>hist1")
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
gr.SetTitle('Bias test for  non prompt normalization ')
gr.GetXaxis().SetTitle("Expected non prompt normalization values");
gr.GetYaxis().SetTitle("Measured non prompt normalization values");
gr.SetMarkerColor(2)
gr.SetMarkerStyle(7)
gr.GetXaxis().SetRangeUser(0,0.1)
gr.GetYaxis().SetRangeUser(0,0.1)
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
c1.Print("nonPrompt_closure_mu_2016.pdf")  ################################################################################################################
