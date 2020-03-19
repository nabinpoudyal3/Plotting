#combine -M MultiDimFit -n CR123_2016   datacard_CR123_2016.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2    
#combine -M MultiDimFit -n CR1_2016     datacard_CR1_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2    
#combine -M MultiDimFit -n CR2_2016     datacard_CR2_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2    
#combine -M MultiDimFit -n CR3_2016     datacard_CR3_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2    
#combine -M MultiDimFit -n CR4_2016     datacard_CR4_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2    
#
#
#combine -M MultiDimFit -n CR123_2017   datacard_CR123_2017.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   
#combine -M MultiDimFit -n CR1_2017     datacard_CR1_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   
#combine -M MultiDimFit -n CR2_2017     datacard_CR2_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   
#combine -M MultiDimFit -n CR3_2017     datacard_CR3_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   
#combine -M MultiDimFit -n CR4_2017     datacard_CR4_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   
#
#combine -M MultiDimFit -n CR123_2018   datacard_CR123_2018.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   
#combine -M MultiDimFit -n CR1_2018     datacard_CR1_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   
#combine -M MultiDimFit -n CR2_2018     datacard_CR2_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   
#combine -M MultiDimFit -n CR3_2018     datacard_CR3_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   
#combine -M MultiDimFit -n CR4_2018     datacard_CR4_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2   

#wait
#echo "Done Fitting"



combine -M FitDiagnostics -n CR123_2016   datacard_CR123_2016.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR1_2016     datacard_CR1_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR2_2016     datacard_CR2_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR3_2016     datacard_CR3_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR4_2016     datacard_CR4_2016.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 


combine -M FitDiagnostics -n CR123_2017   datacard_CR123_2017.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR1_2017     datacard_CR1_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR2_2017     datacard_CR2_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR3_2017     datacard_CR3_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR4_2017     datacard_CR4_2017.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 

combine -M FitDiagnostics -n CR123_2018   datacard_CR123_2018.txt   --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR1_2018     datacard_CR1_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR2_2018     datacard_CR2_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR3_2018     datacard_CR3_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
#combine -M FitDiagnostics -n CR4_2018     datacard_CR4_2018.txt     --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 

wait
echo "Done Fitting"
