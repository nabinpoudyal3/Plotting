#!/bin/bash

#--redefineSignalPOIs r,bkg_norm --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2

rMin=-5
rMax=5

#combine -M FitDiagnostics -n CR123_2016  datacard_CR123_2016.txt  --redefineSignalPOIs r,bkg_norm --saveShapes --saveWithUncertainties --saveNormalizations --rMin=0 --rMax=5 -v2    

combine -M FitDiagnostics -n CR123_2016  datacard_CR123_2016.txt  --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v1   
combine -M FitDiagnostics -n CR1_2016    datacard_CR1_2016.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v1    
combine -M FitDiagnostics -n CR2_2016    datacard_CR2_2016.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v1    
combine -M FitDiagnostics -n CR3_2016    datacard_CR3_2016.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v1    
combine -M FitDiagnostics -n CR4_2016    datacard_CR4_2016.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v1    
combine -M FitDiagnostics -n CR5_2016    datacard_CR5_2016.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v1    
combine -M FitDiagnostics -n CR6_2016    datacard_CR6_2016.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v1    
combine -M FitDiagnostics -n CR7_2016    datacard_CR7_2016.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v1    
combine -M FitDiagnostics -n SR8_2016    datacard_SR8_2016.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v1    


combine -M FitDiagnostics -n CR123_2017  datacard_CR123_2017.txt  --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR1_2017    datacard_CR1_2017.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2  --robustFit=1
combine -M FitDiagnostics -n CR2_2017    datacard_CR2_2017.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR3_2017    datacard_CR3_2017.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR4_2017    datacard_CR4_2017.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR5_2017    datacard_CR5_2017.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR6_2017    datacard_CR6_2017.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR7_2017    datacard_CR7_2017.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n SR8_2017    datacard_SR8_2017.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    


combine -M FitDiagnostics -n CR123_2018  datacard_CR123_2018.txt  --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2   --robustFit=1 
combine -M FitDiagnostics -n CR1_2018    datacard_CR1_2018.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR2_2018    datacard_CR2_2018.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR3_2018    datacard_CR3_2018.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR4_2018    datacard_CR4_2018.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR5_2018    datacard_CR5_2018.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR6_2018    datacard_CR6_2018.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n CR7_2018    datacard_CR7_2018.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
combine -M FitDiagnostics -n SR8_2018    datacard_SR8_2018.txt    --redefineSignalPOIs r,bkg_norm --plots --saveShapes --saveWithUncertainties --saveNormalizations --rMin=$rMin --rMax=$rMax -v2    
wait
echo "Done!!"
