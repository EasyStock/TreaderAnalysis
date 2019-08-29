'''
Created on May 7, 2019

@author: mac
'''
import os
from datetime import date

rawPath = '../data/rawData'
rawStockPath = '%s/股票/'%(rawPath)
rawIndexBanKuaiPath = '%s/板块指数/'%(rawPath)
outPath = '%s/../output/'%(rawPath)
outStockPath = '%s/股票/'%(outPath)
outIndexBanKuaiPath = '%s/板块指数/'%(outPath)

dailyData = '%s/每日数据/'%(outStockPath)
dailyData_Index_BanKuai = '%s/每日数据/'%(outIndexBanKuaiPath)

analysisPath = '%s/分析/'%(outStockPath)
filterPath = '%s/过滤/'%(outStockPath)
SummaryPath = '%s/汇总/'%(outStockPath)
mergedPath = '%s/合并/'%(outStockPath)
advanceFilterPath = '%s/多日过滤/'%(outStockPath)
advanceFilterExPath = '%s/多日过滤Ex/'%(outStockPath)
combinedFilterPath = '%s/组合过滤/'%(outStockPath)

analysisBanKuaiPath = '%s/板块分析/'%(analysisPath)
analysisBanKuaiPath_Repeatable = '%s/板块分析_可重复/'%(analysisPath)

analysisBanKuaiSummaryPath = '%s/板块汇总/'%(SummaryPath)
analysisBanKuaiSummaryPath_Repeatable = '%s/板块汇总_可重复/'%(SummaryPath)


allFolder = (rawPath,
             rawStockPath,
             rawIndexBanKuaiPath,
             outPath,
             outStockPath,
             outIndexBanKuaiPath,
             dailyData,
             analysisPath,
             filterPath,
             SummaryPath,
             mergedPath,
             analysisBanKuaiPath,
             analysisBanKuaiPath_Repeatable,
             analysisBanKuaiSummaryPath,
             analysisBanKuaiSummaryPath_Repeatable,
             )

def CreateAllFolder():
    for folder in allFolder:
        path = os.path.abspath(folder)
        if not os.path.exists(path):
            os.makedirs(path)

def getFolder(folder):
    path = os.path.abspath(folder)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def getFolderWithDate(folder):
    folderWithDate = '%s/%s/'%(folder,date.today())
    path = os.path.abspath(folderWithDate)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def getFolderWithFilter(folder, filterName):
    path = os.path.abspath(folder)
    filterPath = u'%s/%s' % (path,filterName)
    if not os.path.exists(filterPath):
        os.makedirs(filterPath)
    return filterPath

def GetRawDataFolder():
    return getFolder(rawPath)

def GetRawDataFolder_Stock():
    return getFolder(rawStockPath)

def GetRawDataFolder_Index_BanKuai():
    return getFolder(rawIndexBanKuaiPath)

def GetDailyDataFolder():
    return getFolder(dailyData)

def GetDailyDataFolder_Index_BanKuai():
    return getFolder(dailyData_Index_BanKuai)

def GetOutDataFolder():
    return getFolder(outPath)

def GetAnalysisDataFolder():
    return getFolder(analysisPath)

def GetFilterFolder():
    return getFolder(filterPath)
    
def GetFilterFolderWithFilterName(filterName):
    return getFolderWithFilter(filterPath, filterName)

def GetAnalysisBanKuaiFolder():
    return getFolder(analysisBanKuaiPath)

def GetAnalysisBanKuaiSummaryFolder():
    return getFolder(analysisBanKuaiSummaryPath)

def GetAnalysisBanKuaiFolder_Repeatable():
    return getFolder(analysisBanKuaiPath_Repeatable)

def GetAnalysisBanKuaiSummaryFolder_Repeatable():
    return getFolder(analysisBanKuaiSummaryPath_Repeatable)

def GetMergedFolder():
    return getFolder(mergedPath)

def GetAdvanceFilterFolder():
    return getFolderWithDate(advanceFilterPath)

def GetAdvanceFilterExFolder():
    return getFolderWithDate(advanceFilterExPath)

def GetCombinedFilterFolder():
    return getFolderWithDate(combinedFilterPath)

if __name__ == '__main__':
    CreateAllFolder()
#     print(GetRawDataFolder_Stock())
#     print(GetOutDataFolder())
#     print(GetAnalysisDataFolder())
#     print(GetAnalysisBanKuaiFolder())