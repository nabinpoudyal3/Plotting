
#echo "Ele channel 2016"
#combineCards.py -S datacard_ele_2016_M3.txt datacard_ele_2016_ChIso.txt datacard_ele_2016_M30photon.txt datacard_ele_2016_M30btag.txt >  datacard_ele_2016.txt
#echo "Ele channel 2017"
#combineCards.py -S datacard_ele_2017_M3.txt datacard_ele_2017_ChIso.txt datacard_ele_2017_M30photon.txt datacard_ele_2017_M30btag.txt >  datacard_ele_2017.txt
#echo "Ele channel 2018"
#combineCards.py -S datacard_ele_2018_M3.txt datacard_ele_2018_ChIso.txt datacard_ele_2018_M30photon.txt datacard_ele_2018_M30btag.txt >  datacard_ele_2018.txt
#echo "Mu channel 2016"
#combineCards.py -S datacard_mu_2016_M3.txt datacard_mu_2016_ChIso.txt datacard_mu_2016_M30photon.txt datacard_mu_2016_M30btag.txt >  datacard_mu_2016.txt
#echo "Mu channel 2017"
#combineCards.py -S datacard_mu_2017_M3.txt datacard_mu_2017_ChIso.txt datacard_mu_2017_M30photon.txt datacard_mu_2017_M30btag.txt >  datacard_mu_2017.txt
#echo "Mu channel 2018"
#combineCards.py -S datacard_mu_2018_M3.txt datacard_mu_2018_ChIso.txt datacard_mu_2018_M30photon.txt datacard_mu_2018_M30btag.txt >  datacard_mu_2018.txt
#echo "Both Channel 2016"
#combineCards.py -S datacard_ele_2016.txt  datacard_mu_2016.txt > datacard_both_2016.txt
#echo "Both Channel 2017"
#combineCards.py -S datacard_ele_2017.txt  datacard_mu_2017.txt > datacard_both_2017.txt
#echo "Both Channel 2018"
#combineCards.py -S datacard_ele_2018.txt  datacard_mu_2018.txt > datacard_both_2018.txt
#echo "Both channel all year"
#combineCards.py -S datacard_both_2016.txt datacard_both_2017.txt datacard_both_2018.txt > datacard_both_allyear.txt


#echo "Ele channel 2016 4 bins"
#combineCards.py -S datacard_ele_2016_M3.txt datacard_ele_2016_ChIso.txt datacard_ele_2016_M30photon.txt datacard_ele_2016_M30btag.txt >  datacard_ele_2016.txt
#echo "Mu channel 2016 4 bins"
#combineCards.py -S datacard_mu_2016_M3.txt datacard_mu_2016_ChIso.txt datacard_mu_2016_M30photon.txt datacard_mu_2016_M30btag.txt >  datacard_mu_2016.txt
#echo "Both Channel 2016 4 bins"
#combineCards.py -S datacard_ele_2016.txt  datacard_mu_2016.txt > datacard_both_2016.txt


#echo "Ele channel 2016 3 bins"
#combineCards.py -S datacard_ele_2016_M3.txt datacard_ele_2016_ChIso.txt  datacard_ele_2016_M30btag.txt >  datacard_ele_2016.txt
#echo "Mu channel 2016 3 bins"
#combineCards.py -S datacard_mu_2016_M3.txt datacard_mu_2016_ChIso.txt  datacard_mu_2016_M30btag.txt >  datacard_mu_2016.txt
#echo "Both Channel 2016 3 bins"
#combineCards.py -S datacard_ele_2016.txt  datacard_mu_2016.txt > datacard_both_2016.txt


echo "Ele channel 2016 3 bins"
combineCards.py -S M3=datacard_ele_2016_M3.txt ChIso=datacard_ele_2016_ChIso.txt  M30btag=datacard_ele_2016_M30btag.txt >  datacard_ele_2016.txt
echo "Mu channel 2016 3 bins"
combineCards.py -S M3=datacard_mu_2016_M3.txt ChIso=datacard_mu_2016_ChIso.txt  M30btag=datacard_mu_2016_M30btag.txt >  datacard_mu_2016.txt
echo "Both Channel 2016 3 bins"
combineCards.py -S ele=datacard_ele_2016.txt  mu=datacard_mu_2016.txt > datacard_both_2016.txt
