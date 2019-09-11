'''
Created on Jun 10, 2019

@author: mac
'''

from StockDataItem.StockItemDef import stock_ClosePrice, stock_Date, stock_Name,\
    stock_LowerPrice, stock_ZhangDieFu, stock_HighPrice,\
    stock_ClosePrice_Yesterday, stock_Volumn_Ratio, stock_OpenPrice
    
from StockFilter.AdvanceFilter.AdvanceFilterCommon import AdvanceFilterCommon


class CAdvanceFilter_YunXian(AdvanceFilterCommon):

    def __init__(self):
        '''
        params threshold
        '''
        AdvanceFilterCommon.__init__(self)
        self.filterName = u'孕育线'
        self.FilterDescribe = u'孕育线'
        
    def ValidateData(self, df):
        if not self.IsDayGreaterThan(df, 250):
            return False
        
        if self.isST(df):
            return False
        
        try:
            float(df.iloc[-3][stock_ClosePrice])
        except:
            return False
    
        return True
    
        
    def FilterBy(self, df):
        '''
        第二日的最高最低价都在前一日的实体里面
        '''
        if not self.ValidateData(df):
            return (False,)
        
        high1 = float(df.iloc[-1][stock_HighPrice])
        low1 = float(df.iloc[-1][stock_LowerPrice])
        
        close2 = float(df.iloc[-2][stock_ClosePrice])
        open2 = float(df.iloc[-2][stock_OpenPrice])
        max2 = max(close2, open2)
        min2 = min(close2, open2)
        
        if high1 > max2 or low1 < min2:
            return (False,)
        
        close_yesterday = float(df.iloc[-1][stock_ClosePrice_Yesterday])
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
        res = self.shiZhi(df)
        ret.update(res)
        return (True,ret)
        
    
if __name__ == '__main__':
    pass