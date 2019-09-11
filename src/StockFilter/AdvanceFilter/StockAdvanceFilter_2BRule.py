'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockDataItem.StockItemDef import stock_Days, stock_ClosePrice, stock_Date, stock_Name,\
    stock_LowerPrice, stock_ZhangDieFu, stock_HighPrice,\
    stock_ClosePrice_Yesterday, stock_Volumn_Ratio, stock_RSI_6, stock_OpenPrice
from StockFilter.AdvanceFilter.AdvanceFilterCommon import AdvanceFilterCommon


class CAdvanceFilter_2BRule(AdvanceFilterCommon):

    def __init__(self,days):
        '''
        params threshold
        '''
        AdvanceFilterCommon.__init__(self)
        self.filterName = u'突破2B失败_反弹'
        self.FilterDescribe = u'突破2B失败，触底反弹'
        self.days = days
        
    def ValidateData(self, df):
        if not self.IsDayGreaterThan(df, 250):
            return False

        try:
            float(df.iloc[-3][stock_ClosePrice])
        except:
            return False
    
        return True
    
        
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
            res = self.isOpenLowerThanYesterdayClose(df)
            ret.update(res)
            res = self.shiZhi(df)
            ret.update(res)
            return (True,ret)
    
        return (False, )
        
    
if __name__ == '__main__':
    pass