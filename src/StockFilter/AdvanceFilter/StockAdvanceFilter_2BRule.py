'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_ClosePrice, stock_Date, stock_Name,\
    stock_LowerPrice, stock_ZhangDieFu, stock_HighPrice,\
    stock_ClosePrice_Yesterday, stock_Volumn_Ratio, stock_RSI_6, stock_OpenPrice


class CAdvanceFilter_2BRule(IAdvanceFilterBase):

    def __init__(self,days):
        '''
        params threshold
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'突破2B失败_反弹'
        self.FilterDescribe = u'突破2B失败，触底反弹'
        self.days = days
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass
    
        try:
            float(df.iloc[-3][stock_ClosePrice])
        except:
            return False
    
        return True
    
    def RSI(self,df):
        index_Rsi6 = df[stock_RSI_6].idxmin()
        min_row_rsi6= df.loc[index_Rsi6]
        index_closePrice = df[stock_ClosePrice].idxmin()
        min_row_closePrice = df.loc[index_closePrice]
        
        ret = {}
        ret['RSI6最低日'] = min_row_rsi6[stock_Date]
        ret['RSI6最低值'] = min_row_rsi6[stock_RSI_6]
        ret['收盘价与RSI背离'] = (min_row_rsi6[stock_Date] != min_row_closePrice[stock_Date])
        ret['最低收盘价日期'] = min_row_closePrice[stock_Date]
        ret['最低收盘价'] = min_row_closePrice[stock_ClosePrice]
        return ret
        
    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_ClosePrice,stock_RSI_6),copy = True) 
        
        close1 = float(df.iloc[-1][stock_ClosePrice])
        close2 = float(df.iloc[-2][stock_ClosePrice])
        open2 = float(df.iloc[-2][stock_OpenPrice])
        if close1 < open2:
            return (False,)
        
        df_tmp = df1[-self.days: -2]
        min_closePrice = float(df_tmp[stock_ClosePrice].min())
        low1 = float(df.iloc[-1][stock_LowerPrice])
        
        if low1 < close2 < min_closePrice < close1:
            ret = {}
            date = df.iloc[-1][stock_Date]
            ret["0日期"] = date
            ret["1股票简称"] = df.iloc[-1][stock_Name]
            ret[self.filterName] = "YES"
            ret["%s_涨跌幅%%"%(date)] = df.iloc[-1][stock_ZhangDieFu]
            ret["%s_振幅%%"%(date)] = (float(df.iloc[-1][stock_HighPrice]) - float(df.iloc[-1][stock_LowerPrice]))/float(df.iloc[-1][stock_ClosePrice_Yesterday])*100
            ret["%s_量比"%(date)] = float(df.iloc[-1][stock_Volumn_Ratio])
            ret["%s_收盘价"%(date)] = float(df.iloc[-1][stock_ClosePrice])
            ret['昨日收盘价'] = float(df.iloc[-2][stock_ClosePrice])
            res = self.RSI(df[-self.days:])
            ret.update(res)
            return (True,ret)
    
        return (False, )
        
    
if __name__ == '__main__':
    pass