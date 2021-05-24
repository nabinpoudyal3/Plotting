import ROOT
from array import array
import sys

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
   
# gStyle->SetPalette(num)
f1 = ROOT.TFile.Open('fitDiagnosticsele_2017.root','read')

h_signal = f1.Get("shapes_fit_s/overall_total_covar")
print h_signal
h_signal.GetYaxis().SetLabelSize(0.03)
h_signal.GetXaxis().SetLabelSize(0.03)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")
h_signal.SetContour(10000)
h_signal.Draw('colz, Y-')
h_signal.GetXaxis().SetTitle("")
h_signal.GetYaxis().SetTitle("")
canvas.Modified();
canvas.Update();
mypal = h_signal.GetListOfFunctions().FindObject("palette")
mypal.SetX1NDC(0.86);
mypal.SetY1NDC(0.15);
mypal.SetX2NDC(0.91);
mypal.SetY2NDC(0.85);

#ROOT.gApplication.Run()

canvas.SaveAs('totalCovariance_ttgamma_data_ele_2017.pdf') #########################################################


f1 = ROOT.TFile.Open('fitDiagnosticsmu_2017.root','read')

h_signal = f1.Get("shapes_fit_s/overall_total_covar")
print h_signal
h_signal.GetYaxis().SetLabelSize(0.03)
h_signal.GetXaxis().SetLabelSize(0.03)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")
h_signal.SetContour(10000)
h_signal.Draw('colz, Y-')
h_signal.GetXaxis().SetTitle("")
h_signal.GetYaxis().SetTitle("")
canvas.Modified();
canvas.Update();
mypal = h_signal.GetListOfFunctions().FindObject("palette")
mypal.SetX1NDC(0.86);
mypal.SetY1NDC(0.15);
mypal.SetX2NDC(0.91);
mypal.SetY2NDC(0.85);
   
#ROOT.gApplication.Run()

canvas.SaveAs('totalCovariance_ttgamma_data_mu_2017.pdf') #####################################################################


f1 = ROOT.TFile.Open('fitDiagnosticsboth_2017.root','read')

h_signal = f1.Get("shapes_fit_s/overall_total_covar")
print h_signal
h_signal.GetYaxis().SetLabelSize(0.03)
h_signal.GetXaxis().SetLabelSize(0.03)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")
h_signal.SetContour(10000)
h_signal.Draw('colz, Y-')
h_signal.GetXaxis().SetTitle("")
h_signal.GetYaxis().SetTitle("")
canvas.Modified();
canvas.Update();
mypal = h_signal.GetListOfFunctions().FindObject("palette")
mypal.SetX1NDC(0.86);
mypal.SetY1NDC(0.15);
mypal.SetX2NDC(0.91);
mypal.SetY2NDC(0.85);
#ROOT.gApplication.Run()

canvas.SaveAs('totalCovariance_ttgamma_data_both_2017.pdf') #####################################################################


f1 = ROOT.TFile.Open('fitDiagnostics.TOY_ele_2017.root','read')

h_signal = f1.Get("shapes_fit_s/overall_total_covar")
print h_signal
h_signal.GetYaxis().SetLabelSize(0.03)
h_signal.GetXaxis().SetLabelSize(0.03)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")
h_signal.SetContour(10000)
h_signal.Draw('colz, Y-')
h_signal.GetXaxis().SetTitle("")
h_signal.GetYaxis().SetTitle("")
canvas.Modified();
canvas.Update();
mypal = h_signal.GetListOfFunctions().FindObject("palette")
mypal.SetX1NDC(0.86);
mypal.SetY1NDC(0.15);
mypal.SetX2NDC(0.91);
mypal.SetY2NDC(0.85);
   
#ROOT.gApplication.Run()

canvas.SaveAs('totalCovariance_ttgamma_toy_ele_2017.pdf') #########################################################
f1 = ROOT.TFile.Open('fitDiagnostics.TOY_mu_2017.root','read')

h_signal = f1.Get("shapes_fit_s/overall_total_covar")
print h_signal
h_signal.GetYaxis().SetLabelSize(0.03)
h_signal.GetXaxis().SetLabelSize(0.03)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")
h_signal.SetContour(10000)
h_signal.Draw('colz, Y-')
h_signal.GetXaxis().SetTitle("")
h_signal.GetYaxis().SetTitle("")
canvas.Modified();
canvas.Update();
mypal = h_signal.GetListOfFunctions().FindObject("palette")
mypal.SetX1NDC(0.86);
mypal.SetY1NDC(0.15);
mypal.SetX2NDC(0.91);
mypal.SetY2NDC(0.85);
#ROOT.gApplication.Run()

