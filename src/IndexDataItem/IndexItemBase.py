'''
Created on May 3, 2019

@author: mac
'''
from IndexDataItem.IndexItemT import CIndexItemTemplate

class CIndexItemBase(CIndexItemTemplate):

    def __init__(self):
        CIndexItemTemplate.__init__(self)
                 
    def getColunmInfo(self):
        return self.indexInfo.keys()
    
    def formatToDict(self):
        return self.indexInfo
    
    def getindexInfo(self):
        return self.indexInfo
     
    def FilterBy(self, indexFilter):
        if indexFilter:
            return indexFilter.FilterBy(self)
        else:
            return False
        
    def initWithDict(self,dict_):
        for key in dict_:
            self.indexInfo[key] = dict_[key]
        
        self.validate()
            
    def validate(self):
        keys = self.indexInfo.keys()
        for key in keys:
            if self.indexInfo[key] == None:
                msg = 'Key:%s, not set!'%(key)
                raise Exception(msg)
    