'''
Created on Apr 15, 2019

@author: mac
'''
from StockFilter.Filters.StockFilterBase import IStockFilter
from StockDataItem.StockItemDef import stock_Days, stock_DISTANCE_MA_LONG

class CStockFilter_Distance_MA_Short(IStockFilter):

    def __init__(self, params):
        '''
        params 是阈值 表示乖离值
        '''
        IStockFilter.__init__(self, params)
        self.filterName = u'长期均线乖离过滤'
        self.FilterDescribe = u'长期均线粘合过滤'
        
        self.threshold = params
    
    def FilterBy(self, stockInfo):
        info = stockInfo.getStockInfo()
        try:
            days = float(info[stock_Days])
            if days < 250:
                return False
            distance = float(info[stock_DISTANCE_MA_LONG])
            if distance <= float(self.threshold):
                return True
        except:
            return False
        
        return False
    
        