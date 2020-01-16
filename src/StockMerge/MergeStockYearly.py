'''
 Created on Wed Jan 01 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''

import os
from StockDataItemIO.StockItemIO import CStockItemIO
import pandas as pd

class MergeStockYearlyMgr(object):
    def __init__(self):
        pass

    def GroupMergeFilesByYearAndStockID(self, folders):
        years = {}
        for folder in folders:
            (year,_) = folder[folder.rfind('/')+1:].split('-')
            if year not in years:
                years[year] = {}
            fileNames=os.listdir(folder)
            for fileName in fileNames:
                stockID = fileName[: fileName.find('.')]
                if stockID not in years[year]:
                    years[year][stockID] = []
                fullPath = u'%s/%s'%(folder,fileName)
                years[year][stockID].append(fullPath)

        return years

    def MergeFilesWithList(self, year, fileList,destFolder):
        outFolder = u'%s/%s'%(destFolder,year)
        if os.path.exists(outFolder) == False:
            os.makedirs(outFolder)
            
        unifyStockID = None
        columns = None
        dfs = []
        for fileName in fileList:
            if fileName.find('.xlsx') == -1:
                raise Exception('file is not a xlsx file')

            stockID = fileName[fileName.rfind('/')+1:fileName.rfind('.xlsx')]
            if unifyStockID is None:
                unifyStockID = stockID
            else:
                if unifyStockID != stockID:
                    raise Exception('StockID not the same!')
            df = pd.read_excel(fileName, index_col = 0, encoding='utf_8_sig')
            if columns is None:
                columns = df.columns
            dfs.append(df)
        
        df = pd.DataFrame()
        df1 = df.append(dfs,  sort=True)
        destFileName = '%s/%s.xlsx'%(outFolder, unifyStockID)
        df1.to_excel(destFileName,columns=columns, encoding="utf_8_sig", index=True)

    def MergeStockYearlySinceYear(self, srcFolder,destFolder, sinceYear = None):
        folderNames=os.listdir(srcFolder)
        destFolders = []
        for folderName in folderNames:
            if folderName.find('.DS_Store')!=-1:
                continue

            (yearOfFolder,_) = folderName.split('-')
            if sinceYear != None and yearOfFolder < sinceYear:
                continue
            fullPath = os.path.join(srcFolder, folderName) 
            destFolders.append(fullPath)
        fileMaping = self.GroupMergeFilesByYearAndStockID(destFolders)
        # for year in fileMaping:
        #     for stockID in fileMaping[year]:
        #         print(year, fileMaping[year][stockID])
        #         input()
        for year in fileMaping:
            count = len(fileMaping[year].keys())
            index = 1
            for stockID in fileMaping[year]:
                print('index:%04d, start to merge StockID:%08s of %s, total:%s'%(index, stockID, year, count))
                self.MergeFilesWithList(year,fileMaping[year][stockID], destFolder)
                index = index +1

if __name__ == '__main__':
   pass
