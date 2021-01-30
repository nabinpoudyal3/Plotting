import ROOT
import numpy as np
from matplotlib import pyplot as plt
import sys

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

x = [2, 3, 4, 5]
myCR = ["NJ>=2\nNB=0", "NJ=2\nNB=0", "NJ=3\nNB=0", "NJ>=4\nNB=0"]
y =[]
yerrUp = []
yerrDo = []
for ifile in ListOfFiles2016:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    y.append(fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal())
    yerrUp.append(fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorHi())
    yerrDo.append(fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorLo())
fig = plt.figure()
plt.errorbar(x, y, yerr=yerrUp, fmt='o',elinewidth=3, capsize=5,capthick=3)
plt.xticks(x, myCR)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlim(1,6)
plt.ylim(0.1,2.5)
plt.tight_layout()
plt.grid()
plt.ylabel(r'Z$\gamma$ SF',fontsize=30)
plt.xlabel('Jet multipicity',fontsize=30)
plt.title('')
plt.text(2.5, 1.8, r'Z$\gamma$ SF for 2016',fontsize=30)

fig.savefig('Z16.pdf', bbox_inches="tight", dpi=1200)



x = [2, 3, 4, 5]
myCR = ["NJ>=2\nNB=0", "NJ=2\nNB=0", "NJ=3\nNB=0", "NJ>=4\nNB=0"]

y =[]
yerrUp = []
yerrDo = []
for ifile in ListOfFiles2017:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    y.append(fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal())
    yerrUp.append(fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorHi())
    yerrDo.append(fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorLo())
fig = plt.figure()
plt.errorbar(x, y, yerr=yerrUp, fmt='o',elinewidth=3, capsize=5,capthick=3)
plt.xticks(x, myCR)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlim(1,6)
plt.ylim(0.1,2.5)
plt.tight_layout()
plt.grid()
plt.ylabel(r'Z$\gamma$ SF',fontsize=30)
plt.xlabel('Jet multipicity',fontsize=30)
plt.title('')
plt.text(2.5, 1.8, r'Z$\gamma$ SF for 2017',fontsize=30)

fig.savefig('Z17.pdf', bbox_inches="tight", dpi=1200)


x = [2, 3, 4, 5]
myCR = ["NJ>=2\nNB=0", "NJ=2\nNB=0", "NJ=3\nNB=0", "NJ>=4\nNB=0"]
y =[]
yerrUp = []
yerrDo = []
for ifile in ListOfFiles2018:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    y.append(fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal())
    yerrUp.append(fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorHi())
    yerrDo.append(fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorLo())
fig = plt.figure()
plt.errorbar(x, y, yerr=yerrUp, fmt='o',elinewidth=3, capsize=5,capthick=3)
plt.xticks(x, myCR)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlim(1,6)
plt.ylim(0.1,2.5)
plt.tight_layout()
plt.grid()
plt.ylabel(r'Z$\gamma$ SF',fontsize=30)
plt.xlabel('Jet multipicity',fontsize=30)
plt.title('')
plt.text(2.5, 1.8, r'Z$\gamma$ SF for 2018',fontsize=30)

fig.savefig('Z18.pdf', bbox_inches="tight", dpi=1200)


x = [2, 3, 4, 5]
myCR = ["NJ>=2\nNB=0", "NJ=2\nNB=0", "NJ=3\nNB=0", "NJ>=4\nNB=0"]
y =[]
yerrUp = []
yerrDo = []
for ifile in ListOfFiles2016:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    y.append(fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal())
    yerrUp.append(fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorHi())
    yerrDo.append(fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorLo())

fig = plt.figure()
plt.errorbar(x, y, yerr=yerrUp, fmt='o',elinewidth=3, capsize=5,capthick=3)
plt.xticks(x, myCR)
plt.tick_params(axis='y', which='major', labelsize=20)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.xlim(1,6)
plt.ylim(0.5,2.5)
plt.tight_layout()
plt.grid()
plt.ylabel(r'W$\gamma$ SF',fontsize=30)
# plt.xlabel('Jet multipicity',fontsize=30)
plt.title('')
plt.text(2.5, 1.8, r'W$\gamma$ SF for 2016',fontsize=30)

fig.savefig('W16.pdf', bbox_inches="tight", dpi=1200)


x = [2, 3, 4, 5]
myCR = ["NJ>=2\nNB=0", "NJ=2\nNB=0", "NJ=3\nNB=0", "NJ>=4\nNB=0"]
y =[]
yerrUp = []
yerrDo = []
for ifile in ListOfFiles2017:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    y.append(fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal())
    yerrUp.append(fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorHi())
    yerrDo.append(fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorLo())
#     print fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo()
#     print fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorLo(),fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorHi()
#     print fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorLo(),fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorHi()
fig = plt.figure()
plt.errorbar(x, y, yerr=yerrUp, fmt='o',elinewidth=3, capsize=5,capthick=3)
plt.xticks(x, myCR)
plt.tick_params(axis='y', which='major', labelsize=20)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.xlim(1,6)
plt.ylim(0.5,2.5)
plt.tight_layout()
plt.grid()
plt.ylabel(r'W$\gamma$ SF',fontsize=30)
# plt.xlabel('Jet multipicity',fontsize=30)
plt.title('')
plt.text(2.5, 1.8, r'W$\gamma$ SF for 2017',fontsize=30)

fig.savefig('W17.pdf', bbox_inches="tight", dpi=1200)


x = [2, 3, 4, 5]
myCR = ["NJ>=2\nNB=0", "NJ=2\nNB=0", "NJ=3\nNB=0", "NJ>=4\nNB=0"]
y =[]
yerrUp = []
yerrDo = []
for ifile in ListOfFiles2018:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    y.append(fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal())
    yerrUp.append(fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorHi())
    yerrDo.append(fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorLo())
#     print fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorHi(),fit_s.floatParsFinal().find("r").getErrorLo()
#     print fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorLo(),fit_s.floatParsFinal().find("ZGammaBkgPhotonSF").getErrorHi()
#     print fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getVal(),fit_s.floatParsFinal().find("r").getErrorLo(),fit_s.floatParsFinal().find("WGammaBkgPhotonSF").getErrorHi()
fig = plt.figure()
plt.errorbar(x, y, yerr=yerrUp, fmt='o',elinewidth=3, capsize=5,capthick=3)
plt.xticks(x, myCR)
plt.tick_params(axis='y', which='major', labelsize=20)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.xlim(1,6)
plt.ylim(0.5,2.5)
plt.tight_layout()
plt.grid()
plt.ylabel(r'W$\gamma$ SF',fontsize=30)
# plt.xlabel('Jet multipicity',fontsize=30)
plt.title('')
plt.text(2.5, 1.8, r'W$\gamma$ SF for 2018',fontsize=30)

fig.savefig('W18.pdf', bbox_inches="tight", dpi=1200)


sys.exit()
