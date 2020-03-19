import ROOT

ROOT.gROOT.SetBatch(True)
category = {"GenuinePhoton":ROOT.kOrange, "MisIDEle":ROOT.kRed, "HadronicPhoton":ROOT.kBlue, "HadronicFake":ROOT.kGreen+1 }

f1 = ROOT.TFile.Open('root://cmseos.fnal.gov//store/user/npoudyal/histograms_2016/ele/hists_tight/TTbar.root','read')
stack = ROOT.THStack()
legend = ROOT.TLegend(0.7,0.6,0.9,0.9)
hist = None
for item in category.keys():
	hist = f1.Get('phosel_M3_%s_TTbar'%item)
	print item, '==>', hist.Integral(-1,-1)
	hist.Rebin(10)
	hist.SetLineColor(category[item])
	hist.SetFillColor(category[item])
	stack.Add(hist)
	legend.AddEntry(hist,'%s'%item,'f')

canvas = ROOT.TCanvas()
stack.Draw('hist')
legend.Draw('same')
stack.SetTitle('2016,signal region;M3;Events/10 GeV ')	
canvas.Print("fraction.pdf")
