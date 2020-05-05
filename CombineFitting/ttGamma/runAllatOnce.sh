#!/bin/bash

./runSeparateChannelYearFitting.sh >& runSeparateChannelYearFitting.log
./runBothChannelSeparateYear.sh    >& runBothChannelSeparateYear.log
./runBothChannelAllYear.sh         >& runBothChannelAllYear.log

./runCovarianceForSeparateChannelYear.sh >& runCovarianceForSeparateChannelYear.log
./runToyFittingForClosureTest.sh         >& runToyFittingForClosureTest.log

python ttGamma_closureTest.py           >& ttGamma_closureTest.log
python ttGamma_closureTest_nonPrompt.py >& ttGamma_closureTest_nonPrompt.log
python makeCovarianceMatrix.py          >& makeCovarianceMatrix.log


#./runSeparateChannelYearFitting.sh 
#./runBothChannelSeparateYear.sh    
#./runBothChannelAllYear.sh         

#./runCovarianceForSeparateChannelYear.sh 
#./runToyFittingForClosureTest.sh         

#python ttGamma_closureTest.py           
#python ttGamma_closureTest_nonPrompt.py 
#python makeCovarianceMatrix.py          



# nPho==1 && !(((phoPhi>2.3 && phoPhi<2.7) && phoEta<0.1) || ((phoPhi>1.2 && phoPhi<1.6) && (phoEta>-1 && phoEta<0.8)) || ((phoPhi>-1.7 && phoPhi<-1.4) && (phoEta>-1 && phoEta<0.9))) 
# nPho==1 && !(((phoPhi>2.7 && phoPhi<3.1) && phoEta>1.2))
# nPho==1 && !(((phoPhi>0.4 && phoPhi<0.8) && phoEta>0))
