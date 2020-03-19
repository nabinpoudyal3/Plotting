import sys
from MisIDEleSFvalues import *
from MisIDEleSFvaluesForbins import *
def getMisIDEleSF(year,selection):
    selYear = year
    isSelection = selection
    #CR123=looseCRge2e0, CR1 =looseCRe2e0, CR2 =looseCRe3e0, CR3 =looseCRge4e0, CR4 looseCRe2e1

    if selYear == "2016": 
        if isSelection   == "looseCRge2e0":  tupleSF = (MisIDEleSF_2016_looseCRge2e0, ZGammaSF_2016_looseCRge2e0, WGammaSF_2016_looseCRge2e0) 
        elif isSelection == "looseCRe2e0":   tupleSF = (MisIDEleSF_2016_looseCRe2e0,  ZGammaSF_2016_looseCRe2e0,  WGammaSF_2016_looseCRe2e0)  
        elif isSelection == "looseCRe3e0":   tupleSF = (MisIDEleSF_2016_looseCRe3e0,  ZGammaSF_2016_looseCRe3e0,  WGammaSF_2016_looseCRe3e0)  
        elif isSelection == "looseCRge4e0":  tupleSF = (MisIDEleSF_2016_looseCRge4e0, ZGammaSF_2016_looseCRge4e0, WGammaSF_2016_looseCRge4e0)  
        elif isSelection == "looseCRe2e1":   tupleSF = (MisIDEleSF_2016_looseCRe2e1,  ZGammaSF_2016_looseCRe2e1,  WGammaSF_2016_looseCRe2e1)  
       	else: "Print wrong control region selection"
        return tupleSF

    elif selYear == "2017": 
        if isSelection   == "looseCRge2e0":  tupleSF = (MisIDEleSF_2017_looseCRge2e0, ZGammaSF_2017_looseCRge2e0, WGammaSF_2017_looseCRge2e0)
        elif isSelection == "looseCRe2e0":   tupleSF = (MisIDEleSF_2017_looseCRe2e0,  ZGammaSF_2017_looseCRe2e0,  WGammaSF_2017_looseCRe2e0) 
        elif isSelection == "looseCRe3e0":   tupleSF = (MisIDEleSF_2017_looseCRe3e0,  ZGammaSF_2017_looseCRe3e0,  WGammaSF_2017_looseCRe3e0) 
        elif isSelection == "looseCRge4e0":  tupleSF = (MisIDEleSF_2017_looseCRge4e0, ZGammaSF_2017_looseCRge4e0, WGammaSF_2017_looseCRge4e0)
        elif isSelection == "looseCRe2e1":   tupleSF = (MisIDEleSF_2017_looseCRe2e1,  ZGammaSF_2017_looseCRe2e1,  WGammaSF_2017_looseCRe2e1) 
    	else: "Print wrong control region selection"
        return tupleSF

    elif selYear == "2018": 
        if isSelection   == "looseCRge2e0":  tupleSF = (MisIDEleSF_2018_looseCRge2e0, ZGammaSF_2018_looseCRge2e0, WGammaSF_2018_looseCRge2e0)
        elif isSelection == "looseCRe2e0":   tupleSF = (MisIDEleSF_2018_looseCRe2e0,  ZGammaSF_2018_looseCRe2e0,  WGammaSF_2018_looseCRe2e0) 
        elif isSelection == "looseCRe3e0":   tupleSF = (MisIDEleSF_2018_looseCRe3e0,  ZGammaSF_2018_looseCRe3e0,  WGammaSF_2018_looseCRe3e0) 
        elif isSelection == "looseCRge4e0":  tupleSF = (MisIDEleSF_2018_looseCRge4e0, ZGammaSF_2018_looseCRge4e0, WGammaSF_2018_looseCRge4e0)
        elif isSelection == "looseCRe2e1":   tupleSF = (MisIDEleSF_2018_looseCRe2e1,  ZGammaSF_2018_looseCRe2e1,  WGammaSF_2018_looseCRe2e1) 
    	else: "Print wrong control region selection"
        return tupleSF
    else: 
        print "Wrong year"
        sys.exit()
        
def getMisIDEleSFbins(year,nbins):
	selYear = year
	x = nbins
	if selYear=='2016':
		if    x=='3': tupleSF = (MisIDEleSF_2016_looseCRge2e0_3, ZGammaSF_2016_looseCRge2e0_3, WGammaSF_2016_looseCRge2e0_3)
		elif  x=='6': tupleSF = (MisIDEleSF_2016_looseCRge2e0_6, ZGammaSF_2016_looseCRge2e0_6, WGammaSF_2016_looseCRge2e0_6)
		else:         tupleSF = (MisIDEleSF_2016_looseCRge2e0_9, ZGammaSF_2016_looseCRge2e0_9, WGammaSF_2016_looseCRge2e0_9)
		return tupleSF
	elif selYear=='2017':
		if    x=='3': tupleSF = (MisIDEleSF_2017_looseCRge2e0_3, ZGammaSF_2017_looseCRge2e0_3, WGammaSF_2017_looseCRge2e0_3)
		elif  x=='6': tupleSF = (MisIDEleSF_2017_looseCRge2e0_6, ZGammaSF_2017_looseCRge2e0_6, WGammaSF_2017_looseCRge2e0_6)
		else:         tupleSF = (MisIDEleSF_2017_looseCRge2e0_9, ZGammaSF_2017_looseCRge2e0_9, WGammaSF_2017_looseCRge2e0_9)
		return tupleSF
	else:
		if    x=='3': tupleSF = (MisIDEleSF_2018_looseCRge2e0_3, ZGammaSF_2018_looseCRge2e0_3, WGammaSF_2018_looseCRge2e0_3)
		elif  x=='6': tupleSF = (MisIDEleSF_2018_looseCRge2e0_6, ZGammaSF_2018_looseCRge2e0_6, WGammaSF_2018_looseCRge2e0_6)
		else:         tupleSF = (MisIDEleSF_2018_looseCRge2e0_9, ZGammaSF_2018_looseCRge2e0_9, WGammaSF_2018_looseCRge2e0_9)
		return tupleSF
