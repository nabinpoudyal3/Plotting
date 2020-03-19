import uproot
#mytree = uproot.open('root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/ST_tbar_channel_2016_AnalysisNtuple.root')['AnalysisTree']
#mytree = uproot.open('root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/ST_s_channel_2016_AnalysisNtuple.root')['AnalysisTree']
#mytree = uproot.open('root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/ST_tW_channel_2016_AnalysisNtuple.root')['AnalysisTree']
#mytree = uproot.open('root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/ST_t_channel_2016_AnalysisNtuple.root')['AnalysisTree']
#mytree = uproot.open('root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/ST_tbarW_channel_2016_AnalysisNtuple.root')['AnalysisTree']
mytree = uproot.open('root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/2016/ST_tbar_channel_2016_AnalysisNtuple.root')['AnalysisTree']

q2up = mytree.array('q2weight_Do')
a = q2up == 0
b = q2up[a]
print len(b)
