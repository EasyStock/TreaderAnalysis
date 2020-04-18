'''
Created on Apr 15, 2019

@author: mac
'''
from . import SimpleFilterBase

class CSimpleFilter_NotST(SimpleFilterBase.CSimpleFilterBase):
    def __init__(self, params = None):
        SimpleFilterBase.CSimpleFilterBase.__init__(self,None)
        self.filterName = '非ST'
        self.filterDescribe = '非ST过滤'
        
    def FilterCurrentOnly(self, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_ZhangDieFu dataFrame is None!')

        self.filterResult['FilterName'] = self.filterName
        name = dataFrame.iloc[-1][SimpleFilterBase.stock_Name]
        self.filterResult['Name'] = name
        if name.lower().find('st') != -1:
            return False

        return True