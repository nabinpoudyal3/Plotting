#!/bin/bash

./runSeparateChannelYearFitting.sh
./runBothChannelSeparateYear.sh
./runBothChannelAllYear.sh

wait
python makeTTGammaSF_separrateChannel.py
python makeTTGammaSF_bothChannel.py
python makeTTGammaSF_all.py
