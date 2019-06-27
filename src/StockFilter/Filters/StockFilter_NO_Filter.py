'''
Created on Apr 15, 2019

@author: mac
'''
from StockFilter.Filters.StockFilterBase import IStockFilter

class CStockFilterNoFilter(IStockFilter):

    def __init__(self):
        '''
        params 不过滤
        '''
        IStockFilter.__init__(self,None)
        self.filterName = u'不过滤'
        self.FilterDescribe = u'不过滤'
    
    def FilterBy(self, stockInfo):
        return True
    
        