'''
Created on Jun 10, 2019

@author: mac
'''
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days,stock_Date, stock_Name,\
    stock_ClosePrice, stock_MA5, stock_MA10, stock_MA20, stock_MA30, stock_MA60
import pandas as pd


class CAdvanceFilter_MA_Forecast(IAdvanceFilterBase):

    def __init__(self):
        '''
        params None
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'均线预测'
        self.FilterDescribe = u'均线预测'

        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            print(df.iloc[-1][stock_Days])
    
        try:
            float(df.iloc[-5][stock_ClosePrice])
            float(df.iloc[-5][stock_MA5])
            float(df.iloc[-10][stock_MA10])
            float(df.iloc[-20][stock_MA20])
            float(df.iloc[-30][stock_MA30])
            
#             float(df.iloc[-60][stock_MA60])
        except:
            return False
    
        return True
    
    def calcMA(self,df, stock_MA_N, N = 5):
        lastPriceN = float(df[stock_ClosePrice][-N])
        delta = 1.0*(float(df[stock_MA_N][-1]) - float(df[stock_MA_N][-N]))/(N-1)
        nextPrice = N*delta + lastPriceN
#       print(lastPriceN, float(df[stock_MA_N][-1]), float(df[stock_MA_N][-N]), N*delta, nextPrice)
        return nextPrice 

            
            
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
    

if __name__ == '__main__':
    fileN = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/合并/000001.SZ.xlsx'
    df = pd.read_excel(fileN, encoding='utf_8_sig', index_col = 0) 
    forecast = CAdvanceFilter_MA_Forecast()
    print(forecast.calcMA(df,stock_MA10, 5))
