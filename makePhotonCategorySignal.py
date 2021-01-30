from ROOT import *
import os
import sys
from optparse import OptionParser
import CMS_lumi

parser = OptionParser()
parser.add_option("-y", "--year", dest="Year", default="",type='str',
					help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-c", "--channel", dest="channel", default="",type='str',
					help="Specify which channel Mu or Ele? default is Mu" )

parser.add_option("--postfit", dest="postfit", default=False,action="store_true",
					help="draw postfit plots" )

parser.add_option("--tight", dest="tight", default=False,action="store_true",
					help="draw photon Category for tight selection" )

parser.add_option("--looseCRge2ge0", dest="looseCRge2ge0", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 ge0" )

parser.add_option("--looseCRge2e0", dest="looseCRge2e0", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 =0" )

###
parser.add_option("--LooseCRe2e0","--looseCRe2e0", dest="looseCRe2e0", default=False,action="store_true",
                     help="Use ==2 jets + ==0 bjets selection" )  

parser.add_option("--LooseCRe2e1","--looseCRe2e1", dest="looseCRe2e1", default=False,action="store_true",
                     help="Use ==2 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe3e0","--looseCRe3e0", dest="looseCRe3e0", default=False,action="store_true",
                     help="Use ==3 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRge4e0","--looseCRge4e0", dest="looseCRge4e0", default=False,action="store_true",
                     help="Use >=4 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRe3e1","--looseCRe3e1", dest="looseCRe3e1", default=False,action="store_true",
                     help="Use ==3 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe2e2","--looseCRe2e2", dest="looseCRe2e2", default=False,action="store_true",
                     help="Use ==2 jets + ==2 bjets selection" ) 

parser.add_option("--LooseCRe3ge2","--looseCRe3ge2", dest="looseCRe3ge2", default=False,action="store_true",
                     help="Use ==3 jets + >=2 bjets selection" )  
##

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()

finalState = options.channel
tight = options.tight
looseCRge2ge0=options.looseCRge2ge0
looseCRge2e0 =options.looseCRge2e0
looseCRe2e0  =options.looseCRe2e0
looseCRe2e1  =options.looseCRe2e1
looseCRe3e0  =options.looseCRe3e0
looseCRge4e0 =options.looseCRge4e0
looseCRe3e1  =options.looseCRe3e1
looseCRe2e2  =options.looseCRe2e2
looseCRe3ge2 =options.looseCRe3ge2
postfit = options.postfit

gROOT.SetBatch(True)

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"
if tight:      #SR8    
	fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	plotDirectory = "pho_tightplots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"
	if selYear == '2016': MisIDEleSF = 2.208
	elif selYear == '2017': MisIDEleSF = 2.391 
	else: MisIDEleSF = 1.598;

if looseCRge2ge0:  #AR
	fileDir  = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear, channel)
	plotDirectory = "pho_looseCRge2ge0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}#geq0"
	MisIDEleSF =  1#2.25683

if looseCRge2e0:  #CR1+CR2+CR3
	fileDir  = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRge2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}=0"
	MisIDEleSF =  1#2.26355 

###
if looseCRe2e0:  #CR1
	fileDir  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRe2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=0"
	MisIDEleSF = 1#2.34432  

if looseCRe2e1:  #CR4
	fileDir  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
	plotDirectory = "pho_looseCRe2e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=1"
	MisIDEleSF =  1#2.56375

if looseCRe3e0:  #CR2
	fileDir  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRe3e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=0"
	MisIDEleSF =  1#2.03434 

if looseCRge4e0:  #CR3
	fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRge4e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}=0"
	MisIDEleSF =  1#2.65936

if looseCRe3e1:  #CR5
	fileDir  = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
	plotDirectory = "pho_looseCRe3e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=1"
	MisIDEleSF =  1#4.345

if looseCRe2e2:  #CR6
	fileDir  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
	plotDirectory = "pho_looseCRe2e2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=2"
	MisIDEleSF =  1#2.06933

if looseCRe3ge2:  #CR7
	fileDir  = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
	plotDirectory = "pho_looseCRe3ge2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}#geq2"
	MisIDEleSF =  1#2.67638

###


eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"

fileDir = eosFolder + fileDir
print fileDir


