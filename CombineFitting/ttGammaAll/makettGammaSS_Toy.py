import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFilesEle  = ["higgsCombine.TOY_ele.FitDiagnostics.mH120.314159.root"]
ListOfFilesMu   = ["higgsCombine.TOY_mu.FitDiagnostics.mH120.314159.root"]
ListOfFilesBoth = ["higgsCombine.TOY_both.FitDiagnostics.mH120.314159.root"]

parameterDictEle={
"trackedParam_r":["ttgammaSFelFullToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFelFullToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFelFullToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFelFullToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFelFullToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormelFullToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFelFullToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFelFullToy", [100,0,2]],
}
parameterDictMu={
"trackedParam_r":["ttgammaSFmuFullToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFmuFullToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFmuFullToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFmuFullToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFmuFullToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormmuFullToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFmuFullToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFmuFullToy", [100,0,2]],
}
parameterDictBoth={
"trackedParam_r":["ttgammaSFFullToy",             [100,0,2]],
"trackedParam_TTbarSF":["TTbarSFFullToy",         [100,0,2]],
"trackedParam_WGSF":["WGSFFullToy",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFFullToy",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFFullToy",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormFullToy",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFFullToy", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFFullToy", [100,0,2]],
}


line = ""
for ifile in ListOfFilesEle:
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

for ifile in ListOfFilesMu:
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

for ifile in ListOfFilesBoth:
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
with open("TTGamma_nonPrompt_Full_Toy.tex","w") as _file:
    _file.write(line)

