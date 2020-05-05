#!/bin/bash

#######################################################################################
echo -e  "\e[31mRun makeTemplateForZJets.sh to make templates for ZJets fitting!!\e[0m"
./makeTemplateForZJets.sh; wait
echo -e  "\e[31mRunning combine fitting for ZJets\e[0m"
cd CombineFitting/ZJetsFittingAllYear
./runFitDiagnositcs.sh; wait
python makeAllZJetsSF.py
python makeZjetsVsJetMultiplicity.py
cd ../../
echo -e  "\e[31mNow runing  all pre and post fit plots\e[0m"
./makePrePostFitZJets.sh; wait

#############################################################################################
echo -e  "\e[31mRun makeTemplateForMisIDE.sh to make templates for MisIDE fitting!!\e[0m"
./makeTemplateForMisIDE.sh; wait
echo -e  "\e[31mRunning combine fitting for MisIDE\e[0m"
cd CombineFitting/MisIDEleFittingSystematicsSeparateYear
./runFitDiagnostics.sh; wait
python makeAllMisIDEleSF.py
python makeMisIDEleVsJetMultiplicity.py
python makeVGammaVsYearAndJetMultiplicity.py
cd ../../
echo -e  "\e[31mNow runing  all pre and post fit plots\e[0m "
./makePrePostFitMisIDEle.sh; wait

#############################################################################################

echo -e  "\e[31mRun makeTemplateForMisIDE.sh to make templates for ttgamma fitting!!\e[0m"
./makeTemplateForTTGamma.sh; wait
echo -e  "\e[31mRunning combine fitting for MisIDE\e[0m"
cd CombineFitting/ttGamma
./runSeparateChannelYearFitting.sh
./runBothChannelSeparateYear.sh
./runBothChannelAllYear.sh
wait
python makeTTGammaSF_separrateChannel.py
python makeTTGammaSF_bothChannel.py
python makeTTGammaSF_all.py
cd ../../
echo -e  "\e[31mNow runing  all pre and post fit plots\e[0m"
./makePrePostFitTTGamma.sh; wait

wait

echo -e  "\e[31mRunning impact plots and closure tests!!!\e[0m"
cd CombineFitting/ZJetsFittingAllYear
./makeImpactPlots.sh; wait

cd ../MisIDEleFittingSystematicsSeparateYear
./makeImpactPlot.sh; wait
python makeCovarianceMatrix.py
./runClosureTest.sh; wait
python midID_closureTest.py
python zg_closureTest.py
python wg_closureTest.py

cd ../ttGamma
./runCovarianceForSeparateChannelYear.sh; wait
./runToyFittingForClosureTest.sh; wait
python ttGamma_closureTest.py
python ttGamma_closureTest_nonPrompt.py
python makeCovarianceMatrix.py

echo -e  "\e[31mNow copy Pre post plots and tex files to make slides\e[0m"
