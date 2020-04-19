'''
Created on Apr 15, 2019

@author: mac
'''
from . import SimpleFilterBase

class CSimpleFilter_UpStates(SimpleFilterBase.CSimpleFilterBase):
    def __init__(self, params = None):
        self.params = params
        SimpleFilterBase.CSimpleFilterBase.__init__(self,None)
        self.filterName = '上升趋势'
        self.filterDescribe = '上升趋势过滤'

    def FilterCurrentOnly(self, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_UpdateState dataFrame is None!')

        self.filterResult['FilterName'] = self.filterName
        try:
            ma20_1 = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA20])
            ma30_1 = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA30])
            ma60_1 = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA60])

            ma20_2 = float(dataFrame.iloc[-2][SimpleFilterBase.stock_MA20])
            ma30_2 = float(dataFrame.iloc[-2][SimpleFilterBase.stock_MA30])
            ma60_2 = float(dataFrame.iloc[-2][SimpleFilterBase.stock_MA60])

            if ma20_1 < ma20_2:
                return False
            
            if ma30_1 < ma30_2:
                return False

            if ma60_1 < ma60_2:
                return False
            
            if ma60_1 <= ma30_1 <= ma20_1:
                return True
            else:
                return False
        except:
            return False

        