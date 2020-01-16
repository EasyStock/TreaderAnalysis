'''
 Created on Wed Jan 01 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''

from StockMerge.MergeStockMonthly import MergeStockMonthlyMgr
from StockMerge.MergeStockYearly import MergeStockYearlyMgr
from PathManager.StockPathManager import GetMergedFolder_Last,GetMergedFolder_Month,GetMergedFolder_Year,GetDailyDataFolder
import datetime

def GetMergeTimeSinceNow():
    today = str(datetime.date.today())
    (year,month,day) = today.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    
    if day <=3:
        month = month -1
        if month <=0:
            year = year -1
            month = 12
        return(year, month)
    else:
        return(year, month)

def MergeStockYearly(sinceYear = '2019'):
    srcFolder = GetMergedFolder_Month()
    destFolder = GetMergedFolder_Year()
    mgr = MergeStockYearlyMgr()
    mgr.MergeStockYearlySinceYear(srcFolder,destFolder,sinceYear)

def MergeStockMonthly(sinceMonth = '2019-05'):
    srcFolder = GetDailyDataFolder()
    destFolder = GetMergedFolder_Month()
    mgr = MergeStockMonthlyMgr()
    mgr.MergeStockMonthlySince(srcFolder,destFolder,sinceMonth)

def MergeStockMonthlyThisMonth():
    srcFolder = GetDailyDataFolder()
    destFolder = GetMergedFolder_Month()
    mgr = MergeStockMonthlyMgr()
    mgr.MergeStockMonthlyThisMonth(srcFolder,destFolder)

def MergeStockYearlyThisYear():
    today = str(datetime.date.today())
    (year,_,_) = today.split('-')
    sinceYear = '%s'%(year)
    MergeStockYearly(sinceYear)

def MergeStockMonthlyAuto():
    (year,month) = GetMergeTimeSinceNow()
    print(year,month)
    sinceMonth = '%s-%02s'%(year,month)
    MergeStockMonthly(sinceMonth)

def MergeStockYearlyAuto():
    (year,month) = GetMergeTimeSinceNow()
    print(year,month)
    sinceMonth = '%s-%02s'%(year,month)
    sinceYear = '%s'%(year)
    MergeStockMonthly(sinceMonth)
    MergeStockYearly(sinceYear)


if __name__ == '__main__':
    #MergeStockMonthly()
    #MergeStockYearly('2020')
    MergeStockMonthlyAuto()
    #MergeStockYearlyThisYear()
    #MergeStockYearlyAuto()
