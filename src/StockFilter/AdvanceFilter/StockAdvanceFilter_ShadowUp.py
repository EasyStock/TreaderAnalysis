'''
Created on Jun 10, 2019

@author: mac
'''

from StockDataItem.StockItemDef import stock_ClosePrice, stock_Date, stock_Name,\
    stock_LowerPrice, stock_ZhangDieFu, stock_HighPrice,\
    stock_ClosePrice_Yesterday, stock_Volumn_Ratio, stock_OpenPrice
from StockFilter.AdvanceFilter.AdvanceFilterCommon import AdvanceFilterCommon


class CAdvanceFilter_ShadowUp(AdvanceFilterCommon):

    def __init__(self, threshold = 3):
        '''
        params threshold
        '''
        AdvanceFilterCommon.__init__(self)
        self.filterName = u'上影线'
        self.FilterDescribe = u'上影线占比大于百分之%s'%(threshold)
        self.threshold = threshold
        
    def ValidateData(self, df):
        if self.isST(df):
            return False
        
        if not self.IsDayGreaterThan(df, 250):
            return False
        
        try:
            float(df.iloc[-3][stock_ClosePrice])
        except:
            return False
    
        return True
    

    def FilterBy(self, df):
        '''
        上影线的长度/昨日收盘价 > N%
        '''
        if not self.ValidateData(df):
            return (False,)
        
        close1 = float(df.iloc[-1][stock_ClosePrice])
        high1 = float(df.iloc[-1][stock_HighPrice])
        close_yesterday = float(df.iloc[-1][stock_ClosePrice_Yesterday])
        low1 = float(df.iloc[-1][stock_LowerPrice])
        open1 = float(df.iloc[-1][stock_OpenPrice])
        
        max1 = max(close1, open1)
        #长上影线
        if (high1 - max1)/close_yesterday*100 < self.threshold:
            return (False,)
        
        ret = {}
        date = df.iloc[-1][stock_Date]
        ret["0日期"] = date
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        ret["%s_涨跌幅%%"%(date)] = df.iloc[-1][stock_ZhangDieFu]
        ret["%s_振幅%%"%(date)] = (high1 - low1)/close_yesterday*100
        ret["%s_量比"%(date)] = float(df.iloc[-1][stock_Volumn_Ratio])
        res = self.KBody(df)
        ret.update(res)
        res = self.HasZhangTing(df,percentage=9.9,N=30)
        ret.update(res)
        res = self.isOpenLowerThanYesterdayClose(df)
        ret.update(res)
        res = self.isPositive(df)
        ret.update(res)
        res = self.isGreaterThan5MA(df)
        ret.update(res)
        res = self.isGreaterThan10MA(df)
        ret.update(res)
        res = self.isGreaterThan20MA(df)
        ret.update(res)
        return (True,ret)

if __name__ == '__main__':
    pass