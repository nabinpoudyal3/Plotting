import sys
from FullYearMisIDEleSFvalues import *

def getFullYearMisIDEleSF(year,selection):
    selYear = year
    isSelection = selection
    #CR123=looseCRge2e0, CR1 =looseCRe2e0, CR2 =looseCRe3e0, CR3 =looseCRge4e0, CR4 looseCRe2e1

    if selYear == "2016": 
        if isSelection   == "looseCRge2e0":  tupleSF = (MisIDEleSF_2016_looseCRge2e0, ZGammaSF_looseCRge2e0, WGammaSF_looseCRge2e0) 
        elif isSelection == "looseCRe2e0":   tupleSF = (MisIDEleSF_2016_looseCRe2e0,  ZGammaSF_looseCRe2e0,  WGammaSF_looseCRe2e0)  
        elif isSelection == "looseCRe3e0":   tupleSF = (MisIDEleSF_2016_looseCRe3e0,  ZGammaSF_looseCRe3e0,  WGammaSF_looseCRe3e0)  
        elif isSelection == "looseCRge4e0":  tupleSF = (MisIDEleSF_2016_looseCRge4e0, ZGammaSF_looseCRge4e0, WGammaSF_looseCRge4e0)  
        elif isSelection == "looseCRe2e1":   tupleSF = (MisIDEleSF_2016_looseCRe2e1,  ZGammaSF_looseCRe2e1,  WGammaSF_looseCRe2e1)  
        else: "Print wrong control region selection"
        return tupleSF

    elif selYear == "2017": 
        if isSelection   == "looseCRge2e0":  tupleSF = (MisIDEleSF_2017_looseCRge2e0, ZGammaSF_looseCRge2e0, WGammaSF_looseCRge2e0)
        elif isSelection == "looseCRe2e0":   tupleSF = (MisIDEleSF_2017_looseCRe2e0,  ZGammaSF_looseCRe2e0,  WGammaSF_looseCRe2e0) 
        elif isSelection == "looseCRe3e0":   tupleSF = (MisIDEleSF_2017_looseCRe3e0,  ZGammaSF_looseCRe3e0,  WGammaSF_looseCRe3e0) 
        elif isSelection == "looseCRge4e0":  tupleSF = (MisIDEleSF_2017_looseCRge4e0, ZGammaSF_looseCRge4e0, WGammaSF_looseCRge4e0)
        elif isSelection == "looseCRe2e1":   tupleSF = (MisIDEleSF_2017_looseCRe2e1,  ZGammaSF_looseCRe2e1,  WGammaSF_looseCRe2e1) 
        else: "Print wrong control region selection"
        return tupleSF

    elif selYear == "2018": 
        if isSelection   == "looseCRge2e0":  tupleSF = (MisIDEleSF_2018_looseCRge2e0, ZGammaSF_looseCRge2e0, WGammaSF_looseCRge2e0)
        elif isSelection == "looseCRe2e0":   tupleSF = (MisIDEleSF_2018_looseCRe2e0,  ZGammaSF_looseCRe2e0,  WGammaSF_looseCRe2e0) 
        elif isSelection == "looseCRe3e0":   tupleSF = (MisIDEleSF_2018_looseCRe3e0,  ZGammaSF_looseCRe3e0,  WGammaSF_looseCRe3e0) 
        elif isSelection == "looseCRge4e0":  tupleSF = (MisIDEleSF_2018_looseCRge4e0, ZGammaSF_looseCRge4e0, WGammaSF_looseCRge4e0)
        elif isSelection == "looseCRe2e1":   tupleSF = (MisIDEleSF_2018_looseCRe2e1,  ZGammaSF_looseCRe2e1,  WGammaSF_looseCRe2e1) 
        else: "Print wrong control region selection"
        return tupleSF
    else: 
        print "Wrong year"
        sys.exit()
