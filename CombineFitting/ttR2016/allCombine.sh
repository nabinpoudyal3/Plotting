#!/bin/bash

set -x

combineCards.py -S M3=datacard_ele_2016_M3.dat ChIso=datacard_ele_2016_ChIso.dat zerobtag=datacard_ele_2016_M30btag.dat M30photon=datacard_ele_2016_M30photon.dat >  datacard_ele_2016.dat
combineCards.py -S M3=datacard_mu_2016_M3.dat  ChIso=datacard_mu_2016_ChIso.dat  zerobtag=datacard_mu_2016_M30btag.dat  M30photon=datacard_mu_2016_M30photon.dat  >  datacard_mu_2016.dat
combineCards.py -S ele=datacard_ele_2016.dat   mu=datacard_mu_2016.dat > datacard_both_2016.dat

exit 1











# echo "Ele channel 2016 4 bins with Data Driven template"
# combineCards.py -S M3=datacard_ele_2016_M3_DD.dat ChIso=datacard_ele_2016_ChIso_DD.dat  zerobtag=datacard_ele_2016_M30btag_DD.dat M30photon=datacard_ele_2016_M30photon_DD.dat >  datacard_ele_2016.dat
# echo "Mu channel 2016 4 bins  with Data Driven template"
# combineCards.py -S M3=datacard_mu_2016_M3_DD.dat  ChIso=datacard_mu_2016_ChIso_DD.dat   zerobtag=datacard_mu_2016_M30btag_DD.dat  M30photon=datacard_mu_2016_M30photon_DD.dat >   datacard_mu_2016.dat
# echo "Both Channel 2016 4 bins  with Data Driven template"
# combineCards.py -S ele=datacard_ele_2016.dat  mu=datacard_mu_2016.dat > datacard_both_2016.dat

# exit 1

# echo "Ele channel 2016 4 bins"
# combineCards.py -S M3=datacard_ele_2016_M3.dat ChIso=datacard_ele_2016_ChIso.dat  zerobtag=datacard_ele_2016_M30btag.dat M30photon=datacard_ele_2016_M30photon.dat >  datacard_ele_2016.dat
# echo "Mu channel 2016 4 bins"
# combineCards.py -S M3=datacard_mu_2016_M3.dat ChIso=datacard_mu_2016_ChIso.dat zerobtag=datacard_mu_2016_M30btag.dat M30photon=datacard_mu_2016_M30photon.dat >  datacard_mu_2016.dat
# echo "Both Channel 2016 4 bins"
# combineCards.py -S ele=datacard_ele_2016.dat  mu=datacard_mu_2016.dat > datacard_both_2016.dat

# exit 1

#echo "Ele channel 2016"
#combineCards.py -S datacard_ele_2016_M3.dat datacard_ele_2016_ChIso.dat datacard_ele_2016_M30photon.dat datacard_ele_2016_M30btag.dat >  datacard_ele_2016.dat
#echo "Ele channel 2017"
#combineCards.py -S datacard_ele_2017_M3.dat datacard_ele_2017_ChIso.dat datacard_ele_2017_M30photon.dat datacard_ele_2017_M30btag.dat >  datacard_ele_2017.dat
#echo "Ele channel 2018"
#combineCards.py -S datacard_ele_2018_M3.dat datacard_ele_2018_ChIso.dat datacard_ele_2018_M30photon.dat datacard_ele_2018_M30btag.dat >  datacard_ele_2018.dat
#echo "Mu channel 2016"
#combineCards.py -S datacard_mu_2016_M3.dat datacard_mu_2016_ChIso.dat datacard_mu_2016_M30photon.dat datacard_mu_2016_M30btag.dat >  datacard_mu_2016.dat
#echo "Mu channel 2017"
#combineCards.py -S datacard_mu_2017_M3.dat datacard_mu_2017_ChIso.dat datacard_mu_2017_M30photon.dat datacard_mu_2017_M30btag.dat >  datacard_mu_2017.dat
#echo "Mu channel 2018"
#combineCards.py -S datacard_mu_2018_M3.dat datacard_mu_2018_ChIso.dat datacard_mu_2018_M30photon.dat datacard_mu_2018_M30btag.dat >  datacard_mu_2018.dat
#echo "Both Channel 2016"
#combineCards.py -S datacard_ele_2016.dat  datacard_mu_2016.dat > datacard_both_2016.dat
#echo "Both Channel 2017"
#combineCards.py -S datacard_ele_2017.dat  datacard_mu_2017.dat > datacard_both_2017.dat
#echo "Both Channel 2018"
#combineCards.py -S datacard_ele_2018.dat  datacard_mu_2018.dat > datacard_both_2018.dat
#echo "Both channel all year"
#combineCards.py -S datacard_both_2016.dat datacard_both_2017.dat datacard_both_2018.dat > datacard_both_allyear.dat


