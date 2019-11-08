'''
Created on Jun 10, 2019

@author: mac
'''

from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date, stock_Name, stock_ZhangDieFu, stock_ClosePrice,stock_MA20,stock_MA5,stock_MA10,stock_MA30, stock_DISTANCE_MA_SHORT, stock_DISTANCE_MA_MID
import numpy as np

class CStockAdvanceFilter_Forecast_MA20(IAdvanceFilterBase):

    def __init__(self,percentage = 1):
        '''
        params threshold_min
        '''
        IAdvanceFilterBase.__init__(self,None)
        self.filterName = u'预测20日均线'
        self.FilterDescribe = u'预测20日均线 是否突破向上'
        self.percentage = percentage
        #To Do, 计算MA5， MA10， MA20, MA30 的粘合度
        #计算震荡区间的delta
        
    def _validateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False

            if df.shape[0] < 25:
                return False
        except:
            pass

        try:
            float(df.iloc[-3][stock_MA20])
            float(df.iloc[-3][stock_ClosePrice])
        except:
            return False
    
        return True
            
    def FilterBy(self, df):
        if not self._validateData(df):
            return (False,)
        
        closePrice_last =float(df.iloc[-1][stock_ClosePrice])
        closePrice_last5 = float(df.iloc[-5][stock_ClosePrice])
        closePrice_last10 = float(df.iloc[-10][stock_ClosePrice])
        closePrice_last20 = float(df.iloc[-20][stock_ClosePrice])
        closePrice_last30 = float(df.iloc[-30][stock_ClosePrice])

        closePrice_MA5 = float(df.iloc[-1][stock_MA5])
        closePrice_MA10 = float(df.iloc[-1][stock_MA10])
        closePrice_MA20 = float(df.iloc[-1][stock_MA20])
        closePrice_MA30 = float(df.iloc[-1][stock_MA30])

        newClosePrice = self.percentage * closePrice_last

        newMA5 = (newClosePrice - closePrice_last5)/5 + closePrice_MA5
        newMA10 = (newClosePrice - closePrice_last10)/10 + closePrice_MA10

        if newClosePrice < newMA5:
            return (False,)

        if newClosePrice < newMA10:
            return (False,)
    
        newDelta = (newClosePrice - closePrice_last20)/20.0
        if newDelta <0.05:
            return (False,)
        
        newMA20 = (newClosePrice - closePrice_last20)/20 + closePrice_MA20
        newMA30 = (newClosePrice - closePrice_last30)/30 + closePrice_MA30

        v = [newMA5, newMA10, newMA20, newMA30]
        k = [(v[0] - x)/v[0]*100 for x in v]
        distance = np.var(k)
        ret = {}
        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        ret["最后一天收盘价"] = closePrice_last
        ret["5天前收盘价"] = closePrice_last5
        ret["10天前收盘价"] = closePrice_last10
        ret["20天前收盘价"] = closePrice_last20

        ret["5MA_last"] = closePrice_MA5
        ret["10MA_last"] = closePrice_MA10
        ret["20MA_last"] = closePrice_MA20

        ret["预测Price"] = newClosePrice
        ret["预测Value"] = newDelta
        ret["预测纠结值"] = distance
        ret["当日短纠结值"] = df.iloc[-1][stock_DISTANCE_MA_SHORT] 
        ret["当日中纠结值"] = df.iloc[-1][stock_DISTANCE_MA_MID] 
        return (True,ret)

    
if __name__ == '__main__':
    pass