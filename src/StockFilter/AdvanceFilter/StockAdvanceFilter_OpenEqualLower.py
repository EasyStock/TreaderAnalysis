'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date,\
    stock_Name, stock_ClosePrice, stock_OpenPrice, stock_LowerPrice

class CAdvanceFilter_OpenEqualLower(IAdvanceFilterBase):

    def __init__(self):
        '''
        params
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'开盘价就是最低价'
        self.FilterDescribe = u'开盘价就是最低价,'
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass
    
        try:
            float(df.iloc[-3][stock_LowerPrice])
            float(df.iloc[-3][stock_OpenPrice])
        except:
            return False
    
        return True
    

    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_OpenPrice, stock_ClosePrice,stock_LowerPrice),copy = True)
        
        open1 = float(df1.iloc[-1][stock_OpenPrice])
        low1 = float(df1.iloc[-1][stock_LowerPrice])
        close1 = float(df.iloc[-1][stock_ClosePrice])
        if open1 != low1:
            return (False,)
        
        ret = {}
        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        date = df.iloc[-1][stock_Date]
        ret["%s_收盘价"%(date)] = close1
        
        return (True,ret)
    
if __name__ == '__main__':
    pass