canvas.SaveAs('totalCovariance_ttgamma_toy_mu_2017.pdf') #####################################################################


f1 = ROOT.TFile.Open('fitDiagnostics.TOY_both_2017.root','read')

h_signal = f1.Get("shapes_fit_s/overall_total_covar")
print h_signal
h_signal.GetYaxis().SetLabelSize(0.03)
h_signal.GetXaxis().SetLabelSize(0.03)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")
h_signal.SetContour(10000)
h_signal.Draw('colz, Y-')
h_signal.GetXaxis().SetTitle("")
h_signal.GetYaxis().SetTitle("")
canvas.Modified();
canvas.Update();
mypal = h_signal.GetListOfFunctions().FindObject("palette")
mypal.SetX1NDC(0.86);
mypal.SetY1NDC(0.15);
mypal.SetX2NDC(0.91);
mypal.SetY2NDC(0.85);
   
#ROOT.gApplication.Run()

canvas.SaveAs('totalCovariance_ttgamma_toy_both_2017.pdf') #####################################################################


############

f1 = ROOT.TFile.Open('fitDiagnostics.Asimov_ele_2017.root','read')

h_signal = f1.Get("shapes_fit_s/overall_total_covar")
print h_signal
h_signal.GetYaxis().SetLabelSize(0.03)
h_signal.GetXaxis().SetLabelSize(0.03)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")
h_signal.SetContour(10000)
h_signal.Draw('colz, Y-')
h_signal.GetXaxis().SetTitle("")
h_signal.GetYaxis().SetTitle("")
canvas.Modified();
canvas.Update();
mypal = h_signal.GetListOfFunctions().FindObject("palette")
mypal.SetX1NDC(0.86);
mypal.SetY1NDC(0.15);
mypal.SetX2NDC(0.91);
mypal.SetY2NDC(0.85);
#ROOT.gApplication.Run()

canvas.SaveAs('totalCovariance_ttgamma_Asimov_ele_2017.pdf') #########################################################
f1 = ROOT.TFile.Open('fitDiagnostics.Asimov_mu_2017.root','read')

h_signal = f1.Get("shapes_fit_s/overall_total_covar")
print h_signal
h_signal.GetYaxis().SetLabelSize(0.03)
h_signal.GetXaxis().SetLabelSize(0.03)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")
h_signal.SetContour(10000)
h_signal.Draw('colz, Y-')
h_signal.GetXaxis().SetTitle("")
h_signal.GetYaxis().SetTitle("")
canvas.Modified();
canvas.Update();
mypal = h_signal.GetListOfFunctions().FindObject("palette")
mypal.SetX1NDC(0.86);
mypal.SetY1NDC(0.15);
mypal.SetX2NDC(0.91);
mypal.SetY2NDC(0.85);
   
#ROOT.gApplication.Run()

canvas.SaveAs('totalCovariance_ttgamma_Asimov_mu_2017.pdf') #####################################################################


f1 = ROOT.TFile.Open('fitDiagnostics.Asimov_both_2017.root','read')

h_signal = f1.Get("shapes_fit_s/overall_total_covar")
print h_signal
h_signal.GetYaxis().SetLabelSize(0.03)
h_signal.GetXaxis().SetLabelSize(0.03)
h_signal.GetZaxis().SetLabelSize(0.03)
h_signal.SetMarkerSize(0.7)
h_signal.LabelsOption("v", "X")
h_signal.SetContour(10000)
h_signal.Draw('colz, Y-')
h_signal.GetXaxis().SetTitle("")
h_signal.GetYaxis().SetTitle("")
canvas.Modified();
canvas.Update();
mypal = h_signal.GetListOfFunctions().FindObject("palette")
mypal.SetX1NDC(0.86);
mypal.SetY1NDC(0.15);
mypal.SetX2NDC(0.91);
mypal.SetY2NDC(0.85);
   
#ROOT.gApplication.Run()

canvas.SaveAs('totalCovariance_ttgamma_Asimov_both_2017.pdf') #####################################################################




print "exiting after 2017 plots only."
sys.exit()

