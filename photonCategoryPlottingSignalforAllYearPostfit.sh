for year in 2016 2017 2018
do
python makePhotonCategorySignal.py -y $year -c Ele --tight  --postfit    --tight_photonCategory &
python makePhotonCategorySignal.py -y $year -c Mu  --tight  --postfit    --tight_photonCategory &
done

wait
echo "Done making postfit signal region photonCategory Plots!!"

