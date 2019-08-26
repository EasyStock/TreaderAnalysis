'''
Created on Aug 13, 2019

@author: mac
'''
from RegressionTest.RegressionTest import RegressionTest
from _datetime import date

def RegressionTwo():
    daily1 = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/每日数据/2019-08-20.xlsx'
    daily2 = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/每日数据/2019-08-26.xlsx'
    
    srcFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/多日过滤Ex/2019-08-20/BOLL带宽_2019-08-20.xlsx'
    destFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/BOLL带宽_2019-08-20.xlsx'
    
    tmp = "/tmp/tmp_%s.xlsx"%(date.today())
    RegressionTest(daily1, srcFile,tmp)
    RegressionTest(daily2, tmp,destFile)
    
    
    
def Regression():
    srcFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/多日过滤Ex/2019-08-20/BOLL带宽_2019-08-20.xlsx'
    destFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/每日数据/2019-08-26.xlsx'
    destFile1 = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/BOLL带宽_2019-08-20.xlsx'
    RegressionTest(destFile, srcFile,destFile1)

    
if __name__ == '__main__':
    #Regression()
    RegressionTwo()