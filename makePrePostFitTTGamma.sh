#!/bin/bash


declare -a YEAR16=("2016") #"2017" "2018")
declare -a YEAR1718=("2017" "2018")
# declare -a YEAR1718=("2018")

######################################
######################################
##### I won't have postfit plots yet. 
######################################
######################################
#### These prefit below contains all the SFs applied such as misID,Wgamma,Zgamma,ZJets
######################################
######################################

set -x
for year in ${YEAR16[@]}; do
	           python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot  --prefitPlots --datadriven
	           python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot  --prefitPlots --datadriven 
	           python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot     --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot     --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Ele   --btag0      --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --btag0      --prefitPlots 
	           python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton --prefitPlots 
	           python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton --prefitPlots 
 
	           python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot  --postfitPlots --datadriven 
	           python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot  --postfitPlots --datadriven 
	           python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot     --postfitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot     --postfitPlots 
	           python makePlots_TTGamma.py  -y $year -c Ele   --btag0      --postfitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --btag0      --postfitPlots 
	           python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton --postfitPlots 
	           python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton --postfitPlots 

	           python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot  --ratioPlot --postfitPlots --datadriven 
	           python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot  --ratioPlot --postfitPlots --datadriven 
	           python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot     --ratioPlot --postfitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot     --ratioPlot --postfitPlots 
	           python makePlots_TTGamma.py  -y $year -c Ele   --btag0      --ratioPlot --postfitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --btag0      --ratioPlot --postfitPlots 
	           python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton --ratioPlot --postfitPlots 
	           python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton --ratioPlot --postfitPlots 


	           python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot  --xsecPlot --postfitPlots --datadriven 
	           python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot  --xsecPlot --postfitPlots --datadriven 
	           python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot     --xsecPlot --postfitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot     --xsecPlot --postfitPlots 
	           python makePlots_TTGamma.py  -y $year -c Ele   --btag0      --xsecPlot --postfitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --btag0      --xsecPlot --postfitPlots 
	           python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton --xsecPlot --postfitPlots 
	           python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton --xsecPlot --postfitPlots 


done

exit 1

for year in ${YEAR1718[@]}; do
	           python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot   --prefitPlots  --noData --datadriven
	           python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot   --prefitPlots  --noData --datadriven
	           python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot      --prefitPlots  --noData
	           python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot      --prefitPlots  --noData
	           python makePlots_TTGamma.py  -y $year -c Ele   --btag0       --prefitPlots 
	           python makePlots_TTGamma.py  -y $year -c Mu    --btag0       --prefitPlots
	           python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton  --prefitPlots
	           python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton  --prefitPlots

	           # python makePlots_TTGamma.py  -y $year -c Ele   --ChIsoPlot   --postfitPlots  --noData --datadriven
	           # python makePlots_TTGamma.py  -y $year -c Mu    --ChIsoPlot   --postfitPlots  --noData --datadriven
	           # python makePlots_TTGamma.py  -y $year -c Ele   --M3Plot      --postfitPlots  --noData
	           # python makePlots_TTGamma.py  -y $year -c Mu    --M3Plot      --postfitPlots  --noData
	           # python makePlots_TTGamma.py  -y $year -c Ele   --btag0       --postfitPlots  
	           # python makePlots_TTGamma.py  -y $year -c Mu    --btag0       --postfitPlots  
	           # python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton  --postfitPlots  
	           # python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton  --postfitPlots  

	           # python makePlots_TTGamma.py  -y $year -c Ele   --btag0       --postfitPlots --ratioPlot 
	           # python makePlots_TTGamma.py  -y $year -c Mu    --btag0       --postfitPlots --ratioPlot 
	           # python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton  --postfitPlots --ratioPlot 
	           # python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton  --postfitPlots --ratioPlot 

	           # python makePlots_TTGamma.py  -y $year -c Ele   --btag0       --postfitPlots --xsecPlot  
	           # python makePlots_TTGamma.py  -y $year -c Mu    --btag0       --postfitPlots --xsecPlot  
	           # python makePlot_M3Control.py -y $year -c Ele   --zeroPhoton  --postfitPlots --xsecPlot  
	           # python makePlot_M3Control.py -y $year -c Mu    --zeroPhoton  --postfitPlots --xsecPlot  

done


exit 1

