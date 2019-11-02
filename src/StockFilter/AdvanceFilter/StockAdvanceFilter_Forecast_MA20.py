'''
Created on Jun 10, 2019

@author: mac
'''

from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date, stock_Name, stock_ZhangDieFu, stock_ClosePrice,stock_MA20

class CStockAdvanceFilter_Forecast_MA20(IAdvanceFilterBase):

    def __init__(self):
        '''
        params threshold_min
        '''
        IAdvanceFilterBase.__init__(self,None)
        self.filterName = u'预测20日均线'
        self.FilterDescribe = u'预测20日均线 是否突破向上'
        
    def _validateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False

            if df.shape[0] < 25:
                return False
        except:
            pass

        try:
            float(df.iloc[-3][stock_MA20])
            float(df.iloc[-3][stock_ClosePrice])
        except:
            return False
    
        return True
            
    def FilterBy(self, df):
        if not self._validateData(df):
            return (False,)
        
        closePrice_last =float(df.iloc[-1][stock_ClosePrice])
        closePrice_20 = float(df.iloc[-20][stock_ClosePrice])
        closeForecast = 0.05*20 + closePrice_20
        percentage = (closeForecast - closePrice_last) / closePrice_last
        if percentage > 0.1 or percentage < -0.1:
            return (False,)

        delta = (closePrice_last - closePrice_20)/20
        delta1 = (1.03*closePrice_last - closePrice_20)/20
        ret = {}
        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        ret["最后一天收盘价"] = closePrice_last
        ret["20天前收盘价"] = closePrice_20
        ret["预测收盘价"] = closeForecast
        ret["预测涨跌幅"] = percentage
        ret["不涨"] = delta
        ret["涨3"] = delta1
        return (True,ret)

    
if __name__ == '__main__':
    pass