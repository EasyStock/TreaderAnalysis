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
    
    def HasZhangTing(self,df, percentage, N):
        ret = {}
        key = '最近%s天大于%s天数'%(N,percentage)
        aa = (df.ix[-N:][stock_ZhangDieFu] > percentage)
        t = df.loc[aa]
        ret[key] = t.shape[0]
        print(ret)
        return ret
    
    def isST(self,df):
        res = {}
        key = "是否ST"
        if df.iloc[-1][stock_Name].find("ST") != -1:
            res[key] = "是"
        else:
            res[key] = "否"
        return res

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
    
    def KBody(self,df):
        ret = {}
        date = df.iloc[-1][stock_Date]
        close1 = float(df.iloc[-1][stock_ClosePrice])
        open1 = float(df.iloc[-1][stock_OpenPrice])
        high1 = float(df.iloc[-1][stock_HighPrice])
        low1 = float(df.iloc[-1][stock_LowerPrice])
        close_yesterday = float(df.iloc[-1][stock_ClosePrice_Yesterday])
        ret["%s_收盘价"%(date)] = close1
        ret["%s_K线实体"%(date)] = (close1 -  open1)/close_yesterday*100
        ret["%s_K线上影线"%(date)] = (high1 - max(close1, open1)) / close_yesterday *100
        ret["%s_K线下影线"%(date)] = (min(close1,open1) - low1) / close_yesterday*100
        return ret
        
    def FilterBy(self, df):
        '''
        前一日创新低， 当日低开，向下突破，突破失败，反抽超过次低点
        '''
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_ClosePrice,stock_RSI_6),copy = True) 
        
        close1 = float(df.iloc[-1][stock_ClosePrice])
        high1 = float(df.iloc[-1][stock_HighPrice])
        close_yesterday = float(df.iloc[-1][stock_ClosePrice_Yesterday])
        
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
            ret["%s_振幅%%"%(date)] = (high1 - low1)/close_yesterday*100
            ret["%s_量比"%(date)] = float(df.iloc[-1][stock_Volumn_Ratio])
            res = self.RSI(df[-self.days:])
            ret.update(res)
            res = self.KBody(df)
            ret.update(res)
            res = self.HasZhangTing(df,percentage=9.9,N=30)
            ret.update(res)
            res = self.isST(df)
            ret.update(res)
            return (True,ret)
    
        return (False, )
        
    
if __name__ == '__main__':
    pass