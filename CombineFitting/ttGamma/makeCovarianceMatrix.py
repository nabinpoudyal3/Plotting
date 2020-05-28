import ROOT
from array import array

ROOT.gROOT.SetBatch(True)

Red    = [ 1.00, 0.00, 0.00, 0.87, 1.00, 0.51 ]
Green  = [ 1.00, 0.00, 0.81, 1.00, 0.20, 0.00 ]
Blue   = [ 1.00, 0.51, 1.00, 0.12, 0.00, 0.00 ]
Length = [ 0.00, 0.02, 0.34, 0.51, 0.64, 1.00 ]

lengthArray = array('d', Length)
redArray = array('d', Red)
greenArray = array('d', Green)
blueArray = array('d', Blue)

ROOT.TColor.CreateGradientColorTable(6,lengthArray,redArray,greenArray,blueArray,99)

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat('5.1f');

canvas = ROOT.TCanvas()
canvas.SetFillColor(10);
canvas.SetBorderMode(0);
canvas.SetBorderSize(0);
canvas.SetTickx();
canvas.SetTicky();
canvas.SetLeftMargin(0.15);
canvas.SetRightMargin(0.15);
canvas.SetTopMargin(0.15);
canvas.SetBottomMargin(0.15);
canvas.SetFrameFillColor(0);
canvas.SetFrameBorderMode(0);
   
   
f1 = ROOT.TFile.Open('fitDiagnosticsel_2016.root','read')
h_background = f1.Get('covariance_fit_b')
h_signal = f1.Get('covariance_fit_s')

h_signal.GetYaxis().SetLabelSize(0.02)
h_signal.GetXaxis().SetLabelSize(0.02)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")


h_signal.SetContour(99)
h_signal.Draw('colz, Y+, TEXT0')

mypal = h_signal.GetListOfFunctions().FindObject('palette')
print mypal
mypal.SetX1NDC(0.02);
mypal.SetX2NDC(0.06);
mypal.SetY1NDC(0.1);
mypal.SetY2NDC(0.9);
canvas.Modified();
canvas.Update();
   
#ROOT.gApplication.Run()

canvas.SaveAs('covariance_ttgamma_ele_2016.pdf') #########################################################
f1 = ROOT.TFile.Open('fitDiagnosticsmu_2016.root','read')
h_background = f1.Get('covariance_fit_b')
h_signal = f1.Get('covariance_fit_s')

h_signal.GetYaxis().SetLabelSize(0.02)
h_signal.GetXaxis().SetLabelSize(0.02)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")


h_signal.SetContour(99)
h_signal.Draw('colz, Y+, TEXT0')

mypal = h_signal.GetListOfFunctions().FindObject('palette')
mypal.SetX1NDC(0.02);
mypal.SetX2NDC(0.06);
mypal.SetY1NDC(0.1);
mypal.SetY2NDC(0.9);
canvas.Modified();
canvas.Update();
   
#ROOT.gApplication.Run()

canvas.SaveAs('covariance_ttgamma_mu_2016.pdf') #####################################################################

   
f1 = ROOT.TFile.Open('fitDiagnosticsel_2017.root','read')
h_background = f1.Get('covariance_fit_b')
h_signal = f1.Get('covariance_fit_s')

h_signal.GetYaxis().SetLabelSize(0.02)
h_signal.GetXaxis().SetLabelSize(0.02)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")


h_signal.SetContour(99)
h_signal.Draw('colz, Y+, TEXT0')

mypal = h_signal.GetListOfFunctions().FindObject('palette')
mypal.SetX1NDC(0.02);
mypal.SetX2NDC(0.06);
mypal.SetY1NDC(0.1);
mypal.SetY2NDC(0.9);
canvas.Modified();
canvas.Update();
   
#ROOT.gApplication.Run()

canvas.SaveAs('covariance_ttgamma_ele_2017.pdf') #########################################################
f1 = ROOT.TFile.Open('fitDiagnosticsmu_2017.root','read')
h_background = f1.Get('covariance_fit_b')
h_signal = f1.Get('covariance_fit_s')

h_signal.GetYaxis().SetLabelSize(0.02)
h_signal.GetXaxis().SetLabelSize(0.02)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")


h_signal.SetContour(99)
h_signal.Draw('colz, Y+, TEXT0')

mypal = h_signal.GetListOfFunctions().FindObject('palette')
mypal.SetX1NDC(0.02);
mypal.SetX2NDC(0.06);
mypal.SetY1NDC(0.1);
mypal.SetY2NDC(0.9);
canvas.Modified();
canvas.Update();
   
#ROOT.gApplication.Run()

canvas.SaveAs('covariance_ttgamma_mu_2017.pdf') #####################################################################

   
f1 = ROOT.TFile.Open('fitDiagnosticsel_2018.root','read')
h_background = f1.Get('covariance_fit_b')
h_signal = f1.Get('covariance_fit_s')

h_signal.GetYaxis().SetLabelSize(0.02)
h_signal.GetXaxis().SetLabelSize(0.02)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")


h_signal.SetContour(99)
h_signal.Draw('colz, Y+, TEXT0')

mypal = h_signal.GetListOfFunctions().FindObject('palette')
mypal.SetX1NDC(0.02);
mypal.SetX2NDC(0.06);
mypal.SetY1NDC(0.1);
mypal.SetY2NDC(0.9);
canvas.Modified();
canvas.Update();
   
#ROOT.gApplication.Run()

canvas.SaveAs('covariance_ttgamma_ele_2018.pdf') #########################################################

f1 = ROOT.TFile.Open('fitDiagnosticsmu_2018.root','read')
h_background = f1.Get('covariance_fit_b')
h_signal = f1.Get('covariance_fit_s')

h_signal.GetYaxis().SetLabelSize(0.02)
h_signal.GetXaxis().SetLabelSize(0.02)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")


h_signal.SetContour(99)
h_signal.Draw('colz, Y+, TEXT0')

mypal = h_signal.GetListOfFunctions().FindObject('palette')
mypal.SetX1NDC(0.02);
mypal.SetX2NDC(0.06);
mypal.SetY1NDC(0.1);
mypal.SetY2NDC(0.9);
canvas.Modified();
canvas.Update();
   
#ROOT.gApplication.Run()

canvas.SaveAs('covariance_ttgamma_mu_2018.pdf') #####################################################################

