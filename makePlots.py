from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kGreen
#from ROOT import *
import os

import sys
from optparse import OptionParser
from sampleInformation import sampleList
import sampleInformation
from numpy import log10
from array import array

padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
parser = OptionParser()

parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
		help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
		help="Use 4j1t selection" )
		  
parser.add_option("--VeryTight","--verytight", dest="isVeryTightSelection", default=False,action="store_true",
		help="Use 4j2t selection" )
		  
parser.add_option("--Tight0b","--tight0b", dest="isTight0bSelection", default=False,action="store_true",
		help="Use >=4j exactly 0t control region selection" )

##nabin
parser.add_option("--makeNabinPlots", dest="makeNabinPlots",action="store_true",default=False,
		help="Make larger list of plots in histogramDict (mostly object kinematics)" )
##
parser.add_option("--LooseCRge2ge0","--looseCRge2ge0", dest="isLooseCRge2ge0Selection", default=False,action="store_true",
		help="Use >=2 jets + >=0 bjets selection" )  

parser.add_option("--LooseCRge2e0","--looseCRge2e0", dest="isLooseCRge2e0Selection", default=False,action="store_true",
		help="Use >=2 jets + =0 bjets selection" ) 

## today
parser.add_option("--LooseCRe2e0","--looseCRe2e0", dest="isLooseCRe2e0Selection", default=False,action="store_true",
		help="Use ==2 jets + ==0 bjets selection" )  

parser.add_option("--LooseCRe2e1","--looseCRe2e1", dest="isLooseCRe2e1Selection", default=False,action="store_true",
		help="Use ==2 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe3e0","--looseCRe3e0", dest="isLooseCRe3e0Selection", default=False,action="store_true",
		help="Use ==3 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRge4e0","--looseCRge4e0", dest="isLooseCRge4e0Selection", default=False,action="store_true",
		help="Use >=4 jets + ==0 bjets selection" ) 

## 3 more
parser.add_option("--LooseCRe3e1","--looseCRe3e1", dest="isLooseCRe3e1Selection", default=False,action="store_true",
		help="Use ==3 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe2e2","--looseCRe2e2", dest="isLooseCRe2e2Selection", default=False,action="store_true",
		help="Use ==2 jets + ==2 bjets selection" ) 

parser.add_option("--LooseCRe3ge2","--looseCRe3ge2", dest="isLooseCRe3ge2Selection", default=False,action="store_true",
		help="Use ==3 jets + >=2 bjets selection" )  

parser.add_option("--useQCDCR",dest="useQCDCR", default=False, action="store_true",
		help="to make plots in QCDCR region")

parser.add_option("--dilepmassPlots","--dilepmassPlots", dest="Dilepmass",action="store_true",default=False,
		help="Make only plots for ZJetsSF fits" )

parser.add_option("--postfitplot",dest="postfitplot", default=False, action="store_true",
		help="make post fit plots")

parser.add_option("--makePlotsForSF","--makePlotsForSF", dest="makePlotsForSF",action="store_true",default=False,
		help="Extra jets" )
##nabin       

parser.add_option("--makePhotonSplitplots", dest="makePhotonSplitplots",action="store_true",default=False,
					 help="" )
					 
					                                    
parser.add_option("--LooseCRe3g1","--looseCRe3g1", dest="isLooseCRe3g1Selection", default=False,action="store_true",
		help="Use 3j exactly 0t control region selection" )
parser.add_option("--LooseCRe3g0","--looseCRe3g0", dest="isLooseCRe3g0Selection", default=False,action="store_true",
		help="Use exactly 3j with 0btag control region selection" )
parser.add_option("--LooseCR2g0","--looseCR2g0", dest="isLooseCR2g0Selection", default=False,action="store_true",
		help="Use 2j at least 0t control region selection" )
parser.add_option("--LooseCR2g1","--looseCR2g1", dest="isLooseCR2g1Selection", default=False,action="store_true",
		help="Use 2j at least 1t control region selection" )
parser.add_option("--overflow", dest="useOverflow",default=False,action="store_true",
		help="Add oveflow bin to the plots" )
parser.add_option("--plot", dest="plotList",action="append",
		help="Add plots" )
parser.add_option("--makeSignalRegionPlots",dest="makeSignalRegionPlots",action="store_true",default=False,
		help="Make larger list of kinematic distributions" )
parser.add_option("--allPlots","--allPlots",dest="makeAllPlots",action="store_true",default=False,
		help="Make plots of all distributions" )
parser.add_option("--file",dest="inputFile",default=None,
		help="Specify specific input file")
parser.add_option("--useQCDMC","--qcdMC",dest="useQCDMC", default=False, action="store_true",
		help="")
parser.add_option("--noQCD",dest="noQCD", default=False, action="store_true",
		help="")

parser.add_option("--reorderTop", dest="newStackListTop",action="append",
		help="New order for stack list (which plots will be put on top of the stack)" )
parser.add_option("--reorderBot", dest="newStackListBot",action="append",
		help="New order for stack list (which plots will be put on top of the stack)" )

parser.add_option("-y", "--year", dest="Year", default="",type='str',
		help="Specify which year 2016, 2017 or 2018?" )

(options, args) = parser.parse_args()


selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()


samples = sampleInformation.main([selYear])
Dilepmass = options.Dilepmass
isTightSelection = options.isTightSelection
isVeryTightSelection = options.isVeryTightSelection
isTight0bSelection = options.isTight0bSelection
# nabin added sth
makeNabinPlots = options.makeNabinPlots
##
postfitplot = options.postfitplot
isLooseCRge2ge0Selection = options.isLooseCRge2ge0Selection
isLooseCRge2e0Selection  = options.isLooseCRge2e0Selection
##
isLooseCRe2e0Selection   = options.isLooseCRe2e0Selection
isLooseCRe2e1Selection   = options.isLooseCRe2e1Selection
isLooseCRe3e0Selection   = options.isLooseCRe3e0Selection
isLooseCRge4e0Selection  = options.isLooseCRge4e0Selection
## 3 more
isLooseCRe3e1Selection  = options.isLooseCRe3e1Selection
isLooseCRe2e2Selection  = options.isLooseCRe2e2Selection
isLooseCRe3ge2Selection = options.isLooseCRe3ge2Selection
useQCDMC = options.useQCDMC
useQCDCR = options.useQCDCR
makePlotsForSF = options.makePlotsForSF

makePhotonSplitplots = options.makePhotonSplitplots
#
isLooseCR2g0Selection = options.isLooseCR2g0Selection
isLooseCR2g1Selection = options.isLooseCR2g1Selection
isLooseCRe3g1Selection = options.isLooseCRe3g1Selection
isLooseCRe3g0Selection = options.isLooseCRe3g0Selection
plotList = options.plotList

newStackListTop = options.newStackListTop
newStackListBot = options.newStackListBot

useOverflow = options.useOverflow

inputFile = options.inputFile
noQCD = options.noQCD
makeSignalRegionPlots = options.makeSignalRegionPlots
makeAllPlots = options.makeAllPlots

finalState = options.channel

print "Running on the %s channel"%(finalState)
if finalState=='Mu':
	_fileDir = "histograms_%s/mu/hists/"%(selYear)
	plotDirectory = "plots_mu_%s/"%(selYear)
	regionText = ", N_{j}#geq3, N_{b}#geq1"
	dir_=""
	channel = 'mu'
	# if useQCDCR:
	# 	_fileDir = "histograms_%s/mu/qcdhistsCR_tight/"%(selYear)
	# 	plotDirectory = "plots_mu_QCDCR_%s/"%(selYear)
	# 	regionText = ", QCD CR"

#/store/user/aldas/histograms_*/ele/hists_*/QCD_DD.root

if finalState=="Ele":
	_fileDir = "histograms_%s/ele/hists/"%(selYear)
	plotDirectory = "plots_ele_%s/"%(selYear)
	regionText = ", N_{j}#geq3, N_{b}#geq1"
	dir_=""
	channel = 'ele'
	# if useQCDCR:
 #                _fileDir = "histograms_%s/qcdhistsCR_tight/"%(selYear)
 #                plotDirectory = "plots_ele_QCDCR_%s/"%(selYear)
 #                regionText = ", QCD CR"

if finalState=="DiEle":
	channel = 'ele'
elif finalState=="DiMu":
	channel = 'mu'

#print channel

if isVeryTightSelection:
	plotDirectory = "verytightplots_%s_%s/"%(channel, selYear)
	_fileDir = "histograms_%s/%s/hists_verytight/"%(selYear,channel)
	regionText = ", N_{j}#geq4, N_{b}#geq2"
	
if isTight0bSelection:
	plotDirectory = "tight0bplots_%s_%s/"%(channel,selYear)
	_fileDir = "histograms_%s/%s/hists_tight0b/"%(selYear,channel)
	regionText = ", N_{j}#geq4, N_{b}=0"
		
##nabin start

