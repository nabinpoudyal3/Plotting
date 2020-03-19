
for year in 2016 2017 2018
do
python makePhotonCategoryYield.py -y $year -c Ele --tight &
python makePhotonCategoryYield.py -y $year -c Mu  --tight &
done

wait
echo "Done making photon category yields !!"

