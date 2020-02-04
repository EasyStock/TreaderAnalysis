
'''
 Created on Tue Feb 04 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''

from StockDataItemIO.StockItemIO import CStockItemIO
from StockDataItem.StockItemDef import stock_ID, stock_Date
import os
import pandas as pd

class CMergeStockLastNMgr(object):
    def __init__(self):
        pass

    def listAllFileInFolderWithLastN(self, srcFolder,lastN = 90):
        lastFiles = []
        fileNames=os.listdir(srcFolder)
        for fileName in fileNames:
            if fileName.find('xlsx') == -1:
                continue
            fullPath = os.path.join(srcFolder,fileName)
            lastFiles.append(fullPath)
        
        lastFiles.sort(reverse=False)
        size = len(lastFiles)
        if size > lastN:
            lastFiles = lastFiles[-int(lastN):]
        return lastFiles

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

    def MergeLastN(self, srcFolder, destFolder,lastNDay = None):
        if os.path.exists(destFolder) == False:
            os.makedirs(destFolder)
        fileList = self.listAllFileInFolderWithLastN(srcFolder,lastNDay)
        for path in fileList:
            print(path)
        self.MergeWithList(destFolder,fileList)

if __name__ == '__main__':
   pass

