'''
Created on Jun 10, 2019

@author: mac
'''

import pandas as pd
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date,\
    stock_BOLL_Band_width, stock_BOLLMid, stock_Name

class CAdvanceFilter_BOOL_WIDTH(IAdvanceFilterBase):

    def __init__(self):
        '''
        params threshold_min
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'BOLL带宽'
        self.FilterDescribe = u'BOLL带宽连续三天带宽变大'
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass

        try:
            float(df.iloc[-3][stock_BOLL_Band_width])
            float(df.iloc[-3][stock_BOLLMid])
        except:
            return False
    
        return True
    

    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_BOLL_Band_width,stock_BOLLMid),copy = True)
        
        count = 1
        rows = df1.shape[0]
        last = float(df1.iloc[-1][stock_BOLL_Band_width])
        for i in range(2, rows):
            band_width = float(df1.iloc[-i][stock_BOLL_Band_width])
            if band_width < last:
                last = band_width
                count = count + 1
            else:
                break
        l1 = float(df1.iloc[-1][stock_BOLLMid])
        l2 = float(df1.iloc[-2][stock_BOLLMid])
        l3 = float(df1.iloc[-3][stock_BOLLMid])
        flag = 'UnKnown'
        if l1 >= l2 >= l3:
            flag = 'UP'
        elif l1 <= l2 <= l3:
            flag = 'DOWN'
        else:
            flag = 'UnKnown'
        if count >=2 and flag == 'UP':
            ret = {}
            ret["0日期"] = df.iloc[-1][stock_Date]
            ret["1股票简称"] = df.iloc[-1][stock_Name]
            ret[self.filterName] = "YES"
            ret["BOLL方向"] = flag
            ret["BOLL带宽变大天数"] = count
            return (True,ret)
        
        return (False,)
    
if __name__ == '__main__':
    pass