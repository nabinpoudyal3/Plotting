
for year in 2016
do

python simpleStackHists.py -y $year -c Ele --useQCDMC --looseCRge2e0 &
python simpleStackHists.py -y $year -c Mu  --useQCDMC --looseCRge2e0 &

python simpleStackHists.py -y $year -c Ele --useQCDMC --looseCRe2e0 &
python simpleStackHists.py -y $year -c Mu  --useQCDMC --looseCRe2e0 &

python simpleStackHists.py -y $year -c Ele --useQCDMC --looseCRe3e0 &
python simpleStackHists.py -y $year -c Mu  --useQCDMC --looseCRe3e0 &

python simpleStackHists.py -y $year -c Ele --useQCDMC --looseCRge4e0 &
python simpleStackHists.py -y $year -c Mu  --useQCDMC --looseCRge4e0 &

python simpleStackHists.py -y $year -c Ele --useQCDMC --looseCRe2e1 &
python simpleStackHists.py -y $year -c Mu  --useQCDMC --looseCRe2e1 &

done

wait
echo "Done making Flav category yields !!"

