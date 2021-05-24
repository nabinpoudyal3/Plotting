import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2016Ele  = ["higgsCombine.TOY_ele_2016.FitDiagnostics.mH120.314159.root"]
ListOfFiles2016Mu   = ["higgsCombine.TOY_mu_2016.FitDiagnostics.mH120.314159.root"]
ListOfFiles2016Both = ["higgsCombine.TOY_both_2016.FitDiagnostics.mH120.314159.root"]

parameterDictEle={
"trackedParam_r":["ttgammaSFelsixteenToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFelsixteenToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFelsixteenToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFelsixteenToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFelsixteenToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormelsixteenToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFelsixteenToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFelsixteenToy", [100,0,2]],
}
parameterDictMu={
"trackedParam_r":["ttgammaSFmusixteenToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFmusixteenToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFmusixteenToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFmusixteenToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFmusixteenToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormmusixteenToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFmusixteenToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFmusixteenToy", [100,0,2]],
}
parameterDictBoth={
"trackedParam_r":["ttgammaSFsixteenToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFsixteenToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFsixteenToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFsixteenToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFsixteenToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormsixteenToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFsixteenToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFsixteenToy", [100,0,2]],
}


line = ""
for ifile in ListOfFiles2016Ele:
    myfile = ROOT.TFile(ifile,"read")
    limit = myfile.Get("limit")
    for param in parameterDictEle.keys():
        hist = ROOT.TH1F("hist","",parameterDictEle[param][1][0],parameterDictEle[param][1][1],parameterDictEle[param][1][2])
        limit.Draw("%s>>hist"%(param))
        hist = ROOT.gDirectory.Get('hist')
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictEle[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist

for ifile in ListOfFiles2016Mu:
    myfile = ROOT.TFile(ifile,"read")
    limit = myfile.Get("limit")
    for param in parameterDictMu.keys():
        hist = ROOT.TH1F("hist","",parameterDictMu[param][1][0],parameterDictMu[param][1][1],parameterDictMu[param][1][2])
        limit.Draw("%s>>hist"%(param))
        hist = ROOT.gDirectory.Get('hist')
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictMu[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist

for ifile in ListOfFiles2016Both:
    myfile = ROOT.TFile(ifile,"read")
    limit = myfile.Get("limit")
    for param in parameterDictBoth.keys():
        hist = ROOT.TH1F("hist","",parameterDictBoth[param][1][0],parameterDictBoth[param][1][1],parameterDictBoth[param][1][2])
        limit.Draw("%s>>hist"%(param))
        hist = ROOT.gDirectory.Get('hist')
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictBoth[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist


print line
with open("TTGamma_nonPrompt_2016_Toy.tex","w") as _file:
    _file.write(line)

