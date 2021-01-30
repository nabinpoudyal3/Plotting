
set -x
set -e
ulimit -s unlimited
ulimit -c 0

function error_exit
{
  if [ $1 -ne 0 ]; then
    echo "Error with exit code ${1}"
    if [ -e FrameworkJobReport.xml ]
    then
      cat << EOF > FrameworkJobReport.xml.tmp
      <FrameworkJobReport>
      <FrameworkError ExitStatus="${1}" Type="" >
      Error with exit code ${1}
      </FrameworkError>
EOF
      tail -n+2 FrameworkJobReport.xml >> FrameworkJobReport.xml.tmp
      mv FrameworkJobReport.xml.tmp FrameworkJobReport.xml
    else
      cat << EOF > FrameworkJobReport.xml
      <FrameworkJobReport>
      <FrameworkError ExitStatus="${1}" Type="" >
      Error with exit code ${1}
      </FrameworkError>
      </FrameworkJobReport>
EOF
    fi
    exit 0
  fi
}

trap 'error_exit $?' ERR

if [ $1 -eq 1 ]; then
  ./combine --toys=1000 --expectSignal=1 --redefineSignalPOIs r,nonPromptSF,TTbarSF,WGSF,ZGSF,OtherSF,Other_norm --saveNormalizations --rMin=-1 --rMax=5 --minos all --saveToys -M FitDiagnostics -s 314159 -d datacard_ele_2016.root --setParameterRanges nonPromptSF=-10,10 -n .test
fi
tar -cf combine_output.tar higgsCombine*.root
rm higgsCombine*.root
