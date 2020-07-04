ControlRegion=["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]
SampleListEle=["TTGamma", "TTbar", "TGJets", "WJets", "ZJets", "WGamma", "ZGamma", "Diboson", "SingleTop", "TTV","QCDEle" ,"GJets" ,"DataEle" ]
SampleListMu= ["TTGamma", "TTbar" ,"TGJets" ,"WJets", "ZJets" ,"WGamma" ,"ZGamma","Diboson", "SingleTop", "TTV" ,"QCDMu", "GJets" ,"DataMu" ]

#systematics = ["PU","MuEff","PhoEff","BTagSF_b","BTagSF_l","EleEff","Q2","Pdf","isr","fsr","prefireEcal"]
systematics = ["prefireEcal"]
for syst in systematics:
	myfile = open('condor_makeHistograms_Dilep_%s.jdl'%syst,'w')
	common_command = \
'Executable =  makeHistograms_Dilep_condor_syst.sh \n\
Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
Transfer_Input_Files = myHistograms.tar, makeHistograms_Dilep_condor_syst.sh\n\
use_x509userproxy = true\n\
Output = condor/log$(cluster)_$(process).stdout\n\
Error  = condor/log$(cluster)_$(process).stderr\n\
Log    = condor/log$(cluster)_$(process).condor\n\n'

	myfile.write(common_command)

	for year in ["2016", "2017", "2018"]:
		for cr in ControlRegion:
			run_commandEleup =  \
			'arguments  = DiEle %s %s %s up \n\
queue 1\n\n' %(year, cr, syst)
			myfile.write(run_commandEleup)
			run_commandMuup =  \
			'arguments  = DiMu %s %s %s up\n\
queue 1\n\n' %(year, cr, syst)
			myfile.write(run_commandMuup)
			run_commandEledown =  \
			'arguments  = DiEle %s %s %s down\n\
queue 1\n\n' %(year, cr, syst)
			myfile.write(run_commandEledown)
			run_commandMudown =  \
			'arguments  = DiMu %s %s %s down\n\
queue 1\n\n' %(year, cr, syst)
			myfile.write(run_commandMudown)           
			
	myfile.close() 
