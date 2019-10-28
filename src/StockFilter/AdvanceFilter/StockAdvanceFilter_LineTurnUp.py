'''
Created on Apr 15, 2019

@author: mac
'''

import pandas as pd

from StockDataItem.StockItemDef import (stock_Date, stock_Days, stock_MA5, stock_MA10, stock_MA20, stock_MA30, stock_MA60, stock_MA120,
                                        stock_Name)
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockFilter.AdvanceFilter.StockAdvanceFilter_LineTurning import CStockAdvanceFilter_LineTurning

class CAdvanceFilter_LineTurnUp(IAdvanceFilterBase):

    def __init__(self,threshold = 0.05):
        '''
        params threshold
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'20日均线向上并且值大于%s'%(threshold)
        self.FilterDescribe = u'20日均线向上并且值大于threshold'
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass
    
        try:
            float(df.iloc[-3][stock_MA20])
        except:
            return False
    
        return True
    
    def FilterMA(self, df, MA):
        df1 = pd.DataFrame(df, columns=(stock_Date, MA),copy = True)
        df1 = df1.set_index(stock_Date)
        try:
            float(df1.iloc[-10][MA])
        except:
            return None

        lineTurning = CStockAdvanceFilter_LineTurning()
        ret = {}
        try:
            res = lineTurning.GetAllTurnPoints(df1)
            if len(res) == 0:
                return None

            last = res[-1]
            key_date = "%s最后转折点日期" %(MA)
            key_direction = "%s最后转折点方向" %(MA)
            key_value = "%s最后转折点值" %(MA)
            ret[key_date] = last['Date']
            ret[key_direction] = last['Direction']
            ret[key_value] = last['Value']
        except:
            return None
        return ret

    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        ret = {}
        res = self.FilterMA(df, stock_MA5)
        if res != None:
            ret.update(res)
        
        res = self.FilterMA(df, stock_MA10)
        if res != None:
            ret.update(res)

        res = self.FilterMA(df, stock_MA20)
        if res != None:
            ret.update(res)

        res = self.FilterMA(df, stock_MA30)
        if res != None:
            ret.update(res)

        res = self.FilterMA(df, stock_MA60)
        if res != None:
            ret.update(res)

        res = self.FilterMA(df, stock_MA120)
        if res != None:
            ret.update(res)

        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"

        return (True,ret)

    
if __name__ == '__main__':
    pass