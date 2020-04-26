
'''
Created on May 6, 2019

@author: mac
'''
from PathManager.StockPathManager import GetRawDataFolder_Stock, GetDailyDataFolder
import os
from StockDataItemIO.StockItemIO import CStockItemIO
import multiprocessing as mp
import time

def _converHTMLToXLSX(srcFileName, outFullName):
    print(srcFileName,'Begin!')
    io = CStockItemIO()
    io.readFrom(srcFileName)
    io.saveTo(outFullName)
    print(srcFileName,'Done!')

def ConverHTMLToXlSX():
    begin_time = time.time()
    folder = GetRawDataFolder_Stock()
    outFolder = GetDailyDataFolder()
    filenames=os.listdir(folder)
    pool = mp.Pool(mp.cpu_count()*2)
    for htmlFile in filenames:
        if htmlFile.find('.xls') == -1:
            continue
        fName = htmlFile[:htmlFile.rfind('.')]
        srcFileName = os.path.join(folder,htmlFile)
        outFullName = u'%s/%s.xlsx' %(outFolder,fName)
        if os.path.exists(outFullName):
            continue
        pool.apply_async(_converHTMLToXLSX, (srcFileName, outFullName))

    pool.close() 
    pool.join()
    endTime = time.time()
    print('ConverHTMLToXlSX:%s'%(endTime - begin_time))

if __name__ == '__main__':
    ConverHTMLToXlSX()