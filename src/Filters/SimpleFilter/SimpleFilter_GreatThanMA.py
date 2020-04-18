'''
Created on Apr 15, 2019

@author: mac
'''
from . import SimpleFilterBase

class CSimpleFilter_GreatThanMA(SimpleFilterBase.CSimpleFilterBase):
    def __init__(self, params):
        if isinstance(params, int) == False:
            raise Exception('CSimpleFilter_TradingDay paramater error!')
        self.N = params
        SimpleFilterBase.CSimpleFilterBase.__init__(self,None)
        self.filterName = '股价大于MA%d'%(self.N )
        self.filterDescribe = '股价大于MA%d'%(self.N )
        
    def FilterCurrentOnly(self, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_ZhangDieFu dataFrame is None!')
        
        self.filterResult['FilterName'] = self.filterName
        closePrice = float(dataFrame.iloc[-1][SimpleFilterBase.stock_ClosePrice])
        ma = None
        if self.N == 5:
            ma = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA5])
        elif self.N == 10:
            ma = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA10])
        elif self.N == 20:
            ma = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA20])
        elif self.N == 30:
            ma = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA30])
        elif self.N == 60:
            ma = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA60])
        elif self.N == 120:
            ma = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA120])
        elif self.N == 240:
            try:
             ma = float(dataFrame.iloc[-1][SimpleFilterBase.stock_MA240])
            except:
                ma = 99999999999999
        else:
            raise Exception('CSimpleFilter_GreatThanMA FilterCurrentOnly parameter error!')
        
        key = 'MA%s过滤'%(self.N)
        value = '%s----%s'%(closePrice,ma)
        self.filterResult[key] = value
        if closePrice > ma:
            return True
        else:
            return False