# python makePlots_TTGamma.py  -y 2016 -c Ele   --ChIsoPlot  --prefitPlots 
# python makePlots_TTGamma.py  -y 2016 -c Mu    --ChIsoPlot  --prefitPlots 
# python makePlots_TTGamma.py  -y 2016 -c Ele   --M3Plot     --prefitPlots 
# python makePlots_TTGamma.py  -y 2016 -c Mu    --M3Plot     --prefitPlots 
# python makePlots_TTGamma.py  -y 2016 -c Ele   --btag0      --prefitPlots 
# python makePlots_TTGamma.py  -y 2016 -c Mu    --btag0      --prefitPlots
# python makePlot_M3Control.py -y 2016 -c Ele   --zeroPhoton --prefitPlots 
# python makePlot_M3Control.py -y 2016 -c Mu    --zeroPhoton --prefitPlots 

# python makePlots_TTGamma.py  -y 2017 -c Ele   --ChIsoPlot  --prefitPlots 
# python makePlots_TTGamma.py  -y 2017 -c Mu    --ChIsoPlot  --prefitPlots 
# python makePlots_TTGamma.py  -y 2017 -c Ele   --M3Plot     --prefitPlots 
# python makePlots_TTGamma.py  -y 2017 -c Mu    --M3Plot     --prefitPlots 
# python makePlots_TTGamma.py  -y 2017 -c Ele   --btag0      --prefitPlots 
# python makePlots_TTGamma.py  -y 2017 -c Mu    --btag0      --prefitPlots
# python makePlot_M3Control.py -y 2017 -c Ele   --zeroPhoton --prefitPlots 
# python makePlot_M3Control.py -y 2017 -c Mu    --zeroPhoton --prefitPlots 

# python makePlots_TTGamma.py  -y 2018 -c Ele   --ChIsoPlot  --prefitPlots 
# python makePlots_TTGamma.py  -y 2018 -c Mu    --ChIsoPlot  --prefitPlots 
# python makePlots_TTGamma.py  -y 2018 -c Ele   --M3Plot     --prefitPlots 
# python makePlots_TTGamma.py  -y 2018 -c Mu    --M3Plot     --prefitPlots 
# python makePlots_TTGamma.py  -y 2018 -c Ele   --btag0      --prefitPlots 
# python makePlots_TTGamma.py  -y 2018 -c Mu    --btag0      --prefitPlots
# python makePlot_M3Control.py -y 2018 -c Ele   --zeroPhoton --prefitPlots 
# python makePlot_M3Control.py -y 2018 -c Mu    --zeroPhoton --prefitPlots 



# python makePlot_M3Control.py -y 2018 -c Ele   --zeroPhoton --prefitPlots 
# python makePlot_M3Control.py -y 2018 -c Mu    --zeroPhoton --prefitPlots 
# python makePlot_M3Control.py -y 2018 -c Ele   --zeroPhoton --postfitPlots 
# python makePlot_M3Control.py -y 2018 -c Mu    --zeroPhoton --postfitPlots  
# python makePlot_M3Control.py -y 2017 -c Ele   --zeroPhoton --prefitPlots 
# python makePlot_M3Control.py -y 2017 -c Mu    --zeroPhoton --prefitPlots 
# python makePlot_M3Control.py -y 2017 -c Ele   --zeroPhoton --postfitPlots 
# python makePlot_M3Control.py -y 2017 -c Mu    --zeroPhoton --postfitPlots  
# python makePlot_M3Control.py -y 2016 -c Ele   --zeroPhoton --prefitPlots 
# python makePlot_M3Control.py -y 2016 -c Mu    --zeroPhoton --prefitPlots 
# python makePlot_M3Control.py -y 2016 -c Ele   --zeroPhoton --postfitPlots 
# python makePlot_M3Control.py -y 2016 -c Mu    --zeroPhoton --postfitPlots  	           

# python makePlots_TTGamma.py  -y 2016 -c Ele   --ChIsoPlot  --postfitPlots
# python makePlots_TTGamma.py  -y 2016 -c Mu    --ChIsoPlot  --postfitPlots
# python makePlots_TTGamma.py  -y 2016 -c Ele   --M3Plot     --postfitPlots
# python makePlots_TTGamma.py  -y 2016 -c Mu    --M3Plot     --postfitPlots 
# python makePlots_TTGamma.py  -y 2016 -c Ele   --btag0      --postfitPlots 
# python makePlots_TTGamma.py  -y 2016 -c Mu    --btag0      --postfitPlots 

