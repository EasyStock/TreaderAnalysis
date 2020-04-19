'''
Created on Apr 15, 2019

@author: mac
'''
from . import SimpleFilterBase

class CSimpleFilter_ClosePriceNewHigh(SimpleFilterBase.CSimpleFilterBase):
    def __init__(self, params):
        self.params = params
        SimpleFilterBase.CSimpleFilterBase.__init__(self,None)
        self.filterName = '收盘价新高%d天'%(self.params)
        self.filterDescribe = '收盘价新高%d天'%(self.params)
    
    def FilterCurrentOnly(self, dataFrame):
        if dataFrame is None:
            raise Exception('SimpleFilter_ClosePriceNewHigh dataFrame is None!')

        self.filterResult['FilterName'] = self.filterName
        rows = dataFrame.shape[0]
        last = float(dataFrame.iloc[-1][SimpleFilterBase.stock_ClosePrice])
        N = 0
        for i in range(2, rows):
            if last < float(dataFrame.iloc[-i][SimpleFilterBase.stock_ClosePrice]):
                break
            N = N +1
        
        if N < self.params:
            return False

        return True