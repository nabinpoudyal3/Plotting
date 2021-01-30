import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2018Ele  = ["fitDiagnostics.TOY_ele_2018.root"]
ListOfFiles2018Mu   = ["fitDiagnostics.TOY_mu_2018.root"]
ListOfFiles2018Both = ["fitDiagnostics.TOY_both_2018.root"]

#parameterDictEle  = {"r":"ttgammaSFeleighteenToyRatio","nonPromptSF":"nonPromptSFeleighteenToyRatio","TTbarSF":"TTbarSFeleighteenToyRatio","WGSF":"WGSFeleighteenToyRatio","ZGSF":"ZGSFeleighteenToyRatio","OtherSF":"OtherSFeleighteenToyRatio"}#,"Other_norm":"OtherNormeleighteenToyRatio"}
#parameterDictMu   = {"r":"ttgammaSFmueighteenToyRatio","nonPromptSF":"nonPromptSFmueighteenToyRatio","TTbarSF":"TTbarSFmueighteenToyRatio","WGSF":"WGSFmueighteenToyRatio","ZGSF":"ZGSFmueighteenToyRatio","OtherSF":"OtherSFmueighteenToyRatio"}#,"Other_norm":"OtherNormmueighteenToyRatio"}
#parameterDictBoth = {"r":"ttgammaSFeighteenToyRatio","nonPromptSF":"nonPromptSFeighteenToyRatio","TTbarSF":"TTbarSFeighteenToyRatio","WGSF":"WGSFeighteenToyRatio","ZGSF":"ZGSFeighteenToyRatio","OtherSF":"OtherSFeighteenToyRatio"}#,"Other_norm":"OtherNormeighteenToyRatio"}

parameterDictEle  = {"r":"ttgammaSFeleighteenToyRatio","TTbarSF":"TTbarSFeleighteenToyRatio","WGSF":"WGSFeleighteenToyRatio","ZGSF":"ZGSFeleighteenToyRatio","OtherSF":"OtherSFeleighteenToyRatio", "Other_norm":"OtherNormeleighteenToyRatio"}
parameterDictMu   = {"r":"ttgammaSFmueighteenToyRatio","TTbarSF":"TTbarSFmueighteenToyRatio","WGSF":"WGSFmueighteenToyRatio","ZGSF":"ZGSFmueighteenToyRatio","OtherSF":"OtherSFmueighteenToyRatio", "Other_norm":"OtherNormmueighteenToyRatio"}
parameterDictBoth = {"r":"ttgammaSFeighteenToyRatio","TTbarSF":"TTbarSFeighteenToyRatio","WGSF":"WGSFeighteenToyRatio","ZGSF":"ZGSFeighteenToyRatio","OtherSF":"OtherSFeighteenToyRatio", "Other_norm":"OtherNormeighteenToyRatio"}

line = ""
for ifile in ListOfFiles2018Ele:
    myfile = ROOT.TFile(ifile,"read")
    tree_fit_sb = myfile.Get("tree_fit_sb")
    for param in parameterDictEle.keys():
    	if param == "nonPromptSF": continue
        print param
        hist = ROOT.TH1F("hist","",100,-2,2)
        tree_fit_sb.Draw("%s>>hist"%param)
        hist = ROOT.gDirectory.Get('hist')
        print "==>",hist.GetMean(), hist.GetRMS()
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        print "==>>>",fit.GetParameter(1),fit.GetParameter(2)
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictEle[param],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist
        print line

#sys.exit()


    
for ifile in ListOfFiles2018Mu:
    myfile = ROOT.TFile(ifile,"read")
    tree_fit_sb = myfile.Get("tree_fit_sb")
    for param in parameterDictMu.keys():
        print param
        hist = ROOT.TH1F("hist","",100,-2,2)
        tree_fit_sb.Draw("%s>>hist"%param)
        hist = ROOT.gDirectory.Get('hist')
        print "==>",hist.GetMean(), hist.GetRMS()
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        print "==>>>",fit.GetParameter(1),fit.GetParameter(2)
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictMu[param],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist

for ifile in ListOfFiles2018Both:
    myfile = ROOT.TFile(ifile,"read")
    tree_fit_sb = myfile.Get("tree_fit_sb")
    for param in parameterDictBoth.keys():
        print param
        hist = ROOT.TH1F("hist","",100,-2,2)
        tree_fit_sb.Draw("%s>>hist"%param)
        hist = ROOT.gDirectory.Get('hist')
        print "==>",hist.GetMean(), hist.GetRMS()
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        print "==>>>",fit.GetParameter(1),fit.GetParameter(2)
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDictBoth[param],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist

with open("TTGamma_nonPrompt_2018_ToyRatio.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2018_ToyRatio.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')
