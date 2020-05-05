import uproot
import shutil
 
 
ListOfFiles2016 = ["fitDiagnosticsCR123_2016.root", "fitDiagnosticsCR1_2016.root",  "fitDiagnosticsCR2_2016.root", "fitDiagnosticsCR3_2016.root",
			   "fitDiagnosticsCR4_2016.root", "fitDiagnosticsCR5_2016.root", "fitDiagnosticsCR6_2016.root", "fitDiagnosticsCR7_2016.root",  "fitDiagnosticsSR8_2016.root"]


ListOfFiles2017 = ["fitDiagnosticsCR123_2017.root", "fitDiagnosticsCR1_2017.root",  "fitDiagnosticsCR2_2017.root", "fitDiagnosticsCR3_2017.root",
			   "fitDiagnosticsCR4_2017.root", "fitDiagnosticsCR5_2017.root", "fitDiagnosticsCR6_2017.root", "fitDiagnosticsCR7_2017.root",  "fitDiagnosticsSR8_2017.root"]


ListOfFiles2018 = ["fitDiagnosticsCR123_2018.root", "fitDiagnosticsCR1_2018.root",  "fitDiagnosticsCR2_2018.root", "fitDiagnosticsCR3_2018.root",
			   "fitDiagnosticsCR4_2018.root", "fitDiagnosticsCR5_2018.root", "fitDiagnosticsCR6_2018.root", "fitDiagnosticsCR7_2018.root",  "fitDiagnosticsSR8_2018.root"]


controlRegionDict ={"SR8":"tight", "CR123":"looseCRge2e0", "CR7":"looseCRe3ge2", "CR3":"looseCRge4e0", "CR2":"looseCRe3e0", 
				   "CR4":"looseCRe2e1", "CR1":"looseCRe2e0", "CR6":"looseCRe2e2", "CR5":"looseCRe3e1" }

CRDict ={"SR8":"zjetsfSReight", "CR123":"zjetsfCRall", "CR7":"zjetsfCRseven", "CR3":"zjetsfCRthree", "CR2":"zjetsfCRtwo", 
		 "CR4":"zjetsfCRfour", "CR1":"zjetsfCRone", "CR6":"zjetsfCRsix", "CR5":"zjetsfCRfive" }


line = ""
for ifile in ListOfFiles2016:
    print ifile
    itree = uproot.open(ifile)["tree_fit_sb"]
    line += "ZJetSF_2016_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],itree.array("r"))

for ifile in ListOfFiles2017:
    print ifile
    itree = uproot.open(ifile)["tree_fit_sb"]
    line += "ZJetSF_2017_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],itree.array("r"))
    
for ifile in ListOfFiles2018:
    print ifile
    itree = uproot.open(ifile)["tree_fit_sb"]
    line += "ZJetSF_2018_%s = %.3f \n"%(controlRegionDict[ifile[14:-10]],itree.array("r"))
    
with open("ZJetSFvalues.py","w") as _file:
    _file.write(line)

#get_ipython().system('cp ZJetSFvalues.py /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')
shutil.copy("ZJetSFvalues.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')

line = ""

for ifile in ListOfFiles2016:
    itree = uproot.open(ifile)["tree_fit_sb"]
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ -%.3f}}}\n"%(CRDict[ifile[14:-10]]+"Sixteen",itree.array("r"),itree.array("rHiErr"),itree.array("rLoErr"))

for ifile in ListOfFiles2017:
    itree = uproot.open(ifile)["tree_fit_sb"]
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ -%.3f}}}\n"%(CRDict[ifile[14:-10]]+"Seventeen",itree.array("r"),itree.array("rHiErr"),itree.array("rLoErr"))

for ifile in ListOfFiles2018:
    itree = uproot.open(ifile)["tree_fit_sb"]
    line += "\\newcommand{\\%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ -%.3f}}}\n"%(CRDict[ifile[14:-10]]+"Eighteen",itree.array("r"),itree.array("rHiErr"),itree.array("rLoErr"))
    
with open("ZJetSFvalues.tex","w") as _file:
    _file.write(line)
## copy the file to plotting folder
#get_ipython().system('cp ZJetSFvalues.tex ../AllTexFiles ')
shutil.copy("ZJetSFvalues.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')

