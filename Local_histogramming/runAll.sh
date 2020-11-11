#!/bin/bash

#./runThisFirst.sh
#./runDilepNominal.sh >& dilepNominal.log
./runDilepSyst.sh    >& dilepSyst.log
./runNominal.sh      >& singleNominal.log
./runSyst.sh         >& singleSyst.log

wait 
echo "Done"
