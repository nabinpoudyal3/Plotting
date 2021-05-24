#!/bin/bash

condor_submit nominal1.jdl
condor_submit nominal2.jdl
condor_submit nominal3.jdl
condor_submit nominal4.jdl
condor_submit nominal5.jdl
condor_submit nominal6.jdl

condor_submit nominal_ttbar1.jdl
condor_submit nominal_ttbar2.jdl
condor_submit nominal_ttbar3.jdl
condor_submit nominal_ttbar4.jdl
condor_submit nominal_ttbar5.jdl
condor_submit nominal_ttbar6.jdl

# good for nominal

condor_submit syst.jdl
condor_submit syst_ttbar.jdl


exit 1

# makeHistograms_condor_nominal.sh makeHistograms_condor_nominal_onlyTTbar.sh
# makeHistograms_condor_syst.sh    makeHistograms_condor_syst_onlyTTbar.sh


# makeHistograms_Dilep_condor_nominal.sh 
# makeHistograms_Dilep_condor_syst.sh    

condor_submit syst_SS.jdl
condor_submit syst_SS_ttbar.jdl