'''
Created on May 6, 2019

@author: mac
'''

from Filters.SimpleFilter import SimpleFilter_TradingDay,SimpleFilter_ZhangDieFu
import pandas as pd


if __name__ == '__main__':
    fileName = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/最近合并/000488.SZ.xlsx'
    df = pd.read_excel(fileName, index_col = None, encoding='utf_8_sig')
    filter1 = SimpleFilter_TradingDay.CSimpleFilter_TradingDay([250,9999999])
    filter2 = SimpleFilter_ZhangDieFu.CSimpleFilter_ZhangDieFu([-10,-1])
    filter3 = SimpleFilter_TradingDay.CSimpleFilter_TradingDay([250,9999999])
    res = filter1.Filter(df,(filter2,filter3))
    print(filter1.callStack)
    print(res)