if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gStyle.SetOptStat(0)
sampleList = ['TTGamma', 'TTbar','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
category = {"GenuinePhoton":kOrange, "MisIDEle":kRed, "HadronicPhoton":kBlue, "HadronicFake":kGreen+1 }
file = {}


import CMS_lumi


if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"

from Style import *
thestyle = Style()

HasCMSStyle = False
style = None
if os.path.isfile('tdrstyle.C'):
	ROOT.gROOT.ProcessLine('.L tdrstyle.C')
	ROOT.setTDRStyle()
	# print "Found tdrstyle.C file, using this style."
	HasCMSStyle = True
	if os.path.isfile('CMSTopStyle.cc'):
		gROOT.ProcessLine('.L CMSTopStyle.cc+')
		tyle = CMSTopStyle()
		style.setupICHEPv1()
		# print "Found CMSTopStyle.cc file, use TOP style if requested in xml file."
if not HasCMSStyle:
	# print "Using default style defined in cuy package."
	thestyle.SetStyle()

ROOT.gROOT.ForceStyle()

histName    = "phosel_LeadingPhotonEt_%s_%s"
histNameData= "phosel_LeadingPhotonEt_%s"

# histName    = "phosel_noCut_SIEIE_%s_%s"
# histNameData= "phosel_noCut_SIEIE_%s"

# histName    = "phosel_M3_%s_%s"
# histNameData= "phosel_M3_%s"

rebin = 10

if finalState=='Ele':
	sample = "DataEle"
	file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
	dataHist = file[sample].Get(histNameData%(sample))
	dataHist.SetLineColor(kBlack)
	dataHist.SetMarkerStyle(8)
	dataHist.Rebin(rebin)

elif finalState=='Mu':
	sample = "DataMu"
	file[sample] = TFile.Open("%s%s.root"%(fileDir,sample),"read")
	dataHist = file[sample].Get(histNameData%(sample))
	dataHist.SetLineColor(kBlack)
	dataHist.SetMarkerStyle(8)
	dataHist.Rebin(rebin)

else:
	print "Select the channel !!!"
	sys.exit()	

summedHist ={}

for item in category.keys():
	summedHist[item] = None
	for sample in sampleList:
		if finalState == 'Ele' and sample == 'QCD': sample = 'QCDEle'
		if finalState == 'Mu'  and sample == 'QCD': sample = 'QCDMu'
		file[sample] = TFile.Open('%s%s.root'%(fileDir,sample),'read')
		tempHist = file[sample].Get(histName%(item,sample))
		if summedHist[item] is None:
			summedHist[item] = tempHist.Clone(item)
			summedHist[item].SetDirectory(0)
		else:
			summedHist[item].Add(tempHist)
if postfit:
	summedHist['MisIDEle'].Scale(MisIDEleSF)

for ih in summedHist:
	summedHist[ih].Rebin(rebin)
	summedHist[ih].SetLineColor(category[ih])
	summedHist[ih].SetFillColor(category[ih])

stack = THStack()
stack.Add(summedHist['HadronicPhoton'])
stack.Add(summedHist['HadronicFake'])
stack.Add(summedHist['GenuinePhoton'])
stack.Add(summedHist['MisIDEle'])
#stack.SetTitle(';;Events/%sGeV '%rebin)
stack.SetTitle(';;<Events/GeV> ')
###

MisIDEleHist  = summedHist['MisIDEle']
OtherHisttemp = summedHist['GenuinePhoton']
OtherHisttemp.Add(summedHist['HadronicFake'])
OtherHisttemp.Add(summedHist['HadronicPhoton'])
OtherHist     = OtherHisttemp.Clone("OtherHist")
data_obs    = dataHist.Clone("data_obs")

MySumHist = MisIDEleHist.Clone("MySumHist")
MySumHist.Add(OtherHist)
if postfit:
	myfile = TFile(plotDirectory+"myM3_Postfit.root","recreate")
else:
	myfile = TFile(plotDirectory+"myM3_Prefit.root","recreate")

MisIDEleHist.Write()
OtherHist.Write()
data_obs.Write()
MySumHist.Write()
myfile.Close()

# if  stack.GetBinContent(stack.GetMaximumBin()) >= dataHist.GetBinContent(dataHist.GetMaximumBin()): ymax = stack.GetBinContent(stack.GetMaximumBin()) 
# else: ymax = dataHist.GetBinContent(dataHist.GetMaximumBin())
oneLine = TF1("oneline","1",-9e9,9e9)
oneLine.SetLineColor(kBlack)
oneLine.SetLineWidth(1)
oneLine.SetLineStyle(2)
#############
text1 = TPaveText(0.75,.92,.9,1,"NDC")
text1.SetTextColor(kBlack)
text1.SetFillColor(0)
text1.SetTextSize(0.04)
text1.SetTextFont(42)
if selYear == '2016':text1.AddText('35.92 fb^{-1}(13TeV)')
if selYear == '2017':text1.AddText('41.53 fb^{-1}(13TeV)')
if selYear == '2018':text1.AddText('59.74 fb^{-1}(13TeV)')
###################
regionText = regionText
text = TPaveText(0.35,.75,0.45,0.85,"NDC")
text.SetTextColor(kBlack)
text.SetFillColor(0)
text.SetTextSize(0.04)
text.SetTextFont(42)
text.AddText('CMS'); #text.GetListOfLines().Set
text.AddText('Preliminary')
text.AddText(regionText) 
##########################
H = 600;
W = 800;
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

padRatio = 0.25
padOverlap = 0.15
padGap = 0.01
#################
errorband=stack.GetStack().Last().Clone("error")
# errorband.Sumw2()
errorband.SetLineColor(kBlack)
errorband.SetFillColor(kBlack)
errorband.SetFillStyle(3245)
errorband.SetMarkerSize(0)

# legendR.AddEntry(errorband,"Uncertainty","f")
#############################
legendHeightPer = 0.04
legendStart = 0.69
legendEnd = 0.97-(R/W)
legList = ['Data','MisIDEle','GenuinePhoton','HadronicFake','HadronicPhoton','Uncertainty']

legend = TLegend(legendStart , 1-T/H-0.01 - legendHeightPer*(len(legList)+1), legendEnd, 0.99-(T/H)-0.01)

# legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
# legend.SetNColumns(2)
# legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
# legendR.SetNColumns(2)
# legendR.SetBorderSize(0)
# legendR.SetFillColor(0)
legend.SetBorderSize(0)
legend.SetFillColor(0)
# legend = TLegend(0.65,0.65,.88,.9)

legend.AddEntry(dataHist,                    'Data',          'pe')
legend.AddEntry(summedHist['MisIDEle'],      'MisIDEle',      'f')
legend.AddEntry(summedHist['GenuinePhoton'], 'GenuinePhoton', 'f')
legend.AddEntry(summedHist['HadronicFake'],  'HadronicFake',  'f')
legend.AddEntry(summedHist['HadronicPhoton'],'HadronicPhoton','f')
legend.AddEntry(errorband,                   'Uncertainty',   'f')

legend.SetBorderSize(0)
legend.SetFillColor(0)

canvas = TCanvas('c1','c1',W,H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(0)

canvas.cd()
canvas.ResetDrawn()
SetOwnership(stack,True)

pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
pad1.SetLeftMargin( L/W )
pad1.SetRightMargin( R/W )
pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
pad1.SetFillColor(0)
pad1.SetBorderMode(0)
pad1.SetFrameFillStyle(0)
pad1.SetFrameBorderMode(0)
pad1.SetTickx(0)
pad1.SetTicky(0)
pad1.Draw();             
pad1.cd(); 
# pad1.SetLogy()              
stack.Draw('hist')
dataHist.Draw('e1,X0,same')
legend.Draw('same')
text.Draw('same')
text1.Draw('same')
stack.GetHistogram().GetXaxis().SetTickLength(0)
stack.GetHistogram().GetXaxis().SetLabelOffset(999)
# stack.GetHistogram().GetXaxis().SetRangeUser(0,0.03)
#stack.GetHistogram().GetXaxis().SetRangeUser(60,140)

ymax = 0
if stack.GetHistogram().GetBinContent(stack.GetHistogram().GetMaximumBin()) >= dataHist.GetBinContent(dataHist.GetMaximumBin()): 
	ymax = stack.GetHistogram().GetBinContent(stack.GetHistogram().GetMaximumBin())
else: 
	ymax = dataHist.GetBinContent(dataHist.GetMaximumBin())

stack.SetMaximum(ymax*1.1)

pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
pad2.SetLeftMargin( L/W )
pad2.SetRightMargin( R/W )
pad2.SetTopMargin( (padOverlap+.08)/(padRatio+padOverlap) )
pad2.SetBottomMargin( 0.1 )
pad2.SetFillColor(0)
pad2.SetFillStyle(4000)
pad2.SetBorderMode(0)
pad2.SetFrameFillStyle(0)
pad2.SetFrameBorderMode(0)
pad2.SetTickx(0)
pad2.SetTicky(0)
pad2.Draw()
pad2.cd()

ratioHist = dataHist.Clone("ratioHist")
ratioHist.SetLineColor(kBlack)
ratioHist.SetMinimum(0.8)  
ratioHist.SetMaximum(1.2) 
# ratioHist.Sumw2()
ratioHist.SetStats(0)     
h = stack.GetHistogram().Clone('h') 
ratioHist.Divide(h)
ratioHist.SetMarkerStyle(8)
# ratioHist.SetTitle(';Photon SIEIE;Data/MC')
ratioHist.SetTitle(';M3;Data/MC')
ratioHist.SetLabelSize(0.085,'xy')
ratioHist.SetTitleSize(0.09,'xy')
ratioHist.SetTitleOffset(0.48,'y')
ratioHist.SetTitleOffset(1,'x')
ratioHist.SetNdivisions(2,'y')
ratioHist.SetNdivisions(12,'x')

ratioHist.Draw('e,x0') 
# ratioHist.GetXaxis().SetRangeUser(0,0.03)
# ratioHist.GetXaxis().SetRangeUser(60,140)
errorband.Draw('e4,same')
oneLine.Draw("same")

if postfit:
	canvas.SaveAs("%s%s_M3_Postfit.root"%(plotDirectory,plotDirectory[:-1]))
	canvas.Print("%s%s_M3_Postfit.pdf" %(plotDirectory,plotDirectory[:-1]))
else:
	canvas.SaveAs("%s%s_M3.root"%(plotDirectory,plotDirectory[:-1]))
	canvas.Print("%s%s_M3.pdf" %(plotDirectory,plotDirectory[:-1]))
canvas.Close()

# gApplication.Run()
