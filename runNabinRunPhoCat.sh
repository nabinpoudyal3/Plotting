



#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "pass the year !!!"
    exit 1
fi
# --makePhotonSplitplots
python makeHistograms.py -y $1 -c Ele --tight -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s QCDEle    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --tight -s DataEle   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s QCDMu     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --tight -s DataMu    --makePhotonSplitplots &



wait

python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s QCDEle    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s DataEle   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s QCDMu     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s DataMu    --makePhotonSplitplots &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s QCDEle    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s DataEle   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s QCDMu     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s DataMu    --makePhotonSplitplots &

wait
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s QCDEle    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s DataEle   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s QCDMu     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s DataMu    --makePhotonSplitplots &

wait

python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s QCDEle    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s DataEle   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s QCDMu     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s DataMu    --makePhotonSplitplots &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s QCDEle    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s DataEle   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s QCDMu     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s DataMu    --makePhotonSplitplots &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s QCDEle    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s DataEle   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s QCDMu     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s DataMu    --makePhotonSplitplots &

wait
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s QCDEle    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s DataEle   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s QCDMu     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s DataMu    --makePhotonSplitplots &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s QCDEle    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s DataEle   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTGamma   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTbar     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TGJets    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s WJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s ZJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s WGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s ZGamma    --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s Diboson   --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s SingleTop --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTV       --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s QCDMu     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s GJets     --makePhotonSplitplots &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s DataMu    --makePhotonSplitplots &
wait







#
#declare -a ControlRegion=("tight" "looseCRge2e0" "looseCRge2ge0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
#declare -a SampleListEle=("TTGamma" "TTbar" "TGJets" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "SingleTop" "TTV" "QCDEle" "GJets" "DataEle" )
#declare -a SampleListMu=("TTGamma" "TTbar" "TGJets" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "SingleTop" "TTV" "QCDMu" "GJets" "DataMu" )
#
#for year in 2016 2017 2018
#	for cr in ${ControlRegion[@]}; do
#		for myEsample in ${SampleListEle[@]}; do
#			python makeHistograms.py -y $1 -c Ele --$cr -s $myEsample --makePhotonSplitplots
#		done 
#	done
#done
#
#