if isTightSelection:
	dir_= "tight"
	if Dilepmass:
		plotDirectory = "tightplots_%s_%s_Dilep/"%(channel, selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_tight/"%(selYear,channel)
		regionText = ", N_{j}#geq4, N_{b}#geq1"
	else:
		plotDirectory = "tightplots_%s_%s/"%(channel, selYear)
		_fileDir = "histograms_%s/%s/hists_tight/"%(selYear,channel)
		regionText = ", N_{j}#geq4, N_{b}#geq1"
			 
if isLooseCRge2ge0Selection:
	dir_= "looseCRge2ge0"
	if Dilepmass:
		plotDirectory = "looseCRge2ge0plots_%s_%s_Dilep/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_looseCRge2ge0/"%(selYear,channel)
		regionText = ", N_{j}#geq2, N_{b}=0"
	else:    
		plotDirectory = "looseCRge2ge0plots_%s_%s/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear,channel)
		regionText = ", N_{j}#geq2, N_{b}=0"
		
if isLooseCRge2e0Selection: # 
	dir_= "looseCRge2e0"
	if Dilepmass:
		plotDirectory = "looseCRge2e0plots_%s_%s_Dilep/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_looseCRge2e0/"%(selYear,channel)
		regionText = ", N_{j}#geq2, N_{b}=0"
	else:   
		plotDirectory = "looseCRge2e0plots_%s_%s/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear,channel)
		regionText = ", N_{j}#geq2, N_{b}=0"

if isLooseCRe2e0Selection:
	dir_= "looseCRe2e0"
	if Dilepmass:
		plotDirectory = "looseCRe2e0plots_%s_%s_Dilep/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_looseCRe2e0/"%(selYear,channel)
		regionText = ", N_{j}=2, N_{b}=0"
	else:   
		plotDirectory = "looseCRe2e0plots_%s_%s/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear,channel)
		regionText = ", N_{j}=2, N_{b}=0"

if isLooseCRe3e0Selection:
	dir_= "looseCRe3e0"
	if Dilepmass:
		plotDirectory = "looseCRe3e0plots_%s_%s_Dilep/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_looseCRe3e0/"%(selYear,channel)
		regionText = ", N_{j}=3, N_{b}=0"
	else:   
		plotDirectory = "looseCRe3e0plots_%s_%s/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear,channel)
		regionText = ", N_{j}=3, N_{b}=0"


if isLooseCRge4e0Selection:
	dir_= "looseCRge4e0"
	if Dilepmass:
		plotDirectory = "looseCRge4e0plots_%s_%s_Dilep/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_looseCRge4e0/"%(selYear,channel)
		regionText = ", N_{j}#geq4, N_{b}=0"
	else:   
		plotDirectory = "looseCRge4e0plots_%s_%s/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear,channel)
		regionText = ", N_{j}#geq4, N_{b}=0"
				
if isLooseCRe2e1Selection:
	dir_= "looseCRe2e1"
	if Dilepmass:
		plotDirectory = "looseCRe2e1plots_%s_%s_Dilep/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_looseCRe2e1/"%(selYear,channel)
		regionText = ", N_{j}=2, N_{b}=1"
	else:   
		plotDirectory = "looseCRe2e1plots_%s_%s/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear,channel)
		regionText = ", N_{j}=2, N_{b}=1"

if isLooseCRe3e1Selection:
	dir_= "looseCRe3e1"
	if Dilepmass:
		plotDirectory = "looseCRe3e1plots_%s_%s_Dilep/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_looseCRe3e1/"%(selYear,channel)
		regionText = ", N_{j}=3, N_{b}=1"
	else:   
		plotDirectory = "looseCRe3e1plots_%s_%s/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear,channel)
		regionText = ", N_{j}=3, N_{b}=1"

if isLooseCRe2e2Selection:
	dir_= "looseCRe2e2"
	if Dilepmass:
		plotDirectory = "looseCRe2e2plots_%s_%s_Dilep/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_looseCRe2e2/"%(selYear,channel)
		regionText = ", N_{j}=2, N_{b}=2"
	else:   
		plotDirectory = "looseCRe2e2plots_%s_%s/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear,channel)
		regionText = ", N_{j}=2, N_{b}=2"

if isLooseCRe3ge2Selection:
	dir_= "looseCRe3ge2"
	if Dilepmass:
		plotDirectory = "looseCRe3ge2plots_%s_%s_Dilep/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/Dilep_hists_looseCRe3ge2/"%(selYear,channel)
		regionText = ", N_{j}=3, N_{b}#geq2"
	else:   
		plotDirectory = "looseCRe3ge2plots_%s_%s/"%(channel,selYear)
		_fileDir = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear,channel)
		regionText = ", N_{j}=3, N_{b}#geq2"

###		end nabin


if isLooseCR2g0Selection:
	plotDirectory = "looseplots_%s_CR2g0_%s/"%(channel,selYear)
	_fileDir = "histograms_%s/%s/hists_looseCR2g0/"%(selYear,channel)
	regionText = ", N_{j}=2, N_{b}#geq0"
if isLooseCR2g1Selection:
	plotDirectory = plotDirectory+"_looseCR2g1_/"
	_fileDir = _fileDir+"_looseCR2g1"
	dir_="_looseCR2g1"
	regionText = ", N_{j}#geq2, N_{b}#geq1"

if isLooseCRe3g1Selection:
	plotDirectory =  plotDirectory+"_looseCRe3g1_"
	_fileDir = "histograms_%s/ele/hists_looseCRe3g1/"%(selYear)
	dir_="_looseCRe3g1"
	regionText = ", N_{j}=3, N_{b}#geq1"

if isLooseCRe3g0Selection:
		plotDirectory =  "plots_looseCRe3g0_"
		_fileDir = "histograms_%s/ele/hists_looseCRe3g0/"%(selYear)
		dir_="_looseCRe3g0"
		regionText = ", N_{j}=3, N_{b}=0"

if not inputFile is None:
	_fileDir = "histograms_%s/%s/%s"%(selYear,channel,inputFile)
	if not _file.IsOpen():
		print "Unable to open file"
		sys.exit()

# if finalState=='DiMu':
#         _fileDir = "histograms_%s/mu/dilephists"%(selYear)
#         plotDirectory = "plots_mu_%s"%(selYear)
#         regionText = ", N_{j}#geq3, N_{b}#geq1"
# 	dir_=""
#         channel = 'mu'
#         if isTightSelection:
#                 _fileDir = "histograms_%s/mu/dilephists_tight"%(selYear)
# 		_dir="_tight"
#                 plotDirectory = "tightplots_mu_%s"%(selYear)
#                 regionText = ", N_{j}#geq4, N_{b}#geq1"

# if finalState=="DiEle":
#         _fileDir = "histograms_%s/ele/dilephists"%(selYear)
# 	_dir=""
#         plotDirectory = "plots_ele_%s"%(selYear)
#         regionText = ", N_{j}#geq3, N_{b}#geq1"
#         channel = 'ele'
#         if isTightSelection:
#                 _fileDir = "histograms_%s/ele/dilephists_tight"%(selYear)
# 		_dir="_tight"
#                 plotDirectory = "tightplots_ele_%s"%(selYear)
#                 regionText = ", N_{j}#geq4, N_{b}#geq1"

eosFolder="root://cmseos.fnal.gov//store/user/npoudyal/"
_fileDir = eosFolder+_fileDir

print _fileDir

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)


gROOT.SetBatch(True)

YesLog = True
NoLog=False

# Histogram Information:
# [X-axis title, 
#  Y-axis title,
#  Rebinning factor,
#  [x-min,x-max], -1 means keep as is
#  Extra text about region
#  log plot]

histograms_dilep = {"presel_DilepMass"   : ["m_(lepton,lepton) (GeV)", "<Events/GeV>",2 , [70,130], regionText, NoLog, " "],
					"phosel_DilepMass"   : ["m_(lepton,lepton) (GeV)", "<Events/GeV>", [20., 30., 40., 50., 60., 70., 85., 95., 110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240., 250., 260., 270.], [-1,-1], regionText, NoLog, " "]
		}

