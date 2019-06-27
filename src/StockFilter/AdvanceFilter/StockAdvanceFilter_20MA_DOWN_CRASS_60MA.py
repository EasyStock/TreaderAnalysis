'''
Created on Jun 10, 2019

@author: mac
'''
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_MA20, stock_MA60,\
    stock_Date, stock_Name
import pandas as pd

class CAdvanceFilter_20MA_Down_Cross_60MA(IAdvanceFilterBase):

    def __init__(self):
        '''
        params None
        '''
        IAdvanceFilterBase.__init__(self, None)
        self.filterName = u'MA20死叉60MA'
        self.FilterDescribe = u'20MA 向下死叉 60MA'
        
    def ValidateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            print(df.iloc[-1][stock_Days])
    
        try:
            float(df.iloc[-3][stock_MA20])
            float(df.iloc[-3][stock_MA60])
        except:
            return False
    
        return True
    
    def FilterBy(self, df):
        if not self.ValidateData(df):
            return (False,)
        
        df1 = pd.DataFrame(df, columns=(stock_Date,stock_MA20,stock_MA60),copy = True)
        LINE60_1 = float(df1.iloc[-1][stock_MA60])
        LINE60_2 = float(df1.iloc[-2][stock_MA60])
        
        LINE20_1 = float(df1.iloc[-1][stock_MA20])
        LINE20_2 = float(df1.iloc[-2][stock_MA20])
        if LINE60_1 > LINE20_1 and LINE20_2 > LINE60_2 and LINE20_1 < LINE20_2:
            ret = {}
            ret["0日期"] = df.iloc[-1][stock_Date]
            ret["1股票简称"] = df.iloc[-1][stock_Name]
            ret[self.filterName] = "YES"
            return (True,ret)

        return (False,)
    
if __name__ == '__main__':
    fileName = u'/Volumes/Data/StockAssistant/TreaderAnalysis/data/output/合并/002761.SZ.xlsx'
    df = pd.read_excel(fileName, index_col = None, encoding='utf_8_sig')
    ma = CAdvanceFilter_20MA_Down_Cross_60MA()
    print(ma.FilterBy(df))
    