#!/bin/bash

combine -M GoodnessOfFit  -n CR123_gof_2016   datacard_CR123_2016.txt  --toysFrequentist --algo=saturated -t 100 -s -1 --plots

wait
echo "Done Fitting"

#

#saturated: Compute a goodness-of-fit measure for binned fits based on the saturated model method, as prescribed by the StatisticsCommittee (note). 
#This quantity is similar to a chi-square, but can be computed for an arbitrary combination of binned channels with arbitrary constraints.
# giving best fit test statistics as 10. What is meant by this?

#KS: Compute a goodness-of-fit measure for binned fits using the Kolmogorov-Smirnov test. 
#It is based on the highest difference between the cumulative distribution function and the empirical distribution function of any bin.
# CDF=cumulative distribution function, EDF=emperical. 

#AD: Compute a goodness-of-fit measure for binned fits using the Anderson-Darling test. 
#It is based on the integral of the difference between the cumulative distribution function and the empirical distribution function over all bins. 
#It also gives the tail ends of the distribution a higher weighting.
