'''
Created on Jun 10, 2019

@author: mac
'''

from StockDataItem.StockItemDef import stock_ClosePrice, stock_Date, stock_Name,\
    stock_LowerPrice, stock_ZhangDieFu, stock_HighPrice,\
    stock_ClosePrice_Yesterday, stock_Volumn_Ratio, stock_OpenPrice
from StockFilter.AdvanceFilter.AdvanceFilterCommon import AdvanceFilterCommon


class CAdvanceFilter_AttackDay(AdvanceFilterCommon):

    def __init__(self):
        '''
        params threshold
        '''
        AdvanceFilterCommon.__init__(self)
        self.filterName = u'攻击日形态'
        self.FilterDescribe = u'攻击日形态，长上影线，次日大阳线吞噬上影线'
        
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
        攻击日形态，长上影线，次日大阳线吞噬上影线
        '''
        if not self.ValidateData(df):
            return (False,)
        
        close2 = float(df.iloc[-2][stock_ClosePrice])
        high2 = float(df.iloc[-2][stock_HighPrice])
        
        #长上影线
        if (high2 - close2) < 0.03:
            return (False,)
        
        close1 = float(df.iloc[-1][stock_ClosePrice])
        high1 = float(df.iloc[-1][stock_HighPrice])
        open1 = float(df.iloc[-1][stock_OpenPrice])
        low1 = float(df.iloc[-1][stock_LowerPrice])
        
        #大阳线
        if open1 > close1:
            return (False,)
        
        #超过昨天最高
        if close1 < high2:
            return (False,)
        
        close_yesterday = float(df.iloc[-1][stock_ClosePrice_Yesterday])
        
        close2 = float(df.iloc[-2][stock_ClosePrice])
        open2 = float(df.iloc[-2][stock_OpenPrice])
        if close1 < open2:
            return (False,)
        
        ret = {}
        date = df.iloc[-1][stock_Date]
        ret["0日期"] = date
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        ret["%s_涨跌幅%%"%(date)] = df.iloc[-1][stock_ZhangDieFu]
        ret["%s_振幅%%"%(date)] = (high1 - low1)/close_yesterday*100
        ret["%s_量比"%(date)] = float(df.iloc[-1][stock_Volumn_Ratio])
        res = self.KBody(df[:-1])
        ret.update(res)
        res = self.HasZhangTing(df,percentage=9.9,N=30)
        ret.update(res)
        res = self.isOpenLowerThanYesterdayClose(df)
        ret.update(res)
        return (True,ret)

if __name__ == '__main__':
    pass