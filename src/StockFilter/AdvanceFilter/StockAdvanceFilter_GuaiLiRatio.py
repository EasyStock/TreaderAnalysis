'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_RSI_6, stock_Date,\
    stock_Name

class CAdvanceFilter_GaiLiRatio(IAdvanceFilterBase):

    def __init__(self,threshold_min = None, threshold_max = None):
        '''
        params threshold_min, threshold_max
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'乖离率'
        self.FilterDescribe = u'历史乖离率'
        #to do
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass
    
        try:
            float(df.iloc[-3][stock_RSI_6])
        except:
            return False
    
        return True
    

    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_RSI_6),copy = True)        
        count = 0
        rows = df1.shape[0]
        for i in range(1, rows):
            RSI6 = float(df1.iloc[-i][stock_RSI_6])
            if self.threshold[0] != None and RSI6 < self.threshold[0]:
                count = count + 1
                continue
            if self.threshold[1] != None and RSI6 > self.threshold[1]:
                count = count +1
                continue
            break
        
        if count >=1:
            ret = {}
            ret["0日期"] = df.iloc[-1][stock_Date]
            ret["1股票简称"] = df.iloc[-1][stock_Name]
            ret[self.filterName] = "YES"
            ret["RSI钝化天数"] = count
            return (True,ret)
        
        return (False,)
    
if __name__ == '__main__':
    pass