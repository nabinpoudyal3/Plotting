#!/bin/bash

channel=$1
year=$2
controlRegion=$3

if [ $channel == "Ele" ]; then
	mychannel="ele"
else
	mychannel="mu"

fi

printf "Start Running Histogramming at ";/bin/date
printf "Worker node hostname ";/bin/hostname
echo "---------------------------------------------"

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
    echo "Running Interactively" ; 
else
    echo "Running In Batch"
    cd ${_CONDOR_SCRATCH_DIR}
    echo ${_CONDOR_SCRATCH_DIR}
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    xrdcp -f root://cmseos.fnal.gov//store/user/npoudyal/CMSSW_10_2_14.tgz .
    tar -xvf CMSSW_10_2_14.tgz
    cd CMSSW_10_2_14/src
    eval `scramv1 runtime -sh`
    cd ../..
    tar -xvf myHistograms.tar

fi

outputdir="root://cmseos.fnal.gov//store/user/npoudyal"

echo "Running python makeHistograms "
#declare -a    SampleList=("TTGamma" "TTbar" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCD" "Data" )
#declare -a SampleListEle=("TTGamma" "TTbar" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCDEle" "DataEle" )
#declare -a  SampleListMu=("TTGamma" "TTbar" "SingleTop" "WJets" "ZJets" "WGamma" "ZGamma" "Diboson" "TTV" "GJets" "QCDMu" "DataMu" )

declare -a    SampleList=("TTGamma" )
#declare -a SampleListEle=("DataEle" )
#declare -a  SampleListMu=("DataMu" )


for mysample in ${SampleList[@]}; do
	python makeHistograms.py -c $channel -y $year --$controlRegion -s $mysample --makePlotsForSF --verbose
done
printf "Done Histogramming at ";/bin/date