histograms = {
		"presel_jet1Pt"   :     ["Leading Jet Pt (GeV)", "Events", 5, [30,400], regionText, YesLog, " "],
		#"phosel_jet1Pt"   :     ["Leading Jet Pt (GeV)", "Events", 5, [30,400], regionText, YesLog, " "],
		"presel_jet2Pt"   :     ["Second Jet Pt (GeV)" , "Events", 5, [30,400], regionText, YesLog, " "],
		"presel_jet3Pt"   :     ["Third Jet Pt (GeV)"  , "Events", 5, [30,400], regionText, YesLog, " "],
		"presel_jet4Pt"   :     ["Fourth Jet Pt (GeV)"  , "Events", 5, [30,400], regionText, YesLog, " "],
		"presel_muPt"     :     ["Muon p_{T} (GeV)"    , "Events/5 GeV", 5, [30,200], regionText,  NoLog, " "],
		"presel_muEta"    :     ["Muon #eta"           , "Events/0.05", 5, [-2.4,2.4], regionText,  NoLog, " "],
		"presel_muPhi"    :     ["Muon #phi"           , "Events/0.06", 5, [-1,-1], regionText,  NoLog, " "],
		"presel_elePt"    :     ["Electron p_{T} (GeV)", "Events/5 GeV", 5, [35.,200.], regionText,  NoLog, " "],
		"presel_eleSCEta" : ["Electron #eta"       , "Events/0.04", 4, [-2.1,2.1], regionText,  NoLog, " "],
		"presel_elePhi"   : ["Electron #phi"       , "Events/0.06", 5, [-1,-1], regionText,  NoLog, " "],
		"presel_Njet"     : ["N Jets"              , "Events", 1, [2,10], regionText,  NoLog, " "],
		"presel_Nbjet"    : ["N B-Jets"            , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		#"presel_M3"       : ["M_{3} (GeV)"         , "<Events/GeV>", [60., 80., 100, 110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240., 250., 260., 270., 280., 290., 300., 310., 320., 330., 340., 350., 360., 370., 380., 390., 400., 420., 440., 460., 480., 500.], [-1,-1], regionText,  NoLog, " "],

		"presel_M3_control": ["Events"         , "Events", 550 ,[-1,-1],  regionText,  NoLog, " "],
		"presel_MET"      : ["MET (GeV)  "         , "Events/2 GeV", 5, [-1,-1], regionText,  NoLog, " "],
		"presel_WtransMass"     : ["W transverse mass (GeV)  ", "Events/5 GeV", 5, [-1,-1], regionText,  NoLog, " "],
		"presel_HT"       :["H_{T} (GeV)","Events", 5, [180,1000], regionText,  NoLog, " "],
		"presel_nVtx"     : ["N Vtx nominal"       , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		"presel_nVtxup"   : ["N Vtx up"               , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		"presel_nVtxdo"   : ["N Vtx down"               , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		"presel_nVtxNoPU" : ["N Vtx noPU"               , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		## nabin
		"phosel_LeadingPhotonEt"               : ["Photon Et (GeV)"                  , "Events", 2, [0,300], regionText,  NoLog, " "],     
		"phosel_LeadingPhotonEt_GenuinePhoton" : ["GenuinePhoton Et (GeV)"           , "Events", 5, [0,300], regionText,  NoLog, " "],   
		"phosel_LeadingPhotonEt_MisIDEle"      : ["MisIDElePhoton Et (GeV)"          , "Events", 5, [0,300], regionText,  NoLog, " "],   
		"phosel_LeadingPhotonEt_HadronicPhoton": ["HadronicPhoton Et (GeV)"          , "Events", 5, [0,300], regionText,  NoLog, " "],   
		"phosel_LeadingPhotonEt_HadronicFake"  : ["HadronicFakePhoton Et (GeV)"      , "Events", 5, [0,300], regionText,  NoLog, " "], 
		
		"phosel_LeadingPhotonPhi"               : ["Photon Phi "         , "Events", 2, [-4,4],     regionText,  NoLog, " "],   
		"phosel_LeadingPhotonEta"               : ["Photon Eta "         , "Events", 2, [-2.5,2.5], regionText,  NoLog, " "],  
		
		
		  ## nabin
		  

		"phosel_LeadingPhotonEt_barrel"         : ["Photon Et (GeV)"          , "Events", 5, [20,150], regionText,  NoLog, " "],
		#"phosel_SecondLeadingPhotonEt"          : ["Photon Phi (GeV)"         , "Events", 1, [-1,-1], regionText,  NoLog, " "],    
 
		"phosel_LeadingPhotonSCEta"             : ["Photon SCEta (GeV)"       , "Events/0.1", 1, [-1,-1], regionText,  NoLog, " "], 
		"phosel_LeadingPhotonEta_barrel"               : ["Photon Eta (GeV)"         , "Events/0.1", 1, [-1.47,1.47], regionText,  NoLog, " "],
		"phosel_LeadingPhotonSCEta_barrel"             : ["Photon SCEta (GeV)"       , "Events/0.1", 1, [-1.47,1.47], regionText,  NoLog, " "],	
		#"phosel_dRLeadingPhotonLepton"          : ["dR(LeadingPhoton,Lepton)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, " "],
		"phosel_dRLeadingPromptPhotonLepton"    : ["dR(LeadingPhoton,Lepton)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, "Prompt Photon"],
		#"phosel_dRLeadingNonPromptPhotonLepton" : ["dR(LeadingPhoton,Lepton)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, "NonPrompt Photon"],
		#"phosel_dRLeadingPhotonJet"             : ["dR(LeadingPhoton,Jet)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, " "],  
		"phosel_dRLeadingPromptPhotonJet"       : ["dR(LeadingPhoton,Jet)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, "Prompt Photon"],
		#"phosel_dRLeadingNonPromptPhotonJet"    : ["dR(LeadingPhoton,Jet)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, "NonPrompt Photon"],
		"phosel_dRLeadingGenuinePhotonLepton"   : ["dR(LeadingPhoton,Jet)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, "Genuine"],
		"phosel_dRLeadingMisIDEleLepton"        : ["dR(LeadingPhoton,Jet)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, "MisIDEle"],
		"phosel_dRLeadingHadronicPhotonLepton"          : ["dR(LeadingPhoton,Jet)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, "Hadronic Photon"],
		"phosel_dRLeadingHadronicFakeLepton"         : ["dR(LeadingPhoton,Jet)" , "Events/0.025", 2, [-1,-1], regionText,  NoLog, "Hadronic Fake"],
		#"phosel_WtransMass"              : ["W transverse mass GeV "        , "Events/5 GeV", 5, [-1,-1], regionText,  NoLog, " "],
		"phosel_Nphotons"                : ["Number of Photons "            , "Events", 1, [-1,-1], regionText,  YesLog, " "],
		"phosel_Nphotons_barrel"         : ["Number of Photons "            , "Events", 1, [1,3], regionText,  YesLog, " "],
		"phosel_HT_barrel"               : ["H_{T} (GeV)"                ,"Events",  5, [180,1000], regionText,  NoLog, " "],
		"phosel_MET"                     : ["MET (GeV)  "                , "Events/2", 5, [-1,-1], regionText,  NoLog, " "],
		"phosel_M3_gamma"                : ["M3(ttbar+#gamma) GeV"       ,"Events",10,[50,1000],regionText,  NoLog, " "],
		"phosel_Mbjj_gamma"              : ["Reconstructed Top quark mass+#gamma GeV" ,"Events",10,[50,1000],regionText,  YesLog, " "],
		"phosel_M3_barrel"               : ["M_{3} (GeV)"                , "Events/20 GeV", [60., 80., 100, 110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240., 250.,260.,270.,280.,290.,300.,310.,320.,330.,340.,350.,360.,370.,380.,390., 400., 420.,440.,460., 480., 500.], [60,500],regionText,  NoLog, " "],   
		"phosel_M3_endcap"               : ["M_{3} (GeV)"                , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, " "],   
		  
		"phosel_M3_GenuinePhoton_barrel"  : ["M_{3} (GeV)"                , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "Genuine Photon"],   
		"phosel_M3_MisIDEle_barrel"       : ["M_{3} (GeV)"                , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "MisIDEle"],
		"phosel_M3_HadronicPhoton_barrel" : ["M_{3} (GeV)"                , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "Hadronic Photon"],
		"phosel_M3_HadronicFake_barrel"   : ["M_{3} (GeV)"                , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "Hadronic Fake"],
		"phosel_M3_GenuinePhoton_endcap"  : ["M_{3} (GeV)"                , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "Genuine Photon"],   
		"phosel_M3_MisIDEle_endcap"       : ["M_{3} (GeV)"                , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "MisIDEle"],
		"phosel_M3_HadronicPhoton_endcap" : ["M_{3} (GeV)"                , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "Hadronic Photon"],
		"phosel_M3_HadronicFake_endcap"   : ["M_{3} (GeV)"                , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "Hadronic Fake"],

		"phosel_muEta"                   : ["Muon #eta"                  , "Events/0.05", 5, [-2.4,2.4], regionText,  NoLog, " "],
		#"phosel_muPt_barrel"    		       : ["Muon p_{T} (GeV) "          , "Events", 5, [30,200], regionText,  NoLog, " "],
		#"phosel_elePt_barrel"                   : ["Electron p_{T} (GeV)"       , "Events", 15,[35.,200.], regionText,  NoLog, " "],
		"phosel_muPt"    		       : ["Muon p_{T} (GeV) "          , "Events", 5, [30,200], regionText,  NoLog, " "],
		"phosel_elePt"                   : ["Electron p_{T} (GeV)"       , "Events", 5,[35,200.], regionText,  NoLog, " "],
		"phosel_eleSCEta"                : ["Electron SC#eta"            , "Events/0.04", 4, [-2.1,2.1], regionText,  NoLog, " "],
		"phosel_Njet"                    : ["N Jets"                     , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		"phosel_Njet_barrel"                    : ["N Jets"                     , "Events", 1, [4,10], regionText,  NoLog, " "],
		"phosel_Nbjet"                   : ["N B-Jets"                   , "Events",1, [-1,1], regionText,  NoLog, " "],
		"phosel_HoverE_barrel"           : ["H over E"                   , "Events/0.004", 10, [0,0.4], regionText, YesLog, " "],
		"phosel_SIEIE_barrel"                   : ["Sigma Ieta Ieta"            , "Events/0.0003", 1, [-1,-1], regionText, YesLog, " "],
		"phosel_ChIso_barrel"                   : ["Charged Hadron Iso (GeV)"   , "Events/0.005", 1, [0,0.441], regionText, YesLog, " "],
		"phosel_NeuIso_barrel"                  : ["Neutral Hadron Iso (GeV)"   , "Events/0.05", 1,  [0,3.5], regionText, YesLog, " "],
		"phosel_nVtx_barrel"     : ["N Vtx nominal"            , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		"phosel_nVtxup_barrel"   : ["N Vtx up"                 , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		"phosel_nVtxdo_barrel"   : ["N Vtx down"               , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		#"phosel_nVtxNoPU_barrel" : ["N Vtx noPU"               , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		"phosel_PhoIso_barrel"   : ["Photon Iso (GeV)"         , "Events/0.1", 1, [0,2.9], regionText, YesLog, " "],
		"phosel_noCut_HoverE_barrel"            : ["H over E"                   , "Events/0.002", 1, [-1,-1], regionText, YesLog, " "],
		"phosel_noCut_SIEIE_barrel"             : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog, " "],
		"phosel_noCut_SIEIE_GenuinePho"  : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog, "Genuine Photon"],
		"phosel_noCut_SIEIE_MisIDEle"    : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog,"MisIDEle"],
		#"phosel_noCut_SIEIE_HadPho"      : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog, "Hadronic Photon"],
		#"phosel_noCut_SIEIE_HadFake"     : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog, "Hadronic Fake"],
		"phosel_noCutSIEIEChIso_GenuinePho_barrel" :["Charged Hadron Iso (GeV)"  , "Events", 1, [-1,-1], regionText, YesLog, "Genuine Photon"],
		  "phosel_noCutSIEIEChIso_GenuinePho_endcap" :["Charged Hadron Iso (GeV)"            , "Events", 1, [-1,-1], regionText, YesLog, "Genuine Photon"],
		  "phosel_noCutSIEIEChIso_MisIDEle_barrel": ["Charged Hadron Iso (GeV)"           , "Events", 1, [-1,-1], regionText, YesLog,"MisIDEle"],
		  "phosel_noCutSIEIEChIso_MisIDEle_endcap": ["Charged Hadron Iso (GeV)"            , "Events", 1, [-1,-1], regionText, YesLog,"MisIDEle"],
		#"phosel_noCutSIEIEChIso_HadPho_barrel": ["Charged Hadron Iso (GeV)"            , "Events", 1, [-1,-1], regionText, YesLog, "Hadronic Photon"],
		"phosel_noCutSIEIEChIso_HadPho_endcap": ["Charged Hadron Iso (GeV)"            , "Events", 1, [-1,-1], regionText, YesLog, "Hadronic Photon"],
		#"phosel_noCutSIEIEChIso_HadFake_barrel": ["Charged Hadron Iso (GeV)"            , "Events", 1, [-1,-1], regionText, YesLog, "Hadronic Fake"],
		"phosel_noCutSIEIEChIso_HadFake_endcap": ["Charged Hadron Iso (GeV)"            , "Events", 1, [-1,-1], regionText, YesLog, "Hadronic Fake"],
		"phosel_noCutSIEIEChIso" : ["Charged Hadron Iso (GeV)"            , "Events", 1, [-1,-1], regionText, YesLog, " "],
		#	      "phosel_noCut_ChIso"             : ["Charged Hadron Iso (GeV)"   , "Events/0.25", 1, [-1,-1], regionText, NoLog, " "],
		"phosel_noCut_ChIso"             : ["Charged Hadron Iso (GeV)"   , "<Events/GeV>", [0.,0.1,1.,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.,20.], [-1,-1], regionText, YesLog, " "],
		"phosel_noCut_ChIso_barrel"      : ["Charged Hadron Iso (GeV)"   , "<Events/GeV>", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, YesLog, " "],
		"phosel_noCut_ChIso_endcap"      : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, NoLog, " "],
		####
		"phosel_noCut_ChIso_GenuinePhoton": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, YesLog, "Genuine Photon"],
		"phosel_noCut_ChIso_MisIDEle"    : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, YesLog, "MisIDEle"],
		"phosel_noCut_ChIso_HadronicPhoton": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, YesLog, "Hadronic Photon"],
		"phosel_noCut_ChIso_HadronicFake": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, YesLog, "Hadronic Fake"],


		"phosel_noCut_ChIso_GenuinePhoton_barrel": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, YesLog, "Genuine Photon"],
		"phosel_noCut_ChIso_MisIDEle_barrel"    : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, YesLog, "MisIDEle"],
		"phosel_noCut_ChIso_HadronicPhoton_barrel": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, YesLog, "Hadronic Photon"],
		"phosel_noCut_ChIso_HadronicFake_barrel": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, YesLog, "Hadronic Fake"],

		"phosel_noCut_ChIso_GenuinePhoton_endcap": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, YesLog, "Genuine Photon"],
		"phosel_noCut_ChIso_MisIDEle_endcap"    : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, YesLog, "MisIDEle"],
		"phosel_noCut_ChIso_HadronicPhoton_endcap": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, YesLog, "Hadronic Photon"],
		"phosel_noCut_ChIso_HadronicFake_endcap": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, YesLog, "Hadronic Fake"],

		"phosel_noCut_ChIso_PromptPhoton": ["Charged Hadron Iso (GeV)"   , "Events/0.25", 1, [-1,-1], regionText, YesLog, "Prompt Photon"],
		"phosel_noCut_ChIso_NonPromptPhoton": ["Charged Hadron Iso (GeV)"   , "Events/0.25", 1, [-1,-1], regionText, YesLog, "NonPrompt Photon"],

		"phosel_noCut_ChIso_PUdown"             : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, NoLog, " "],
		"phosel_noCut_ChIso_PUup"               : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, NoLog, " "],
		"phosel_noCut_ChIso_0nVtx15"               : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, NoLog, " "],
		"phosel_noCut_ChIso_15nVtx20"               : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, NoLog, " "],
		"phosel_noCut_ChIso_20nVtx25"               : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, NoLog, " "],
		"phosel_noCut_ChIso_25nVtx50"               : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, NoLog, " "],



		# "phosel_noCut_PhoIso"            : ["Photon Iso (GeV)"           , "<Events/GeV>", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText, YesLog, " "], [-1,-1], regionText, YesLog, " "],
		"phosel_noCut_NeuIso_barrel"            : ["Neutral Hadron Iso (GeV)"   , "<Events/GeV>", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10], [-1,-1], regionText, YesLog, " "],
		"phosel_noCut_PhoIso_barrel"            : ["Photon Iso (GeV)"           , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10], [-1,-1], regionText, YesLog, " "],
		"phosel_AntiSIEIE_ChIso"         : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText,  NoLog, " "],
		"phosel_AntiSIEIE_ChIso_barrel"  : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText,  NoLog, " "],
		"phosel_AntiSIEIE_ChIso_endcap"  : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText,  NoLog, " "],
		"phosel_AntiSIEIE_ChIso_GenuinePhoton_barrel": ["Charged Hadron Iso (GeV)"   , "Events",  [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText,  NoLog, "Genuine Photon"],
		"phosel_AntiSIEIE_ChIso_GenuinePhoton_endcap": ["Charged Hadron Iso (GeV)"   , "Events",  [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.], [-1,-1], regionText,  NoLog, "Genuine Photon"],
		"phosel_AntiSIEIE_ChIso_MisIDEle_barrel": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.] , [-1,-1], regionText,  NoLog, "MisIDEle"],    

		"phosel_AntiSIEIE_ChIso_MisIDEle_endcap": ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.] , [-1,-1], regionText,  NoLog, "MisIDEle"],
		"phosel_AntiSIEIE_ChIso_HadronicPhoton_barrel"  : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.] , [-1,-1], regionText,  NoLog,"Hadronic Photon"],       
		"phosel_AntiSIEIE_ChIso_HadronicPhoton_endcap"  : ["Charged Hadron Iso (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.] , [-1,-1], regionText,  NoLog,"Hadronic Photon"],
		"phosel_AntiSIEIE_ChIso_HadronicFake_barrel" : ["Charged Hadron Iso HadFake (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.] , [-1,-1], regionText,  NoLog, "Hadronic Fake"],
		"phosel_AntiSIEIE_ChIso_HadronicFake_endcap" : ["Charged Hadron Iso HadFake (GeV)"   , "Events", [0.,0.1,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.] , [-1,-1], regionText,  NoLog, "Hadronic Fake"],
		"phosel_noCut_SIEIE_endcap"      : ["Sigma Ieta Ieta"            , "Events/0.0005", 5, [0.015,0.07], regionText,  NoLog, "Endcap"],
		"phosel_noCut_SIEIE_barrel"      : ["Sigma Ieta Ieta"            , "Events/0.0005", 5, [0.008,0.028], regionText,  NoLog, "Barrel"],
		"phosel_noCut_SIEIE_noChIso_barrel":["Sigma Ieta Ieta"            , "Events/0.0005", 5, [0.008,0.028], regionText,  NoLog, "Barrel"],
		"phosel_mcMomPIDGenuinePho"      : ["ParentPID of GenuinePho"  , "Events", 1, [-25,25], regionText,  YesLog, ""],
		"phosel_mcMomPIDMisIDEle"        : ["ParentPID of MisIDEle"    , "Events", 1, [-1,-1], regionText,  YesLog, "MisIDEle"],
		#"phosel_mcMomPIDHadPho"          : ["ParentPID of HadronicPho" , "Events", 1, [-1000,600], regionText, YesLog, "Hadronic Photon"],
		#"phosel_mcMomPIDHadFake"         : ["ParentPID of HadronicFake", "Events", 1, [-1,-1], regionText,  YesLog, "Hadronic Fake"],
		#  "phosel_RandomCone"              : ["RandomConeIsolation GeV"  , "Events", 1, [-1,-1], regionText,  NoLog, " "],
		"phosel_PhotonCategory_barrel"          : ["Photon Category","Events", 1, [-1,-1], regionText,  NoLog, " "],
		#"phosel_MassEGamma_barrel"       : ["m_{e,#gamma} GeV"  , "Events/10 GeV", [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185], [25,185], regionText,  NoLog, " "],

		#"phosel_MassEGamma"              : ["m_{e,#gamma} GeV"  , "Events/10 GeV", [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175], [-1,-1], regionText,  NoLog, " "],
		#"phosel_MassEGammaMisIDEle"              : ["m_{e,#gamma(misIDEle)} GeV"  , "Events/10 GeV", [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175], [-1,-1], regionText,  NoLog, " "],
		#"phosel_MassEGammaOthers"              : ["m_{e,#gamma(others)} GeV"  , "Events/10 GeV", [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175], [-1,-1], regionText,  NoLog, " "],

		# "phosel_MassEGamma"              : ["m_{e,#gamma} GeV",           "Events/3 GeV", 3, [60,140], regionText,  NoLog, " "],
		"phosel_MassEGammaMisIDEle"      : ["m_{e,#gamma(misIDEle)} GeV", "Events/3 GeV", 3, [60,140], regionText,  NoLog, " "],
		"phosel_MassEGammaOthers"        : ["m_{e,#gamma(others)} GeV",   "Events/3 GeV", 3, [60,140], regionText,  NoLog, " "],
		"phosel_MassLepGamma"            : ["m_{lepton,#gamma} GeV"    , "Events", 5, [-1,-1], regionText,  NoLog, " "],
		"phosel_R9_barrel"  :["R9","Events",1,[-1,-1],regionText,  NoLog, " "],

		"phosel_noCut_SIEIE"      : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog, " "],
		"phosel_noCut_SIEIE_GenuinePhoton"  : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog, "Genuine Photon"],
		"phosel_noCut_SIEIE_MisIDEle"    : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog,"MisIDEle"],
		"phosel_noCut_SIEIE_HadronicPhoton"      : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog, "Hadronic Photon"],
		"phosel_noCut_SIEIE_HadronicFake"     : ["Sigma Ieta Ieta"            , "Events/0.0007", 1, [-1,-1], regionText, YesLog, "Hadronic Fake"],

		"phosel_MassEGamma"                             : ["m_{e,#gamma} GeV",           "Events/2 GeV", 2, [50,140], regionText,  NoLog, " "],
		"phosel_MassEGamma_GenuinePhoton"               : ["m_{e,#gamma} GeV",           "Events/10 GeV", 10, [50,140], regionText,  NoLog, " "],
		"phosel_MassEGamma_MisIDEle"                    : ["m_{e,#gamma} GeV",           "Events/10 GeV", 10, [50,140], regionText,  NoLog, " "],
		"phosel_MassEGamma_HadronicPhoton"              : ["m_{e,#gamma} GeV",           "Events/10 GeV", 10, [50,140], regionText,  NoLog, " "],
		"phosel_MassEGamma_HadronicFake"                : ["m_{e,#gamma} GeV",           "Events/10 GeV", 10, [50,140], regionText,  NoLog, " "],

		"phosel_jet1Pt"                             : ["Leading Jet Pt (GeV)", "Events", 10, [30,400], regionText, NoLog, " "],
		"phosel_jet1Pt_GenuinePhoton"               : ["Leading Jet Pt (GeV)", "Events", 10, [30,400], regionText, NoLog, " "],
		"phosel_jet1Pt_MisIDEle"                    : ["Leading Jet Pt (GeV)", "Events", 10, [30,400], regionText, NoLog, " "],
		"phosel_jet1Pt_HadronicPhoton"              : ["Leading Jet Pt (GeV)", "Events", 10, [30,400], regionText, NoLog, " "],
		"phosel_jet1Pt_HadronicFake"                : ["Leading Jet Pt (GeV)", "Events", 10, [30,400], regionText, NoLog, " "],

		"phosel_WtransMass"                             : ["W transverse mass GeV "        , "Events/15 GeV", 15, [-1,-1], regionText,  NoLog, " "],
		"phosel_WtransMass_GenuinePhoton"               : ["W transverse mass GeV "        , "Events/15 GeV", 15, [-1,-1], regionText,  NoLog, " "],
		"phosel_WtransMass_MisIDEle"                    : ["W transverse mass GeV "        , "Events/15 GeV", 15, [-1,-1], regionText,  NoLog, " "],
		"phosel_WtransMass_HadronicPhoton"              : ["W transverse mass GeV "        , "Events/15 GeV", 15, [-1,-1], regionText,  NoLog, " "],
		"phosel_WtransMass_HadronicFake"                : ["W transverse mass GeV "        , "Events/15 GeV", 15, [-1,-1], regionText,  NoLog, " "],

		"phosel_mediumID_ChIso"                 : ["Charged Hadron Iso (GeV)"   , "<Events/GeV>", [0.,0.1,1.,2.,3.,4.,5.,7.,9.,11.,13.,15.,17.,20.], [-1,-1], regionText, YesLog, " "],
		"phosel_mediumID_ChIso_GenuinePhoton"   : ["Charged Hadron Iso (GeV)"   , "<Events/GeV>", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, YesLog, "Genuine Photon"],
		"phosel_mediumID_ChIso_MisIDEle"        : ["Charged Hadron Iso (GeV)"   , "<Events/GeV>", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, YesLog, "MisIDEle"],
		"phosel_mediumID_ChIso_HadronicPhoton"  : ["Charged Hadron Iso (GeV)"   , "<Events/GeV>", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, YesLog, "Hadronic Photon"],
		"phosel_mediumID_ChIso_HadronicFake"    : ["Charged Hadron Iso (GeV)"   , "<Events/GeV>", [0.,0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 15.0, 17.0, 20.0], [-1,-1], regionText, YesLog, "Hadronic Fake"],

		"presel_M3"                      : ["M_{3} (GeV)"  , "<Events/GeV>", [60., 70., 80., 90.,  100., 110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240., 250., 260., 270., 280., 290., 300., 310., 320., 330., 340., 350., 360., 370., 380., 390., 400., 410.,420.,430., 440.,450., 460.,470., 480.,490., 500.], [-1,-1], regionText,  NoLog, " "],
		"phosel_M3"                      : ["M_{3} (GeV)"  , "<Events/GeV>", [60., 70., 80., 90.,  100,  110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240., 250., 260., 270., 280., 290., 300., 310., 320., 330., 340., 350., 360., 370., 380., 390., 400., 410.,420.,430., 440.,450., 460.,470., 480.,490., 500.], [-1,-1], regionText,  NoLog, " "],   
		"phosel_M3_GenuinePhoton"        : ["M_{3} (GeV)"  , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "Genuine Photon"],   
		"phosel_M3_MisIDEle"             : ["M_{3} (GeV)"  , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "MisIDEle"],
		"phosel_M3_HadronicPhoton"       : ["M_{3} (GeV)"  , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "Hadronic Photon"],
		"phosel_M3_HadronicFake"         : ["M_{3} (GeV)"  , "<Events/GeV>", [60., 90., 100, 110., 120., 130., 140., 150., 160., 180., 200., 220., 240., 260., 280., 300., 350., 400., 450., 500.], [-1,-1], regionText,  NoLog, "Hadronic Fake"],

		  }

