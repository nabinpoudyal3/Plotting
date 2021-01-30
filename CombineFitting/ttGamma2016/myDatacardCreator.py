
#comment: not effective way to make data card so stop using it

line = ""
line += "imax 4\n"
line += "jmax *\n"
line += "kmax *\n"
line += "-------------------------------------------------------------------------------------------------------------------------------\n"
line += "shapes *  *  ../../ttgamma_tightplots_ele_2016/ttgamma_Prefit.root  $CHANNEL/$PROCESS/nominal   $CHANNEL/$PROCESS/$SYSTEMATIC\n"
line += "-------------------------------------------------------------------------------------------------------------------------------\n"
line += "bin			    ChIso	M3     M30btag    M30photon\n"
line += "observation		-1		-1     -1         -1\n"

for mybin in ["ChIso","M3","M30btag","M30photon"]:
	line += "bin     %s		%s"


with open("myTestDatacard.txt","w") as _file:
    _file.write(line)
