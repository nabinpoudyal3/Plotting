import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2016Ele  = ["fitDiagnostics.TOY_ele_2016.root"]
ListOfFiles2016Mu   = ["fitDiagnostics.TOY_mu_2016.root"]
ListOfFiles2016Both = ["fitDiagnostics.TOY_both_2016.root"]

#parameterDictEle  = {"r":"ttgammaSFelsixteenToyRatio","nonPromptSF":"nonPromptSFelsixteenToyRatio","TTbarSF":"TTbarSFelsixteenToyRatio","WGSF":"WGSFelsixteenToyRatio","ZGSF":"ZGSFelsixteenToyRatio","OtherSF":"OtherSFelsixteenToyRatio"}#,"Other_norm":"OtherNormelsixteenToyRatio"}
#parameterDictMu   = {"r":"ttgammaSFmusixteenToyRatio","nonPromptSF":"nonPromptSFmusixteenToyRatio","TTbarSF":"TTbarSFmusixteenToyRatio","WGSF":"WGSFmusixteenToyRatio","ZGSF":"ZGSFmusixteenToyRatio","OtherSF":"OtherSFmusixteenToyRatio"}#,"Other_norm":"OtherNormmusixteenToyRatio"}
#parameterDictBoth = {"r":"ttgammaSFsixteenToyRatio","nonPromptSF":"nonPromptSFsixteenToyRatio","TTbarSF":"TTbarSFsixteenToyRatio","WGSF":"WGSFsixteenToyRatio","ZGSF":"ZGSFsixteenToyRatio","OtherSF":"OtherSFsixteenToyRatio"}#,"Other_norm":"OtherNormsixteenToyRatio"}

parameterDictEle  = {"r":"ttgammaSFelsixteenToyRatio","TTbarSF":"TTbarSFelsixteenToyRatio","WGSF":"WGSFelsixteenToyRatio","ZGSF":"ZGSFelsixteenToyRatio","OtherSF":"OtherSFelsixteenToyRatio", "Other_norm":"OtherNormelsixteenToyRatio"}
parameterDictMu   = {"r":"ttgammaSFmusixteenToyRatio","TTbarSF":"TTbarSFmusixteenToyRatio","WGSF":"WGSFmusixteenToyRatio","ZGSF":"ZGSFmusixteenToyRatio","OtherSF":"OtherSFmusixteenToyRatio", "Other_norm":"OtherNormmusixteenToyRatio"}
parameterDictBoth = {"r":"ttgammaSFsixteenToyRatio","TTbarSF":"TTbarSFsixteenToyRatio","WGSF":"WGSFsixteenToyRatio","ZGSF":"ZGSFsixteenToyRatio","OtherSF":"OtherSFsixteenToyRatio", "Other_norm":"OtherNormsixteenToyRatio"}

line = ""
for ifile in ListOfFiles2016Ele:
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


    
for ifile in ListOfFiles2016Mu:
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

for ifile in ListOfFiles2016Both:
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

with open("TTGamma_nonPrompt_2016_ToyRatio.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2016_ToyRatio.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')