if not plotList is None:
	allHistsDefined = True
	for hist in plotList:
		if not hist in histograms:
			print "Histogram %s plotting information not defined" % hist
			allHistsDefined = False
	if not allHistsDefined:
		print "Problem with defined histograms, exiting"
		sys.exit()

if plotList is None:
	if makeSignalRegionPlots:
		plotList = ["presel_M3", "phosel_M3", "phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake",
					"phosel_mediumID_ChIso", "phosel_mediumID_ChIso_GenuinePhoton", "phosel_mediumID_ChIso_MisIDEle","phosel_mediumID_ChIso_HadronicPhoton","phosel_mediumID_ChIso_HadronicFake"]
	elif makePhotonSplitplots:
		plotList = ["phosel_LeadingPhotonEt", "phosel_LeadingPhotonEta", "phosel_LeadingPhotonPhi"]
	
	elif makePlotsForSF:
		plotList =["presel_Njet","presel_WtransMass", "phosel_MassEGamma", "phosel_MassEGamma_GenuinePhoton",  
	   "phosel_MassEGamma_MisIDEle", "phosel_MassEGamma_HadronicPhoton", "phosel_MassEGamma_HadronicFake",
	   "phosel_Njet","phosel_WtransMass","presel_jet1Pt","phosel_jet1Pt",
	   "phosel_WtransMass_GenuinePhoton","phosel_WtransMass_MisIDEle","phosel_WtransMass_HadronicPhoton",
	   "phosel_WtransMass_HadronicFake","phosel_jet1Pt_GenuinePhoton",
	   "phosel_jet1Pt_MisIDEle","phosel_jet1Pt_HadronicPhoton","phosel_jet1Pt_HadronicFake",
	   "presel_M3", "phosel_M3", "phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake",
	   "phosel_mediumID_ChIso", "phosel_mediumID_ChIso_GenuinePhoton", "phosel_mediumID_ChIso_MisIDEle","phosel_mediumID_ChIso_HadronicPhoton","phosel_mediumID_ChIso_HadronicFake",
	   "phosel_noCut_SIEIE", "phosel_noCut_SIEIE_GenuinePhoton", "phosel_noCut_SIEIE_MisIDEle","phosel_noCut_SIEIE_HadronicPhoton", "phosel_noCut_SIEIE_HadronicFake","presel_MET","phosel_MET"]
		#plotList = ["presel_Njet","presel_WtransMass", "phosel_MassEGamma","phosel_WtransMass", "presel_M3"]
		#plotList = ["presel_Njet","presel_WtransMass", "phosel_MassEGamma", "phosel_MassEGamma_GenuinePhoton",  "phosel_MassEGamma_MisIDEle", "phosel_MassEGamma_HadronicPhoton", "phosel_MassEGamma_HadronicFake"]
	elif makeNabinPlots and finalState == 'Mu':
		plotList = [
		"presel_muEta",
		"phosel_muEta",
		"presel_muPhi",
		"phosel_LeadingPhotonEta",
		"phosel_LeadingPhotonEt", 
		"phosel_LeadingPhotonEt_GenuinePhoton",
		"phosel_LeadingPhotonEt_MisIDEle",
		"phosel_LeadingPhotonEt_HadronicPhoton", 
		"phosel_LeadingPhotonEt_HadronicFake", 
		"presel_jet1Pt", 
		"presel_jet2Pt",
		"presel_Njet", 
		"presel_muPt",  
		"presel_M3", 
		"presel_WtransMass", 
		"phosel_Njet", 
		"phosel_muPt",  
		"phosel_M3", 
		"phosel_WtransMass", 
		"phosel_MassEGammaMisIDEle", 
		"phosel_MassEGammaOthers",
		"phosel_noCut_SIEIE",                   
		"phosel_noCut_SIEIE_GenuinePhoton",      
		"phosel_noCut_SIEIE_MisIDEle",           
		"phosel_noCut_SIEIE_HadronicPhoton",     
		"phosel_noCut_SIEIE_HadronicFake",
		"presel_MET",
		"phosel_MET",
		"phosel_MassEGamma",               
		"phosel_MassEGamma_GenuinePhoton", 
		"phosel_MassEGamma_MisIDEle",      
		"phosel_MassEGamma_HadronicPhoton",
		"phosel_MassEGamma_HadronicFake"
		]

	elif makeNabinPlots and finalState == 'Ele':
		plotList = [
		"presel_eleSCEta",
		"phosel_eleSCEta",
		"presel_elePhi",
		"phosel_LeadingPhotonEta",
		"phosel_LeadingPhotonEt", 
		"phosel_LeadingPhotonEt_GenuinePhoton",
		"phosel_LeadingPhotonEt_MisIDEle",
		"phosel_LeadingPhotonEt_HadronicPhoton", 
		"phosel_LeadingPhotonEt_HadronicFake", 
		"presel_jet1Pt", 
		"presel_jet2Pt",
		"presel_Njet", 
		"presel_elePt",  
		"presel_M3", 
		"presel_WtransMass", 
		"phosel_Njet", 
		"phosel_elePt",  
		"phosel_M3", 
		"phosel_WtransMass", 
		"phosel_MassEGammaMisIDEle", 
		"phosel_MassEGammaOthers",
		"phosel_noCut_SIEIE",                   
		"phosel_noCut_SIEIE_GenuinePhoton",      
		"phosel_noCut_SIEIE_MisIDEle",           
		"phosel_noCut_SIEIE_HadronicPhoton",     
		"phosel_noCut_SIEIE_HadronicFake",
		"presel_MET",
		"phosel_MET",
		"phosel_MassEGamma",               
		"phosel_MassEGamma_GenuinePhoton", 
		"phosel_MassEGamma_MisIDEle",      
		"phosel_MassEGamma_HadronicPhoton",
		"phosel_MassEGamma_HadronicFake"
		]

	elif Dilepmass:
		plotList =["presel_DilepMass"]
	else:
		#plotList = ["presel_M3_control","phosel_noCut_ChIso","phosel_noCut_ChIso_GenuinePhoton","phosel_noCut_ChIso_MisIDEle","phosel_noCut_ChIso_HadronicPhoton","phosel_noCut_ChIso_HadronicFake","phosel_M3","phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake","phosel_AntiSIEIE_ChIso","phosel_AntiSIEIE_ChIso_barrel","phosel_AntiSIEIE_ChIso_endcap"]
		plotList = ["presel_M3_control","presel_M3","phosel_noCut_ChIso","phosel_noCut_ChIso_barrel","phosel_noCut_ChIso_GenuinePhoton_barrel","phosel_noCut_ChIso_MisIDEle_barrel","phosel_noCut_ChIso_HadronicPhoton_barrel","phosel_noCut_ChIso_HadronicFake_barrel","phosel_M3","phosel_M3_barrel","phosel_M3_GenuinePhoton_barrel","phosel_M3_MisIDEle_barrel","phosel_M3_HadronicPhoton_barrel","phosel_M3_HadronicFake_barrel","phosel_AntiSIEIE_ChIso_barrel"]
