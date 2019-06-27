'''
Created on Apr 15, 2019

@author: mac
'''
from StockFilter.Filters.StockFilterBase import IStockFilter
from StockDataItem.StockItemDef import stock_ClosePrice, stock_BOLLUp,\
    stock_Volumn_Ratio, stock_Turnover, stock_Days

class CStockFilterBOLLUP(IStockFilter):

    def __init__(self, params):
        '''
        params 是量比值，带量突破
        '''
        IStockFilter.__init__(self, params)
        self.filterName = u'带量突破上轨'
        self.FilterDescribe = u'股价带量突破上轨'
        
        self.threshold = params
    
    def FilterBy(self, stockInfo):
        info = stockInfo.getStockInfo()
        try:
            days = float(info[stock_Days])
            if days < 250:
                return False
            price = float(info[stock_ClosePrice])
            turnover = float(info[stock_Turnover])
            BOOLUP = float(info[stock_BOLLUp])
            volumn_Ratio = float(info[stock_Volumn_Ratio])
            if isinstance(self.threshold, (list, tuple)):
                if price >= BOOLUP and self.threshold[0] < volumn_Ratio <self.threshold[1] :
                    if turnover < 100000000:
                        print("< 100000000", stockInfo)
                    return True
            else:
                if price >= BOOLUP and volumn_Ratio >= self.threshold :
                    if turnover < 100000000:
                        print("< 100000000", stockInfo)
                    return True
        except:
            return False
        
        return False
    
        