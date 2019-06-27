'''
Created on Apr 15, 2019

@author: mac
'''

from StockDataItem.StockItemDef import stock_ClosePrice,stock_OpenPrice,\
    stock_MA5, stock_MA240, stock_MA120, stock_MA60, stock_MA30,\
    stock_MA20, stock_MA10, stock_Volumn_Ratio, stock_ClosePrice_Yesterday,\
    stock_Days
from StockFilter.Filters.StockFilterBase import IStockFilter

class CStockFilterCROSS_MA_N(IStockFilter):

    def __init__(self, params):
        '''
        params:穿过MAN，量比
        '''
        IStockFilter.__init__(self, params)
        self.filterName = u'上穿MA%03d线' %(int(params[0]))
        self.FilterDescribe = u'带量，上穿MA N'
        
        self.threshold = params
    
    def _IsCrossLine(self,down, up, mid):
        if float(down) <= float(mid) <= float(up):
            return True
        return False
    
    def FilterBy(self, stockInfo):
        info = stockInfo.getStockInfo()
        try:
            days = float(info[stock_Days])
            if days < 250:
                return False
            closePrice = float(info[stock_ClosePrice])
            openPrice = float(info[stock_OpenPrice])
            closePriceYesterday = float(info[stock_ClosePrice_Yesterday])
            if openPrice > closePrice:
                return False
            
            down = min((openPrice, closePriceYesterday))
            #volumn_Ratio = float(info[stock_Volumn_Ratio])
            LINE5 = float(info[stock_MA5])
            LINE10 = float(info[stock_MA10])
            LINE20 = float(info[stock_MA20])
            LINE30 = float(info[stock_MA30])
            LINE60 = float(info[stock_MA60])
            LINE120 = float(info[stock_MA120])
            LINE240 = float(info[stock_MA240])
        except:
            return False 
        N = float(self.threshold[0])
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
        
        if(self._IsCrossLine(down, closePrice, ma)):
            return True
#             if(self._IsCrossLine(down, closePrice, ma)) and volumn_Ratio>= self.threshold[1]:
#                 return True

        return False
    
        