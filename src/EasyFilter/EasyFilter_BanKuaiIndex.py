'''
Created on Aug 29, 2019

@author: mac
'''

import pandas as pd
import numpy as np

from EasyFilter.IEasyFilterBase import IEasyFilterBase
from PathManager.StockPathManager import GetDailyDataFolder_Index_BanKuai
from IndexDataItem.IndexItemDef import index_MA5, index_ClosePrice, index_MA20


class EasyFilter_BanKuaiIndex(IEasyFilterBase):
    def __init__(self):
        IEasyFilterBase.__init__(self)
        self.dailyFolder = GetDailyDataFolder_Index_BanKuai()
        self.filterName = '板块指数简单过滤'
        self.FilterDescribe = '''
        1.板块指数在5日线之上，即大于MA5
        2.板块指数在中轨之上，即大于MA20
        
        '''
        
    def FilterOneFile(self,dailyFile):
        dailyData = pd.read_excel(dailyFile, index_col = None, encoding='utf_8_sig')
        count = 0
        for _, row in dailyData.iterrows():
            try:
                ma5 = float(row[index_MA5])
                ma20 = float(row[index_MA20])
                close = float(row[index_ClosePrice])
                if close > ma5 and close > ma20:
                    print(row)
                    count = count +1
                    
            except:
                continue
        print(count)

if __name__ == '__main__':
    easy = EasyFilter_BanKuaiIndex()
    dailyFile = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/板块指数/每日数据/2019-08-29.xlsx'
    easy.FilterOneFile(dailyFile)
        