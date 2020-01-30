'''
 Created on Sat Jan 04 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''

from StockMerge.MergeStockMonthly import MergeStockMonthlyMgr
from StockMerge.MergeStockYearly import MergeStockYearlyMgr
from StockDataItemIO.StockItemIO import CStockItemIO
from StockDataItem.StockItemDef import stock_ID, stock_Date
import os
import pandas as pd

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

    def ListAllFileInSourceFolder(self, srcFolder,fromDay = None, toDay = None, lastNDay = None):
        fileNames=os.listdir(srcFolder)
        res = []
        for fileName in fileNames:
            if fileName.find('.xlsx') == -1:
                continue
            date = fileName[: fileName.find('.')]
            if fromDay is not None and date < fromDay:
                continue
            if toDay is not None and date > toDay:
                continue
            fullPath = os.path.join(srcFolder,fileName)
            res.append(fullPath)

        if lastNDay is not None:
            res = res[-int(lastNDay):]
        res.sort(reverse=False)
        return res

    def MergeWithList(self,destFolder, fileList):
        res = {}
        columns = None
        for fileName in fileList:
            print('start to read file:%s'%(fileName[-15:])) 
            if fileName.find('xlsx') == -1:
                continue
            date = fileName[fileName.rfind('/')+1: fileName.find('.')]
            io = CStockItemIO()
            io.readFrom(fileName)
            stocks = io.stocks
            for stock in stocks:
                dictStock = dict(stock.formatToDict().copy())
                dictStock[stock_Date] = date
                stockId = dictStock[stock_ID]
                if stockId not in res:
                    res[stockId] = []
                res[stockId].append(dictStock)
                if columns is None:
                    columns = list(stock.getColunmInfo())
                    columns.remove(stock_ID)
                    columns.insert(0, stock_Date)
        index = 1
        count = len(res)
        for stockId in res:
            print(u'OutPut----> index: %4s of %4s,stockID:%s, size:%d'%(index, count, stockId, len(res[stockId])))
            df = pd.DataFrame(res[stockId],columns = columns)
            destFileName = '%s/%s.xlsx'%(destFolder, stockId)
            df.to_excel(destFileName,encoding="utf_8_sig", index=False)
            index = index + 1

    def NormalMerge(self, srcFolder, destFolder, sinceDay = None, toDay = None, lastNDay = None):
        if os.path.exists(destFolder) == False:
            os.makedirs(destFolder)
        fileList = self.ListAllFileInSourceFolder(srcFolder,sinceDay,toDay,lastNDay)
        for path in fileList:
            print(path)
        self.MergeWithList(destFolder,fileList)

    def QuickMereWithFile(self, lastFile, destFolder):
        pass

    def QuickMerge(self, srcFolder, destFolder, sinceDay = None, toDay = None, lastNDay = None):
        if os.path.exists(destFolder) == False:
            os.makedirs(destFolder)
        fileList = self.ListAllFileInSourceFolder(srcFolder,sinceDay,toDay,lastNDay)
        for path in fileList:
            print(path)
        lastFile =  fileList[-1]
        self.QuickMereWithFile(lastFile, destFolder)
    
    def Merge(self, srcFolder, destFolder, monthlyFolder, yearlyFolder, sinceDay = None, toDay = None, lastNDay = None):
        # self.CheckMonthlyFolder(srcFolder,destFolder,monthlyFolder)
        # self.CheckYearlyFolder(srcFolder, destFolder, yearlyFolder)
        pass








if __name__ == '__main__':
   pass
