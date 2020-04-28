#!/bin/bash

condor_submit condor_makeHistograms_Dilep_nominal.jdl
condor_submit condor_makeHistograms_Dilep_PU.jdl
condor_submit condor_makeHistograms_Dilep_MuEff.jdl
condor_submit condor_makeHistograms_Dilep_PhoEff.jdl
condor_submit condor_makeHistograms_Dilep_BTagSF_b.jdl
condor_submit condor_makeHistograms_Dilep_BTagSF_l.jdl
condor_submit condor_makeHistograms_Dilep_EleEff.jdl
condor_submit condor_makeHistograms_Dilep_Q2.jdl
#condor_submit condor_makeHistograms_Dilep_Pdf.jdl
#condor_submit condor_makeHistograms_Dilep_isr.jdl
#condor_submit condor_makeHistograms_Dilep_fsr.jdl


