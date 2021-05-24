
# CR1_TTGamma_Dilepton_2016_AnalysisNtuple.root
# CR1_TTGamma_SingleLept_2016_AnalysisNtuple.root
# CR2_TTGamma_Dilepton_2016_AnalysisNtuple.root
# CR2_TTGamma_SingleLept_2016_AnalysisNtuple.root

# TuneDown_TTGamma_Dilepton_2016_AnalysisNtuple.root
# TuneDown_TTGamma_SingleLept_2016_AnalysisNtuple.root
# TuneUp_TTGamma_Dilepton_2016_AnalysisNtuple.root
# TuneUp_TTGamma_SingleLept_2016_AnalysisNtuple.root

# erdOn_TTGamma_Dilepton_2016_AnalysisNtuple.root
# erdOn_TTGamma_SingleLept_2016_AnalysisNtuple.root



python makeHistograms.py -y 2016 -c Ele --tight -s TTGamma --syst Tune    --level up            --verbose --allPlots  #--plot presel_M3
python makeHistograms.py -y 2016 -c Ele --tight -s TTGamma --syst Tune    --level down          --verbose --allPlots  #--plot presel_M3

python makeHistograms.py -y 2016 -c Ele --looseCRge4e0 -s TTGamma --syst Tune    --level up            --verbose --allPlots  #--plot presel_M3
python makeHistograms.py -y 2016 -c Ele --looseCRge4e0 -s TTGamma --syst Tune    --level down          --verbose --allPlots  #--plot presel_M3


exit 1

for year in 2016 2017 2018; do
for channel in Ele Mu; do
for cr in tight looseCRge4e0; do
# python makeHistograms.py -y $year -c $channel --$cr -s TTGamma --moreSyst CR1   --output hists_CR1    --verbose --allPlots  #--plot presel_M3
# python makeHistograms.py -y $year -c $channel --$cr -s TTGamma --moreSyst CR2   --output hists_CR2    --verbose --allPlots  #--plot presel_M3
# python makeHistograms.py -y $year -c $channel --$cr -s TTGamma --moreSyst erdOn --output hists_erdOn  --verbose --allPlots  #--plot presel_M3
# python makeHistograms.py -y $year -c $channel --$cr -s TTGamma --moreSyst erdOn --output hists_erdOn  --verbose --allPlots  #--plot presel_M3
python makeHistograms.py -y $year -c $channel --$cr -s TTGamma --syst Tune    --level up            --verbose --allPlots  #--plot presel_M3
python makeHistograms.py -y $year -c $channel --$cr -s TTGamma --syst Tune    --level down          --verbose --allPlots  #--plot presel_M3
done
done
done


exit 1
python makeHistograms.py -y 2016 -c Ele --tight -s TTGamma --syst TuneUp --level up --plot presel_M3

eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2016/TTGamma_Hadronic_2016_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2016/CR1_TTGamma_Hadronic_2016_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2016/TTGamma_Hadronic_2016_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2016/CR2_TTGamma_Hadronic_2016_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2016/TTGamma_Hadronic_2016_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2016/erdOn_TTGamma_Hadronic_2016_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2016/TTGamma_Hadronic_2016_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2016/TuneUp_TTGamma_Hadronic_2016_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2016/TTGamma_Hadronic_2016_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2016/TuneDown_TTGamma_Hadronic_2016_AnalysisNtuple.root

eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2017/TTGamma_Hadronic_2017_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2017/CR1_TTGamma_Hadronic_2017_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2017/TTGamma_Hadronic_2017_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2017/CR2_TTGamma_Hadronic_2017_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2017/TTGamma_Hadronic_2017_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2017/erdOn_TTGamma_Hadronic_2017_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2017/TTGamma_Hadronic_2017_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2017/TuneUp_TTGamma_Hadronic_2017_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2017/TTGamma_Hadronic_2017_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2017/TuneDown_TTGamma_Hadronic_2017_AnalysisNtuple.root

eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2018/TTGamma_Hadronic_2018_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2018/CR1_TTGamma_Hadronic_2018_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2018/TTGamma_Hadronic_2018_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2018/CR2_TTGamma_Hadronic_2018_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2018/TTGamma_Hadronic_2018_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2018/erdOn_TTGamma_Hadronic_2018_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2018/TTGamma_Hadronic_2018_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2018/TuneUp_TTGamma_Hadronic_2018_AnalysisNtuple.root
eos cp root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/2018/TTGamma_Hadronic_2018_AnalysisNtuple.root root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples_Feb2021/Systematics/2018/TuneDown_TTGamma_Hadronic_2018_AnalysisNtuple.root



