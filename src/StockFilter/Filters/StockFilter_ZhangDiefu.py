'''
Created on Apr 15, 2019

@author: mac
'''
from StockFilter.Filters.StockFilterBase import IStockFilter
from StockDataItem.StockItemDef import stock_ZhangDieFu, stock_Days

class CStockFilterZhangDieFu(IStockFilter):

    def __init__(self,low=-10.5, high=10.5):
        '''
        params 涨跌幅限制
        '''
        IStockFilter.__init__(self,None)
        self.filterName = u'涨幅%s%%-%s%%'%(low , high)
        self.FilterDescribe = u'涨跌幅在 %s%%-%s%% 之间过滤' %(low , high)
        
        self.threshold = (low,high)
    
    def FilterBy(self, stockInfo):
        info = stockInfo.getStockInfo()
        try:
            zhangdieFu = float(info[stock_ZhangDieFu])
            days = float(info[stock_Days])
            if days < 250:
                return False

            if float(self.threshold[0])<= zhangdieFu < float(self.threshold[1]):
                return True
        except:
            return False
        
        return False
    
        