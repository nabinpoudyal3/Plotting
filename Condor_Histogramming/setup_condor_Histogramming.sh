#!/bin/bash
rm makeHistograms.py
rm sampleInformation.py
rm HistogramListDict.py
rm myListOfHistograms.py
cd ..
tar cfP myHistograms.tar makeHistograms.py sampleInformation.py HistogramListDict.py myListOfHistograms.py
mv myHistograms.tar Condor_Histogramming
cd Condor_Histogramming
xrdcp -f myHistograms.tar  root://cmseos.fnal.gov//store/user/npoudyal/

tar -xvf myHistograms.tar


                                               

