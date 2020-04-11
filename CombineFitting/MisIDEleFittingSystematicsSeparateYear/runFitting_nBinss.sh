#!/bin/bash







#combine -M FitDiagnostics -n CR123_2016_nbins3   datacard_CR123_2016_nbins3.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR123_2016_nbins6   datacard_CR123_2016_nbins6.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR123_2016_nbins9   datacard_CR123_2016_nbins9.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 

#combine -M FitDiagnostics -n CR123_2017_nbins3   datacard_CR123_2017_nbins3.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR123_2017_nbins6   datacard_CR123_2017_nbins6.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR123_2017_nbins9   datacard_CR123_2017_nbins9.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 

#combine -M FitDiagnostics -n CR123_2018_nbins3   datacard_CR123_2018_nbins3.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR123_2018_nbins6   datacard_CR123_2018_nbins6.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR123_2018_nbins9   datacard_CR123_2018_nbins9.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 

#wait
#echo "Done Fitting"



#combine -M MultiDimFit -n CR123_2016_nbins3   datacard_CR123_2016_nbins3.txt -s 1 -t 1000 --expectSignal 2 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
#combine -M MultiDimFit -n CR123_2016_nbins6   datacard_CR123_2016_nbins6.txt -s 2 -t 1000 --expectSignal 2 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
#combine -M MultiDimFit -n CR123_2016_nbins9   datacard_CR123_2016_nbins9.txt -s 3 -t 1000 --expectSignal 2 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
#
#combine -M MultiDimFit -n CR123_2017_nbins3   datacard_CR123_2017_nbins3.txt -s 4 -t 1000 --expectSignal 2 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
#combine -M MultiDimFit -n CR123_2017_nbins6   datacard_CR123_2017_nbins6.txt -s 5 -t 1000 --expectSignal 2 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
#combine -M MultiDimFit -n CR123_2017_nbins9   datacard_CR123_2017_nbins9.txt -s 6 -t 1000 --expectSignal 2 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
#
#combine -M MultiDimFit -n CR123_2018_nbins3   datacard_CR123_2018_nbins3.txt -s 7 -t 1000 --expectSignal 2 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
#combine -M MultiDimFit -n CR123_2018_nbins6   datacard_CR123_2018_nbins6.txt -s 8 -t 1000 --expectSignal 2 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
#combine -M MultiDimFit -n CR123_2018_nbins9   datacard_CR123_2018_nbins9.txt -s 9 -t 1000 --expectSignal 2 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &


combine -M MultiDimFit -n CR123_2016   datacard_CR123_2016.txt -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
combine -M MultiDimFit -n CR123_2017   datacard_CR123_2017.txt -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &
combine -M MultiDimFit -n CR123_2018   datacard_CR123_2018.txt -s 314159 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2  &



wait
echo "Done Fitting"
