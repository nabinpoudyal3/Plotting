python makePlots.py -y $1 -c DiEle --tight           --useQCDMC  --dilepmassPlots &      
python makePlots.py -y $1 -c DiMu  --tight           --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRge2ge0   --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRge2ge0   --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRge2e0    --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRge2e0    --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe2e0     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe2e0     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe3e0     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe3e0     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRge4e0    --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRge4e0    --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe2e1     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe2e1     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe3e1     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe3e1     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe2e2     --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe2e2     --useQCDMC  --dilepmassPlots &

python makePlots.py -y $1 -c DiEle --looseCRe3ge2   --useQCDMC  --dilepmassPlots &
python makePlots.py -y $1 -c DiMu  --looseCRe3ge2   --useQCDMC  --dilepmassPlots &
