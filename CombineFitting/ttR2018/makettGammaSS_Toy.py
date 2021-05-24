import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2016Ele  = ["higgsCombine.TOY_ele_2016.FitDiagnostics.mH120.314159.root"]
ListOfFiles2016Mu   = ["higgsCombine.TOY_mu_2016.FitDiagnostics.mH120.314159.root"]
ListOfFiles2016Both = ["higgsCombine.TOY_both_2016.FitDiagnostics.mH120.314159.root"]

parameterDictEle={
"trackedParam_r":["ttgammaSFelsixteenToyRatio",             [100,0,0.1]],
"trackedParam_TTbarSF":["TTbarSFelsixteenToyRatio",         [100,700,900]],
"trackedParam_WGSF":["WGSFelsixteenToyRatio",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFelsixteenToyRatio",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFelsixteenToyRatio",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormelsixteenToyRatio",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFelsixteenToyRatio", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFelsixteenToyRatio", [100,0,2]],
}
parameterDictMu={
"trackedParam_r":["ttgammaSFmusixteenToyRatio",             [100,0,0.1]],
"trackedParam_TTbarSF":["TTbarSFmusixteenToyRatio",         [100,700,900]],
"trackedParam_WGSF":["WGSFmusixteenToyRatio",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFmusixteenToyRatio",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFmusixteenToyRatio",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormmusixteenToyRatio",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFmusixteenToyRatio", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFmusixteenToyRatio", [100,0,2]],
}
parameterDictBoth={
"trackedParam_r":["ttgammaSFsixteenToyRatio",             [100,0,0.1]],
"trackedParam_TTbarSF":["TTbarSFsixteenToyRatio",         [100,700,900]],
"trackedParam_WGSF":["WGSFsixteenToyRatio",               [100,0,2]],
"trackedParam_ZGSF":["ZGSFsixteenToyRatio",               [100,0,2]],
"trackedParam_OtherSF":["OtherSFsixteenToyRatio",         [100,0,2]],
"trackedParam_Other_norm":["OtherNormsixteenToyRatio",    [100,0,2]],
"trackedParam_SingleTopSF":["SingleTopSFsixteenToyRatio", [100,0,2]],
"trackedParam_nonPromptSF":["nonPromptSFsixteenToyRatio", [100,0,2]],
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
        if param == "trackedParam_r":
            line += "\\newcommand{\\%s} {\ensuremath{%.5f \\substack{+%.5f \\\\ -%.5f}}}\n"%(parameterDictEle[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        else:
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
        if param == "trackedParam_r":
            line += "\\newcommand{\\%s} {\ensuremath{%.5f \\substack{+%.5f \\\\ -%.5f}}}\n"%(parameterDictMu[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        else:
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
        if param == "trackedParam_r":
            line += "\\newcommand{\\%s} {\ensuremath{%.5f \\substack{+%.5f \\\\ -%.5f}}}\n"%(parameterDictBoth[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        else:
            line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictBoth[param][0],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist


print line
with open("TTGamma_nonPrompt_2016_ToyRatio.tex","w") as _file:
    _file.write(line)


# import ROOT
# import shutil
# import sys

# ROOT.gROOT.SetBatch(True)

# ListOfFiles2016Ele  = ["fitDiagnostics.TOY_ele_2016.root"]
# ListOfFiles2016Mu   = ["fitDiagnostics.TOY_mu_2016.root"]
# ListOfFiles2016Both = ["fitDiagnostics.TOY_both_2016.root"]


# c1 = ROOT.TCanvas( 'c1', 'toy histogram', 800,800 )
# mylist = ["r","ZGSF","SingleTopSF","TTbarSF","OtherSF","WGSF","Other_norm","nonPromptSF"]
# for ifile in ListOfFiles2016Ele:
#     myfile = ROOT.TFile(ifile,"read")
#     mytree=myfile.tree_fit_sb
#     mytree.Draw("ZGSF>>hist1(50,0,2)")
#     hist1 = ROOT.gDirectory.Get('hist1')
#     hist1.Fit("gaus")
# c1.Draw()
# c1.Print("ZGSF_ele_2016.pdf") #####

# sys.exit()

# line = ""
# for ifile in ListOfFiles2016Ele:
#     myfile = ROOT.TFile(ifile,"read")
#     if myfile.GetListOfKeys().Contains("fit_s") is False:
#         print ifile[14:-10], ": Fit failed."
#         continue
#     fit_s = myfile.Get("fit_s")
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.5f \\\\ %.5f}}}\n"%("ttgammaSFelsixteenToyRatio",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFelsixteenToyRatio",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("nonPromptSF").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFelsixteenToyRatio",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFelsixteenToyRatio",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFelsixteenToyRatio",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFelsixteenToyRatio",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormelsixteenToyRatio",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

# for ifile in ListOfFiles2016Mu:
#     myfile = ROOT.TFile(ifile,"read")
#     if myfile.GetListOfKeys().Contains("fit_s") is False:
#         print ifile[14:-10], ": Fit failed."
#         continue
#     fit_s = myfile.Get("fit_s")
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.5f \\\\ %.5f}}}\n"%("ttgammaSFmusixteenToyRatio",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFmusixteenToyRatio",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFmusixteenToyRatio",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFmusixteenToyRatio",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFmusixteenToyRatio",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFmusixteenToyRatio",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormmusixteenToyRatio",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

# for ifile in ListOfFiles2016Both:
#     myfile = ROOT.TFile(ifile,"read")
#     if myfile.GetListOfKeys().Contains("fit_s") is False:
#         print ifile[14:-10], ": Fit failed."
#         continue
#     fit_s = myfile.Get("fit_s")
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.5f \\\\ %.5f}}}\n"%("ttgammaSFsixteenToyRatio",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFsixteenToyRatio",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFsixteenToyRatio",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFsixteenToyRatio",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFsixteenToyRatio",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFsixteenToyRatio",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
#     line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormsixteenToyRatio",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

# print line
# with open("TTGamma_nonPrompt_2016_ToyRatio.tex","w") as _file:
#     _file.write(line)




