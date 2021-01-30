#!/bin/bash

cp /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/Plotting/ttgamma_tightplots_ele_2016/ttgamma_Prefit.root ttgamma_tightplots_ele_2016/

tar cfP myFitting.tar ttgamma_tightplots_ele_2016 datacard_ele_2016.txt

xrdcp -f myFitting.tar  root://cmseos.fnal.gov//store/user/npoudyal/

tar -xvf myFitting.tar


                                               

