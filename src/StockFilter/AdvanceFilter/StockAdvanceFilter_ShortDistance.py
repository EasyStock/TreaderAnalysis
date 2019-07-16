'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date,\
    stock_Name, stock_DISTANCE_MA_SHORT, stock_ZhangDieFu, stock_Volumn_Ratio,\
    stock_DistanceMA60, stock_DistanceMA5, stock_ClosePrice, stock_CLOSE_TO_BOLLUP,\
    stock_DistanceMA20

class CAdvanceFilter_ShortDistance(IAdvanceFilterBase):

    def __init__(self,threshold):
        '''
        params threshold
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'短线均线纠结'
        self.FilterDescribe = u'短线均线纠结'
        self.threshold = threshold
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass
    
        try:
            float(df.iloc[-3][stock_DISTANCE_MA_SHORT])
            float(df.iloc[-3][stock_ZhangDieFu])
            float(df.iloc[-3][stock_Volumn_Ratio])
            float(df.iloc[-3][stock_DistanceMA60])
            float(df.iloc[-3][stock_CLOSE_TO_BOLLUP])
        except:
            return False
    
        return True
    

    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_DISTANCE_MA_SHORT,stock_ZhangDieFu,stock_Volumn_Ratio,stock_DistanceMA60,stock_DistanceMA5,stock_DistanceMA20,stock_CLOSE_TO_BOLLUP),copy = True)        
        zhangDieFu = float(df1.iloc[-1][stock_ZhangDieFu])
        distanceOfMA5 = float(df1.iloc[-1][stock_DistanceMA5])
        distanceOfMA20 = float(df1.iloc[-1][stock_DistanceMA20])
        if zhangDieFu <0 or distanceOfMA5 < 0 or distanceOfMA20 < 0:
            return (False,) 
        
        count = 0
        rows = df1.shape[0]
        for i in range(2, rows):
            shortDistance = float(df1.iloc[-i][stock_DISTANCE_MA_SHORT])
            if  shortDistance < self.threshold:
                count = count + 1
                continue
            break
        
        zhangDieFu = float(df1.iloc[-1][stock_ZhangDieFu])
        if count >=1 and zhangDieFu >0:
            ret = {}
            ret["0日期"] = df.iloc[-1][stock_Date]
            ret["1股票简称"] = df.iloc[-1][stock_Name]
            ret[self.filterName] = "YES"
            ret["短线均线纠结天数"] = count
            ret['最后一天纠结值'] = float(df1.iloc[-1][stock_DISTANCE_MA_SHORT])
            ret['最后一天涨跌幅'] = zhangDieFu
            ret['最后一天量比'] = float(df1.iloc[-1][stock_Volumn_Ratio])
            ret['到MA60的距离'] = float(df1.iloc[-1][stock_DistanceMA60])
            ret['到MA5的距离'] = float(df1.iloc[-1][stock_DistanceMA5])
            ret['到BOLL上轨距离'] = float(df1.iloc[-1][stock_CLOSE_TO_BOLLUP])
            key = '%s收盘价'%(df.iloc[-1][stock_Date])
            ret[key] = df.iloc[-1][stock_ClosePrice]
            return (True,ret)
        
        return (False,)
    
if __name__ == '__main__':
    pass