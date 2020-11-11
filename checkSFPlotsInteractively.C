{
TChain chain("AnalysisTree");

chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/DYjetsM10to50_2016_AnalysisNtuple.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/DYjetsM50_2016_AnalysisNtuple_1of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/DYjetsM50_2016_AnalysisNtuple_2of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/DYjetsM50_2016_AnalysisNtuple_3of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/DYjetsM50_2016_AnalysisNtuple_4of5.root");
chain.Add("root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/DYjetsM50_2016_AnalysisNtuple_5of5.root");

vector<string> weights = {"PUweight","btagWeight_1a","btagSF","muEffWeight","prefireSF","eleEffWeight","phoEffWeight","loosePhoEffWeight","evtWeight"};


for  (int i=0; i < 9; i++){
TH1F *hist = new TH1F("hist","",100,-4,4);
TCanvas *can = new TCanvas("can","",800,800);
//cout << weights[i] << endl;
AnalysisTree->Draw("weights[i]>>hist","","hist");      
can->Print("WeightPlots/weights[i].pdf");
delete hist;
delete can;
}

//AnalysisTree->Draw("prefireSF","","hist");         c1->Print("WeightPlots/prefireSF.pdf");
//AnalysisTree->Draw("btagWeight_1a","","hist");     c1->Print("WeightPlots/btagWeight_1a.pdf");
//AnalysisTree->Draw("btagSF","","hist");            c1->Print("WeightPlots/btagSF.pdf");
//AnalysisTree->Draw("muEffWeight","","hist");       c1->Print("WeightPlots/muEffWeight.pdf");
//AnalysisTree->Draw("eleEffWeight","","hist");      c1->Print("WeightPlots/eleEffWeight.pdf");
//AnalysisTree->Draw("phoEffWeight","","hist");      c1->Print("WeightPlots/phoEffWeight.pdf");
//AnalysisTree->Draw("loosePhoEffWeight","","hist"); c1->Print("WeightPlots/loosePhoEffWeight.pdf");
//AnalysisTree->Draw("evtWeight","","hist");         c1->Print("WeightPlots/evtWeight.pdf");
}


