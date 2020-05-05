{
TChain chain("AnalysisTree");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_b_2017_AnalysisNtuple_1of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_b_2017_AnalysisNtuple_2of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_b_2017_AnalysisNtuple_3of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_b_2017_AnalysisNtuple_4of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_b_2017_AnalysisNtuple_5of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_c_2017_AnalysisNtuple_1of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_c_2017_AnalysisNtuple_2of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_c_2017_AnalysisNtuple_3of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_c_2017_AnalysisNtuple_4of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_c_2017_AnalysisNtuple_5of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_d_2017_AnalysisNtuple_1of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_d_2017_AnalysisNtuple_2of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_d_2017_AnalysisNtuple_3of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_d_2017_AnalysisNtuple_4of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_d_2017_AnalysisNtuple_5of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_e_2017_AnalysisNtuple_1of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_e_2017_AnalysisNtuple_2of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_e_2017_AnalysisNtuple_3of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_e_2017_AnalysisNtuple_4of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_e_2017_AnalysisNtuple_5of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_f_2017_AnalysisNtuple_1of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_f_2017_AnalysisNtuple_2of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_f_2017_AnalysisNtuple_3of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_f_2017_AnalysisNtuple_4of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2017/Data_SingleEle_f_2017_AnalysisNtuple_5of5.root");
AnalysisTree->Draw("phoEta:phoPhi","(passPresel_Ele && nJet==2 && nBJet==0 && nPho==1 && !(((phoPhi>2.7 && phoPhi<3.1) && phoEta>1.2)))*evtWeight*PUweight*muEffWeight*eleEffWeight*1.0*1.0*btagWeight_1a","colz");
}





// for 2016: AnalysisTree->Draw("phoEta:phoPhi","(passPresel_Ele && nJet==2 && nBJet==0 && nPho==1 && !(((phoPhi>2.3 && phoPhi<2.7) && phoEta<0.1) || ((phoPhi>1.2 && phoPhi<1.6) && (phoEta>-1 && phoEta<0.8)) || ((phoPhi>-1.7 && phoPhi<-1.4) && (phoEta>-1 && phoEta<0.9))) )*evtWeight*PUweight*muEffWeight*eleEffWeight*1.0*1.0*btagWeight_1a","colz");
// for 2017: AnalysisTree->Draw("phoEta:phoPhi","(passPresel_Ele && nJet==2 && nBJet==0 && nPho==1 && !(((phoPhi>2.7 && phoPhi<3.1) && phoEta>1.2)))*evtWeight*PUweight*muEffWeight*eleEffWeight*1.0*1.0*btagWeight_1a","colz");
// for 2018: AnalysisTree->Draw("phoEta:phoPhi","(passPresel_Ele && nJet==2 && nBJet==0 && nPho==1 && !(((phoPhi>0.4 && phoPhi<0.8) && phoEta>0)))*evtWeight*PUweight*muEffWeight*eleEffWeight*1.0*1.0*btagWeight_1a","colz");
