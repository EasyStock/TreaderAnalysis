'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_RSI_6, stock_Date,\
    stock_Name, stock_MA5, stock_ClosePrice, stock_DistanceMA5,\
    stock_DistanceMA60

class CAdvanceFilter_RSI_DunHua(IAdvanceFilterBase):

    def __init__(self,threshold_min = None, threshold_max = None):
        '''
        params threshold_min, threshold_max
        '''
        IAdvanceFilterBase.__init__(self, None)
        if threshold_min != None and threshold_max == None:
            self.filterName = u'RSI<%s' %(threshold_min)
        elif threshold_min == None and threshold_max != None:
            self.filterName = u'RSI>%s'%(threshold_max)
        elif threshold_min != None and threshold_max != None:
            self.filterName = u'%s<RSI<%s'%(threshold_min,threshold_max)
        else:
            raise Exception('param error')
        
        self.FilterDescribe = u'RSI 连续钝化'
        self.threshold = (threshold_min,threshold_max)
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass
    
        try:
            float(df.iloc[-3][stock_RSI_6])
            float(df.iloc[-3][stock_MA5])
            float(df.iloc[-3][stock_ClosePrice])
        except:
            return False
    
        return True
    

    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_RSI_6, stock_ClosePrice, stock_MA5),copy = True)        
        count = 0
        rows = df1.shape[0]
        for i in range(1, rows):
            RSI6 = float(df1.iloc[-i][stock_RSI_6])
            ma5 = float(df1.iloc[-i][stock_MA5])
            close = float(df1.iloc[-i][stock_ClosePrice])
            if self.threshold[0] != None and self.threshold[1] == None:
                if RSI6 < self.threshold[0] and close <= ma5:
                    count = count + 1
                    continue
            elif self.threshold[0] == None and self.threshold[1] != None:
                if RSI6 > self.threshold[1] and close >=ma5:
                    count = count + 1
                    continue
            elif self.threshold[0] != None and self.threshold[1] != None:
                if self.threshold[0] < RSI6 < self.threshold[1]:
                    count = count + 1
                    continue
            else:
                raise Exception('param error')
    
            break
        if count >=3:
            ret = {}
            ret["0日期"] = df.iloc[-1][stock_Date]
            ret["1股票简称"] = df.iloc[-1][stock_Name]
            ret[self.filterName] = "YES"
            ret["RSI钝化天数"] = count
            ret["收盘价>=MA5"] = (df.iloc[-1][stock_ClosePrice] >= df.iloc[-1][stock_MA5])
            ret['到MA5的距离'] = df.iloc[-1][stock_DistanceMA5]
            ret['到MA60的距离'] = df.iloc[-1][stock_DistanceMA60]
            key = '%s收盘价'%(df.iloc[-1][stock_Date])
            ret[key] = df.iloc[-1][stock_ClosePrice]
            return (True,ret)
        return (False,)
    
if __name__ == '__main__':
    pass