python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst BTagSF_b    --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst BTagSF_l    --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst EleEff      --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst MuEff       --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst JECTotal    --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst prefireEcal --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst isr         --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst fsr         --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst Q2          --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst PhoEff      --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst Pdf         --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst PU          --level down --verbose --plot phosel_elePt
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --syst JER         --level down --verbose --plot phosel_elePt

exit 1



python makeHistograms.py -y 2016 -c Ele --looseCRge2e0  -s TTGamma   --allPlots
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0  -s TTGamma   --allPlots
exit 1
python makeHistograms.py -y 2016 -c Ele --tight  -s TTGamma   --plot presel_elePt
exit 1
#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "pass the year !!!"
    exit 1
fi
# --makePlotsForSF
python makeHistograms.py -y $1 -c Ele --tight -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s DataMu    --makePlotsForSF &


wait

python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s DataMu    --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s DataMu    --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s DataMu    --makePlotsForSF &

wait
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s DataMu    --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s DataMu    --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s DataMu    --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s DataMu    --makePlotsForSF &

wait
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s DataMu    --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s DataMu    --makePlotsForSF &
wait

echo "All processes done!"

python makePlots.py -y $1 -c Ele --tight           --useQCDMC  --makePlotsForSF &      
python makePlots.py -y $1 -c Mu  --tight           --useQCDMC  --makePlotsForSF &

python makePlots.py -y $1 -c Ele --looseCRge2ge0   --useQCDMC  --makePlotsForSF &
python makePlots.py -y $1 -c Mu  --looseCRge2ge0   --useQCDMC  --makePlotsForSF &

python makePlots.py -y $1 -c Ele --looseCRge2e0    --useQCDMC  --makePlotsForSF &
python makePlots.py -y $1 -c Mu  --looseCRge2e0    --useQCDMC  --makePlotsForSF &

python makePlots.py -y $1 -c Ele --looseCRe2e0     --useQCDMC  --makePlotsForSF &
python makePlots.py -y $1 -c Mu  --looseCRe2e0     --useQCDMC  --makePlotsForSF &

python makePlots.py -y $1 -c Ele --looseCRe3e0     --useQCDMC  --makePlotsForSF &
python makePlots.py -y $1 -c Mu  --looseCRe3e0     --useQCDMC  --makePlotsForSF &

python makePlots.py -y $1 -c Ele --looseCRge4e0    --useQCDMC  --makePlotsForSF &
python makePlots.py -y $1 -c Mu  --looseCRge4e0    --useQCDMC  --makePlotsForSF &

python makePlots.py -y $1 -c Ele --looseCRe2e1     --useQCDMC  --makePlotsForSF &
python makePlots.py -y $1 -c Mu  --looseCRe2e1     --useQCDMC  --makePlotsForSF &

python makePlots.py -y $1 -c Ele --looseCRe3e1     --useQCDMC  --makePlotsForSF &
python makePlots.py -y $1 -c Mu  --looseCRe3e1     --useQCDMC  --makePlotsForSF &

python makePlots.py -y $1 -c Ele --looseCRe2e2     --useQCDMC  --makePlotsForSF &
python makePlots.py -y $1 -c Mu  --looseCRe2e2     --useQCDMC  --makePlotsForSF &

python makePlots.py -y $1 -c Ele --looseCRe3ge2    --useQCDMC  --makePlotsForSF &
python makePlots.py -y $1 -c Mu  --looseCRe3ge2    --useQCDMC  --makePlotsForSF &

wait
echo "All processes done!"





#
#declare -a ControlRegion=("tight" "looseCRge2e0" "looseCRge2ge0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
#declare -a SampleListEle=("TTGamma" "TTbar" "TGJets" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "SingleTop" "TTV" "QCDEle" "GJets" "DataEle" )
#declare -a SampleListMu=("TTGamma" "TTbar" "TGJets" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "SingleTop" "TTV" "QCDMu" "GJets" "DataMu" )
#
#for year in 2016 2017 2018
#	for cr in ${ControlRegion[@]}; do
#		for myEsample in ${SampleListEle[@]}; do
#			python makeHistograms.py -y $1 -c Ele --$cr -s $myEsample --makePlotsForSF
#		done 
#	done
#done
#
#


