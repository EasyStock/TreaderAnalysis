'''
Created on Jun 10, 2019

@author: mac
'''
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days,stock_Date, stock_Name,\
    stock_ClosePrice
import pandas as pd

class CAdvanceFilter_NewHigh(IAdvanceFilterBase):

    def __init__(self,days):
        '''
        params None
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'%s日新高'%(days)
        self.FilterDescribe = u'创%s日新高'%(days)
        self.param = days
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            print(df.iloc[-1][stock_Days])
    
        try:
            float(df.iloc[-self.param][stock_ClosePrice])
        except:
            return False
    
        return True
    
    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_ClosePrice),copy = True)
        rows = df1.shape[0]
        last = float(df1.iloc[-1][stock_ClosePrice])
        N = 0
        for i in range(2, rows):
            if last < float(df1.iloc[-i][stock_ClosePrice]):
                break
            N = N +1
        
        if N < self.param:
            return (False,)
        
        ret = {}
        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        key = u'%s_天数' %(self.filterName)
        ret[key] = N
        return (True,ret)