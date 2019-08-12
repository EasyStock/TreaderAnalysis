'''
Created on Jun 10, 2019

@author: mac
'''

'''
股价与RSI 背离: 
1. 股价创新高，RSI 没有
2. 股价破新低， RSI没有
'''

from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_ClosePrice, stock_Date, stock_Name,\
    stock_LowerPrice, stock_ZhangDieFu, stock_HighPrice,\
    stock_ClosePrice_Yesterday, stock_Volumn_Ratio, stock_RSI_6


class CAdvanceFilter_RSI_BeiLi(IAdvanceFilterBase):

    def __init__(self,days):
        '''
        params threshold
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'RSI背离过滤'
        self.FilterDescribe = u'RSI背离过滤'
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
        
    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        if df.iloc[-1][stock_Name].find("ST") != -1:
            return (False,)
        
        index_closePrice = df[stock_ClosePrice].idxmin()
        min_row_closePrice = df.loc[index_closePrice]
        
        if min_row_closePrice[stock_Date] != df.iloc[-1][stock_Date]: #昨天不是最低价
            return (False,)
        
        index_Rsi6 = df[stock_RSI_6].idxmin()
        min_row_rsi6= df.loc[index_Rsi6]
        
        if min_row_rsi6[stock_Date] == min_row_closePrice[stock_Date]:
            return (False,)
            
        
        ret = {}
        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        ret['最后一天涨跌幅%'] = df.iloc[-1][stock_ZhangDieFu]
        ret['最后一天振幅%'] = (float(df.iloc[-1][stock_HighPrice]) - float(df.iloc[-1][stock_LowerPrice]))/float(df.iloc[-1][stock_ClosePrice_Yesterday])*100
        ret['最后一天量比'] = float(df.iloc[-1][stock_Volumn_Ratio])
        ret['最后一天收盘价'] = float(df.iloc[-1][stock_ClosePrice])
        
        ret['RSI6最低日'] = min_row_rsi6[stock_Date]
        ret['RSI6最低值'] = min_row_rsi6[stock_RSI_6]
        ret['最低收盘价日期'] = min_row_closePrice[stock_Date]
        ret['最低收盘价'] = min_row_closePrice[stock_ClosePrice]
        return (True,ret)
    
    
if __name__ == '__main__':
    pass