'''
Created on May 6, 2019

@author: mac
'''
from PathManager.StockPathManager import GetRawDataFolder_Stock, GetDailyDataFolder, GetMergedFolder,GetMergedFolder_Month
import os
from StockDataItemIO.StockItemIO import CStockItemIO
from StockMerge.MergeStock import MergeStockMgr
from advanceFilterMain import DoAdvanceFilterMain
from filterMain import DoFilterMain
from thresholdCalcMgr import CalcThreshold
from CombinedFilterMain import CombinedFilteMain

def ConverHTMLToXlSX():
    folder = GetRawDataFolder_Stock()
    outFolder = GetDailyDataFolder()
    filenames=os.listdir(folder)
    for htmlFile in filenames:
        if htmlFile.find('.xls') == -1:
            continue
        fName = htmlFile[:htmlFile.rfind('.')]
        srcFileName = os.path.join(folder,htmlFile)
        outFullName = u'%s/%s.xlsx' %(outFolder,fName)
        if os.path.exists(outFullName):
            continue
        io = CStockItemIO()
        io.readFrom(srcFileName)
        io.saveTo(outFullName)

    
def MergeFiles():
    srcFolder = GetDailyDataFolder()
    destFolder = GetMergedFolder()
    merge = MergeStockMgr()
    merge.MergeStockWithFolder(srcFolder, destFolder)

def TestMergeFiles():
    srcFolder = GetDailyDataFolder()
    destFolder = GetMergedFolder_Month()
    merge = MergeStockMgr()
    merge.FastMerge_Last_TwoMonth(srcFolder, destFolder)

if __name__ == '__main__':
     ConverHTMLToXlSX()
     MergeFiles()
    #TestMergeFiles()
     CalcThreshold()
    
    #DoFilterMain()
     DoAdvanceFilterMain()
    #CombinedFilteMain()
   

