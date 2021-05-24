import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2018Ele  = ["higgsCombine.TOY_ele_2018.FitDiagnostics.mH120.314159.root"]
ListOfFiles2018Mu   = ["higgsCombine.TOY_mu_2018.FitDiagnostics.mH120.314159.root"]
ListOfFiles2018Both = ["higgsCombine.TOY_both_2018.FitDiagnostics.mH120.314159.root"]

parameterDictEle={
"trackedParam_r":["ttgammaSFeleighteenToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFeleighteenToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFeleighteenToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFeleighteenToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFeleighteenToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormeleighteenToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFeleighteenToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFeleighteenToy", [100,0,2]],
}
parameterDictMu={
"trackedParam_r":["ttgammaSFmueighteenToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFmueighteenToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFmueighteenToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFmueighteenToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFmueighteenToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormmueighteenToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFmueighteenToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFmueighteenToy", [100,0,2]],
}
parameterDictBoth={
"trackedParam_r":["ttgammaSFeighteenToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFeighteenToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFeighteenToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFeighteenToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFeighteenToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormeighteenToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFeighteenToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFeighteenToy", [100,0,2]],
}


line = ""
for ifile in ListOfFiles2018Ele:
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

for ifile in ListOfFiles2018Mu:
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

for ifile in ListOfFiles2018Both:
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
with open("TTGamma_nonPrompt_2018_Toy.tex","w") as _file:
    _file.write(line)

