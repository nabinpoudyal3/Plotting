import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2016Ele  = ["fitDiagnostics.TOY_ele_2016.root"]
ListOfFiles2016Mu   = ["fitDiagnostics.TOY_mu_2016.root"]
ListOfFiles2016Both = ["fitDiagnostics.TOY_both_2016.root"]

parameterDict2016Ele   =     {"r":"ttgammaSFelsixteenToy",
    "nonPromptSF":"nonPromptSFelsixteenToy",
    "TTbarSF":"TTbarSFelsixteenToy",
    "WGSF":"WGSFelsixteenToy",
    "ZGSF":"ZGSFelsixteenToy",
    "OtherSF":"OtherSFelsixteenToy",
    "Other_norm":"OtherNormelsixteenToy"}

parameterDict2016Mu    =     {"r":"ttgammaSFmusixteenToy",
    "nonPromptSF":"nonPromptSFmusixteenToy",
    "TTbarSF":"TTbarSFmusixteenToy",
    "WGSF":"WGSFmusixteenToy",
    "ZGSF":"ZGSFmusixteenToy",
    "OtherSF":"OtherSFmusixteenToy",
    "Other_norm":"OtherNormmusixteenToy"}

parameterDict2016Both  =     {"r":"ttgammaSFsixteenToy",
    "nonPromptSF":"nonPromptSFsixteenToy",
    "TTbarSF":"TTbarSFsixteenToy",
    "WGSF":"WGSFsixteenToy",
    "ZGSF":"ZGSFsixteenToy",
    "OtherSF":"OtherSFsixteenToy",
    "Other_norm":"OtherNormsixteenToy"}



line = ""
for ifile in ListOfFiles2016Ele:
    myfile = ROOT.TFile(ifile,"read")
    tree_fit_sb = myfile.Get("tree_fit_sb")
    for param in parameterDict2016Ele.keys():
        if param == "nonPromptSF": continue
        print param
        hist = ROOT.TH1F("hist","",100,-2,2)
        tree_fit_sb.Draw("%s>>hist"%param)
        hist = ROOT.gDirectory.Get('hist')
        print "==>",hist.GetMean(), hist.GetRMS()
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        print "==>>>",fit.GetParameter(1),fit.GetParameter(2)
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDict2016Ele[param],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist
        print line


for ifile in ListOfFiles2016Mu:
    myfile = ROOT.TFile(ifile,"read")
    tree_fit_sb = myfile.Get("tree_fit_sb")
    for param in parameterDict2016Mu.keys():
        if param == "nonPromptSF": continue
        print param
        hist = ROOT.TH1F("hist","",100,-2,2)
        tree_fit_sb.Draw("%s>>hist"%param)
        hist = ROOT.gDirectory.Get('hist')
        print "==>",hist.GetMean(), hist.GetRMS()
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        print "==>>>",fit.GetParameter(1),fit.GetParameter(2)
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDict2016Mu[param],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist
        print line

for ifile in ListOfFiles2016Both:
    myfile = ROOT.TFile(ifile,"read")
    tree_fit_sb = myfile.Get("tree_fit_sb")
    for param in parameterDict2016Both.keys():
        if param == "nonPromptSF": continue
        print param
        hist = ROOT.TH1F("hist","",100,-2,2)
        tree_fit_sb.Draw("%s>>hist"%param)
        hist = ROOT.gDirectory.Get('hist')
        print "==>",hist.GetMean(), hist.GetRMS()
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        print "==>>>",fit.GetParameter(1),fit.GetParameter(2)
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDict2016Both[param],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist
        print line        



print line
with open("TTGamma_nonPrompt_2016_Toy.tex","w") as _file:
    _file.write(line)


