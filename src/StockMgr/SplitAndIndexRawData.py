
'''
Created on May 6, 2019

@author: mac
'''

from PathManager import StockPathManager
import os
import shutil
from Path import PathOperator

rawDataIndexFile = 'RawDataIndex.json'

def GetFolderNameByDate(date):
    year,month,_ = date.split('-')
    Quarter = (int(month)-1)//3+1
    return '%s/Q%s'%(year,Quarter)

def SplitRawData():
    res = {}
    srcFolder = StockPathManager.GetRawStockTempDataFolder()
    destFolder = StockPathManager.GetRawDataFolder_Stock()
    if os.path.exists(destFolder) == False:
        os.makedirs(destFolder)
    
    files = os.listdir(srcFolder)
    for file_ in files:
        fullpath = os.path.join(srcFolder, file_)
        if fullpath.find('.xls') == -1:
            continue
        date = file_[:file_.find('.')]
        resFolder = os.path.join(destFolder,GetFolderNameByDate(date))
        if os.path.exists(resFolder) == False:
            os.makedirs(resFolder)
        destFileName = os.path.join(resFolder,file_)
        shutil.move(fullpath, destFileName)
        res[date] = destFileName
    return res


def ReCreatIndexOfRawData():
    srcFolder = StockPathManager.GetRawDataFolder_Stock()
    files = PathOperator.listAllFilesInFolder(srcFolder)
    res = {}
    for file_ in files:
        if file_.find('.xls') == -1:
            continue
        date = file_[file_.rfind('/')+1:file_.rfind('.xls')]
        res[date] = file_
    return res


def SplitRawDataAndCreateIndex():
    SplitRawData()
    return ReCreatIndexOfRawData()
