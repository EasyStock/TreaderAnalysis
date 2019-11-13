'''
Created on Jun 10, 2019

@author: mac
'''

from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date, stock_Name, stock_ZhangDieFu, stock_ClosePrice,stock_MA20,stock_MA5,stock_MA10,stock_MA30, stock_DISTANCE_MA_SHORT, stock_DISTANCE_MA_MID
import numpy as np
import pandas as pd
from StockFilter.AdvanceFilter.StockAdvanceFilter_LineTurning import CStockAdvanceFilter_LineTurning


class CStockAdvanceFilter_Forecast_MA(IAdvanceFilterBase):

    def __init__(self,percentageMin = 0.98, percentageMax = 1.02,threshold = 0.05):
        '''
        params threshold_min
        '''
        IAdvanceFilterBase.__init__(self,None)
        self.filterName = u'预测均线%s ~ %s'%(percentageMin, percentageMax)
        self.FilterDescribe = u'预测均线 是否突破向上'
        self.percentageMin = percentageMin
        self.percentageMax = percentageMax
        self.threshold = threshold
        
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
    
    def FilterMA(self, df, MA):
        df1 = pd.DataFrame(df, columns=(stock_Date, MA),copy = True)
        df1 = df1.set_index(stock_Date)
        try:
            float(df1.iloc[-10][MA])
        except:
            return None

        lineTurning = CStockAdvanceFilter_LineTurning()
        ret = {}
        try:
            res = lineTurning.GetAllTurnPoints(df1)
            if len(res) == 0:
                return None
            last = res[-1]
            key_date = "D_%s最后转折点日期" %(MA)
            key_direction = "F_%s最后转折点方向" %(MA)
            key_value = "E_%s最后转折点值" %(MA)

            ret[key_date] = last['Date']
            ret[key_direction] = last['Direction']
            ret[key_value] = last['Value']
        except:
            return None
        return ret

    def _calcNewDataFrame(self, df ,percentage):
        if not self._validateData(df):
            return (False,)

        closePrice_last =float(df.iloc[-1][stock_ClosePrice])
        closePrice_last5 = float(df.iloc[-5][stock_ClosePrice])
        closePrice_last10 = float(df.iloc[-10][stock_ClosePrice])
        closePrice_last20 = float(df.iloc[-20][stock_ClosePrice])
        closePrice_last30 = float(df.iloc[-30][stock_ClosePrice])

        last_MA5 = float(df.iloc[-1][stock_MA5])
        last_MA10 = float(df.iloc[-1][stock_MA10])
        last_MA20 = float(df.iloc[-1][stock_MA20])
        last_MA30 = float(df.iloc[-1][stock_MA30])

        newClosePrice = percentage * closePrice_last
        newMA5 = (newClosePrice - closePrice_last5)/5 + last_MA5
        newMA10 = (newClosePrice - closePrice_last10)/10 + last_MA10
        newMA20 = (newClosePrice - closePrice_last20)/20 + last_MA20
        newMA30 = (newClosePrice - closePrice_last30)/30 + last_MA30

        df1 = pd.DataFrame(df, columns=(stock_Date, stock_MA5, stock_MA10, stock_MA20,stock_MA30),copy = True)
        df1 = df1.append({stock_Date:"预测日前", stock_MA5:newMA5, stock_MA10:newMA10, stock_MA20:newMA20, stock_MA30:newMA30}, ignore_index=True)
        return df1
    
    def FilterByPercentage(self, df , percentage):
        if not self._validateData(df):
            return (False,)
        ret = {}
        ret["A_日期"] = df.iloc[-1][stock_Date]
        ret["B_股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        ret['C_收盘价'] = df.iloc[-1][stock_ClosePrice]
        ret['C_预测涨跌幅'] = percentage

        res = self.FilterMA(df, stock_MA20)
        if res != None:
            key_value = "E_%s最后转折点值" %(stock_MA20)
            if(res[key_value] < self.threshold):#and (res[key_value_last] < self.threshold):
                return (False,)
            ret.update(res)
        else:
            return (False,)

        res = self.FilterMA(df, stock_MA5)
        if res != None:
            key_value = "E_%s最后转折点值" %(stock_MA5)
            if(res[key_value] < 0):
                return (False,)
            ret.update(res)
        
        res = self.FilterMA(df, stock_MA10)
        if res != None:
            key_value = "E_%s最后转折点值" %(stock_MA10)
            if(res[key_value] < 0):
                return (False,)
            ret.update(res)

        res = self.FilterMA(df, stock_MA30)
        if res != None:
            key_value = "E_%s最后转折点值" %(stock_MA30)
            if(res[key_value] < 0):
                return (False,)
            ret.update(res)
        return (True,ret)



    def FilterBy(self, df):
        if not self._validateData(df):
            return (False,)

        newDataFrame = self._calcNewDataFrame(df, self.percentageMin)
        res = self.FilterByPercentage(newDataFrame, self.percentageMin)
        if(res[0] == True):
            return res

        res = self.FilterByPercentage(newDataFrame, self.percentageMax)
        if(res[0] == True):
            return res 
        
        return (False,)
    
if __name__ == '__main__':
    pass