import ROOT
import shutil
import sys

ROOT.gROOT.SetBatch(True)

ListOfFiles  = ["fitDiagnostics.TOY.root"]

parameterDict  = {"r":"ttgammaSFToy","nonPromptSF":"nonPromptSFToy"}#,"TTbarSF":"TTbarSFToy","WGSF":"WGSFToy","ZGSF":"ZGSFToy","OtherSF":"OtherSFToy", "Other_norm":"OtherNormToy"}

line = ""
for ifile in ListOfFiles:
    myfile = ROOT.TFile(ifile,"read")
    tree_fit_sb = myfile.Get("tree_fit_sb")
    for param in parameterDict.keys():
    	if param == "nonPromptSF": continue
        print param
        hist = ROOT.TH1F("hist","",100,-2,2)
        tree_fit_sb.Draw("%s>>hist"%param)
        hist = ROOT.gDirectory.Get('hist')
        print "==>",hist.GetMean(), hist.GetRMS()
        hist.Fit("gaus")
        fit = hist.GetFunction("gaus")
        print "==>>>",fit.GetParameter(1),fit.GetParameter(2)
        line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(parameterDict[param],fit.GetParameter(1),fit.GetParameter(2),fit.GetParameter(2))
        del hist
        print line

with open("TTGamma_nonPrompt_Toy.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2016_Toy.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')
