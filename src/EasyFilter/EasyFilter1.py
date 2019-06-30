'''
Created on Jun 27, 2019

@author: mac
'''

from EasyFilter.IEasyFilterBase import IEasyFilterBase
from StockDataItem.StockItemDef import stock_ClosePrice, stock_MA5, stock_MA10,\
    stock_MA20, stock_MA60, stock_ID, stock_Name
import pandas as pd
import numpy as np 

class EasyFilter(IEasyFilterBase):
    def __init__(self):
        IEasyFilterBase.__init__(self)
        self.filterName = 'EasyFilter1'
        self.FilterDescribe = '''
        选股条件:
            1. 股价 > MA60
            2. 股价 > MA5
            3. 股价 > MA20
            4. 三线(MA5, MA10, MA20)纠结, 纠结系数<0.01
            
            输出:
            1. 过滤器名称
            2. 股票名称
            3. BOLL线开合信息
            4. 红三兵信息
        '''
    def ScalcDistance(self,v):
        k = [(v[0] - x)/v[0]*100 for x in v]
        return np.var(k)
    
    def FilterDailyData(self,dailyFile):
        df = pd.read_excel(dailyFile, index_col = None, encoding='utf_8_sig')
        count = 0
        for i in range(0, len(df)):
            stockID = df.iloc[i][stock_ID]
            stockName = df.iloc[i][stock_Name]
            try:
                close = float(df.iloc[i][stock_ClosePrice])
                ma5 = float(df.iloc[i][stock_MA5])
                ma10 = float(df.iloc[i][stock_MA10])
                ma20 = float(df.iloc[i][stock_MA20])
                ma60 = float(df.iloc[i][stock_MA60])
                if close > ma5 and close >ma10 and close > ma20 and close > ma60:
                    distance = self.ScalcDistance((close, ma5, ma10, ma20))
                    if distance >0.5:
                        continue
                    print(count, stockID, stockName, distance)
                    count = count +1
                else:
                    continue
            except:
                continue
            
        
    def FilterOneFile(self,dailyFile, mergeFile):
         dailyData = pd.read_csv(dailyFile, index_col = None, encoding='utf_8_sig')
         mergeData = pd.read_csv(mergeFile, index_col = None, encoding='utf_8_sig')
         
    
        
    def Filter(self):
        pass

if __name__ == '__main__':
    e = EasyFilter()
    dailyFile = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/每日数据/2019-06-28.xlsx'
    e.FilterDailyData(dailyFile)
