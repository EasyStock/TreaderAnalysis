'''
Created on Aug 13, 2019

@author: mac
'''
from RegressionTest.RegressionTest import RegressionTest

def Regression():
    srcFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/多日过滤/突破2B失败_反弹_2019-08-12.xlsx'
    destFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/每日数据/2019-08-14.xlsx'
    destFile1 = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/突破2B失败_反弹_2019-08-12.xlsx'
    RegressionTest(destFile, srcFile,destFile1)
    
if __name__ == '__main__':
    Regression()