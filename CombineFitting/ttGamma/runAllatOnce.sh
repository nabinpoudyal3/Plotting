#!/bin/bash

./runSeparateChannelYearFitting.sh >& runSeparateChannelYearFitting.log
./runBothChannelSeparateYear.sh    >& runSeparateChannelYearFitting.log
./runBothChannelAllYear.sh         >& runBothChannelAllYear.log

./runCovarianceForSeparateChannelYear.sh >& runCovarianceForSeparateChannelYear.log
./runToyFittingForClosureTest.sh         >& runToyFittingForClosureTest.log

python ttGamma_closureTest.py           >& ttGamma_closureTest.log
python ttGamma_closureTest_nonPrompt.py >& ttGamma_closureTest_nonPrompt.log
python makeCovarianceMatrix.py          >& makeCovarianceMatrix.log
