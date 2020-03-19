
#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "pass the year !!!"
    exit 1
fi
# --dilepmassPlots
python makeHistograms.py -y $1 -c DiEle --tight -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --tight -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --tight -s DataMu    --dilepmassPlots &

wait

python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2ge0 -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2ge0 -s DataMu    --dilepmassPlots &

wait

python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge2e0  -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge2e0  -s DataMu    --dilepmassPlots &

wait

python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e0 -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e0 -s DataMu    --dilepmassPlots &

wait
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e0 -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e0 -s DataMu    --dilepmassPlots &

wait

python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRge4e0 -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRge4e0 -s DataMu    --dilepmassPlots &

wait

python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e1 -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e1 -s DataMu    --dilepmassPlots &

wait

python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3e1 -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3e1 -s DataMu    --dilepmassPlots &

wait
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe2e2 -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe2e2 -s DataMu    --dilepmassPlots &

wait

python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiEle --looseCRe3ge2 -s DataEle   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s TTbar     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s TGJets    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s WJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s ZJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s WGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s Diboson   --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s SingleTop --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s TTV       --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s GJets     --dilepmassPlots &
python makeHistograms.py -y $1 -c DiMu  --looseCRe3ge2 -s DataMu    --dilepmassPlots &
wait

echo "Done Histogramming!" 

#python makePlots.py -y $1 -c DiEle --tight           --useQCDMC  --dilepmassPlots &	   
#python makePlots.py -y $1 -c DiMu  --tight           --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiEle --looseCRge2ge0   --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiMu  --looseCRge2ge0   --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiEle --looseCRge2e0    --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiMu  --looseCRge2e0    --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiEle --looseCRe2e0     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiMu  --looseCRe2e0     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiEle --looseCRe3e0     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiMu  --looseCRe3e0     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiEle --looseCRge4e0    --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiMu  --looseCRge4e0    --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiEle --looseCRe2e1     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiMu  --looseCRe2e1     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiEle --looseCRe3e1     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiMu  --looseCRe3e1     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiEle --looseCRe2e2     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiMu  --looseCRe2e2     --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiEle --looseCRe3ge2    --useQCDMC  --dilepmassPlots &
#python makePlots.py -y $1 -c DiMu  --looseCRe3ge2    --useQCDMC  --dilepmassPlots &
#
#wait
#echo "All processes done!"



#
#
##wait
#declare -a allyear=("2017")
#for year in ${allyear[@]}; do
#	python makePlots.py -y $year -c DiEle --tight          --postfitplot --useQCDMC  --dilepmassPlots &	   
#	python makePlots.py -y $year -c DiMu  --tight          --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiEle --looseCRge2ge0  --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiMu  --looseCRge2ge0  --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiEle --looseCRge2e0   --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiMu  --looseCRge2e0   --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiEle --looseCRe2e0    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiMu  --looseCRe2e0    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiEle --looseCRe3e0    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiMu  --looseCRe3e0    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiEle --looseCRge4e0   --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiMu  --looseCRge4e0   --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiEle --looseCRe2e1    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiMu  --looseCRe2e1    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiEle --looseCRe3e1    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiMu  --looseCRe3e1    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiEle --looseCRe2e2    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiMu  --looseCRe2e2    --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiEle --looseCRe3ge2   --postfitplot --useQCDMC  --dilepmassPlots &
#	python makePlots.py -y $year -c DiMu  --looseCRe3ge2   --postfitplot --useQCDMC  --dilepmassPlots &
#done
#wait
#echo "All processes done!"


