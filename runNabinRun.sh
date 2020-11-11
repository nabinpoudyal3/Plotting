

python makeHistograms.py -y 2016 -c Ele --looseCRge2e0  -s TTGamma   --allPlots
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0  -s TTGamma   --allPlots

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