# if useQCDCR:
# 	plotList = ["presel_M3_control","phosel_noCut_ChIso","phosel_noCut_ChIso_barrel","phosel_M3","phosel_M3_barrel","phosel_AntiSIEIE_ChIso_barrel"]


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
	print "Found tdrstyle.C file, using this style."
	HasCMSStyle = True
	if os.path.isfile('CMSTopStyle.cc'):
		gROOT.ProcessLine('.L CMSTopStyle.cc+')
		style = CMSTopStyle()
		style.setupICHEPv1()
		print "Found CMSTopStyle.cc file, use TOP style if requested in xml file."
if not HasCMSStyle:
	print "Using default style defined in cuy package."
	thestyle.SetStyle()

ROOT.gROOT.ForceStyle()

isMC=999
print "==> ",sampleList

if useQCDMC:
	if channel=="mu":
		sampleList[-2] = "QCDMu"
	if channel=="ele":
		sampleList[-2] = "QCDEle"
	stackList = sampleList[:-1]
elif noQCD:
	stackList = sampleList[:-3]
else:
	sampleList[-2] = "QCD_DD"
	stackList = sampleList[:-1]
	stackList.remove("GJets") 
	samples["QCD_DD"] = [[],kGreen+3,"Multijet",isMC]


stackList.reverse()


