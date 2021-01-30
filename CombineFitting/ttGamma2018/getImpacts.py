import json
from numpy import mean
import sys
import os

from optparse import OptionParser
parser = OptionParser()

parser.add_option("-f", "--filename", dest="filename", default="mu",type='str',
                  help="Specify which json file" )
(options, args) = parser.parse_args()


parNamesJSON = open("parameterNames.json")
parNames = json.load(parNamesJSON)

filename=options.filename
jsonfile = open("%s"%(filename))
data = json.load(jsonfile)
data['params'].sort(key=lambda x: abs(x['impact_r']), reverse=True)


print data['POIs'][0]['fit'][1],data['params'][1]['impact_r']*100

total_sys=0.

print parNames["r"]

table=''
table +=  '\\begin{tabular}{| l | c | c | } \n'
table +=  '\\hline\n'
table +=  'Nuisance Parameter & Total uncertainty on \\ttgamma & Relative Uncertainty (\\%) \\\\ \n'
table +=  '\\hline\n'
for i in range(len(data["params"])):
	vUp = data['params'][i]['r'][2]-data['params'][i]['r'][1]
	vDown = data['params'][i]['r'][0]-data['params'][i]['r'][1]
	print parNames[data["params"][i]['name']]
	table += '%s & %+.4f/%+.4f & %.2f \\\\ \n' %( parNames[data["params"][i]['name']], max(vUp,vDown), min(vUp,vDown),data['params'][i]['impact_r']*100/data['POIs'][0]['fit'][1])

        total_sys+=(data['params'][i]['impact_r']*100/(data['POIs'][0]['fit'][1]))**2.
table += '\\hline \n'
table += '\\end{tabular} \n'
print ""
print ""
print ""
print table
print ""
print ""
print ""

print "Table_%s.tex"%(filename[:-5])
with open("Table_%s.tex"%(filename[:-5]),"w") as _file:
	_file.write(table)
_file.close()


print "contribution from systematics",(total_sys)**0.5



sys.exit()
'''
python getImpacts.py -f impacts_toy_ele_2016.json
python getImpacts.py -f impacts_data_ele_2016.json
python getImpacts.py -f impacts_toy_mu_2016.json
python getImpacts.py -f impacts_data_mu_2016.json
python getImpacts.py -f impacts_toy_both_2016.json
python getImpacts.py -f impacts_data_both_2016.json
'''