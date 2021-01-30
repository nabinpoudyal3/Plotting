import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2017Ele  = ["fitDiagnostics.TOY_ele_2017.root"]
ListOfFiles2017Mu   = ["fitDiagnostics.TOY_mu_2017.root"]
ListOfFiles2017Both = ["fitDiagnostics.TOY_both_2017.root"]

#parameterDictEle  = {"r":"ttgammaSFelseventeenToyRatio","nonPromptSF":"nonPromptSFelseventeenToyRatio","TTbarSF":"TTbarSFelseventeenToyRatio","WGSF":"WGSFelseventeenToyRatio","ZGSF":"ZGSFelseventeenToyRatio","OtherSF":"OtherSFelseventeenToyRatio"}#,"Other_norm":"OtherNormelseventeenToyRatio"}
#parameterDictMu   = {"r":"ttgammaSFmuseventeenToyRatio","nonPromptSF":"nonPromptSFmuseventeenToyRatio","TTbarSF":"TTbarSFmuseventeenToyRatio","WGSF":"WGSFmuseventeenToyRatio","ZGSF":"ZGSFmuseventeenToyRatio","OtherSF":"OtherSFmuseventeenToyRatio"}#,"Other_norm":"OtherNormmuseventeenToyRatio"}
#parameterDictBoth = {"r":"ttgammaSFseventeenToyRatio","nonPromptSF":"nonPromptSFseventeenToyRatio","TTbarSF":"TTbarSFseventeenToyRatio","WGSF":"WGSFseventeenToyRatio","ZGSF":"ZGSFseventeenToyRatio","OtherSF":"OtherSFseventeenToyRatio"}#,"Other_norm":"OtherNormseventeenToyRatio"}

parameterDictEle  = {"r":"ttgammaSFelseventeenToyRatio","TTbarSF":"TTbarSFelseventeenToyRatio","WGSF":"WGSFelseventeenToyRatio","ZGSF":"ZGSFelseventeenToyRatio","OtherSF":"OtherSFelseventeenToyRatio", "Other_norm":"OtherNormelseventeenToyRatio"}
parameterDictMu   = {"r":"ttgammaSFmuseventeenToyRatio","TTbarSF":"TTbarSFmuseventeenToyRatio","WGSF":"WGSFmuseventeenToyRatio","ZGSF":"ZGSFmuseventeenToyRatio","OtherSF":"OtherSFmuseventeenToyRatio", "Other_norm":"OtherNormmuseventeenToyRatio"}
parameterDictBoth = {"r":"ttgammaSFseventeenToyRatio","TTbarSF":"TTbarSFseventeenToyRatio","WGSF":"WGSFseventeenToyRatio","ZGSF":"ZGSFseventeenToyRatio","OtherSF":"OtherSFseventeenToyRatio", "Other_norm":"OtherNormseventeenToyRatio"}

line = ""
for ifile in ListOfFiles2017Ele:
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


    
for ifile in ListOfFiles2017Mu:
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

for ifile in ListOfFiles2017Both:
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

with open("TTGamma_nonPrompt_2017_ToyRatio.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2017_ToyRatio.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')
