#!/bin/bash

combine -M FitDiagnostics -n CR123_2016   datacard_CR123_2016.txt -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &
combine -M FitDiagnostics -n CR1_2016     datacard_CR1_2016.txt   -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &
combine -M FitDiagnostics -n CR2_2016     datacard_CR2_2016.txt   -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &
combine -M FitDiagnostics -n CR3_2016     datacard_CR3_2016.txt   -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &


combine -M FitDiagnostics -n CR123_2017   datacard_CR123_2017.txt -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  & 
combine -M FitDiagnostics -n CR1_2017     datacard_CR1_2017.txt   -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &
combine -M FitDiagnostics -n CR2_2017     datacard_CR2_2017.txt   -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &
combine -M FitDiagnostics -n CR3_2017     datacard_CR3_2017.txt   -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &

combine -M FitDiagnostics -n CR123_2018   datacard_CR123_2018.txt -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &
combine -M FitDiagnostics -n CR1_2018     datacard_CR1_2018.txt   -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &
combine -M FitDiagnostics -n CR2_2018     datacard_CR2_2018.txt   -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &
combine -M FitDiagnostics -n CR3_2018     datacard_CR3_2018.txt   -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF,OtherSampleBkgPhotonSF -v2 --saveShape --robustFit=1 --saveNormalizations  &

wait
echo "Done Fitting"


#combine -M FitDiagnostics -n CR123_2016   datacard_CR123_2016.txt -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1 --saveNormalizations  
#combine -M FitDiagnostics -n CR123_2017   datacard_CR123_2017.txt -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1 --saveNormalizations  
#combine -M FitDiagnostics -n CR123_2018   datacard_CR123_2018.txt -s 314159  --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1 --saveNormalizations  


#combine -M MultiDimFit -n CR123_2016   datacard_CR123_2016.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1    
#combine -M MultiDimFit -n CR1_2016     datacard_CR1_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1    
#combine -M MultiDimFit -n CR2_2016     datacard_CR2_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1    
#combine -M MultiDimFit -n CR3_2016     datacard_CR3_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1    
#combine -M MultiDimFit -n CR4_2016     datacard_CR4_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1    


#combine -M MultiDimFit -n CR123_2017   datacard_CR123_2017.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   
#combine -M MultiDimFit -n CR1_2017     datacard_CR1_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   
#combine -M MultiDimFit -n CR2_2017     datacard_CR2_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   
#combine -M MultiDimFit -n CR3_2017     datacard_CR3_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   
#combine -M MultiDimFit -n CR4_2017     datacard_CR4_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   

#combine -M MultiDimFit -n CR123_2018   datacard_CR123_2018.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   
#combine -M MultiDimFit -n CR1_2018     datacard_CR1_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   
#combine -M MultiDimFit -n CR2_2018     datacard_CR2_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   
#combine -M MultiDimFit -n CR3_2018     datacard_CR3_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   
#combine -M MultiDimFit -n CR4_2018     datacard_CR4_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --robustFit=1   

#wait
#echo "Done Fitting"

#combine workspace.root -M FitDiagnostics -t -1 --expectSignal=1 -v2 --cminDefaultMinimizerStrategy 0,
# --cminDefaultMinimizerStrategy 0 if covariance matrix is failed to be computed or some other error related to covariance matrix




