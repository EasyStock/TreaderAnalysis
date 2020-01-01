'''
 Created on Wed Jan 01 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''

from StockMerge.MergeStockMonthly import MergeStockMonthlyMgr
from StockMerge.MergeStockYearly import MergeStockYearlyMgr



if __name__ == '__main__':
    # mgr = MergeStockMonthlyMgr()
    folder = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/每日数据/'
    dest = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/aa/'
    dest1 = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/bb/'
    # # mgr.ReadFromSrcFolder(folder)
    # mgr.MergeStockMonthlySince(folder, dest,'2019-11')
    mgr = MergeStockYearlyMgr()
    mgr.MergeStockYearlySinceYear(dest,dest1)

