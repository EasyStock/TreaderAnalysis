'''
Created on Jun 10, 2019

@author: mac
'''

from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date, stock_Name, stock_ZhangDieFu,\
    stock_Volumn_Ratio, stock_ClosePrice

class CAdvanceFilter_BigVolumn(IAdvanceFilterBase):

    def __init__(self,day, volumn_ratio):
        '''
        params threshold_min
        '''
        IAdvanceFilterBase.__init__(self,None)
        self.filterName = u'%s天爆大量,量比%s'%(day,volumn_ratio)
        self.FilterDescribe = u'前N天爆大量，判断低位还是高位'
        self.day = day
        self.volumn_ratio = volumn_ratio
        
    def _validateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < self.day+10:
                return False
        except:
            pass

        try:
            float(df.iloc[-3][stock_Volumn_Ratio])
            float(df.iloc[-3][stock_ClosePrice])
        except:
            return False
    
        return True
    
    def _getClosePriceRatio(self,df):
        last2 = float(df.iloc[-2][stock_ClosePrice])
        big = 0
        small = 0
        for i in range(3, self.day + 3):
            close = float(df.iloc[-i][stock_ClosePrice])
            if close > last2:
                big = big + 1
            if close < last2:
                small = small +1
        
        return(1.0*big/self.day, 1.0*small/self.day)
            
            
    def FilterBy(self, df):
        if not self._validateData(df):
            return (False,)
        
        if float(df.iloc[-1][stock_Volumn_Ratio]) < self.volumn_ratio:
            return (False,)
        
        big, small = self._getClosePriceRatio(df)
    
        ret = {}
        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        ret["最后一天涨幅"] = float(df.iloc[-1][stock_ZhangDieFu])
        ret['量比'] = float(df.iloc[-1][stock_Volumn_Ratio])
        ret['天数'] = self.day
        ret["大于比例"] = big
        ret["小于比例"] = small
        return (True,ret)

    
if __name__ == '__main__':
    pass