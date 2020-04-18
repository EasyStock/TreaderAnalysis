'''
Created on Apr 15, 2019

@author: mac
'''
from . import SimpleFilterBase

class CSimpleFilter_TradingDay(SimpleFilterBase.CSimpleFilterBase):
    def __init__(self, params):
        if isinstance(params, (list,tuple)) == False:
            raise Exception('CSimpleFilter_TradingDay paramater error!')
        self.params = params
        SimpleFilterBase.CSimpleFilterBase.__init__(self,None)
        self.filterName = '上市日期%d-%d'%(params[0], params[1])
        self.filterDescribe = '上市日期%d-%d之间过滤'%(params[0], params[1])
        
    def FilterCurrentOnly(self, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_ZhangDieFu dataFrame is None!')

        self.filterResult['FilterName'] = self.filterName
        tradingDays = dataFrame.iloc[-1][SimpleFilterBase.stock_Days]
        try:
            tradingDays = int(tradingDays)
        except:
            tradingDays = int(float(tradingDays[:tradingDays.find('万')])*10000)

        self.filterResult['tradingDays'] = tradingDays
        if float(self.params[0])<= tradingDays < float(self.params[1]):
            return True
        else:
            return False
