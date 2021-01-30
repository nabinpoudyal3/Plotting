import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles2017Ele  = ["fitDiagnostics.TOY_ele_2017.root"]
ListOfFiles2017Mu   = ["fitDiagnostics.TOY_mu_2017.root"]
ListOfFiles2017Both = ["fitDiagnostics.TOY_both_2017.root"]

#parameterDictEle  = {"r":"ttgammaSFelseventeenToy","nonPromptSF":"nonPromptSFelseventeenToy","TTbarSF":"TTbarSFelseventeenToy","WGSF":"WGSFelseventeenToy","ZGSF":"ZGSFelseventeenToy","OtherSF":"OtherSFelseventeenToy"}#,"Other_norm":"OtherNormelseventeenToy"}
#parameterDictMu   = {"r":"ttgammaSFmuseventeenToy","nonPromptSF":"nonPromptSFmuseventeenToy","TTbarSF":"TTbarSFmuseventeenToy","WGSF":"WGSFmuseventeenToy","ZGSF":"ZGSFmuseventeenToy","OtherSF":"OtherSFmuseventeenToy"}#,"Other_norm":"OtherNormmuseventeenToy"}
#parameterDictBoth = {"r":"ttgammaSFseventeenToy","nonPromptSF":"nonPromptSFseventeenToy","TTbarSF":"TTbarSFseventeenToy","WGSF":"WGSFseventeenToy","ZGSF":"ZGSFseventeenToy","OtherSF":"OtherSFseventeenToy"}#,"Other_norm":"OtherNormseventeenToy"}

parameterDictEle  = {"r":"ttgammaSFelseventeenToy","TTbarSF":"TTbarSFelseventeenToy","WGSF":"WGSFelseventeenToy","ZGSF":"ZGSFelseventeenToy","OtherSF":"OtherSFelseventeenToy", "Other_norm":"OtherNormelseventeenToy"}
parameterDictMu   = {"r":"ttgammaSFmuseventeenToy","TTbarSF":"TTbarSFmuseventeenToy","WGSF":"WGSFmuseventeenToy","ZGSF":"ZGSFmuseventeenToy","OtherSF":"OtherSFmuseventeenToy", "Other_norm":"OtherNormmuseventeenToy"}
parameterDictBoth = {"r":"ttgammaSFseventeenToy","TTbarSF":"TTbarSFseventeenToy","WGSF":"WGSFseventeenToy","ZGSF":"ZGSFseventeenToy","OtherSF":"OtherSFseventeenToy", "Other_norm":"OtherNormseventeenToy"}

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

with open("TTGamma_nonPrompt_2017_Toy.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2017_Toy.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')
