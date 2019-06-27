'''
Created on Apr 15, 2019

@author: mac
'''
from StockFilter.Filters.StockFilterBase import IStockFilter
from StockDataItem.StockItemDef import stock_ClosePrice,\
    stock_MA5, stock_MA240, stock_MA120, stock_MA60, stock_MA30,\
    stock_MA20, stock_MA10,\
    stock_Days

class CStockFilterGreater_Than_MA_N(IStockFilter):

    def __init__(self, params):
        '''
        params:大于MA N
        '''
        IStockFilter.__init__(self, params)
        self.filterName = u'大于MA%03d线' %(int(params))
        self.FilterDescribe = u'大于MA N'
        
        self.threshold = params
    
    def FilterBy(self, stockInfo):
        info = stockInfo.getStockInfo()
        try:
            days = float(info[stock_Days])
            if days < 250:
                return False
            closePrice = float(info[stock_ClosePrice])

            LINE5 = float(info[stock_MA5])
            LINE10 = float(info[stock_MA10])
            LINE20 = float(info[stock_MA20])
            LINE30 = float(info[stock_MA30])
            LINE60 = float(info[stock_MA60])
            LINE120 = float(info[stock_MA120])
            LINE240 = float(info[stock_MA240])
        except:
            return False 
        N = float(self.threshold)
        ma = LINE5
        if N == 5:
            ma = LINE5
        elif N == 10:
            ma = LINE10
        elif N == 20:
            ma = LINE20
        elif N == 30:
            ma = LINE30
        elif N == 60:
            ma = LINE60
        elif N == 120:
            ma = LINE120
        elif N == 240:
            ma = LINE240
        else:
            raise Exception("unkonw MA %d",N)
        
        if(closePrice > ma):
            return True

        return False
    
        