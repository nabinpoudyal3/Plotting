

combine -M FitDiagnostics -n   el_2016 datacard_ele_2016.txt -s 314159 --redefineSignalPOIs r,nonPromptSF   --saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file22.txt 
combine -M FitDiagnostics -n   mu_2016 datacard_mu_2016.txt  -s 314159 --redefineSignalPOIs r,nonPromptSF   --saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file23.txt 

combine -M FitDiagnostics -n   el_2017 datacard_ele_2017.txt -s 314159 --redefineSignalPOIs r,nonPromptSF   --saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file24.txt 
combine -M FitDiagnostics -n   mu_2017 datacard_mu_2017.txt  -s 314159 --redefineSignalPOIs r,nonPromptSF   --saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file25.txt 

combine -M FitDiagnostics -n   el_2018 datacard_ele_2018.txt -s 314159 --redefineSignalPOIs r,nonPromptSF   --saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file26.txt 
combine -M FitDiagnostics -n   mu_2018 datacard_mu_2018.txt  -s 314159 --redefineSignalPOIs r,nonPromptSF   --saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file27.txt


#combine -M FitDiagnostics -n   el_2016 datacard_ele_2016.txt -s 314159 -t 500 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF -v2  #--saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file22.txt 
#combine -M FitDiagnostics -n   mu_2016 datacard_mu_2016.txt  -s 314159 -t 500 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF -v2  #--saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file23.txt 

#combine -M FitDiagnostics -n   el_2017 datacard_ele_2017.txt -s 314159 -t 500 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF -v2  #--saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file24.txt 
#combine -M FitDiagnostics -n   mu_2017 datacard_mu_2017.txt  -s 314159 -t 500 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF -v2  #--saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file25.txt 

#combine -M FitDiagnostics -n   el_2018 datacard_ele_2018.txt -s 314159 -t 500 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF -v2  #--saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file26.txt 
#combine -M FitDiagnostics -n   mu_2018 datacard_mu_2018.txt  -s 314159 -t 500 --expectSignal 1 --redefineSignalPOIs r,nonPromptSF -v2  #--saveNormalizations --saveWithUncertainties --plots  #>& outputFiles/file27.txt 
wait
echo "Done"
