'''
Created on May 6, 2019

@author: mac
'''
from PathManager.StockPathManager import GetRawDataFolder_Stock, GetDailyDataFolder, GetMergedFolder_Last,GetMergedFolder_Month
import os
from StockDataItemIO.StockItemIO import CStockItemIO
from StockMerge.MergeStock import MergeStockMgr
from advanceFilterMain import DoAdvanceFilterMain
from filterMain import DoFilterMain
from thresholdCalcMgr import CalcThreshold
from CombinedFilterMain import CombinedFilteMain
from StockMergeMain import MergeStockLastNAuto
import time
from Log.StockLog import INFO_LOG, ERROR_LOG, WARNING_LOG

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
    destFolder = GetMergedFolder_Last()
    merge = MergeStockMgr()
    merge.MergeStockWithFolder(srcFolder, destFolder)

def TestMergeFiles():
    srcFolder = GetDailyDataFolder()
    destFolder = GetMergedFolder_Month()
    merge = MergeStockMgr()
    merge.FastMerge_Last_TwoMonth(srcFolder, destFolder)

if __name__ == '__main__':
     begin_time = time.time()
     ConverHTMLToXlSX()
     ConverToXMLTime = time.time()
     WARNING_LOG(("ConverToXMLTime:%s"%(ConverToXMLTime - begin_time)))
     MergeStockLastNAuto(95)
     mergeTime = time.time()
     WARNING_LOG(("mergeTime:%s"%(mergeTime - ConverToXMLTime)))
    #MergeFiles()
    #TestMergeFiles() 
     CalcThreshold()
     CalcThresholdTime = time.time()
     WARNING_LOG(("CalcThresholdTime:%s"%(CalcThresholdTime - mergeTime)))
    #DoFilterMain()
     DoAdvanceFilterMain()
     DoAdvanceFilterTime = time.time()
     WARNING_LOG(("DoAdvanceFilterTime:%s"%(DoAdvanceFilterTime - CalcThresholdTime)))
    #CombinedFilteMain()
   