#echo "Ele channel 2016 4 bins"
#combineCards.py -S datacard_ele_2016_M3.dat datacard_ele_2016_ChIso.dat datacard_ele_2016_M30photon.dat datacard_ele_2016_M30btag.dat >  datacard_ele_2016.dat
#echo "Mu channel 2016 4 bins"
#combineCards.py -S datacard_mu_2016_M3.dat datacard_mu_2016_ChIso.dat datacard_mu_2016_M30photon.dat datacard_mu_2016_M30btag.dat >  datacard_mu_2016.dat
#echo "Both Channel 2016 4 bins"
#combineCards.py -S datacard_ele_2016.dat  datacard_mu_2016.dat > datacard_both_2016.dat


#echo "Ele channel 2016 3 bins"
#combineCards.py -S datacard_ele_2016_M3.dat datacard_ele_2016_ChIso.dat  datacard_ele_2016_M30btag.dat >  datacard_ele_2016.dat
#echo "Mu channel 2016 3 bins"
#combineCards.py -S datacard_mu_2016_M3.dat datacard_mu_2016_ChIso.dat  datacard_mu_2016_M30btag.dat >  datacard_mu_2016.dat
#echo "Both Channel 2016 3 bins"
#combineCards.py -S datacard_ele_2016.dat  datacard_mu_2016.dat > datacard_both_2016.dat


#echo "Ele channel 2016 3 bins"
#combineCards.py -S M3=datacard_ele_2016_M3.dat ChIso=datacard_ele_2016_ChIso.dat  zerobtag=datacard_ele_2016_M30btag.dat >  datacard_ele_2016.dat
#echo "Mu channel 2016 3 bins"
#combineCards.py -S M3=datacard_mu_2016_M3.dat ChIso=datacard_mu_2016_ChIso.dat  zerobtag=datacard_mu_2016_M30btag.dat >  datacard_mu_2016.dat
#echo "Both Channel 2016 3 bins"
#combineCards.py -S ele=datacard_ele_2016.dat  mu=datacard_mu_2016.dat > datacard_both_2016.dat

exit 1



subl -n datacard_ele_2016_M3.dat datacard_ele_2016_ChIso.dat  datacard_ele_2016_M30btag.dat datacard_ele_2016_M30photon.dat datacard_mu_2016_M3.dat datacard_mu_2016_ChIso.dat datacard_mu_2016_M30btag.dat datacard_mu_2016_M30photon.dat
cp datacard_ele_2016_M3_DD.dat       datacard_ele_2016_M3.dat       
cp datacard_ele_2016_ChIso_DD.dat     datacard_ele_2016_ChIso.dat     
cp datacard_ele_2016_M30btag_DD.dat   datacard_ele_2016_M30btag.dat   
cp datacard_ele_2016_M30photon_DD.dat   datacard_ele_2016_M30photon.dat   
cp datacard_mu_2016_M3_DD.dat         datacard_mu_2016_M3.dat         
cp datacard_mu_2016_ChIso_DD.dat       datacard_mu_2016_ChIso.dat       
cp datacard_mu_2016_M30btag_DD.dat      datacard_mu_2016_M30btag.dat      
cp datacard_mu_2016_M30photon_DD.dat    datacard_mu_2016_M30photon.dat    

exit 1









