if not newStackListTop is None:
	newStackListTop.reverse()
	for sample in newStackListTop:
		if not sample in stackList:
			print "Unknown sample name %s"%sample
			continue
		stackList.remove(sample)
		stackList.append(sample)

if not newStackListBot is None:
	newStackListBot.reverse()
	for sample in newStackListBot:
		if not sample in stackList:
			print "Unknown sample name %s"%sample
			continue
		stackList.remove(sample)
		stackList.insert(0,sample)

if finalState=="Mu":
	_channelText = "#mu+jets"
elif finalState=="Ele":
		_channelText = "e+jets"

elif finalState=="DiEle":
		_channelText = "ee+jets"
elif finalState=="DiMu":
		_channelText = "#mu#mu+jets"

CMS_lumi.channelText = _channelText
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True

H = 600;
W = 800;

# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W


# SetOwnership(canvas, False)
# SetOwnership(canvasRatio, False)
# SetOwnership(pad1, False)
# SetOwnership(pad2, False)



legendHeightPer = 0.04
legList = stackList[:]
legList.reverse()

legendStart = 0.69
legendEnd = 0.97-(R/W)

#legend = TLegend(2*legendStart - legendEnd, 1-T/H-0.01 - legendHeightPer*(len(legList)+1), legendEnd, 0.99-(T/H)-0.01)
legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legend.SetNColumns(2)

#legendR = TLegend(0.71, 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*(len(legList)+1), 0.99-(R/W), 0.99-(T/H)/(1.-padRatio+padOverlap))


legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))

legendR.SetNColumns(2)

legendR.SetBorderSize(0)
legendR.SetFillColor(0)


legend.SetBorderSize(0)
legend.SetFillColor(0)

_file = {}

if useQCDCR:
	stackList.remove("QCD_DD")
	if finalState=="mu":
		stackList.remove("QCDMu")
	else:
		stackList.remove("QCDEle")

#if finalState=="Mu":
#	systematics = ["JER","JECTotal","phosmear","phoscale","BTagSF_b","BTagSF_l","Q2","Pdf","PU","MuEff","PhoEff","isr","fsr"]
#else:
#	systematics = ["JER","JECTotal","phosmear","phoscale","BTagSF_b","BTagSF_l","Q2","Pdf","PU","EleEff","PhoEff","elesmear","elescale","isr","fsr"]

#if finalState=="Mu":
#	systematics = ["BTagSF_b"]
#else:
#	systematics = ["BTagSF_b"]

if finalState=="Mu" or "DiMu":
	ZJetsSF=1.22 # just for now, need to check again
	# WJetsSF=1.21
elif finalState=="Ele" or "DiEle":
	ZJetsSF=1.22 # just for now, need to check again
	# WJetsSF=1.21             
else:
	print "neither Ele,Mu,DiEle or DiMu!!!!!!!!!!"

systematics2 = ["isr","fsr"]

if finalState=="Mu":
	channel="mu"
else:
	channel="ele"


skipData = False

#if selYear in ["2017","2018"] and isTightSelection: # blinding 2017 and 2018 for validation region
#    skipData = True

#if selYear in ["2017","2018"]:
#	skipData = True

#_file_sys = TFile.Open("Combine_withDDTemplateData_v6_%s_tight_binned_PDF.root"%(channel),"read")


#_filesys_up={}
#_filesys_down={}
for sample in stackList:
	#_filesys_up[sample]={}
	#_filesys_down[sample]={}

	_file[sample] = TFile.Open("%s%s.root"%(_fileDir,sample),"read")
	#print '=====>', _fileDir, '       ', sample
	#for sys in systematics:
		#if sys=="isr" or sys=="fsr": # forget about isr and fsr for now.
		#	if sample not in ["TTGamma" ,"TTbar"]:continue
		#"histograms_%s/%s/hists_looseCR2g0/"%(selYear,channel)
		#_filesys_up  [sample][sys]=TFile("histograms_%s/%s/hists_%s_up_%s/%s.root"%(selYear,channel,sys,dir_,sample),"read")
		#_filesys_down[sample][sys]=TFile("histograms_%s/%s/hists_%s_down_%s/%s.root"%(selYear,channel,sys,dir_,sample),"read")


if 'Ele'in finalState:
	sample = "DataEle"
	_file[sample] = TFile.Open("%s%s.root"%(_fileDir,sample),"read")
	
if 'Mu'in finalState:
	sample = "DataMu"
	_file[sample] = TFile.Open("%s%s.root"%(_fileDir,sample),"read")

#print _file
histName = plotList[0]

#print "%s_DataMu"%(histName)
if finalState=='Ele':
#    print _file["DataEle"], "%s_DataEle"%(histName)
	dataHist = _file["DataEle"].Get("%s_DataEle"%(histName))

elif finalState=='Mu':
	dataHist = _file["DataMu"].Get("%s_DataMu"%(histName))

#else: print "wrong channel"

if finalState=='DiEle':
	dataHist = _file["DataEle"].Get("%s_DataEle"%(histName))

elif finalState=='DiMu':
	dataHist = _file["DataMu"].Get("%s_DataMu"%(histName))

#else:
#	print " pass the channel"
legend.AddEntry(dataHist, "Data", 'pe')
legendR.AddEntry(dataHist, "Data", 'pe')
#legList.remove("QCD_DD")

# if Dilepmass:
# 	legList.remove("QCD_DD")
if useQCDCR:
	legList.remove("QCD_DD")

for sample in legList:
	#print "%s_%s"%(histName,sample)
	hist =_file[sample].Get("%s_%s"%(histName,sample))
	#print hist
	hist.SetFillColor(samples[sample][1])
	hist.SetLineColor(samples[sample][1])
	legend.AddEntry(hist,samples[sample][2],'f')

	#legendR.AddEntry(hist,samples[sample][2],'f')

### Splitting the legend into two columns (with order going top to bottom in first column, then top to bottom in second column)
X = int(len(legList)/2)
sample = legList[X]
#print histName, _file[sample], "%s_%s"%(histName,sample)
hist = _file[sample].Get("%s_%s"%(histName,sample))
hist.SetFillColor(samples[sample][1])
hist.SetLineColor(samples[sample][1])
legendR.AddEntry(hist,samples[sample][2],'f')

for i in range(X):
	if "PhotonCategory" in histName:continue
	
	sample = legList[i]
	if "phosel_PhotonCategory_barrel" in histName and "QCD" in sample:continue
	hist = _file[sample].Get("%s_%s"%(histName,sample))
#	print histName,sample
	hist.SetFillColor(samples[sample][1])
	hist.SetLineColor(samples[sample][1])
	legendR.AddEntry(hist,samples[sample][2],'f')

	if X+i+1 < len(legList):
		if histName=="phosel_PhotonCategory_barrel" and "QCD" in sample:continue		 
		sample = legList[i+X+1]
		#print histName,sample
		hist = _file[sample].Get("%s_%s"%(histName,sample))
		hist.SetFillColor(samples[sample][1])
		hist.SetLineColor(samples[sample][1])
		legendR.AddEntry(hist,samples[sample][2],'f')

errorband=TH1F("error","error",20,0,20)
errorband.SetLineColor(0)
errorband.SetFillColor(kBlack)
errorband.SetFillStyle(3245)
errorband.SetMarkerSize(0)
legendR.AddEntry(errorband,"Uncertainty","f")

TGaxis.SetMaxDigits(3)

