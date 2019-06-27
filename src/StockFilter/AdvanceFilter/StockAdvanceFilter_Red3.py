'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date,\
    stock_Name, stock_ClosePrice, stock_OpenPrice

class CAdvanceFilter_Red3(IAdvanceFilterBase):

    def __init__(self):
        '''
        params
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'红三兵'
        self.FilterDescribe = u'股价连续三天阳线,'
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass
    
        try:
            float(df.iloc[-3][stock_ClosePrice])
            float(df.iloc[-3][stock_OpenPrice])
        except:
            return False
    
        return True
    

    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_OpenPrice, stock_ClosePrice),copy = True)
        
        open1 = float(df1.iloc[-1][stock_OpenPrice])
        close1 =  float(df1.iloc[-1][stock_ClosePrice])
        open2 = float(df1.iloc[-2][stock_OpenPrice])
        close2 =  float(df1.iloc[-2][stock_ClosePrice])
        open3 = float(df1.iloc[-3][stock_OpenPrice])
        close3 =  float(df1.iloc[-3][stock_ClosePrice])
        
        ret = {}
        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"

        if  close1 > close2 > close3 and  open1 > open2 > open3      \
            and  close1 > open1 and  close2 > open2 and  close3 > open3:
            return (True,ret)
        
        return (False,)
    
if __name__ == '__main__':
    pass