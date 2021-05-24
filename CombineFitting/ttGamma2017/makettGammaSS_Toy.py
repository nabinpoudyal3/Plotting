import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2017Ele  = ["higgsCombine.TOY_ele_2017.FitDiagnostics.mH120.314159.root"]
ListOfFiles2017Mu   = ["higgsCombine.TOY_mu_2017.FitDiagnostics.mH120.314159.root"]
ListOfFiles2017Both = ["higgsCombine.TOY_both_2017.FitDiagnostics.mH120.314159.root"]

parameterDictEle={
"trackedParam_r":["ttgammaSFelseventeenToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFelseventeenToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFelseventeenToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFelseventeenToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFelseventeenToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormelseventeenToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFelseventeenToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFelseventeenToy", [100,0,2]],
}
parameterDictMu={
"trackedParam_r":["ttgammaSFmuseventeenToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFmuseventeenToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFmuseventeenToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFmuseventeenToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFmuseventeenToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormmuseventeenToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFmuseventeenToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFmuseventeenToy", [100,0,2]],
}
parameterDictBoth={
"trackedParam_r":["ttgammaSFseventeenToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFseventeenToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFseventeenToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFseventeenToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFseventeenToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormseventeenToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFseventeenToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFseventeenToy", [100,0,2]],
}


line = ""
for ifile in ListOfFiles2017Ele:
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

for ifile in ListOfFiles2017Mu:
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

for ifile in ListOfFiles2017Both:
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
with open("TTGamma_nonPrompt_2017_Toy.tex","w") as _file:
    _file.write(line)

