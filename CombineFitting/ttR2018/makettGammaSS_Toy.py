import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2018Ele  = ["higgsCombine.TOY_ele_2018.FitDiagnostics.mH120.314159.root"]
ListOfFiles2018Mu   = ["higgsCombine.TOY_mu_2018.FitDiagnostics.mH120.314159.root"]
ListOfFiles2018Both = ["higgsCombine.TOY_both_2018.FitDiagnostics.mH120.314159.root"]

parameterDictEle={
"trackedParam_r":["ttgammaSFeleighteenToyRatio",             [100,0,0.1]],
"trackedParam_TTbarSF":["TTbarSFeleighteenToyRatio",         [100,700,900]],
"trackedParam_WGSF":["WGSFeleighteenToyRatio",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFeleighteenToyRatio",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFeleighteenToyRatio",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormeleighteenToyRatio",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFeleighteenToyRatio", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFeleighteenToyRatio", [100,0,2]],
}
parameterDictMu={
"trackedParam_r":["ttgammaSFmueighteenToyRatio",             [100,0,0.1]],
"trackedParam_TTbarSF":["TTbarSFmueighteenToyRatio",         [100,700,900]],
"trackedParam_WGSF":["WGSFmueighteenToyRatio",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFmueighteenToyRatio",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFmueighteenToyRatio",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormmueighteenToyRatio",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFmueighteenToyRatio", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFmueighteenToyRatio", [100,0,2]],
}
parameterDictBoth={
"trackedParam_r":["ttgammaSFeighteenToyRatio",             [100,0,0.1]],
"trackedParam_TTbarSF":["TTbarSFeighteenToyRatio",         [100,700,900]],
"trackedParam_WGSF":["WGSFeighteenToyRatio",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFeighteenToyRatio",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFeighteenToyRatio",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormeighteenToyRatio",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFeighteenToyRatio", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFeighteenToyRatio", [100,0,2]],
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
        if param == "trackedParam_r":
            line += "\\newcommand{\\%s} {\ensuremath{%.5f \\substack{+%.5f \\\\ -%.5f}}}\n"%(parameterDictEle[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        else:
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
        if param == "trackedParam_r":
            line += "\\newcommand{\\%s} {\ensuremath{%.5f \\substack{+%.5f \\\\ -%.5f}}}\n"%(parameterDictMu[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        else:
            line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictMu[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist

# for ifile in ListOfFiles2018Both:
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
with open("TTGamma_nonPrompt_2018_ToyRatio.tex","w") as _file:
    _file.write(line)


# import ROOT
# import shutil
# import sys

# ROOT.gROOT.SetBatch(True)

# ListOfFiles2018Ele  = ["fitDiagnostics.TOY_ele_2018.root"]
# ListOfFiles2018Mu   = ["fitDiagnostics.TOY_mu_2018.root"]
# ListOfFiles2018Both = ["fitDiagnostics.TOY_both_2018.root"]


# c1 = ROOT.TCanvas( 'c1', 'toy histogram', 800,800 )
# mylist = ["r","ZGSF","SingleTopSF","TTbarSF","OtherSF","WGSF","Other_norm","nonPromptSF"]
# for ifile in ListOfFiles2018Ele:
#     myfile = ROOT.TFile(ifile,"read")
#     mytree=myfile.tree_fit_sb
#     mytree.Draw("ZGSF>>hist1(50,0,2)")
#     hist1 = ROOT.gDirectory.Get('hist1')
#     hist1.Fit("gaus")
# c1.Draw()
# c1.Print("ZGSF_ele_2018.pdf") #####

# sys.exit()

# line = ""
# for ifile in ListOfFiles2018Ele:
#     myfile = ROOT.TFile(ifile,"read")
#     if myfile.GetListOfKeys().Contains("fit_s") is False:
#         print ifile[14:-10], ": Fit failed."
#         continue
#     fit_s = myfile.Get("fit_s")
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.5f \\\\ %.5f}}}\n"%("ttgammaSFeleighteenToyRatio",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFeleighteenToyRatio",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("nonPromptSF").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFeleighteenToyRatio",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFeleighteenToyRatio",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFeleighteenToyRatio",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFeleighteenToyRatio",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormeleighteenToyRatio",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

# for ifile in ListOfFiles2018Mu:
#     myfile = ROOT.TFile(ifile,"read")
#     if myfile.GetListOfKeys().Contains("fit_s") is False:
#         print ifile[14:-10], ": Fit failed."
#         continue
#     fit_s = myfile.Get("fit_s")
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.5f \\\\ %.5f}}}\n"%("ttgammaSFmueighteenToyRatio",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFmueighteenToyRatio",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFmueighteenToyRatio",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFmueighteenToyRatio",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFmueighteenToyRatio",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFmueighteenToyRatio",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormmueighteenToyRatio",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

# for ifile in ListOfFiles2018Both:
#     myfile = ROOT.TFile(ifile,"read")
#     if myfile.GetListOfKeys().Contains("fit_s") is False:
#         print ifile[14:-10], ": Fit failed."
#         continue
#     fit_s = myfile.Get("fit_s")
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.5f \\\\ %.5f}}}\n"%("ttgammaSFeighteenToyRatio",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFeighteenToyRatio",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFeighteenToyRatio",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFeighteenToyRatio",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFeighteenToyRatio",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFeighteenToyRatio",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormeighteenToyRatio",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

# print line
# with open("TTGamma_nonPrompt_2018_ToyRatio.tex","w") as _file:
#     _file.write(line)