def drawHist(histName,plotInfo, plotDirectory, _file, skipData = False):
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

	canvasRatio = TCanvas('c1Ratio','c1Ratio',W,H)
	canvasRatio.SetFillColor(0)
	canvasRatio.SetBorderMode(0)
	canvasRatio.SetFrameFillStyle(0)
	canvasRatio.SetFrameBorderMode(0)
	canvasRatio.SetLeftMargin( L/W )
	canvasRatio.SetRightMargin( R/W )
	canvasRatio.SetTopMargin( T/H )
	canvasRatio.SetBottomMargin( B/H )
	canvasRatio.SetTickx(0)
	canvasRatio.SetTicky(0)
	canvasRatio.Draw()
	canvasRatio.cd()

	pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
	pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
	pad1.SetLeftMargin( L/W )
	pad1.SetRightMargin( R/W )
	pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
	pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
	pad2.SetLeftMargin( L/W )
	pad2.SetRightMargin( R/W )
	pad2.SetTopMargin( (padOverlap)/(padRatio+padOverlap) )
	pad2.SetBottomMargin( B/H/(padRatio+padOverlap) )

	pad1.SetFillColor(0)
	pad1.SetBorderMode(0)
	pad1.SetFrameFillStyle(0)
	pad1.SetFrameBorderMode(0)
	pad1.SetTickx(0)
	pad1.SetTicky(0)

	pad2.SetFillColor(0)
	pad2.SetFillStyle(4000)
	pad2.SetBorderMode(0)
	pad2.SetFrameFillStyle(0)
	pad2.SetFrameBorderMode(0)
	pad2.SetTickx(0)
	pad2.SetTicky(0)


	canvasRatio.cd()
	pad1.Draw()
	pad2.Draw()


	canvas.cd()
	canvas.ResetDrawn()
	stack = THStack(histName,histName)
	SetOwnership(stack,True)

	for sample in stackList:
	
		if finalState=="Ele" and "mu" in histName:continue
		if finalState=="Mu" and "ele" in histName:continue
		#if "PhotonCategory" in histName and "QCD" in sample:continue
		if finalState =="Mu" and "MassEGamma" in histName: plotInfo[0] = "m_{#mu,#gamma} GeV"
		#print sample, histName, _file[sample], "%s_%s"%(histName,sample)
	#if 'phosel_nVtx' in histName and sample=="QCD_DD":
		 #       hist = _file["QCD_DD"].Get("phosel_nVtx_barrel_QCD_DD")
	#elif 'presel_nVtx' in histName and sample=="QCD_DD":
		 #       hist = _file["QCD_DD"].Get("presel_nVtx_QCD_DD")
	#else:
		#	hist = _file[sample].Get("%s_%s"%(histName,sample))
		hist = _file[sample].Get("%s_%s"%(histName,sample)) # my input

		if sample=="ZJets":
		 #       print sample, histName
			hist.Scale(ZJetsSF)
	# if sample=="WJets":
 #         #       print sample, histName
	# 	hist.Scale(WJetsSF)
	#else:
	#	hist.Scale(bkgSF)
		#hist = _file[sample].Get("%s/%s_%s"%(sample,histName,sample))
#	print "%s/%s_%s"%(sample,histName,sample), type(hist)
		if type(hist)==type(TObject()):continue
		hist = hist.Clone(sample)	
		hist.SetFillColor(samples[sample][1])
		hist.SetLineColor(samples[sample][1])

		if type(plotInfo[2]) is type(list()):
			hist = hist.Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
			if "MassEGamma" not in histName:
				hist.Scale(1.,"width")
		else:
			hist.Rebin(plotInfo[2])
		#hist = hist.Rebin(plotInfo[2],'hist',x)
		#print hist.GetNbinsX(), hist.GetBinWidth(2)

	#print "number of bins:  ",plotInfo[2], hist.GetNbinsX(), sample

		if useOverflow:
			lastBin = hist.GetNbinsX()
			lastBinContent = hist.GetBinContent(lastBin)
			lastBinError   = hist.GetBinError(lastBin)
			overFlowContent = hist.GetBinContent(lastBin+1)
			overFlowError   = hist.GetBinError(lastBin+1)
			hist.SetBinContent(lastBin,lastBinContent + overFlowContent)
			hist.SetBinError(lastBin, (lastBinError**2 + overFlowError**2)**0.5 )

	
	#print sample, histName, hist.Integral(-1,-1)
	#if type(plotInfo[2]) is type(list()):
		#hist.Scale(1.,"width")
		stack.Add(hist)

	if 'Ele' in finalState:
		if 'phosel_nVtx' in histName:
			dataHist = _file["DataEle"].Get("phosel_nVtx_barrel_DataEle")
		#    qcdHist = _file["QCD_DD"].Get("phosel_nVtx_barrel_QCD_DD")
		elif 'presel_nVtx' in histName:
			dataHist = _file["DataEle"].Get("presel_nVtx_DataEle")
			#qcdHist = _file["QCD_DD"].Get("phosel_nVtx_QCD_DD")
		elif 'phosel_nVtxNoPU' in histName:
			dataHist = _file["DataEle"].Get("phosel_nVtxNoPU_barrel_DataEle")
	#	    qcdHist = _file["QCD_DD"].Get("phosel_nVtxNoPU_barrel_QCD_DD")
		else:
			dataHist = _file["DataEle"].Get("%s_DataEle"%(histName))

				#    if not Dilepmass: 
		 #   	qcdHist = _file["QCD_DD"].Get("%s_QCD_DD"%(histName))
#	dataHist.Draw()
	elif 'Mu' in finalState:
		if 'phosel_nVtx' in histName:
			dataHist = _file["DataMu"].Get("phosel_nVtx_barrel_DataMu")
		  #  qcdHist = _file["QCD_DD"].Get("phosel_nVtx_barrel_QCD_DD")
		elif 'presel_nVtx' in histName:
			dataHist = _file["DataMu"].Get("presel_nVtx_DataMu")
		   # qcdHist = _file["QCD_DD"].Get("phosel_nVtx_QCD_DD")
		elif 'phosel_nVtxNoPU' in histName:
			dataHist = _file["DataMu"].Get("phosel_nVtxNoPU_barrel_DataMu")
	#	    qcdHist = _file["QCD_DD"].Get("phosel_nVtxNoPU_barrel_QCD_DD")
		else:
			dataHist = _file["DataMu"].Get("%s_DataMu"%(histName))

	#	    if not Dilepmass:
	#	    	qcdHist = _file["QCD_DD"].Get("%s_QCD_DD"%(histName))
	
	noData = False
	#print dataHist
	if type(dataHist)==type(TObject()): noData = True

	if skipData == True: 
		noData = True
		print 'Skipping Data'

	if not noData:
		dataHist.Sumw2()
		if type(plotInfo[2]) is type(list()):	
			dataHist = dataHist.Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
			if "MassEGamma" not in histName:
				dataHist.Scale(1.,"width")
		else:
			dataHist.Rebin(plotInfo[2])
			#dataHist = dataHist.Rebin(plotInfo[2],'dataHist',x)
			#print "number of bins in data:  ",plotInfo[2], hist.GetNbinsX()
#	    dataHist.Rebin(plotInfo[2])
		#print dataHist.GetMarkerStyle()
		#dataHist.Sumw2()
		#print dataHist.Integral()
		#exit()
		if useOverflow:
			lastBin = dataHist.GetNbinsX()
			lastBinContent = dataHist.GetBinContent(lastBin)
			lastBinError   = dataHist.GetBinError(lastBin)
			overFlowContent = dataHist.GetBinContent(lastBin+1)
			overFlowError   = dataHist.GetBinError(lastBin+1)
			dataHist.SetBinContent(lastBin,lastBinContent + overFlowContent)
			dataHist.SetBinError(lastBin, (lastBinError**2 + overFlowError**2)**0.5 )



	oneLine = TF1("oneline","1",-9e9,9e9)
	oneLine.SetLineColor(kBlack)
	oneLine.SetLineWidth(1)
	oneLine.SetLineStyle(2)
	
	_text = TPaveText(0.35,.75,0.45,0.85,"NDC")
	_text.SetTextColor(kBlack)
	_text.SetFillColor(0)
	_text.SetTextSize(0.04)
	_text.SetTextFont(42)
	_text.AddText(plotInfo[6])

	#histograms list has flag whether it's log or not
	canvas.SetLogy(plotInfo[5])
	#canvas.SetLogy()
	maxVal = stack.GetMaximum()
	if not noData: 
		maxVal = max(dataHist.GetMaximum(),maxVal)
	
	minVal = 1
	if plotInfo[5]:
		#print histName, plotInfo[5], stack.GetStack()[1].GetMinimum()
		minVal = max(stack.GetStack()[0].GetMinimum(),1)
		stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
#	    stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(stack.GetMinimum())))
#	    print minVal
		stack.SetMinimum(minVal)
		# print stack.GetStack()[0]
		# print stack.GetStack()[0].GetName()
		# print stack.GetStack()[0].GetMinimum()
	else:
		stack.SetMaximum(2.5*maxVal) # 1.5 to 2.5
		stack.SetMinimum(minVal)

	if not noData:
		stack.SetMaximum(2.35*max(dataHist.GetMaximum(),stack.GetMaximum()))
	else:
		stack.SetMaximum(2.35*stack.GetMaximum())

	errorband=stack.GetStack().Last().Clone("error")
	errorband.Sumw2()
	errorband.SetLineColor(kBlack)
	errorband.SetFillColor(kBlack)
	errorband.SetFillStyle(3245)
	errorband.SetMarkerSize(0)
	#### Uncertainty
	#h1_up={}
