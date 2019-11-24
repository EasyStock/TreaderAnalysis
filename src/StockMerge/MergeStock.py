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

class MergeStockMgr(object):
    def __init__(self):
        pass
    
    def ReadFromStockFiles(self, fileList):
        columns = None
        res = {}
        for xlsxFile in fileList:
            date = xlsxFile[xlsxFile.rfind('/')+1: xlsxFile.find('.')]
            io = CStockItemIO()
            if xlsxFile.find('xlsx') == -1:
                continue
            print('read file: %s'%(xlsxFile))
            io.readFrom(xlsxFile)
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
        print('Read finished!')
        return (res, columns)

    def MergeStocksWithFiles(self, fileList,destFolder):
        (res, columns) = self.ReadFromStockFiles(fileList)
        index = 1
        for stockId in res:
            print(u'index:%04d, stockID:%s, size:%d'%(index, stockId, len(res[stockId])))
            index = index + 1
            df = pd.DataFrame(res[stockId],columns = columns)
            destFileName = '%s/%s.xlsx'%(destFolder, stockId)
            df.to_excel(destFileName,encoding="utf_8_sig", index=False)

    def ListAllFilesInFolderByMonth(self, srcFolder):
        filenames=os.listdir(srcFolder)
        monthFiles = {}
        for xlsxFile in filenames:
            srcFileName = os.path.join(srcFolder,xlsxFile)
            date = xlsxFile[: xlsxFile.find('.')]
            if srcFileName.find('xlsx') == -1:
                continue
            (year,month,_) = date.split('-')
            key = u'%s_%s'%(year,month)
            if key not in monthFiles:
                monthFiles[key] = []
            monthFiles[key].append(srcFileName)
        return monthFiles

    def FastMerge_Month(self,srcFolder, destFolder):
        monthFiles = self.ListAllFilesInFolderByMonth(srcFolder)
        for month in monthFiles:
            print("start to merge %s month"%(month))
            allFiles = monthFiles[month]
            folder = u'%s/%s'%(destFolder,month)
            if os.path.exists(folder) == False:
                os.makedirs(folder)
            self.MergeStocksWithFiles(allFiles,folder)

    def FastMerge_Last_Month(self,srcFolder, destFolder):
        monthFiles = self.ListAllFilesInFolderByMonth(srcFolder)
        keys = list(monthFiles.keys())
        keys = sorted(keys,reverse=False)
        needMerge = [keys[-1],]
        for key in keys:
            folder = u'%s/%s'%(destFolder,key)
            if os.path.exists(folder) == False:
                if key not in needMerge:
                    needMerge.append(key)
                os.makedirs(folder)

        for index in needMerge:
            month = index
            print("start to merge %s month"%(month))
            allFiles = monthFiles[month]
            folder = u'%s/%s'%(destFolder,month)
            if os.path.exists(folder) == False:
                os.makedirs(folder)
            self.MergeStocksWithFiles(allFiles,folder)


    def FastMerge_Last_TwoMonth(self,srcFolder, destFolder):
        monthFiles = self.ListAllFilesInFolderByMonth(srcFolder)
        keys = list(monthFiles.keys())
        keys = sorted(keys,reverse=False)
        needMerge = [keys[-2],keys[-1]]
        for key in keys:
            folder = u'%s/%s'%(destFolder,key)
            if os.path.exists(folder) == False:
                if key not in needMerge:
                    needMerge.append(key)
                os.makedirs(folder)

        for index in needMerge:
            month = index
            print("start to merge %s month"%(month))
            allFiles = monthFiles[month]
            folder = u'%s/%s'%(destFolder,month)
            if os.path.exists(folder) == False:
                os.makedirs(folder)
            self.MergeStocksWithFiles(allFiles,folder)


    def MergeStockWithFolder(self,srcFolder, destFolder):
        filenames=os.listdir(srcFolder)
        res = {}
        columns = None
        for xlsxFile in filenames:
            srcFileName = os.path.join(srcFolder,xlsxFile)
            date = xlsxFile[: xlsxFile.find('.')]
            io = CStockItemIO()
            if srcFileName.find('xlsx') == -1:
                continue
            print('read file: %s'%(srcFileName))
            io.readFrom(srcFileName)
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
        print('Read finished!')
        index = 1
        for stockId in res:
            print(u'index:%04d, stockID:%s, size:%d'%(index, stockId, len(res[stockId])))
            index = index + 1
            df = pd.DataFrame(res[stockId],columns = columns)
            destFileName = '%s/%s.xlsx'%(destFolder, stockId)
            df.to_excel(destFileName,encoding="utf_8_sig", index=False)


if __name__ == '__main__':
    mgr = MergeStockMgr()
    folder = u'/Volumes/Data/StockAssistant/TreaderAnalysis/data/output/每日数据/'
    dest = u'/Volumes/Data/StockAssistant/TreaderAnalysis/data/output/aa/'
    mgr.MergeStockWithFolder(folder,dest)
    mgr.FastMerge(folder, dest)