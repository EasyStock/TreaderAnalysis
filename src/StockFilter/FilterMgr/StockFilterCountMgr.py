'''
Created on May 18, 2019

@author: mac
'''
from StockDataItemIO.StockItemIO import CStockItemIO
import pandas as pd
import os
from PathManager.StockPathManager import GetFilterFolder, GetOutDataFolder
from datetime import date


class CStockFilterCountMgr(object):
    
    def __init__(self):
        pass
    
    def AnalysisOneFoler(self,srcFolder):
        res = {}
        filenames=os.listdir(srcFolder)
        filterName = srcFolder[srcFolder.rfind('/')+1:]
        res[filterName] = {}
        for fileName in filenames:
            fullName = os.path.join(srcFolder, fileName)
            date = fullName[fullName.rfind('/')+1: fullName.rfind('.')]
            io = CStockItemIO()
            io.readFrom(fullName)
            res[filterName][date] = len(io.stocks)
        df = pd.DataFrame(res).T
        return df
        
    def Analysis(self):
        foler = GetFilterFolder()
        filenames=os.listdir(foler)
        dfs = []
        for fileName in  filenames:
            srcFolder = u'%s/%s' %(foler, fileName)
            try:
                df = self.AnalysisOneFoler(srcFolder)
                dfs.append(df)
            except Exception as e:
                print(srcFolder)
                raise(e)
        
        res = pd.concat(dfs,sort=False)
        res = res.fillna(0)
        destFolder = GetOutDataFolder();
        destFile = u"%s/../statics_%s.xlsx" %(destFolder,date.today())
        res.to_excel(destFile,encoding='utf_8_sig')
    
        
if __name__ == '__main__':
    pass