#	h1_do={}
#	
#	for sample in stackList:
#		if Dilepmass:	continue 
#		h1_up[sample]={}
#		h1_do[sample]={}
#		for sys in systematics:		
#			if "phosel_PhotonCategory" in histName and sample=="QCD_DD":continue	
#			if sys=="Q2" or sys=="Pdf" or sys=="isr" or sys=="fsr":
#				if sample not in ["TTbar","TTGamma"]:continue
#			#elif finalState=="Mu" and "ele" in histName:continue
#			#elif finalState=="Ele" and "mu" in histName:continue
#
#			print sample,sys
#			
#			if sample=="QCD_DD": 
#				h1_up[sample][sys]=qcdHist.Clone("%s_%s_up"%(sys,sample))
#				h1_do[sample][sys]=qcdHist.Clone("%s_%s_do"%(sys,sample))
#		
#			elif sample=="TTGamma" and (sys=="Pdf" or sys=="Q2"):
#				#print sample,sys
#				h1_up[sample][sys]=_filesys_up[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_up"%(sys,sample))
#				h1_do[sample][sys]=_filesys_down[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_do"%(sys,sample))	
#				total=_file[sample].Get("%s_%s"%(histName,sample)).Integral()
#				h1_up[sample][sys].Scale(total/h1_up[sample][sys].Integral())
#				h1_do[sample][sys].Scale(total/h1_do[sample][sys].Integral())
#			elif sample=="TTbar" and sys=="Q2":
#				#print sample, sys, _filesys_up[sample][sys], _filesys_down[sample][sys], "%s_%s"%(histName,sample) 	
#				h1_up[sample][sys]=_filesys_up[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_up"%(sys,sample))
#				h1_do[sample][sys]=_filesys_down[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_do"%(sys,sample))     
#				total=_file[sample].Get("%s_%s"%(histName,sample)).Integral()
#				h1_up[sample][sys].Scale(total/h1_up[sample][sys].Integral())
#				h1_do[sample][sys].Scale(total/h1_do[sample][sys].Integral())
#			
#			else:
#		#		print sample, sys, _filesys_down[sample][sys], histName
#				h1_up[sample][sys]=_filesys_up[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_up"%(sys,sample))
#				h1_do[sample][sys]=_filesys_down[sample][sys].Get("%s_%s"%(histName,sample)).Clone("%s_%s_do"%(sys,sample))
#
#			if type(plotInfo[2]) is type(list()):
#			
#			
#				h1_up[sample][sys] = h1_up[sample][sys].Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
#				h1_do[sample][sys] = h1_do[sample][sys].Rebin(len(plotInfo[2])-1,"",array('d',plotInfo[2]))
#				h1_do[sample][sys].Scale(1,"width")
#				h1_up[sample][sys].Scale(1,"width")
#
#			else:
#				h1_up[sample][sys].Rebin(plotInfo[2])
#				h1_do[sample][sys].Rebin(plotInfo[2])
#	error=0.
#	diff={}		
#	sum_={}
#	for i_bin in range(1,errorband.GetNbinsX()+1):
#		if isLooseCRe3g1Selection or Dilepmass:continue
#		sum_[i_bin]=0.	
#		diff[i_bin]=[]
#		for sys in systematics:
#			for sample in stackList:
#				if "phosel_PhotonCategory" in histName:
#					if sample=="QCD_DD":continue			
#				if sys=="Q2" or sys=="Pdf" or sys=="isr" or sys=="fsr":
#					if sample not in ["TTbar","TTGamma"]:continue
#				if finalState=="Mu" and "ele" in histName:continue
#				if finalState=="Ele" and "mu" in histName:continue
#				if finalState=="Mu" and "MassEGamma" in histName:continue
#				print "adding sys",sample,sys, ((h1_up[sample][sys].GetBinContent(i_bin)-h1_do[sample][sys].GetBinContent(i_bin))/2.)**2
#				sum_[i_bin]+=((h1_up[sample][sys].GetBinContent(i_bin)-h1_do[sample][sys].GetBinContent(i_bin))/2.)**2
#			#diff[i_bin].append(((h1_up[sample][sys].GetBinContent(i_bin)-h1_do[sample][sys].GetBinContent(i_bin))/2.)**2.)
#			
# 
#		print (sum_[i_bin])**0.5		
#		errorband.SetBinError(i_bin,(sum_[i_bin])**0.5)
	#### Uncertainty end
	
	stack.Draw('hist')
	_text.Draw("same")

	#histograms list has x-axis title

	stack.GetHistogram().GetXaxis().SetTitle(plotInfo[0])
	#print histName
	#if "phosel_PhotonCategory" in histName:
		#print "phosel_Category"
		#stack.GetHistogram().GetXaxis().SetBinLabel(1,"Genuine")
		#stack.GetHistogram().GetXaxis().SetBinLabel(2,"Mis-id ele")
		#stack.GetHistogram().GetXaxis().SetBinLabel(3,"Hadronic Photon")
		#stack.GetHistogram().GetXaxis().SetBinLabel(4,"Hadronic Fake")

	#stack.GetHistogram().GetYaxis().SetTitle(plotInfo[1])
	if not -1 in plotInfo[3]:
		stack.GetHistogram().GetXaxis().SetRangeUser(plotInfo[3][0],plotInfo[3][1])
	if not noData:
		dataHist.GetXaxis().SetRangeUser(plotInfo[3][0],plotInfo[3][1])
	else:
		dataHist = stack.GetStack().Last().Clone("temp")
		dataHist.GetXaxis().SetRangeUser(plotInfo[3][0],plotInfo[3][1])
		for i_bin in range(0,dataHist.GetNbinsX()+1):
			dataHist.SetBinContent(i_bin,0)
		dataHist.GetXaxis().SetRangeUser(plotInfo[3][0],plotInfo[3][1])

	if not noData:
		dataHist.SetLineColor(kBlack)
		dataHist.Draw("e,X0,same")

	 
	#residue=dataHist.Clone()
	#temp=stack.GetStack().Last().Clone("temp")
	#residue.Add(temp,-1)
	#residue.Draw("hist")
	#canvas.Print("%s/%s_residue.pdf"%(plotDirectory,histName))
	#canvas.Clear()

	legend.Draw("same")


	#_text.Draw()
	CMS_lumi.channelText = _channelText+plotInfo[4]
	CMS_lumi.CMS_lumi(canvas, 4, 11)
	#canvas.SaveAs("%s%s.root"%(plotDirectory,histName))
	#canvas.Print("%s%s.pdf"%(plotDirectory,histName))

	if not noData:
		ratio = dataHist.Clone("temp")
		temp = stack.GetStack().Last().Clone("temp")
		#print temp.GetNbinsX()
		#print temp.Integral(5,16)
		for i_bin in range(1,temp.GetNbinsX()+1):
			temp.SetBinError(i_bin,0.)
		ratio.Divide(temp)
	else:
		ratio = dataHist.Clone("temp")

		temp = stack.GetStack().Last().Clone("temp")

	#errorband.Divide(temp)
	
		
	# pad1.Clear()
	# pad2.Clear()

	canvasRatio.cd()	
	canvasRatio.ResetDrawn()
	canvasRatio.Draw()

	canvasRatio.cd()

	pad1.Draw()
	pad2.Draw()

	pad1.cd()
	pad1.SetLogy(plotInfo[5])
	
	stack.Draw('HIST')
	y2 = pad1.GetY2()

	
#	stack.SetMinimum(1)
	#    pad1.Update()
	stack.GetXaxis().SetTitle('')
	stack.GetYaxis().SetTitle(dataHist.GetYaxis().GetTitle())

	stack.SetTitle('')
	stack.GetXaxis().SetLabelSize(0)
	stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
	stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
	stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
	stack.GetYaxis().SetTitle(plotInfo[1])
	dataHist.Draw('E,X0,SAME')
	#errorband.Draw('e2,same')

#    legendR.AddEntry(errorband,"Uncertainty","f")
	legendR.Draw()

	_text = TPaveText(0.42,.75,0.5,0.85,"NDC")
	_text.AddText(plotInfo[6])
	_text.SetTextColor(kBlack)
	_text.SetFillColor(0)
	_text.SetTextSize(0.05)
	_text.SetTextFont(42)
	_text.Draw("same")


	
	ratio.SetTitle('')
	
	ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
	ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
	ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
	ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
	ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
#	ratio.GetYaxis().SetRangeUser(0.5,1.5)

	maxRatio = ratio.GetMaximum()
	minRatio = ratio.GetMinimum()


	maxRatio = 1.5
	minRatio = 0.5
	for i_bin in range(1,ratio.GetNbinsX()):
		if ratio.GetBinError(i_bin)<1:
			if ratio.GetBinContent(i_bin)>maxRatio:
				maxRatio = ratio.GetBinContent(i_bin)
			if ratio.GetBinContent(i_bin)<minRatio:
				minRatio = ratio.GetBinContent(i_bin)

	if maxRatio > 1.8:
		ratio.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
	elif maxRatio < 1:
		ratio.GetYaxis().SetRangeUser(0,1.2)
	elif maxRatio-1 < 1-minRatio:
		ratio.GetYaxis().SetRangeUser((1-(1-minRatio)*1.2),1.1*maxRatio)		
	else:
		ratio.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)
	
	#maxRatio = 1.5
		#minRatio = 0.5	
	ratio.GetYaxis().SetRangeUser(0.7,1.3)
	ratio.GetYaxis().SetNdivisions(504)
	ratio.GetXaxis().SetTitle(plotInfo[0])
	ratio.GetYaxis().SetTitle("Data/MC")
	CMS_lumi.CMS_lumi(pad1, 4, 11)

	pad2.cd()
	#for i_bin in range(1,errorband.GetNbinsX()):
	#	errorband.SetBinContent(i_bin,1.)
	maxRatio = 1.5
	minRatio = 0.5
	ratio.SetMarkerStyle(dataHist.GetMarkerStyle())
	ratio.SetMarkerSize(dataHist.GetMarkerSize())
	ratio.SetLineColor(dataHist.GetLineColor())
	ratio.SetLineWidth(dataHist.GetLineWidth())
	ratio.Draw('e,x0')
	errorbandRatio = errorband.Clone("errorRatio")
	errorbandRatio.Divide(temp)
	errorbandRatio.Draw('e2,same')
	oneLine.Draw("same")
	
	#    pad2.Update()
	canvasRatio.Update()
	canvasRatio.RedrawAxis()
	if postfitplot:
		canvasRatio.SaveAs("%s%s_ratio_postfit.root"%(plotDirectory,histName))
		canvasRatio.SaveAs("%s%s_ratio_postfit.pdf"%(plotDirectory,histName))
	else:
		canvasRatio.SaveAs("%s%s_ratio.root"%(plotDirectory,histName))
		canvasRatio.SaveAs("%s%s_ratio.pdf"%(plotDirectory,histName))
#    canvasRatio.Clear()
	canvasRatio.SetLogy(0)
	canvas.Close()
	canvasRatio.Close()
	
if Dilepmass:
	for histName in plotList:
		drawHist(histName,histograms_dilep[histName],plotDirectory,_file,skipData=skipData)
else:
	for histName in plotList:
		if finalState=="Ele" and "mu" in histName:continue
		if finalState=="Mu" and "ele" in histName:continue
		#if finalState=="Mu" and "EGamma" in histName:continue
#		if "AntiSIEIE" in histName or "Genuine" in histName or "MisIDEle" in histName or "HadronicPhoton" in histName or "HadronicFake" in histName or "endcap" in histName:continue
		drawHist(histName,histograms[histName],plotDirectory,_file,skipData=skipData)


# for histName in phoselhistograms:
#         drawHist("phosel_%s"%histName,phoselhistograms[histName],plotDirectory,_file)

