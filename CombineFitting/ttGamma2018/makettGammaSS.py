import ROOT
import shutil
import sys


ListOfFiles2018Ele  = ["fitDiagnosticsele_2018.root"]
ListOfFiles2018Mu   = ["fitDiagnosticsmu_2018.root"]
ListOfFiles2018Both = ["fitDiagnosticsboth_2018.root"]


line = ""
for ifile in ListOfFiles2018Ele:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line +=   "ttgammaSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
    line += "nonPromptSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
    line +=     "TTbarSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
    line +=        "WGSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
    line +=        "ZGSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
    line +=     "OtherSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
    line +=     "Other_norm_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())
	
for ifile in ListOfFiles2018Mu:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line +=   "ttgammaSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
    line += "nonPromptSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
    line +=     "TTbarSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
    line +=        "WGSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
    line +=        "ZGSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
    line +=     "OtherSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
    line +=     "Other_norm_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())	
	
#for ifile in ListOfFiles2018Both:
#    myfile = ROOT.TFile(ifile,"read")
#    if myfile.GetListOfKeys().Contains("fit_s") is False:
#        print ifile[14:-10], ": Fit failed."
#        continue
#    fit_s = myfile.Get("fit_s")
#    line +=   "ttgammaSF_2018 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
#    line += "nonPromptSF_2018 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
#    line +=     "TTbarSF_2018 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
#    line +=        "WGSF_2018 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
#    line +=        "ZGSF_2018 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
#    line +=     "OtherSF_2018 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
#    line +=     "Other_norm_2018 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())

with open("TTGamma_nonPrompt_2018.py","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
shutil.copy("TTGamma_nonPrompt_2018.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')


line = ""
for ifile in ListOfFiles2018Ele:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSFeleighteen",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFeleighteen",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFeleighteen",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFeleighteen",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFeleighteen",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFeleighteen",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormeleighteen",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

for ifile in ListOfFiles2018Mu:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSFmueighteen",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFmueighteen",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFmueighteen",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFmueighteen",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFmueighteen",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFmueighteen",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormmueighteen",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

for ifile in ListOfFiles2018Both:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSFeighteen",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFeighteen",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFeighteen",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFeighteen",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFeighteen",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFeighteen",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormeighteen",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

with open("TTGamma_nonPrompt_2018.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2018.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')


