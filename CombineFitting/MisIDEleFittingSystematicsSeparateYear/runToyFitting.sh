combine -M FitDiagnostics -n toy_CR123_2016   datacard_CR123_2016.txt  --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR1_2016     datacard_CR1_2016.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR2_2016     datacard_CR2_2016.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR3_2016     datacard_CR3_2016.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR4_2016     datacard_CR4_2016.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 


combine -M FitDiagnostics -n toy_CR123_2017   datacard_CR123_2017.txt  --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR1_2017     datacard_CR1_2017.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR2_2017     datacard_CR2_2017.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR3_2017     datacard_CR3_2017.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR4_2017     datacard_CR4_2017.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 

combine -M FitDiagnostics -n toy_CR123_2018   datacard_CR123_2018.txt  --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR1_2018     datacard_CR1_2018.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR2_2018     datacard_CR2_2018.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR3_2018     datacard_CR3_2018.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 
combine -M FitDiagnostics -n toy_CR4_2018     datacard_CR4_2018.txt    --expectSignal=1 -t 1000 -s -1 --redefineSignalPOIs r,ZGammaBkgPhotonSF,WGammaBkgPhotonSF -v2 --saveNormalizations --saveWithUncertainties --plots 

wait
echo "Done Fitting"



