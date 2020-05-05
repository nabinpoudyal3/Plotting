#!/bin/bash
rm makeHistograms.py
rm sampleInformation.py
rm HistogramListDict2016.py
rm HistogramListDict2017.py
rm HistogramListDict2018.py

cd ..
tar cfP myHistograms.tar makeHistograms.py sampleInformation.py HistogramListDict2016.py HistogramListDict2017.py HistogramListDict2018.py
mv myHistograms.tar Condor_Histogramming
cd Condor_Histogramming
xrdcp -f myHistograms.tar  root://cmseos.fnal.gov//store/user/npoudyal/

tar -xvf myHistograms.tar


                                               

