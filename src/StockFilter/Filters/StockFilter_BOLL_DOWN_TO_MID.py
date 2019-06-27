'''
Created on Apr 15, 2019

@author: mac
'''
from StockDataItem.StockItemDef import stock_ClosePrice,\
    stock_Volumn_Ratio, stock_Turnover, stock_OpenPrice, stock_BOLLMid,\
    stock_BOLLDown, stock_Days
from StockFilter.Filters.StockFilterBase import IStockFilter

class CStockFilterBOLL_DOWN_TO_MID(IStockFilter):

    def __init__(self, params):
        '''
        params:是量比值，带量突破
        '''
        IStockFilter.__init__(self, params)
        self.filterName = u'下轨之下破中轨'
        self.FilterDescribe = u'从下轨之下放大阳,带量突破中轨'
        
        self.threshold = params
    
    def FilterBy(self, stockInfo):
        info = stockInfo.getStockInfo()
        try:
            days = float(info[stock_Days])
            if days < 250:
                return False
            closePrice = float(info[stock_ClosePrice])
            openPrice = float(info[stock_OpenPrice])
            turnover = float(info[stock_Turnover])
            BOOLDWON = float(info[stock_BOLLDown])
            BOOLMID = float(info[stock_BOLLMid])
            volumn_Ratio = float(info[stock_Volumn_Ratio])
            if isinstance(self.threshold, (list, tuple)):
                if openPrice <= BOOLDWON and closePrice >= BOOLMID and self.threshold[0] < volumn_Ratio <self.threshold[1] :
                    if turnover < 100000000:
                        print("< 100000000", stockInfo)
                    return True
            else:
                if openPrice <= BOOLDWON and closePrice >= BOOLMID and volumn_Ratio >= self.threshold :
                    if turnover < 100000000:
                        print("< 100000000", stockInfo)
                    return True
        except:
            return False
        
        return False
    
        