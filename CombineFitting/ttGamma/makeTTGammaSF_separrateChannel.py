import ROOT
import shutil

mylist = ["higgsCombineel_2016.MultiDimFit.mH120.314159.root", 
          "higgsCombineel_2017.MultiDimFit.mH120.314159.root", 
          "higgsCombineel_2018.MultiDimFit.mH120.314159.root", 
          "higgsCombinemu_2016.MultiDimFit.mH120.314159.root",
          "higgsCombinemu_2017.MultiDimFit.mH120.314159.root",
          "higgsCombinemu_2018.MultiDimFit.mH120.314159.root"]

line = ""
for ifile in mylist:
    myfile = ROOT.TFile(ifile,"read")
    mytree=myfile.limit
    mytree.Draw("r>>hist1")
    hist1 = ROOT.gDirectory.Get('hist1')
    mytree.Draw("nonPromptSF>>hist2")
    hist2 = ROOT.gDirectory.Get('hist2')
    line +=   "ttgammaSF_%s = %.3f \n"%(ifile[12:-30],hist1.GetMean())
    line += "nonPromptSF_%s = %.3f \n"%(ifile[12:-30],hist2.GetMean())
with open("TTGamma_nonPrompt_values_separateChannelYear.py","w") as _file:
    _file.write(line)  

shutil.copy("TTGamma_nonPrompt_values_separateChannelYear.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')

line = ""
for ifile in mylist:
    myfile = ROOT.TFile(ifile,"read")
    mytree=myfile.limit
    mytree.Draw("r>>hist1")
    hist1 = ROOT.gDirectory.Get('hist1')
    mytree.Draw("nonPromptSF>>hist2")
    hist2 = ROOT.gDirectory.Get('hist2')
    if ifile[15:-30]=='2016': year='sixteen'
    elif ifile[15:-30]=='2017': year='seventeen'
    elif ifile[15:-30]=='2018': year='eightteen'
    line +=   "\\newcommand{\\ttgammaSF%s%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ -%.3f}}}\n"%(ifile[12:-35],year,hist1.GetMean(),hist1.GetRMS(), hist1.GetRMS())
    line +=   "\\newcommand{\\nonPromptSF%s%s} {\ensuremath{%.3f \\substack{+%.3f \\\\ -%.3f}}}\n"%(ifile[12:-35],year,hist2.GetMean(),hist2.GetRMS(), hist2.GetRMS())

with open("TTGamma_nonPrompt_values_separateChannelYear.tex","w") as _file:
    _file.write(line)

shutil.copy("TTGamma_nonPrompt_values_separateChannelYear.tex",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/CombineFitting/AllTexFiles')
