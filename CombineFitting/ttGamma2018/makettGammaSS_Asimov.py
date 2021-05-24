import ROOT
import shutil
import sys


#if sys.argv[1]=="toyFitting":
#	ListOfFiles2018Ele  = ["fitDiagnostics.TOY_ele_2018.root"]
#	ListOfFiles2018Mu   = ["fitDiagnostics.TOY_ele_2018.root"]
	#ListOfFiles2018Both = ["fitDiagnostics.TOY_ele_2018.root"]
	
#else:
ListOfFiles2018Ele  = ["fitDiagnostics.Asimov_ele_2018.root"]
ListOfFiles2018Mu   = ["fitDiagnostics.Asimov_mu_2018.root"]
ListOfFiles2018Both = ["fitDiagnostics.Asimov_both_2018.root"]


lineTest = ""
for ifile in ListOfFiles2018Ele:
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

with open("TTGamma_nonPrompt_2018_Asimov.txt","w") as _file:
    _file.write(lineTest)

#line = ""
#for ifile in ListOfFiles2018Ele:
#    myfile = ROOT.TFile(ifile,"read")
#    if myfile.GetListOfKeys().Contains("fit_s") is False:
#        print ifile[14:-10], ": Fit failed."
#        continue
#    fit_s = myfile.Get("fit_s")
#    line +=   "ttgammaSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
#    line += "nonPromptSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
#    line +=     "TTbarSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
#    line +=        "WGSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
#    line +=        "ZGSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
#    line +=     "OtherSF_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
    #line +=     "Other_norm_el_2018 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())
	
#for ifile in ListOfFiles2018Mu:
#    myfile = ROOT.TFile(ifile,"read")
#    if myfile.GetListOfKeys().Contains("fit_s") is False:
#        print ifile[14:-10], ": Fit failed."
#        continue
#    fit_s = myfile.Get("fit_s")
#    line +=   "ttgammaSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
#    line += "nonPromptSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
#    line +=     "TTbarSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
#    line +=        "WGSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
#    line +=        "ZGSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
#    line +=     "OtherSF_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
    #line +=     "Other_norm_mu_2018 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())	
	
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

#with open("TTGamma_nonPrompt_2018.py","w") as _file:
#    _file.write(line)

# ## copy the file to plotting folder
#shutil.copy("TTGamma_nonPrompt_2018.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')


line = ""
for ifile in ListOfFiles2018Ele:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSFeleighteenAsimov",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFeleighteenAsimov",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("nonPromptSF").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFeleighteenAsimov",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFeleighteenAsimov",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFeleighteenAsimov",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFeleighteenAsimov",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormeleighteenAsimov",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

for ifile in ListOfFiles2018Mu:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSFmueighteenAsimov",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFmueighteenAsimov",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFmueighteenAsimov",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFmueighteenAsimov",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFmueighteenAsimov",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFmueighteenAsimov",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormmueighteenAsimov",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

for ifile in ListOfFiles2018Both:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSFeighteenAsimov",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFeighteenAsimov",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFeighteenAsimov",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFeighteenAsimov",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFeighteenAsimov",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFeighteenAsimov",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormeighteenAsimov",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())
print line
with open("TTGamma_nonPrompt_2018_Asimov.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2018_Asimov.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')


