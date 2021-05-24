#!/bin/bash

set -x

combineCards.py -S M3=datacard_ele_2016_M3.dat ChIso=datacard_ele_2016_ChIso.dat zerobtag=datacard_ele_2016_M30btag.dat M30photon=datacard_ele_2016_M30photon.dat >  datacard_ele_2016.dat
combineCards.py -S M3=datacard_mu_2016_M3.dat  ChIso=datacard_mu_2016_ChIso.dat  zerobtag=datacard_mu_2016_M30btag.dat  M30photon=datacard_mu_2016_M30photon.dat  >  datacard_mu_2016.dat
combineCards.py -S ele=datacard_ele_2016.dat   mu=datacard_mu_2016.dat > datacard_both_2016.dat

exit 1





