'''
Created on Jul 29, 2019

@author: mac
'''
import pandas as pd
from StockFilter.AdvanceFilter.StockAdvanceFilter_BOLL_WIDTH import CAdvanceFilter_BOLL_WIDTH
from StockDataItem.StockItemDef import stock_DISTANCE_MA_MID,\
    stock_BOLL_Band_width, stock_ID
from StockFilter.AdvanceFilter.StockAdvanceFilter_MidDistance import CAdvanceFilter_MidDistance
import os
from datetime import date

K_ADVANCE_FILTER_EX_MID_DISTANCE = "中线均线纠结"
K_ADVANCE_FILTER_EX_BOLL_WIDTH = "BOLL带宽"

class CStockAdvanceFilterMgrEx(object):
    def __init__(self):
        self.threshold = None
    
    def _getBOLLWidthFilterWithStockID(self, stockID):
        if self.threshold is None:
            return None
        
        threhold = 16
        try:
            key = "%s_low"%(stock_BOLL_Band_width)
            threhold = self.threshold.loc[stockID][key]
        except:
            pass
        
        flter = CAdvanceFilter_BOLL_WIDTH(threhold)
        return flter
    
    def _getMidDistanceFilterWithStockID(self,stockID):
        if self.threshold is None:
            return None
        
        threhold = 10
        try:
            key = "%s_low"%(stock_DISTANCE_MA_MID)
            threhold = self.threshold.loc[stockID][key]
            if threhold > 10:
                threhold = 10
        except:
            pass
        
        flter = CAdvanceFilter_MidDistance(threhold)
        return flter
        
        
    def ReadThreshold(self,threadFile):
        self.threshold = pd.read_excel(threadFile, encoding='utf_8_sig', index_col = 0)
    
    
    def ReadSrcFile(self, srcFileName):
        df = pd.read_excel(srcFileName, index_col = None, encoding='utf_8_sig')
        return df
    
    def FilterFile(self, stockID, srcFileName, filterName):
        df = self.ReadSrcFile(srcFileName)
        filter_ = None
        if filterName == K_ADVANCE_FILTER_EX_MID_DISTANCE:
            filter_ = self._getMidDistanceFilterWithStockID(stockID)
        elif filterName == K_ADVANCE_FILTER_EX_BOLL_WIDTH:
            filter_ = self._getBOLLWidthFilterWithStockID(stockID)
    
        return filter_.FilterBy(df)
    
    
    def FilterFileEveryDay(self, stockID, srcFileName, filter_):
        pass
    
    
    def FilterFolder(self,folder, outFolder, filterName):
        ret = []
        filenames=os.listdir(folder)
        for xlsxFile in filenames:
            if xlsxFile.find('.xlsx') == -1:
                continue
            stockID = xlsxFile[:xlsxFile.rfind('.')]
            srcFileName = os.path.join(folder,xlsxFile)
            res = self.FilterFile(stockID, srcFileName, filterName)
            if res[0]:
                res[1][stock_ID] = stockID
                ret.append(res[1])
                print(stockID, srcFileName)

        if len(ret) > 0:
            df = pd.DataFrame(ret)
            fileName = u'%s/%s_%s.xlsx' %(outFolder, filterName,date.today())
            df.to_excel(fileName,encoding="utf_8_sig", index=False)
    
    
    def FilterFolderEveryDay(self,folder,filter_, outFolder):
        pass
    
    
    def FilterFileByFilter_Folder(self,folder,filters, outFolder):
        pass
    
    
if __name__ == '__main__':
    fileName = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/threshold.xlsx'
    ex = CStockAdvanceFilterMgrEx()
    ex.ReadThreshold(fileName)