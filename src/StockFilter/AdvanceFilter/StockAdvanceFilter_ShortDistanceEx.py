'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date,\
    stock_Name, stock_DISTANCE_MA_SHORT, stock_ZhangDieFu, stock_Volumn_Ratio,\
    stock_DistanceMA60, stock_DistanceMA5, stock_ClosePrice, stock_CLOSE_TO_BOLLUP,\
    stock_MA5, stock_DistanceMA20

class CAdvanceFilter_ShortDistanceEx(IAdvanceFilterBase):

    def __init__(self,threshold):
        '''
        params threshold
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'短线均线纠结Ex'
        self.FilterDescribe = u'短线均线纠结Ex'
        self.threshold = threshold
        self.lastN = 20
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass
    
        try:
            float(df.iloc[-self.lastN][stock_DISTANCE_MA_SHORT])
            float(df.iloc[-self.lastN][stock_ZhangDieFu])
            float(df.iloc[-self.lastN][stock_Volumn_Ratio])
            float(df.iloc[-self.lastN][stock_DistanceMA60])
            float(df.iloc[-self.lastN][stock_CLOSE_TO_BOLLUP])
            float(df.iloc[-self.lastN][stock_MA5])
        except:
            return False
    
        return True
    

    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_DISTANCE_MA_SHORT,stock_ZhangDieFu,stock_Volumn_Ratio,stock_DistanceMA60,stock_DistanceMA5,stock_DistanceMA20,stock_CLOSE_TO_BOLLUP,stock_MA5),copy = True)
        zhangDieFu = float(df1.iloc[-1][stock_ZhangDieFu])
        distanceOfMA5 = float(df1.iloc[-1][stock_DistanceMA5])
        distanceOfMA20 = float(df1.iloc[-1][stock_DistanceMA20])
        if zhangDieFu <0 or distanceOfMA5 < 0 or distanceOfMA20 < 0:
            return (False,)
             
        count = self.lastN
        lastNShortDistance = []
        lastNMA5 = []
        for i in range(1, count+1):
            shortDistance = float(df1.iloc[-i][stock_DISTANCE_MA_SHORT])
            ma5 = float(df1.iloc[-i][stock_MA5])
            lastNShortDistance.append(shortDistance)
            lastNMA5.append(ma5)
        
        if lastNMA5[0] < lastNMA5[1] < lastNMA5[2]: #前三日的5日线方向是向下的情况
            return (False,)

        ret = {}
        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        ret['最后一天纠结值'] = float(df1.iloc[-1][stock_DISTANCE_MA_SHORT])
        ret['最后一天涨跌幅'] = float(df1.iloc[-1][stock_ZhangDieFu])
        ret['最后一天量比'] = float(df1.iloc[-1][stock_Volumn_Ratio])
        ret['到MA60的距离'] = float(df1.iloc[-1][stock_DistanceMA60])
        ret['到MA5的距离'] = float(df1.iloc[-1][stock_DistanceMA5])
        ret['到BOLL上轨距离'] = float(df1.iloc[-1][stock_CLOSE_TO_BOLLUP])
        key = '%s收盘价'%(df.iloc[-1][stock_Date])
        ret[key] = df.iloc[-1][stock_ClosePrice]
                
        if min(lastNShortDistance) == lastNShortDistance[0] and lastNShortDistance[0] < self.threshold:
            ret['纠结值当日新低'] = "YES"
            return (True,ret)
        elif min(lastNShortDistance) == lastNShortDistance[1] and lastNShortDistance[1] < self.threshold:
            ret['纠结值前日新低'] = "YES"
            return (True,ret)

        return (False,)
    
    
    def FilterEveryDayBy(self, df):
        res = []
        rows = df.shape[0]
        for i in range(1, rows):
            df1 = df[:-i]
            ret = self.FilterBy(df1)
            if ret[0]:
                res.append(ret[1])
        return res
            
    
if __name__ == '__main__':
    pass