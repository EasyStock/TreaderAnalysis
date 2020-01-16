'''
 Created on Sat Jan 04 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''

from StockMerge.MergeStockMonthly import MergeStockMonthlyMgr
from StockMerge.MergeStockYearly import MergeStockYearlyMgr
import os

class CMergeStockLasterMgr(object):
    def __init__(self):
        pass
    
    def CheckMonthlyFolder(self, srcFolder, destFolder, monthlyFolder):
        if os.path.exists(monthlyFolder) == False:
            mgr = MergeStockMonthlyMgr()
            mgr.MergeStockMonthlySince(srcFolder,destFolder)
            return False

        return True


    def CheckYearlyFolder(self,srcFolder, destFolder, yearlyFolder):
        if os.path.exists(yearlyFolder) == False:
            mgr = MergeStockYearlyMgr()
            mgr.MergeStockYearlySinceYear(srcFolder,destFolder)
            return False

        return True


    def ListAllFileFromSrcFolder(srcFolder, fromDay = None, toDay = None):
        pass

    def MergeFromStart(self, srcFolder, destFolder, monthlyFolder, yearlyFolder, sinceDay = None, toDay = None):
        self.CheckMonthlyFolder(srcFolder,destFolder,monthlyFolder)
        self.CheckYearlyFolder(srcFolder, destFolder, yearlyFolder)

        #1.获取最后一个交易日的日期
        if os.path.exists(destFolder) == False:
            pass
        else:
            pass
            #直接merge






if __name__ == '__main__':
   pass
