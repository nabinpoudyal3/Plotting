import ROOT
import shutil


mylist = ["higgsCombineboth_2016.MultiDimFit.mH120.314159.root", 
          "higgsCombineboth_2017.MultiDimFit.mH120.314159.root", 
          "higgsCombineboth_2018.MultiDimFit.mH120.314159.root" ]

line = ""
for ifile in mylist:
    myfile = ROOT.TFile(ifile,"read")
    mytree=myfile.limit
    mytree.Draw("r>>hist1")
    hist1 = ROOT.gDirectory.Get('hist1')
    mytree.Draw("nonPromptSF>>hist2")
    hist2 = ROOT.gDirectory.Get('hist2')
    line +=   "ttgammaSF_%s = %.3f \n"%(ifile[17:21],hist1.GetMean())
    line += "nonPromptSF_%s = %.3f \n"%(ifile[17:21],hist2.GetMean())

with open("TTGamma_nonPrompt_values_bothChannelSeparateYear.py","w") as _file:
    _file.write(line)

shutil.copy("TTGamma_nonPrompt_values_bothChannelSeparateYear.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')

line = ""
for ifile in mylist:
    myfile = ROOT.TFile(ifile,"read")
    mytree=myfile.limit
    mytree.Draw("r>>hist1")
    hist1 = ROOT.gDirectory.Get('hist1')
    mytree.Draw("nonPromptSF>>hist2")
    hist2 = ROOT.gDirectory.Get('hist2')
    if ifile[17:21]=='2016': year='sixteen'
    elif ifile[17:21]=='2017': year='seventeen'
    elif ifile[17:21]=='2018': year='eightteen'
    line +=   "\\newcommand{\\ttgammaSF%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ -%.3f}}}\n"%(year,hist1.GetMean(),hist1.GetRMS(), hist1.GetRMS())
    line +=   "\\newcommand{\\nonPromptSF%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ -%.3f}}}\n"%(year,hist2.GetMean(),hist2.GetRMS(), hist2.GetRMS())

with open("TTGamma_nonPrompt_values_bothChannelSeparateYear.tex","w") as _file:
    _file.write(line)

shutil.copy("TTGamma_nonPrompt_values_bothChannelSeparateYear.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')
