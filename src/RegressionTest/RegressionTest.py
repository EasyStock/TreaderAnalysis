'''
Created on Jul 25, 2019

@author: mac
'''
import pandas as pd
from StockDataItem.StockItemDef import stock_ID, stock_ClosePrice

def Test():
    srcFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/多日过滤/中线均线纠结_2019-07-25.xlsx'
    destFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/每日数据/2019-07-31.xlsx'
    destFile1 = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/2019-07-31_aa.xlsx'
    src_df = pd.read_excel(srcFile, index_col = None, encoding='utf_8_sig')
    dest_df = pd.read_excel(destFile, index_col = None, encoding='utf_8_sig')
    df1 = pd.DataFrame(dest_df, columns=(stock_ID, stock_ClosePrice),copy = True)
     
    print(src_df.shape)
    print(df1.shape)
    res = pd.merge(src_df, df1)
    print(res.shape)
    print(res)
    res.to_excel(destFile1,encoding="utf_8_sig", index=False)
    
    
if __name__ == '__main__':
    Test()