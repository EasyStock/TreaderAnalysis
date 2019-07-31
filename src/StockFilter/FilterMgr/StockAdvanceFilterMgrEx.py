'''
Created on Jul 29, 2019

@author: mac
'''
import pandas as pd
from _ast import Try
from StockFilter.AdvanceFilter.StockAdvanceFilter_BOLL_WIDTH import CAdvanceFilter_BOLL_WIDTH

class CStockAdvanceFilterMgrEx(object):

    def __init__(self):
        self.threshold = None
        self.filterNames = [
            '短线均线纠结',
            '中线均线纠结',
            '长线均线纠结',
            'BOLL带宽',
            ]
    
    def _getBOLLWidthFilterWithStockID(self, stockID):
        if self.threshold == None:
            return None
        try:
            threhold = self.threshold.loc[stockID]['BOLL带宽_low']
            CAdvanceFilter_BOLL_WIDTH()
        except:
            pass
    def ReadThreshold(self,threadFile):
        self.threshold = pd.read_excel(threadFile, encoding='utf_8_sig', index_col = 0)
        print(self.threshold.loc['000001.SZ']['BOLL带宽_low'])
    
    
    def FilterFile(self, stockID, srcFileName, filterName):
        df = pd.read_excel(srcFileName, index_col = None, encoding='utf_8_sig')
        
    
    
    def FilterFileEveryDay(self, stockID, srcFileName, filter_):
        pass
    
    
    def FilterFolder(self,folder,filter_, outFolder):
        pass
    
    
    def FilterFolderEveryDay(self,folder,filter_, outFolder):
        pass
    
    
    def FilterFileByFilter_Folder(self,folder,filters, outFolder):
        pass
    
    
if __name__ == '__main__':
    fileName = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/threshold.xlsx'
    ex = CStockAdvanceFilterMgrEx()
    ex.ReadThreshold(fileName)