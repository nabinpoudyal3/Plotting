import ROOT
import shutil
import sys


#if sys.argv[1]=="toyFitting":
#	ListOfFiles2017Ele  = ["fitDiagnostics.TOY_ele_2017.root"]
#	ListOfFiles2017Mu   = ["fitDiagnostics.TOY_ele_2017.root"]
	#ListOfFiles2017Both = ["fitDiagnostics.TOY_ele_2017.root"]
	
#else:
ListOfFiles2017Ele  = ["fitDiagnostics.Asimov_ele_2017.root"]
ListOfFiles2017Mu   = ["fitDiagnostics.Asimov_mu_2017.root"]
ListOfFiles2017Both = ["fitDiagnostics.Asimov_both_2017.root"]


lineTest = ""
for ifile in ListOfFiles2017Ele:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    lineTest += "%s = %.2f [+%.2f  %.2f]\n" %("ttgamma   ",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    lineTest += "%s = %.2f [+%.2f  %.2f]\n" %("nonPrompt ",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("nonPromptSF").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    lineTest += "%s = %.2f [+%.2f  %.2f]\n" %("TTbar     ",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    lineTest += "%s = %.2f [+%.2f  %.2f]\n" %("WG        ",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    lineTest += "%s = %.2f [+%.2f  %.2f]\n" %("ZG        ",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    lineTest += "%s = %.2f [+%.2f  %.2f]\n" %("Other     ",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    lineTest += "%s = %.2f [+%.2f  %.2f]\n" %("OtherNorm ",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

with open("TTGamma_nonPrompt_2017_AsimovRatio.txt","w") as _file:
    _file.write(lineTest)

#line = ""
#for ifile in ListOfFiles2017Ele:
#    myfile = ROOT.TFile(ifile,"read")
#    if myfile.GetListOfKeys().Contains("fit_s") is False:
#        print ifile[14:-10], ": Fit failed."
#        continue
#    fit_s = myfile.Get("fit_s")
#    line +=   "ttgammaSF_el_2017 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
#    line += "nonPromptSF_el_2017 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
#    line +=     "TTbarSF_el_2017 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
#    line +=        "WGSF_el_2017 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
#    line +=        "ZGSF_el_2017 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
#    line +=     "OtherSF_el_2017 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
    #line +=     "Other_norm_el_2017 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())
	
#for ifile in ListOfFiles2017Mu:
#    myfile = ROOT.TFile(ifile,"read")
#    if myfile.GetListOfKeys().Contains("fit_s") is False:
#        print ifile[14:-10], ": Fit failed."
#        continue
#    fit_s = myfile.Get("fit_s")
#    line +=   "ttgammaSF_mu_2017 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
#    line += "nonPromptSF_mu_2017 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
#    line +=     "TTbarSF_mu_2017 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
#    line +=        "WGSF_mu_2017 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
#    line +=        "ZGSF_mu_2017 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
#    line +=     "OtherSF_mu_2017 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
    #line +=     "Other_norm_mu_2017 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())	
	
#for ifile in ListOfFiles2017Both:
#    myfile = ROOT.TFile(ifile,"read")
#    if myfile.GetListOfKeys().Contains("fit_s") is False:
#        print ifile[14:-10], ": Fit failed."
#        continue
#    fit_s = myfile.Get("fit_s")
#    line +=   "ttgammaSF_2017 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
#    line += "nonPromptSF_2017 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
#    line +=     "TTbarSF_2017 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
#    line +=        "WGSF_2017 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
#    line +=        "ZGSF_2017 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
#    line +=     "OtherSF_2017 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
#    line +=     "Other_norm_2017 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())

#with open("TTGamma_nonPrompt_2017.py","w") as _file:
#    _file.write(line)

# ## copy the file to plotting folder
#shutil.copy("TTGamma_nonPrompt_2017.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')


line = ""
for ifile in ListOfFiles2017Ele:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.5f \\\\ %.5f}}}\n"%("ttgammaSFelseventeenAsimovRatio",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFelseventeenAsimovRatio",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("nonPromptSF").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFelseventeenAsimovRatio",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFelseventeenAsimovRatio",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFelseventeenAsimovRatio",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFelseventeenAsimovRatio",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormelseventeenAsimovRatio",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

for ifile in ListOfFiles2017Mu:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.5f \\\\ %.5f}}}\n"%("ttgammaSFmuseventeenAsimovRatio",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFmuseventeenAsimovRatio",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFmuseventeenAsimovRatio",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFmuseventeenAsimovRatio",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFmuseventeenAsimovRatio",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFmuseventeenAsimovRatio",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormmuseventeenAsimovRatio",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

for ifile in ListOfFiles2017Both:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.5f \\\\ %.5f}}}\n"%("ttgammaSFseventeenAsimovRatio",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFseventeenAsimovRatio",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFseventeenAsimovRatio",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFseventeenAsimovRatio",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFseventeenAsimovRatio",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFseventeenAsimovRatio",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormseventeenAsimovRatio",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

print line
with open("TTGamma_nonPrompt_2017_AsimovRatio.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2017_AsimovRatio.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')


