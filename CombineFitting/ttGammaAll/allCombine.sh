

combineCards.py -S M3=datacard_ele_2016_M3_DD.txt ChIso=datacard_ele_2016_ChIso_DD.txt  zerobtag=datacard_ele_2016_M30btag_DD.txt M30photon=datacard_ele_2016_M30photon_DD.txt > datacard_ele_2016.txt
combineCards.py -S M3=datacard_mu_2016_M3_DD.txt ChIso=datacard_mu_2016_ChIso_DD.txt  zerobtag=datacard_mu_2016_M30btag_DD.txt M30photon=datacard_mu_2016_M30photon_DD.txt > datacard_mu_2016.txt
combineCards.py -S ele=datacard_ele_2016.txt  mu=datacard_mu_2016.txt > datacard_both_2016.txt

combineCards.py -S M3=datacard_ele_2017_M3_DD.txt ChIso=datacard_ele_2017_ChIso_DD.txt  zerobtag=datacard_ele_2017_M30btag_DD.txt M30photon=datacard_ele_2017_M30photon_DD.txt > datacard_ele_2017.txt
combineCards.py -S M3=datacard_mu_2017_M3_DD.txt ChIso=datacard_mu_2017_ChIso_DD.txt  zerobtag=datacard_mu_2017_M30btag_DD.txt M30photon=datacard_mu_2017_M30photon_DD.txt > datacard_mu_2017.txt
combineCards.py -S ele=datacard_ele_2017.txt  mu=datacard_mu_2017.txt > datacard_both_2017.txt

combineCards.py -S M3=datacard_ele_2018_M3_DD.txt ChIso=datacard_ele_2018_ChIso_DD.txt  zerobtag=datacard_ele_2018_M30btag_DD.txt M30photon=datacard_ele_2018_M30photon_DD.txt > datacard_ele_2018.txt
combineCards.py -S M3=datacard_mu_2018_M3_DD.txt ChIso=datacard_mu_2018_ChIso_DD.txt  zerobtag=datacard_mu_2018_M30btag_DD.txt M30photon=datacard_mu_2018_M30photon_DD.txt > datacard_mu_2018.txt
combineCards.py -S ele=datacard_ele_2018.txt  mu=datacard_mu_2018.txt > datacard_both_2018.txt

combineCards.py -S Six=datacard_both_2016.txt Sev=datacard_both_2017.txt Eig=datacard_both_2018.txt > datacard.txt

exit 1

cp ../ttGamma2016/datacard_ele_2016_M3_DD.txt .
cp ../ttGamma2016/datacard_ele_2016_ChIso_DD.txt .
cp ../ttGamma2016/datacard_ele_2016_M30btag_DD.txt .
cp ../ttGamma2016/datacard_ele_2016_M30photon_DD.txt .
cp ../ttGamma2016/datacard_mu_2016_M3_DD.txt .
cp ../ttGamma2016/datacard_mu_2016_ChIso_DD.txt .
cp ../ttGamma2016/datacard_mu_2016_M30btag_DD.txt .
cp ../ttGamma2016/datacard_mu_2016_M30photon_DD.txt .

cp ../ttGamma2017/datacard_ele_2017_M3_DD.txt .
cp ../ttGamma2017/datacard_ele_2017_ChIso_DD.txt .
cp ../ttGamma2017/datacard_ele_2017_M30btag_DD.txt .
cp ../ttGamma2017/datacard_ele_2017_M30photon_DD.txt .
cp ../ttGamma2017/datacard_mu_2017_M3_DD.txt .
cp ../ttGamma2017/datacard_mu_2017_ChIso_DD.txt .
cp ../ttGamma2017/datacard_mu_2017_M30btag_DD.txt .
cp ../ttGamma2017/datacard_mu_2017_M30photon_DD.txt .

cp ../ttGamma2018/datacard_ele_2018_M3_DD.txt .
cp ../ttGamma2018/datacard_ele_2018_ChIso_DD.txt .
cp ../ttGamma2018/datacard_ele_2018_M30btag_DD.txt .
cp ../ttGamma2018/datacard_ele_2018_M30photon_DD.txt .
cp ../ttGamma2018/datacard_mu_2018_M3_DD.txt .
cp ../ttGamma2018/datacard_mu_2018_ChIso_DD.txt .
cp ../ttGamma2018/datacard_mu_2018_M30btag_DD.txt .
cp ../ttGamma2018/datacard_mu_2018_M30photon_DD.txt .
