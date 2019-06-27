'''
Created on Apr 15, 2019

@author: mac
'''
from StockFilter.Filters.StockFilterBase import IStockFilter
from StockDataItem.StockItemDef import stock_ClosePrice,stock_OpenPrice,\
    stock_MA5, stock_MA240, stock_MA120, stock_MA60, stock_MA30,\
    stock_MA20, stock_MA10, stock_Volumn_Ratio, stock_ClosePrice_Yesterday,\
    stock_Days

class CStockFilterCROSS_MULTI_LINES(IStockFilter):

    def __init__(self, params):
        '''
        params:穿过线根数，量比
        '''
        IStockFilter.__init__(self, params)
        self.filterName = u'一阳穿%s线' %(params[0])
        self.FilterDescribe = u'带量，一阳穿过多根均线'
        
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
            volumn_Ratio = float(info[stock_Volumn_Ratio])
            LINE5 = float(info[stock_MA5])
            LINE10 = float(info[stock_MA10])
            LINE20 = float(info[stock_MA20])
            LINE30 = float(info[stock_MA30])
            LINE60 = float(info[stock_MA60])
            LINE120 = float(info[stock_MA120])
            LINE240 = float(info[stock_MA240])
            MAs = [LINE5, LINE10, LINE20, LINE30, LINE60, LINE120, LINE240]
            count=0
            for ma in MAs:
                if(self._IsCrossLine(down, closePrice, ma)):
                    count = count + 1
            if count == self.threshold[0] and volumn_Ratio>= self.threshold[1]:
                return True
        except:
            return False
        
        return False
    
        