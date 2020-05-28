
combine -M MultiDimFit -n   el_2016 datacard_ele_2016.txt -s 314159 -t 1000 --expectSignal 1  --redefineSignalPOIs r,nonPromptSF -v2& # --justFit --autoBoundsPOIs "*" --saveNormalizations
combine -M MultiDimFit -n   mu_2016 datacard_mu_2016.txt  -s 314159 -t 1000 --expectSignal 1  --redefineSignalPOIs r,nonPromptSF -v2& #--justFit --autoBoundsPOIs "*" --saveNormalizations

combine -M MultiDimFit -n   el_2017 datacard_ele_2017.txt -s 314159 -t 1000 --expectSignal 1  --redefineSignalPOIs r,nonPromptSF -v2& #--justFit --autoBoundsPOIs "*" --saveNormalizations
combine -M MultiDimFit -n   mu_2017 datacard_mu_2017.txt  -s 314159 -t 1000 --expectSignal 1  --redefineSignalPOIs r,nonPromptSF -v2& #--justFit --autoBoundsPOIs "*" --saveNormalizations

combine -M MultiDimFit -n   el_2018 datacard_ele_2018.txt -s 314159 -t 1000 --expectSignal 1  --redefineSignalPOIs r,nonPromptSF -v2& #--justFit --autoBoundsPOIs "*" --saveNormalizations
combine -M MultiDimFit -n   mu_2018 datacard_mu_2018.txt  -s 314159 -t 1000 --expectSignal 1  --redefineSignalPOIs r,nonPromptSF -v2& #--justFit --autoBoundsPOIs "*" --saveNormalizations


