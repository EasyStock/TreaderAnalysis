'''
Created on Jun 22, 2019

@author: mac
'''

from StockMgr import SplitAndIndexRawData

if __name__ == '__main__':
    res = SplitAndIndexRawData.SplitRawDataAndCreateIndex()
    for date in res:
        print(date, res[date])