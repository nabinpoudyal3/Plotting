
for year in 2016
do

python makeHadFlavYield.py -y $year -c Ele --looseCRge2e0 &
python makeHadFlavYield.py -y $year -c Mu  --looseCRge2e0 &

python makeHadFlavYield.py -y $year -c Ele --looseCRe2e0 &
python makeHadFlavYield.py -y $year -c Mu  --looseCRe2e0 &

python makeHadFlavYield.py -y $year -c Ele --looseCRe3e0 &
python makeHadFlavYield.py -y $year -c Mu  --looseCRe3e0 &

python makeHadFlavYield.py -y $year -c Ele --looseCRge4e0 &
python makeHadFlavYield.py -y $year -c Mu  --looseCRge4e0 &

python makeHadFlavYield.py -y $year -c Ele --looseCRe2e1 &
python makeHadFlavYield.py -y $year -c Mu  --looseCRe2e1 &

done

wait
echo "Done making Flav category yields !!"

