'''
Created on Jun 16, 2019

@author: mac
'''
from StockFilter.AdvanceFilter.StockAdvanceFilter_20MA_DOWN_CRASS_60MA import CAdvanceFilter_20MA_Down_Cross_60MA
from StockFilter.AdvanceFilter.StockAdvanceFilter_RSI_DunHua import CAdvanceFilter_RSI_DunHua
from StockFilter.AdvanceFilter.StockAdvanceFilter_BOLL_WIDTH import CAdvanceFilter_BOLL_WIDTH
from StockFilter.AdvanceFilter.StockAdvanceFilter_Red3 import CAdvanceFilter_Red3
from StockFilter.FilterMgr.StockAdvanceFilterMgr import CAdvanceFilterMgr
from PathManager.StockPathManager import GetMergedFolder, GetAdvanceFilterFolder,\
    GetRawDataFolder
import os
import pandas as pd
from StockFilter.AdvanceFilter.StockAdvanceFilter_ShortDistance import CAdvanceFilter_ShortDistance
from StockFilter.AdvanceFilter.StockAdvanceFilter_MidDistance import CAdvanceFilter_MidDistance

def __advanceFilter(filter_):
    srcFolder = GetMergedFolder()
    folder_dest = GetAdvanceFilterFolder()
    mgr = CAdvanceFilterMgr()
    mgr.FilterFolder(srcFolder, filter_ ,folder_dest)
    
def __advanceFilterByFilter(filters):
    srcFolder = GetMergedFolder()
    folder_dest = GetAdvanceFilterFolder()
    mgr = CAdvanceFilterMgr()
    mgr.FilterFileByFilter_Folder(srcFolder, filters ,folder_dest)
    
def advanceFilterAll():
    filter0 = CAdvanceFilter_20MA_Down_Cross_60MA()
    filter1 = CAdvanceFilter_RSI_DunHua(threshold_max=78)
    filter2 = CAdvanceFilter_RSI_DunHua(threshold_min=22)
    filter3 = CAdvanceFilter_BOLL_WIDTH()
    filter4 = CAdvanceFilter_Red3()
    
    filters = (filter0, filter1, filter2, filter3,filter4)
    for f in filters:
        __advanceFilter(f)

def advanceFilterByFilter():
    filter1 = CAdvanceFilter_RSI_DunHua(threshold_max=78)
    filter2 = CAdvanceFilter_BOLL_WIDTH()
    filter3 = CAdvanceFilter_Red3()
    filter4 = CAdvanceFilter_RSI_DunHua(threshold_min=45,threshold_max=82)
    
    __advanceFilterByFilter((filter1, filter2))
    __advanceFilterByFilter((filter3, filter4))
    
    __advanceFilterByFilter((filter1,filter3))
    __advanceFilterByFilter((filter2,filter3))
    __advanceFilterByFilter((filter1,filter2, filter3))
    


def __GroupMergeFiles():
    folder_src = GetAdvanceFilterFolder()
    filenames=os.listdir(folder_src)
    res = {}
    for xlsxFile in filenames:
        if xlsxFile.find('.xlsx') == -1:
            continue
        date=xlsxFile[xlsxFile.rfind("_")+1:xlsxFile.rfind(".")]
        if date not in res:
            res[date] = []
        fullFileName = os.path.join(folder_src,xlsxFile)
        df = pd.read_excel(fullFileName, index_col = None, encoding='utf_8_sig')
        res[date].append(df)
    
    return res
        
def MergeAllResult():
    folder_dest= GetRawDataFolder()
    groupedFiles = __GroupMergeFiles()
    for date in groupedFiles:
        res = pd.concat(groupedFiles[date], axis=0,join='outer',sort=False)
        res = res.fillna("NO")
        fileName = u'%s/../%s.xlsx' %(folder_dest,date)
        res.to_excel(fileName,encoding="utf_8_sig", index=False)
        
def DoAdvanceFilterMain():
    Test()
#     advanceFilterByFilter()
#     advanceFilterAll()
    

def Test():
    filter1 = CAdvanceFilter_ShortDistance(1.0)
    filter2 = CAdvanceFilter_RSI_DunHua(threshold_max=80)
    filter3 = CAdvanceFilter_MidDistance(1.0)
    __advanceFilter(filter1)
    __advanceFilter(filter2)

if __name__ == '__main__':
    #DoAdvanceFilterMain()
    #MergeAllResult()
    Test()
#     filter3 = CAdvanceFilter_MidDistance(1.0)
#     __advanceFilter(filter3)
    
    