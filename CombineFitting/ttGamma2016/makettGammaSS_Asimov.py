import ROOT
import shutil
import sys


#if sys.argv[1]=="toyFitting":
#	ListOfFiles2016Ele  = ["fitDiagnostics.TOY_ele_2016.root"]
#	ListOfFiles2016Mu   = ["fitDiagnostics.TOY_ele_2016.root"]
	#ListOfFiles2016Both = ["fitDiagnostics.TOY_ele_2016.root"]
	
#else:
ListOfFiles2016Ele  = ["fitDiagnostics.Asimov_ele_2016.root"]
ListOfFiles2016Mu   = ["fitDiagnostics.Asimov_mu_2016.root"]
ListOfFiles2016Both = ["fitDiagnostics.Asimov_both_2016.root"]

lineTest = ""
for ifile in ListOfFiles2016Ele:
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

with open("TTGamma_nonPrompt_2016_Asimov.txt","w") as _file:
    _file.write(lineTest)

#line = ""
#for ifile in ListOfFiles2016Ele:
#    myfile = ROOT.TFile(ifile,"read")
#    if myfile.GetListOfKeys().Contains("fit_s") is False:
#        print ifile[14:-10], ": Fit failed."
#        continue
#    fit_s = myfile.Get("fit_s")
#    line +=   "ttgammaSF_el_2016 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
#    line += "nonPromptSF_el_2016 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
#    line +=     "TTbarSF_el_2016 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
#    line +=        "WGSF_el_2016 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
#    line +=        "ZGSF_el_2016 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
#    line +=     "OtherSF_el_2016 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
    #line +=     "Other_norm_el_2016 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())
	
#for ifile in ListOfFiles2016Mu:
#    myfile = ROOT.TFile(ifile,"read")
#    if myfile.GetListOfKeys().Contains("fit_s") is False:
#        print ifile[14:-10], ": Fit failed."
#        continue
#    fit_s = myfile.Get("fit_s")
#    line +=   "ttgammaSF_mu_2016 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
#    line += "nonPromptSF_mu_2016 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
#    line +=     "TTbarSF_mu_2016 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
#    line +=        "WGSF_mu_2016 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
#    line +=        "ZGSF_mu_2016 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
#    line +=     "OtherSF_mu_2016 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
    #line +=     "Other_norm_mu_2016 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())	
	
#for ifile in ListOfFiles2016Both:
#    myfile = ROOT.TFile(ifile,"read")
#    if myfile.GetListOfKeys().Contains("fit_s") is False:
#        print ifile[14:-10], ": Fit failed."
#        continue
#    fit_s = myfile.Get("fit_s")
#    line +=   "ttgammaSF_2016 = %.2f \n"%(fit_s.floatParsFinal().find("r").getVal())
#    line += "nonPromptSF_2016 = %.2f \n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal())
#    line +=     "TTbarSF_2016 = %.2f \n"%(fit_s.floatParsFinal().find("TTbarSF").getVal())
#    line +=        "WGSF_2016 = %.2f \n"%(fit_s.floatParsFinal().find("WGSF").getVal())
#    line +=        "ZGSF_2016 = %.2f \n"%(fit_s.floatParsFinal().find("ZGSF").getVal())
#    line +=     "OtherSF_2016 = %.2f \n"%(fit_s.floatParsFinal().find("OtherSF").getVal())
#    line +=     "Other_norm_2016 = %.2f \n"%(fit_s.floatParsFinal().find("Other_norm").getVal())

#with open("TTGamma_nonPrompt_2016.py","w") as _file:
#    _file.write(line)

# ## copy the file to plotting folder
#shutil.copy("TTGamma_nonPrompt_2016.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')


line = ""
for ifile in ListOfFiles2016Ele:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSFelsixteenAsimov",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFelsixteenAsimov",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("nonPromptSF").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFelsixteenAsimov",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFelsixteenAsimov",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFelsixteenAsimov",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFelsixteenAsimov",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormelsixteenAsimov",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())


for ifile in ListOfFiles2016Mu:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSFmusixteenAsimov",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFmusixteenAsimov",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFmusixteenAsimov",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFmusixteenAsimov",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFmusixteenAsimov",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFmusixteenAsimov",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormmusixteenAsimov",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

for ifile in ListOfFiles2016Both:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ttgammaSFsixteenAsimov",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("nonPromptSFsixteenAsimov",fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("TTbarSFsixteenAsimov",fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("WGSFsixteenAsimov",fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorHi(),fit_s.floatParsFinal().find("WGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("ZGSFsixteenAsimov",fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorHi(),fit_s.floatParsFinal().find("ZGSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherSFsixteenAsimov",fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorHi(),fit_s.floatParsFinal().find("OtherSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.2f \\substack{+%.2f \\\\ %.2f}}}\n"%("OtherNormsixteenAsimov",fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorHi(),fit_s.floatParsFinal().find("Other_norm").getErrorLo())

print line
with open("TTGamma_nonPrompt_2016_Asimov.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
#shutil.copy("TTGamma_nonPrompt_2016_Asimov.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')


