import sys
from ZJetSFvalues import *
def getZJetsSF(year,selection):
    selYear = year
    isSelection = selection

    if selYear == "2016": 
        if isSelection   == "looseCRge2ge0": ZJetSF = ZJetSF_2016_looseCRge2ge0 
        elif isSelection == "looseCRge2e0":  ZJetSF = ZJetSF_2016_looseCRge2e0  
        elif isSelection == "looseCRe2e0":   ZJetSF = ZJetSF_2016_looseCRe2e0    
        elif isSelection == "looseCRe3e0":   ZJetSF = ZJetSF_2016_looseCRe3e0    
        elif isSelection == "looseCRge4e0":  ZJetSF = ZJetSF_2016_looseCRge4e0   
        elif isSelection == "looseCRe2e1":   ZJetSF = ZJetSF_2016_looseCRe2e1    
        elif isSelection == "looseCRe3e1":   ZJetSF = ZJetSF_2016_looseCRe3e1   
        elif isSelection == "looseCRe2e2":   ZJetSF = ZJetSF_2016_looseCRe2e2   
        elif isSelection == "looseCRe3ge2":  ZJetSF = ZJetSF_2016_looseCRe3ge2  
        elif isSelection == "tight":         ZJetSF = ZJetSF_2016_tight        
    	else: "Print wrong control region selection"
        return ZJetSF

    elif selYear == "2017": 
        if isSelection   == "looseCRge2ge0": ZJetSF = ZJetSF_2017_looseCRge2ge0
        elif isSelection == "looseCRge2e0":  ZJetSF = ZJetSF_2017_looseCRge2e0 
        elif isSelection == "looseCRe2e0":   ZJetSF = ZJetSF_2017_looseCRe2e0  
        elif isSelection == "looseCRe3e0":   ZJetSF = ZJetSF_2017_looseCRe3e0  
        elif isSelection == "looseCRge4e0":  ZJetSF = ZJetSF_2017_looseCRge4e0 
        elif isSelection == "looseCRe2e1":   ZJetSF = ZJetSF_2017_looseCRe2e1  
        elif isSelection == "looseCRe3e1":   ZJetSF = ZJetSF_2017_looseCRe3e1  
        elif isSelection == "looseCRe2e2":   ZJetSF = ZJetSF_2017_looseCRe2e2  
        elif isSelection == "looseCRe3ge2":  ZJetSF = ZJetSF_2017_looseCRe3ge2 
        elif isSelection == "tight":         ZJetSF = ZJetSF_2017_tight        
    	else: "Print wrong control region selection"
        return ZJetSF

    elif selYear == "2018": 
        if isSelection   == "looseCRge2ge0": ZJetSF = ZJetSF_2018_looseCRge2ge0
        elif isSelection == "looseCRge2e0":  ZJetSF = ZJetSF_2018_looseCRge2e0 
        elif isSelection == "looseCRe2e0":   ZJetSF = ZJetSF_2018_looseCRe2e0  
        elif isSelection == "looseCRe3e0":   ZJetSF = ZJetSF_2018_looseCRe3e0  
        elif isSelection == "looseCRge4e0":  ZJetSF = ZJetSF_2018_looseCRge4e0 
        elif isSelection == "looseCRe2e1":   ZJetSF = ZJetSF_2018_looseCRe2e1  
        elif isSelection == "looseCRe3e1":   ZJetSF = ZJetSF_2018_looseCRe3e1  
        elif isSelection == "looseCRe2e2":   ZJetSF = ZJetSF_2018_looseCRe2e2  
        elif isSelection == "looseCRe3ge2":  ZJetSF = ZJetSF_2018_looseCRe3ge2 
        elif isSelection == "tight":         ZJetSF = ZJetSF_2018_tight        
    	else: "Print wrong control region selection"
        return ZJetSF
    else: 
        print "Wrong year"
        sys.exit()
