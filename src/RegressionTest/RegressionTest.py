'''
Created on Jul 25, 2019

@author: mac
'''
import pandas as pd
from StockDataItem.StockItemDef import stock_ID, stock_ClosePrice

def Test():
    srcFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/多日过滤/突破2B失败_反弹_2019-08-16'
    destFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/每日数据/2019-08-19.xlsx'
    destFile1 = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/2019-08-19_aa.xlsx'
    src_df = pd.read_excel(srcFile, index_col = None, encoding='utf_8_sig')
    dest_df = pd.read_excel(destFile, index_col = None, encoding='utf_8_sig')
    df1 = pd.DataFrame(dest_df, columns=(stock_ID, stock_ClosePrice),copy = True)
     
    print(src_df.shape)
    print(df1.shape)
    res = pd.merge(src_df, df1)
    print(res.shape)
    print(res)
    res.to_excel(destFile1,encoding="utf_8_sig", index=False)
    

def RegressionTest(dailyFile, filterFile, outFile):
    daily_df = pd.read_excel(dailyFile, index_col = None, encoding='utf_8_sig')
    filter_df = pd.read_excel(filterFile, index_col = None, encoding='utf_8_sig')
    date = dailyFile[dailyFile.rfind('/')+1:dailyFile.rfind('.')]
    df1 = pd.DataFrame()
    df1[stock_ID] = daily_df[stock_ID]
    key = '%s_%s'%(date,stock_ClosePrice)
    df1[key] = daily_df[stock_ClosePrice]
    print(df1)
    res = pd.merge(filter_df, df1)
    res.to_excel(outFile,encoding="utf_8_sig", index=False)
    
if __name__ == '__main__':
    Test()