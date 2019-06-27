'''
Created on Jun 5, 2019

@author: mac
'''
import os
from StockDataItemIO.StockItemIO import CStockItemIO
from StockDataItem.StockItemDef import stock_ID, stock_Date
import pandas as pd

class MergeStockMgr(object):
    def __init__(self):
        pass
    
    
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