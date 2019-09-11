'''
Created on Jun 10, 2019

@author: mac
'''

from StockDataItem.StockItemDef import  stock_ClosePrice, stock_Date, stock_Name,\
    stock_LowerPrice, stock_ZhangDieFu, stock_HighPrice,\
    stock_ClosePrice_Yesterday, stock_Volumn_Ratio, stock_OpenPrice
    
from StockFilter.AdvanceFilter.AdvanceFilterCommon import AdvanceFilterCommon


class CAdvanceFilter_AYa(AdvanceFilterCommon):

    def __init__(self):
        '''
        params threshold
        '''
        AdvanceFilterCommon.__init__(self)
        self.filterName = u'哎呀形态'
        self.FilterDescribe = u'长下影线，次日跳空低开, 缺口回补'
        
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
        前一日创新低， 当日低开，向下突破，突破失败，反抽超过次低点
        '''
        if not self.ValidateData(df):
            return (False,)
        
        close2 = float(df.iloc[-2][stock_ClosePrice])
        low2 = float(df.iloc[-2][stock_LowerPrice])
        
        #前一日收长下影线
        if (close2 - low2) < 0.03:
            return (False,)
        
        
        close1 = float(df.iloc[-1][stock_ClosePrice])
        open1 = float(df.iloc[-1][stock_OpenPrice])
        high1 = float(df.iloc[-1][stock_HighPrice])
        low1 = float(df.iloc[-1][stock_LowerPrice])
        
        #当天跳空低开
        if open1 > low2:
            return (False,)
        
        #当天低开高走
        if close1 <= open1:
            return (False,)
        
        #回补当天缺口
        
        if close1 <= low2:
            return (False, )
        
        close_yesterday = float(df.iloc[-1][stock_ClosePrice_Yesterday])

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