'''
Created on Jun 5, 2019

@author: mac
'''
import os
from StockDataItemIO.StockItemIO import CStockItemIO
from StockDataItem.StockItemDef import stock_ID, stock_Date
import pandas as pd
import datetime
import sys

class MergeStockMonthlyMgr(object):
    def __init__(self):
        pass

    def ReadFromSrcFolder(self, srcFolder):
        monthMap = {}
        fileNames=os.listdir(srcFolder)
        for fileName in fileNames:
            if fileName.find('xlsx') == -1:
                continue
            month = fileName[:fileName.rfind('-')]
            fullPath = os.path.join(srcFolder,fileName)
            if month not in monthMap:
                monthMap[month] = []
            monthMap[month].append(fullPath)
        return monthMap
    
    def MergeStockFileWithListToFolder(self,month,listOfFiles,destFolder):
            if os.path.exists(destFolder) == False:
                os.makedirs(destFolder)
            res = {}
            columns = None
            for fileName in listOfFiles:
                print('start to merge month:%s with file:%s'%(month, fileName[-15:])) 
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

            for stockId in res:
                print(u'OutPut----> stockID:%s, size:%d'%(stockId, len(res[stockId])))
                df = pd.DataFrame(res[stockId],columns = columns)
                destFileName = '%s/%s.xlsx'%(destFolder, stockId)
                df.to_excel(destFileName,encoding="utf_8_sig", index=False)

    def MergeStockMonthly(self,monthMap, srcFolder, destFolder):
        if os.path.exists(destFolder) == False:
            os.makedirs(destFolder)

        for month in monthMap:
            monthFolder = os.path.join(destFolder,month)
            self.MergeStockFileWithListToFolder(month,monthMap[month],monthFolder)

    
    def MergeStockMonthlySince(self,srcFolder, destFolder,sinceMonth = None,force = False):
        monthMap = self.ReadFromSrcFolder(srcFolder)

        if force is True:
            return self.MergeStockMonthly(monthMap, srcFolder, destFolder)
        
        if sinceMonth is None:
            return self.MergeStockMonthly(monthMap, srcFolder, destFolder)

        filter = {}
        for monthInMap in monthMap:
            if monthInMap >= sinceMonth:
                filter[monthInMap] = monthMap[monthInMap]
        
        return self.MergeStockMonthly(filter, srcFolder, destFolder)

    def MergeStockMonthlyThisMonth(self,srcFolder, destFolder,force = False):
        today = str(datetime.date.today())
        currentMonth = today[:today.rfind('-')]
        return self.MergeStockMonthlySince(srcFolder, destFolder, currentMonth,force)
