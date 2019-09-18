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
    GetRawDataFolder_Stock, GetOutDataFolder, GetAdvanceFilterExFolder
import os
import pandas as pd
from StockFilter.AdvanceFilter.StockAdvanceFilter_ShortDistance import CAdvanceFilter_ShortDistance
from StockFilter.AdvanceFilter.StockAdvanceFilter_MidDistance import CAdvanceFilter_MidDistance
from StockFilter.AdvanceFilter.StockAdvanceFilter_ShortDistanceEx import CAdvanceFilter_ShortDistanceEx
from StockFilter.FilterMgr.StockAdvanceFilterMgrEx import CStockAdvanceFilterMgrEx,\
    K_ADVANCE_FILTER_EX_MID_DISTANCE, K_ADVANCE_FILTER_EX_BOLL_WIDTH
from StockFilter.AdvanceFilter.StockAdvanceFilter_NewHigh import CAdvanceFilter_NewHigh
from StockFilter.AdvanceFilter.StockAdvanceFilter_Big_Volumn import CAdvanceFilter_BigVolumn
from StockFilter.AdvanceFilter.StockAdvanceFilter_2BRule import CAdvanceFilter_2BRule
from StockFilter.AdvanceFilter.StockAdvanceFilter_RSI_BeiLi import CAdvanceFilter_RSI_BeiLi
from StockFilter.AdvanceFilter.StockAdvanceFilter_OpenEqualLower import CAdvanceFilter_OpenEqualLower
from StockFilter.AdvanceFilter.StockAdvanceFilter_YunXian import CAdvanceFilter_YunXian
from StockFilter.AdvanceFilter.StockAdvanceFilter_AttackDay import CAdvanceFilter_AttackDay
from StockFilter.AdvanceFilter.StockAdvanceFilter_AYa import CAdvanceFilter_AYa
from StockFilter.AdvanceFilter.StockAdvanceFilter_ShadowUp import CAdvanceFilter_ShadowUp

def __advanceFilter(filter_):
    message = 'start do job with filter:%s '%(filter_.filterName)
    print(message)
    srcFolder = GetMergedFolder()
    folder_dest = GetAdvanceFilterFolder()
    mgr = CAdvanceFilterMgr()
    mgr.FilterFolder(srcFolder, filter_ ,folder_dest)
    message = 'end job with filter:%s '%(filter_.filterName)
    print(message)

def __advanceFilterEveryDay(filter_):
    srcFolder = GetMergedFolder()
    folder_dest = GetAdvanceFilterFolder()
    mgr = CAdvanceFilterMgr()
    mgr.FilterFolderEveryDay(srcFolder, filter_ ,folder_dest)
    
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
    folder_dest= GetRawDataFolder_Stock()
    groupedFiles = __GroupMergeFiles()
    for date in groupedFiles:
        res = pd.concat(groupedFiles[date], axis=0,join='outer',sort=False)
        res = res.fillna("NO")
        fileName = u'%s/../%s.xlsx' %(folder_dest,date)
        res.to_excel(fileName,encoding="utf_8_sig", index=False)

def DoAdvanceFilter():
    filter1 = CAdvanceFilter_ShortDistance(0.5)
    filter2 = CAdvanceFilter_RSI_DunHua(threshold_max=83)
    __advanceFilter(filter1)
    __advanceFilter(filter2)
#     advanceFilterByFilter()
#     advanceFilterAll()
    filter3 = CAdvanceFilter_MidDistance(0.8)
    __advanceFilter(filter3)
    
    filter8 = CAdvanceFilter_NewHigh(5)
    __advanceFilter(filter8)
    
    filter9 =  CAdvanceFilter_BigVolumn(40, 3)
    __advanceFilter(filter9)
    
    filter10 = CAdvanceFilter_2BRule(40)
    __advanceFilter(filter10)
    
    filter11= CAdvanceFilter_RSI_BeiLi(40)
    __advanceFilter(filter11)
    
    filter13 = CAdvanceFilter_YunXian()
    __advanceFilter(filter13)
     
    filter14 = CAdvanceFilter_AttackDay()
    __advanceFilter(filter14)
    
    filter15 = CAdvanceFilter_AYa()
    __advanceFilter(filter15)
    
    filter16 = CAdvanceFilter_ShadowUp(3.0)
    __advanceFilter(filter16)
    
def DoAdvanceFilterMain():
    DoAdvanceFilter()
    DoAdvanceFilterEx()
    
def DoAdvanceFilterEx():
    advanceMgr = CStockAdvanceFilterMgrEx()
    threadFile = '%s/threshold.xlsx'%(GetOutDataFolder())
    advanceMgr.ReadThreshold(threadFile)
    folder = GetMergedFolder()
    outFolder = GetAdvanceFilterExFolder()
    fitlerNames = [
        K_ADVANCE_FILTER_EX_BOLL_WIDTH,
        K_ADVANCE_FILTER_EX_MID_DISTANCE
        ]
    for filterName in fitlerNames:
        advanceMgr.FilterFolder(folder, outFolder, filterName)
    
def Test():
#     filter1 = CAdvanceFilter_ShortDistance(0.5)
#     __advanceFilter(filter1)
#     filter2 = CAdvanceFilter_ShortDistanceEx(0.8)
#     __advanceFilter(filter2)
#     filter3 = CAdvanceFilter_MidDistance(0.8)
#     __advanceFilter(filter3)
#     filter4 = CAdvanceFilter_NewHigh(100)
#     __advanceFilter(filter4)
#     filter5 = CAdvanceFilter_NewHigh(50)
#     __advanceFilter(filter5)
#     filter6 = CAdvanceFilter_NewHigh(30)
#     __advanceFilter(filter6)
#     filter7 = CAdvanceFilter_NewHigh(10)
#     __advanceFilter(filter7)
#     filter8 = CAdvanceFilter_NewHigh(5)
#     __advanceFilter(filter8)
    
#     filter9 =  CAdvanceFilter_BigVolumn(40, 3)
#     __advanceFilter(filter9)
     
#     filter10 = CAdvanceFilter_2BRule(60)
#     __advanceFilter(filter10)
    
#     filter11= CAdvanceFilter_RSI_BeiLi(40)
#     __advanceFilter(filter11)

#     filter12 = CAdvanceFilter_OpenEqualLower()
#     __advanceFilter(filter12)

#     filter13 = CAdvanceFilter_YunXian()
#     __advanceFilter(filter13)
#      
#     filter14 = CAdvanceFilter_AttackDay()
#     __advanceFilter(filter14)
#     
#     filter15 = CAdvanceFilter_AYa()
#     __advanceFilter(filter15)
    
    filter16 = CAdvanceFilter_ShadowUp(3.0)
    __advanceFilter(filter16)

def AdvanceFilterTest():
    advanceMgr = CStockAdvanceFilterMgrEx()
    threadFile = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/threshold.xlsx'
    advanceMgr.ReadThreshold(threadFile)
    folder = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/合并/'
    outFolder = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/'
    #filterName = K_ADVANCE_FILTER_EX_MID_DISTANCE
    filterName = K_ADVANCE_FILTER_EX_BOLL_WIDTH
    advanceMgr.FilterFolder(folder, outFolder, filterName)

if __name__ == '__main__':
#     DoAdvanceFilterMain()
    #MergeAllResult()
    Test()
#     DoAdvanceFilterEx()
    #AdvanceFilterTest()
#     filter3 = CAdvanceFilter_MidDistance(1.0)
#     __advanceFilter(filter3)
#     filter2 = CAdvanceFilter_ShortDistanceEx(0.8)
#     __advanceFilterEveryDay(filter2)
    
    