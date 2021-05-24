import ROOT
import shutil
import sys


#if sys.argv[1]=="toyFitting":
#	ListOfFiles  = ["fitDiagnostics.TOY_ele_2016.root"]
#	ListOfFiles2016Mu   = ["fitDiagnostics.TOY_ele_2016.root"]
	#ListOfFiles2016Both = ["fitDiagnostics.TOY_ele_2016.root"]
	
#else:
ListOfFiles  = ["fitDiagnostics.Data.root"]



line = ""
for ifile in ListOfFiles:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line +=   "ttgammaSF    = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
    line += "nonPromptSF    = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
    # line +=     "TTbarSF    = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
    # line +=        "WGSF    = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
    # line +=        "ZGSF    = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
    # line +=     "OtherSF    = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
    # line +=     "Other_norm = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())
	

with open("TTGamma_nonPrompt.py","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
shutil.copy("TTGamma_nonPrompt.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')


line = ""
for ifile in ListOfFiles:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSF",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSF",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    # line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSF",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    # line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSF",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    # line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSF",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    # line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSF",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    # line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNorm",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())


with open("TTGamma_nonPrompt.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2016.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')


