'''
Created on Sep 30, 2019

@author: mac
'''
import pandas as pd
import os

'''
想法1:
1. 上证A股
2. 选取2019年6月27日至2019年7月5日的最大值（0626，0627， 0628，0701, 0702,0703,0704,0705）
3. 选取2019年9月5日的到2019年9月19日的最大值(0905,0906,0909,0910,0911,0912,0916,0917,0918,0919)
4. 选取2019年8月6日到2019年8月16日的最大值(0806, 0807,0808,0809, 0912,0813,0814,0815,0816)

'''

def getClosePriceMaxOfRange(df, days):
    res = []
    for day in days:
        price = (df.loc[day]['收盘价'])
        res.append(price)
    return res

def readFromExcel(fileName):
    df = pd.read_excel(fileName, index_col = 0, encoding='utf_8_sig')
    return df 

def thought1(fileName):
    if fileName.find('.SH') == -1:
        return None
    stockID = fileName[fileName.rfind('/')+1:fileName.rfind('.xlsx')]
    df = readFromExcel(fileName)
    print(fileName)
    days1 = ['2019-06-20','2019-06-21','2019-06-24','2019-06-25','2019-06-26','2019-06-27','2019-06-28','2019-07-01','2019-07-02','2019-07-03','2019-07-04','2019-07-05']
    days2 = ['2019-08-06','2019-08-07','2019-08-08','2019-08-09','2019-08-12','2019-08-13','2019-08-14','2019-08-15','2019-08-16']
    days3 = ['2019-09-05','2019-09-06','2019-09-09','2019-09-10','2019-09-11','2019-09-12','2019-09-16','2019-09-17','2019-09-18','2019-09-19']
    value1 = max(getClosePriceMaxOfRange(df, days1))
    value2 = max(getClosePriceMaxOfRange(df, days2))
    value3 = max(getClosePriceMaxOfRange(df, days3))
    if value3 > value1 > value2:
        print(stockID)
        return stockID
    return None


def Analysis(folder):
    filenames=os.listdir(folder)
    for fileName in filenames:
        fullPath = os.path.join(folder,fileName)
        thought1(fullPath)
    
if __name__ == '__main__':
    folder = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/'
    Analysis(folder)