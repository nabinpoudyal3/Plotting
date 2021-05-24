
set -x 

combineCards.py -S M3=datacard_ele_2016_M3.dat ChIso=datacard_ele_2016_ChIso.dat  zerobtag=datacard_ele_2016_M30btag.dat M30photon=datacard_ele_2016_M30photon.dat > datacard_ele_2016.dat
combineCards.py -S M3=datacard_mu_2016_M3.dat ChIso=datacard_mu_2016_ChIso.dat  zerobtag=datacard_mu_2016_M30btag.dat M30photon=datacard_mu_2016_M30photon.dat > datacard_mu_2016.dat

combineCards.py -S M3=datacard_ele_2017_M3.dat ChIso=datacard_ele_2017_ChIso.dat  zerobtag=datacard_ele_2017_M30btag.dat M30photon=datacard_ele_2017_M30photon.dat > datacard_ele_2017.dat
combineCards.py -S M3=datacard_mu_2017_M3.dat ChIso=datacard_mu_2017_ChIso.dat  zerobtag=datacard_mu_2017_M30btag.dat M30photon=datacard_mu_2017_M30photon.dat > datacard_mu_2017.dat

combineCards.py -S M3=datacard_ele_2018_M3.dat ChIso=datacard_ele_2018_ChIso.dat  zerobtag=datacard_ele_2018_M30btag.dat M30photon=datacard_ele_2018_M30photon.dat > datacard_ele_2018.dat
combineCards.py -S M3=datacard_mu_2018_M3.dat ChIso=datacard_mu_2018_ChIso.dat  zerobtag=datacard_mu_2018_M30btag.dat M30photon=datacard_mu_2018_M30photon.dat > datacard_mu_2018.dat

combineCards.py -S EleSix=datacard_ele_2016.dat EleSev=datacard_ele_2017.dat EleEig=datacard_ele_2017.dat > datacard_ele.dat
combineCards.py -S MuSix=datacard_mu_2016.dat   MuSev=datacard_mu_2017.dat   MuEig=datacard_mu_2017.dat   > datacard_mu.dat

combineCards.py -S Ele=datacard_ele.dat Mu=datacard_mu.dat > datacard_both.dat

exit 1

cp ../ttGamma2016/datacard_ele_2016_M3.dat .
cp ../ttGamma2016/datacard_ele_2016_ChIso.dat .
cp ../ttGamma2016/datacard_ele_2016_M30btag.dat .
cp ../ttGamma2016/datacard_ele_2016_M30photon.dat .
cp ../ttGamma2016/datacard_mu_2016_M3.dat .
cp ../ttGamma2016/datacard_mu_2016_ChIso.dat .
cp ../ttGamma2016/datacard_mu_2016_M30btag.dat .
cp ../ttGamma2016/datacard_mu_2016_M30photon.dat .

cp ../ttGamma2017/datacard_ele_2017_M3.dat .
cp ../ttGamma2017/datacard_ele_2017_ChIso.dat .
cp ../ttGamma2017/datacard_ele_2017_M30btag.dat .
cp ../ttGamma2017/datacard_ele_2017_M30photon.dat .
cp ../ttGamma2017/datacard_mu_2017_M3.dat .
cp ../ttGamma2017/datacard_mu_2017_ChIso.dat .
cp ../ttGamma2017/datacard_mu_2017_M30btag.dat .
cp ../ttGamma2017/datacard_mu_2017_M30photon.dat .

cp ../ttGamma2018/datacard_ele_2018_M3.dat .
cp ../ttGamma2018/datacard_ele_2018_ChIso.dat .
cp ../ttGamma2018/datacard_ele_2018_M30btag.dat .
cp ../ttGamma2018/datacard_ele_2018_M30photon.dat .
cp ../ttGamma2018/datacard_mu_2018_M3.dat .
cp ../ttGamma2018/datacard_mu_2018_ChIso.dat .
cp ../ttGamma2018/datacard_mu_2018_M30btag.dat .
cp ../ttGamma2018/datacard_mu_2018_M30photon.dat .


cp datacard_ele_2016_M3.dat            datacard_ele_2017_M3.dat
cp datacard_ele_2016_ChIso.dat         datacard_ele_2017_ChIso.dat
cp datacard_ele_2016_M30btag.dat       datacard_ele_2017_M30btag.dat
cp datacard_ele_2016_M30photon.dat     datacard_ele_2017_M30photon.dat
cp datacard_mu_2016_M3.dat             datacard_mu_2017_M3.dat
cp datacard_mu_2016_ChIso.dat          datacard_mu_2017_ChIso.dat
cp datacard_mu_2016_M30btag.dat        datacard_mu_2017_M30btag.dat
cp datacard_mu_2016_M30photon.dat      datacard_mu_2017_M30photon.dat


cp datacard_ele_2017_M3.dat            datacard_ele_2018_M3.dat
cp datacard_ele_2017_ChIso.dat         datacard_ele_2018_ChIso.dat
cp datacard_ele_2017_M30btag.dat       datacard_ele_2018_M30btag.dat
cp datacard_ele_2017_M30photon.dat     datacard_ele_2018_M30photon.dat
cp datacard_mu_2017_M3.dat            datacard_mu_2018_M3.dat
cp datacard_mu_2017_ChIso.dat         datacard_mu_2018_ChIso.dat
cp datacard_mu_2017_M30btag.dat       datacard_mu_2018_M30btag.dat
cp datacard_mu_2017_M30photon.dat     datacard_mu_2018_M30photon.dat