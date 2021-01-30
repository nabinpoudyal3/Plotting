import ROOT
import shutil


ListOfFiles2017Ele  = ["fitDiagnostics.TOY_ele_2017.root"]

line = ""
for ifile in ListOfFiles2017Ele:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "  ttgammaSF_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorLo(),fit_s.floatParsFinal().find("r").getErrorHi())
    line += "nonPromptSF_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo(),fit_s.floatParsFinal().find("nonPromptSF").getErrorHi())
    line += "    TTbarSF_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi())
    line += "       WGSF_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorLo(),fit_s.floatParsFinal().find("WGSF").getErrorHi())
    line += "       ZGSF_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorLo(),fit_s.floatParsFinal().find("ZGSF").getErrorHi())
    line += "    OtherSF_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorLo(),fit_s.floatParsFinal().find("OtherSF").getErrorHi())
    line += " Other_norm_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorLo(),fit_s.floatParsFinal().find("Other_norm").getErrorHi())
    line += ""
    line += "   BTagSF_b_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("BTagSF_b").getVal(),fit_s.floatParsFinal().find("BTagSF_b").getErrorLo(),fit_s.floatParsFinal().find("BTagSF_b").getErrorHi())
    line += "   BTagSF_l_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("BTagSF_l").getVal(),fit_s.floatParsFinal().find("BTagSF_l").getErrorLo(),fit_s.floatParsFinal().find("BTagSF_l").getErrorHi())
    line += "     EleEff_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("EleEff").getVal(),fit_s.floatParsFinal().find("EleEff").getErrorLo(),fit_s.floatParsFinal().find("EleEff").getErrorHi())
    line += "      MuEff_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("MuEff").getVal(),fit_s.floatParsFinal().find("MuEff").getErrorLo(),fit_s.floatParsFinal().find("MuEff").getErrorHi())
    line += "         PU_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("PU").getVal(),fit_s.floatParsFinal().find("PU").getErrorLo(),fit_s.floatParsFinal().find("PU").getErrorHi())
    line += "     PhoEff_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("PhoEff").getVal(),fit_s.floatParsFinal().find("PhoEff").getErrorLo(),fit_s.floatParsFinal().find("PhoEff").getErrorHi())
    line += "         Q2_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("Q2").getVal(),fit_s.floatParsFinal().find("Q2").getErrorLo(),fit_s.floatParsFinal().find("Q2").getErrorHi())
    line += "        fsr_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("fsr").getVal(),fit_s.floatParsFinal().find("fsr").getErrorLo(),fit_s.floatParsFinal().find("fsr").getErrorHi())
    line += "        isr_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("isr").getVal(),fit_s.floatParsFinal().find("isr").getErrorLo(),fit_s.floatParsFinal().find("isr").getErrorHi())
    line += "       lumi_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("lumi").getVal(),fit_s.floatParsFinal().find("lumi").getErrorLo(),fit_s.floatParsFinal().find("lumi").getErrorHi())
    line += "     misIDE_el_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("misIDE").getVal(),fit_s.floatParsFinal().find("misIDE").getErrorLo(),fit_s.floatParsFinal().find("misIDE").getErrorHi())

with open("POIsNPs_ToyValues_ele.txt","w") as _file:
    _file.write(line)

# ## copy the file to plotting folder
#shutil.copy("TTGamma_nonPrompt_2017.py",'/uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting')\


ListOfFiles2017Mu  = ["fitDiagnostics.TOY_mu_2017.root"]

line = ""
for ifile in ListOfFiles2017Mu:
    myfile = ROOT.TFile(ifile,"read")
    if myfile.GetListOfKeys().Contains("fit_s") is False:
        print ifile[14:-10], ": Fit failed."
        continue
    fit_s = myfile.Get("fit_s")
    line += "  ttgammaSF_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("r").getVal(),fit_s.floatParsFinal().find("r").getErrorLo(),fit_s.floatParsFinal().find("r").getErrorHi())
    line += "nonPromptSF_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("nonPromptSF").getVal(),fit_s.floatParsFinal().find("nonPromptSF").getErrorLo(),fit_s.floatParsFinal().find("nonPromptSF").getErrorHi())
    line += "    TTbarSF_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("TTbarSF").getVal(),fit_s.floatParsFinal().find("TTbarSF").getErrorLo(),fit_s.floatParsFinal().find("TTbarSF").getErrorHi())
    line += "       WGSF_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("WGSF").getVal(),fit_s.floatParsFinal().find("WGSF").getErrorLo(),fit_s.floatParsFinal().find("WGSF").getErrorHi())
    line += "       ZGSF_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("ZGSF").getVal(),fit_s.floatParsFinal().find("ZGSF").getErrorLo(),fit_s.floatParsFinal().find("ZGSF").getErrorHi())
    line += "    OtherSF_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("OtherSF").getVal(),fit_s.floatParsFinal().find("OtherSF").getErrorLo(),fit_s.floatParsFinal().find("OtherSF").getErrorHi())
    line += " Other_norm_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("Other_norm").getVal(),fit_s.floatParsFinal().find("Other_norm").getErrorLo(),fit_s.floatParsFinal().find("Other_norm").getErrorHi())
    line += ""
    line += "   BTagSF_b_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("BTagSF_b").getVal(),fit_s.floatParsFinal().find("BTagSF_b").getErrorLo(),fit_s.floatParsFinal().find("BTagSF_b").getErrorHi())
    line += "   BTagSF_l_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("BTagSF_l").getVal(),fit_s.floatParsFinal().find("BTagSF_l").getErrorLo(),fit_s.floatParsFinal().find("BTagSF_l").getErrorHi())
    line += "     EleEff_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("EleEff").getVal(),fit_s.floatParsFinal().find("EleEff").getErrorLo(),fit_s.floatParsFinal().find("EleEff").getErrorHi())
    line += "      MuEff_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("MuEff").getVal(),fit_s.floatParsFinal().find("MuEff").getErrorLo(),fit_s.floatParsFinal().find("MuEff").getErrorHi())
    line += "         PU_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("PU").getVal(),fit_s.floatParsFinal().find("PU").getErrorLo(),fit_s.floatParsFinal().find("PU").getErrorHi())
    line += "     PhoEff_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("PhoEff").getVal(),fit_s.floatParsFinal().find("PhoEff").getErrorLo(),fit_s.floatParsFinal().find("PhoEff").getErrorHi())
    line += "         Q2_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("Q2").getVal(),fit_s.floatParsFinal().find("Q2").getErrorLo(),fit_s.floatParsFinal().find("Q2").getErrorHi())
    line += "        fsr_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("fsr").getVal(),fit_s.floatParsFinal().find("fsr").getErrorLo(),fit_s.floatParsFinal().find("fsr").getErrorHi())
    line += "        isr_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("isr").getVal(),fit_s.floatParsFinal().find("isr").getErrorLo(),fit_s.floatParsFinal().find("isr").getErrorHi())
    line += "       lumi_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("lumi").getVal(),fit_s.floatParsFinal().find("lumi").getErrorLo(),fit_s.floatParsFinal().find("lumi").getErrorHi())
    line += "     misIDE_mu_2017 = %.2f [%.2f, %.2f]\n"%(fit_s.floatParsFinal().find("misIDE").getVal(),fit_s.floatParsFinal().find("misIDE").getErrorLo(),fit_s.floatParsFinal().find("misIDE").getErrorHi())

with open("POIsNPs_ToyValues_mu.txt","w") as _file:
    _file.write(line)
