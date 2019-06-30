'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date,\
    stock_Name, stock_ZhangDieFu, stock_Volumn_Ratio,\
    stock_DistanceMA60, stock_DISTANCE_MA_MID

class CAdvanceFilter_MidDistance(IAdvanceFilterBase):

    def __init__(self,threshold):
        '''
        params threshold
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'中线均线纠结'
        self.FilterDescribe = u'中线均线纠结'
        self.threshold = threshold
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass
    
        try:
            float(df.iloc[-3][stock_DISTANCE_MA_MID])
            float(df.iloc[-3][stock_ZhangDieFu])
            float(df.iloc[-3][stock_Volumn_Ratio])
            float(df.iloc[-3][stock_DistanceMA60]) 
        except:
            return False
    
        return True
    

    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_DISTANCE_MA_MID,stock_ZhangDieFu,stock_Volumn_Ratio,stock_DistanceMA60),copy = True)        
        count = 0
        rows = df1.shape[0]
        for i in range(2, rows):
            shortDistance = float(df1.iloc[-i][stock_DISTANCE_MA_MID])
            if  shortDistance < self.threshold:
                count = count + 1
                continue
            break
        
        if count >=1:
            ret = {}
            ret["0日期"] = df.iloc[-1][stock_Date]
            ret["1股票简称"] = df.iloc[-1][stock_Name]
            ret[self.filterName] = "YES"
            ret["中线均线纠结天数"] = count
            ret['最后一天纠结值'] = float(df1.iloc[-1][stock_DISTANCE_MA_MID])
            ret['最后一天涨跌幅'] = float(df1.iloc[-1][stock_ZhangDieFu])
            ret['最后一天量比'] = float(df1.iloc[-1][stock_Volumn_Ratio])
            ret['到MA60的距离'] = float(df1.iloc[-1][stock_DistanceMA60])
            return (True,ret)
        
        return (False,)
    
if __name__ == '__main__':
    pass