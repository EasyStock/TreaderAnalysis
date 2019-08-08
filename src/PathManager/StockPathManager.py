'''
Created on May 7, 2019

@author: mac
'''
import os

rawPath = '../data/rawData'
outPath = '%s/../output/'%(rawPath)
dailyData = '%s/每日数据/'%(outPath)
analysisPath = '%s/分析/'%(outPath)
filterPath = '%s/过滤/'%(outPath)
SummaryPath = '%s/汇总/'%(outPath)
mergedPath = '%s/合并/'%(outPath)
advanceFilterPath = '%s/多日过滤/'%(outPath)
advanceFilterExPath = '%s/多日过滤Ex/'%(outPath)
combinedFilterPath = '%s/组合过滤/'%(outPath)

analysisBanKuaiPath = '%s/板块分析/'%(analysisPath)
analysisBanKuaiPath_Repeatable = '%s/板块分析_可重复/'%(analysisPath)

analysisBanKuaiSummaryPath = '%s/板块汇总/'%(SummaryPath)
analysisBanKuaiSummaryPath_Repeatable = '%s/板块汇总_可重复/'%(SummaryPath)


allFolder = (rawPath,
             outPath,
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

def getFolderWithFilter(folder, filterName):
    path = os.path.abspath(folder)
    filterPath = u'%s/%s' % (path,filterName)
    if not os.path.exists(filterPath):
        os.makedirs(filterPath)
    return filterPath

def GetRawDataFolder():
    return getFolder(rawPath)

def GetDailyDataFolder():
    return getFolder(dailyData)

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
    return getFolder(advanceFilterPath)

def GetAdvanceFilterExFolder():
    return getFolder(advanceFilterExPath)

def GetCombinedFilterFolder():
    return getFolder(combinedFilterPath)

if __name__ == '__main__':
    CreateAllFolder()
#     print(GetRawDataFolder())
#     print(GetOutDataFolder())
#     print(GetAnalysisDataFolder())
#     print(GetAnalysisBanKuaiFolder())