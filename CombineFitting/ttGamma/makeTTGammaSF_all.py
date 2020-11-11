import ROOT
import shutil

mylist = ["higgsCombineboth_allyear.MultiDimFit.mH120.314159.root"]

line = ""
for ifile in mylist:
    print ifile[17:24]
    myfile = ROOT.TFile(ifile,"read")
    mytree=myfile.limit
    mytree.Draw("r>>hist1")
    hist1 = ROOT.gDirectory.Get('hist1')
    mytree.Draw("nonPromptSF>>hist2")
    hist2 = ROOT.gDirectory.Get('hist2')
    line +=   "ttgammaSF_%s = %.2f \n"%(ifile[17:24],hist1.GetMean())
    line += "nonPromptSF_%s = %.2f \n"%(ifile[17:24],hist2.GetMean())

with open("TTGamma_nonPrompt_values_all.py","w") as _file:
    _file.write(line)
shutil.copy("TTGamma_nonPrompt_values_all.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')

line = ""
for ifile in mylist:
    myfile = ROOT.TFile(ifile,"read")
    mytree=myfile.limit
    mytree.Draw("r>>hist1")
    hist1 = ROOT.gDirectory.Get('hist1')
    mytree.Draw("nonPromptSF>>hist2")
    hist2 = ROOT.gDirectory.Get('hist2')
    line +=   "\\newcommand{\\ttgammaSF} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(hist1.GetMean(),hist1.GetRMS(), hist1.GetRMS())
    line +=   "\\newcommand{\\nonPromptSF} {\ensuremath{%.2f \\substack{+%.2f \\\\ -%.2f}}}\n"%(hist2.GetMean(),hist2.GetRMS(), hist2.GetRMS())

with open("TTGamma_nonPrompt_values_all.tex","w") as _file:
    _file.write(line)

shutil.copy("TTGamma_nonPrompt_values_all.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')
