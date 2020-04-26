
'''
Created on May 6, 2019

@author: mac
'''

import os
import multiprocessing as mp
import time
import pandas as pd
from PathManager.StockPathManager import GetMergedFolder_Last


def _ReadAllMergedDailyData(fileName):
    stockID = fileName[fileName.rfind('/')+1:fileName.find('.')]
    df = pd.read_excel(fileName, index_col=None, encoding='utf_8_sig')
    print('Read file:', fileName, 'Done!')
    return {stockID: df}


def ReadAllMergedDailyData():
    folder = GetMergedFolder_Last()
    files = os.listdir(folder)
    dataFrames = []
    begin_time = time.time()
    pool = mp.Pool(mp.cpu_count()*2)
    for file_ in files:
        fullpath = os.path.join(folder, file_)
        if fullpath.find('.xlsx') == -1:
            continue
        dataFrames.append(pool.apply_async(
            _ReadAllMergedDailyData, (fullpath, )))
    pool.close()
    pool.join()
    endTime = time.time()
    print('ReadAllMergedDailyData cost:%s' % (endTime - begin_time))
    ret = {}
    for item in dataFrames:
        ret.update(item.get())
    endTime1 = time.time()
    print('ReadAllMergedDailyData to dict:%s' % (endTime1 - endTime))
    return ret


if __name__ == '__main__':
    ret = ReadAllMergedDailyData()
    for stockID in ret:
        print(stockID, ret[stockID])
        input()
