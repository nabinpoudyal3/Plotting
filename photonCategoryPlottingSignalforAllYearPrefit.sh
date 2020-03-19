for year in 2016 2017 2018
do
python makePhotonCategorySignal.py -y $year -c Ele --tight     --tight_photonCategory &
python makePhotonCategorySignal.py -y $year -c Mu  --tight     --tight_photonCategory &
done

wait
echo "Done making prefit signal region M3 photon category Plots!!"

