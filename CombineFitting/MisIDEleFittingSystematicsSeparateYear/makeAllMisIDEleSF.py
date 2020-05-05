import ROOT
import shutil


ListOfFiles2016 = ["fitDiagnosticsCR123_2016.root", "fitDiagnosticsCR1_2016.root",  "fitDiagnosticsCR2_2016.root", "fitDiagnosticsCR3_2016.root"]#,"fitDiagnosticsCR4_2016.root"]
ListOfFiles2017 = ["fitDiagnosticsCR123_2017.root", "fitDiagnosticsCR1_2017.root",  "fitDiagnosticsCR2_2017.root", "fitDiagnosticsCR3_2017.root"]#,"fitDiagnosticsCR4_2017.root"]
ListOfFiles2018 = ["fitDiagnosticsCR123_2018.root", "fitDiagnosticsCR1_2018.root",  "fitDiagnosticsCR2_2018.root", "fitDiagnosticsCR3_2018.root"]#,"fitDiagnosticsCR4_2018.root"]


controlRegionDict ={"SR8":"tight", "CR123":"looseCRge2e0", "AR":"looseCRge2ge0", "CR7":"looseCRe3ge2", "CR3":"looseCRge4e0", "CR2":"looseCRe3e0", 
				   "CR4":"looseCRe2e1", "CR1":"looseCRe2e0", "CR6":"looseCRe2e2", "CR5":"looseCRe3e1" }


CRDictMisID ={"SR8":"misIDsfSReight", "CR123":"misIDsfCRall", "CR7":"misIDsfCRseven", "CR3":"misIDsfCRthree", "CR2":"misIDsfCRtwo", 
		 "CR4":"misIDsfCRfour", "CR1":"misIDsfCRone", "CR6":"misIDsfCRsix", "CR5":"misIDsfCRfive" }

CRDictZGamma ={"SR8":"zGammasfSReight", "CR123":"zGammasfCRall", "CR7":"zGammasfCRseven", "CR3":"zGammasfCRthree", "CR2":"zGammasfCRtwo", 
		 "CR4":"zGammasfCRfour", "CR1":"zGammasfCRone", "CR6":"zGammasfCRsix", "CR5":"zGammasfCRfive" }

CRDictWGamma ={"SR8":"wGammasfSReight", "CR123":"wGammasfCRall", "CR7":"wGammasfCRseven", "CR3":"wGammasfCRthree", "CR2":"wGammasfCRtwo", 
		 "CR4":"wGammasfCRfour", "CR1":"wGammasfCRone", "CR6":"wGammasfCRsix", "CR5":"wGammasfCRfive" }

line = ""
for ifile in ListOfFiles2016:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "MisIDEleSF_2016_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],fit_s.floatParsFinal().find("r").getVal())
    line +=   "ZGammaSF_2016_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal())
    line +=   "WGammaSF_2016_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal())

for ifile in ListOfFiles2017:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "MisIDEleSF_2017_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],fit_s.floatParsFinal().find("r").getVal())
    line +=   "ZGammaSF_2017_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal())
    line +=   "WGammaSF_2017_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal())

for ifile in ListOfFiles2018:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "MisIDEleSF_2018_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],fit_s.floatParsFinal().find("r").getVal())
    line +=   "ZGammaSF_2018_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal())
    line +=   "WGammaSF_2018_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal())

with open("MisIDEleSFvalues.py","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
shutil.copy("MisIDEleSFvalues.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')


line = ""
for ifile in ListOfFiles2016:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ %.3f}}}\n"%(CRDictMisID[ifile[14:-10]]+"Sixteen",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ %.3f}}}\n"%(CRDictZGamma[ifile[14:-10]]+"Sixteen",fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ %.3f}}}\n"%(CRDictWGamma[ifile[14:-10]]+"Sixteen",fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorLo())

for ifile in ListOfFiles2017:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ %.3f}}}\n"%(CRDictMisID[ifile[14:-10]]+"Seventeen",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ %.3f}}}\n"%(CRDictZGamma[ifile[14:-10]]+"Seventeen",fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ %.3f}}}\n"%(CRDictWGamma[ifile[14:-10]]+"Seventeen",fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorLo())

for ifile in ListOfFiles2018:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ %.3f}}}\n"%(CRDictMisID[ifile[14:-10]]+"Eighteen",fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ %.3f}}}\n"%(CRDictZGamma[ifile[14:-10]]+"Eighteen",fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorLo())
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ %.3f}}}\n"%(CRDictWGamma[ifile[14:-10]]+"Eighteen",fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorLo())


with open("MisIDEleSFvalues.tex","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#get_ipython().system('cp MisIDEleSFvalues.tex ../AllTexFiles ')
shutil.copy("MisIDEleSFvalues.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')


