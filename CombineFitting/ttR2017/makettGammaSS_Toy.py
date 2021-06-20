import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2017Ele  = ["higgsCombine.TOY_ele_2017.FitDiagnostics.mH120.314159.root"]
ListOfFiles2017Mu   = ["higgsCombine.TOY_mu_2017.FitDiagnostics.mH120.314159.root"]
ListOfFiles2017Both = ["higgsCombine.TOY_both_2017.FitDiagnostics.mH120.314159.root"]

parameterDictEle={
"trackedParam_r":["ttgammaSFelseventeenToyRatio",             [100,0,0.1]],
"trackedParam_TTbarSF":["TTbarSFelseventeenToyRatio",         [100,700,900]],
"trackedParam_WGSF":["WGSFelseventeenToyRatio",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFelseventeenToyRatio",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFelseventeenToyRatio",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormelseventeenToyRatio",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFelseventeenToyRatio", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFelseventeenToyRatio", [100,0,2]],
}
parameterDictMu={
"trackedParam_r":["ttgammaSFmuseventeenToyRatio",             [100,0,0.1]],
"trackedParam_TTbarSF":["TTbarSFmuseventeenToyRatio",         [100,700,900]],
"trackedParam_WGSF":["WGSFmuseventeenToyRatio",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFmuseventeenToyRatio",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFmuseventeenToyRatio",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormmuseventeenToyRatio",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFmuseventeenToyRatio", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFmuseventeenToyRatio", [100,0,2]],
}
parameterDictBoth={
"trackedParam_r":["ttgammaSFseventeenToyRatio",             [100,0,0.1]],
"trackedParam_TTbarSF":["TTbarSFseventeenToyRatio",         [100,700,900]],
"trackedParam_WGSF":["WGSFseventeenToyRatio",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFseventeenToyRatio",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFseventeenToyRatio",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormseventeenToyRatio",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFseventeenToyRatio", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFseventeenToyRatio", [100,0,2]],
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
        if param == "trackedParam_r":
            line += "\\newcommand{\\%s} {\ensuremath{%.5f \\substack{+%.5f \\\\ -%.5f}}}\n"%(parameterDictEle[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        else:
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
        if param == "trackedParam_r":
            line += "\\newcommand{\\%s} {\ensuremath{%.5f \\substack{+%.5f \\\\ -%.5f}}}\n"%(parameterDictMu[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        else:
            line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictMu[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist

# for ifile in ListOfFiles2017Both:
#     myfile = ROOT.TFile(ifile,"read")
#     limit = myfile.Get("limit")
#     for param in parameterDictBoth.keys():
#         hist = ROOT.TH1F("hist","",parameterDictBoth[param][1][0],parameterDictBoth[param][1][1],parameterDictBoth[param][1][2])
#         limit.Draw("%s>>hist"%(param))
#         hist = ROOT.gDirectory.Get('hist')
#         hist.Fit("gaus")
#         fit = hist.GetFunction("gaus")
#         if param == "trackedParam_r":
#             line += "\\newcommand{\\%s} {\ensuremath{%.5f \\substack{+%.5f \\\\ -%.5f}}}\n"%(parameterDictBoth[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
#         else:
#             line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictBoth[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
#         del hist


print line
with open("TTGamma_nonPrompt_2017_ToyRatio.tex","w") as _file:
    _file.write(line)

