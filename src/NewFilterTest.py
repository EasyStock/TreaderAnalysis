'''
Created on May 6, 2019

@author: mac
'''

from Filters.SimpleFilter import SimpleFilter_TradingDay,SimpleFilter_ZhangDieFu,SimpleFilter_GreatThanMA,SimpleFilter_NotST,SimpleFilter_Market,SimpleFilter_ClosePriceNewHigh,SimpleFilter_UpStates
import pandas as pd
import os
import multiprocessing


def Test():
    folder = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/最近合并/'
    files = os.listdir(folder)


    count = 0
    for file_ in files:
        fullpath = '%s%s'%(folder,file_)
        if fullpath.find('.xlsx') == -1:
            continue
        stockID = file_[:file_.find('.')]
        filter0 =  SimpleFilter_Market.CSimpleFilter_Market((stockID,(SimpleFilter_Market.STOCK_MARKET_ZHONGXIAOBAN,SimpleFilter_Market.STOCK_MARKET_SHANGHAI,SimpleFilter_Market.STOCK_MARKET_CHUANGYEBAN))) #
        if filter0.FilterCurrentOnly(None) == False:
            continue

        df = pd.read_excel(fullpath, index_col = None, encoding='utf_8_sig')
        filter1 = SimpleFilter_TradingDay.CSimpleFilter_TradingDay([250,9999999]) #非新股和次新股
        filter11 =  SimpleFilter_NotST.CSimpleFilter_NotST() #Not ST
        # filter2 = SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(5) #MA5
        # filter21 = SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(10) #MA5
        # filter3 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(20) #MA20
        # filter4 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(30) #MA30
        # filter5 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(60) #MA60
        # filter6 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(120) #MA120
        # filter7 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(240) #MA240

        # res = filter1.Filter(df,(filter11,filter2,filter21,filter3,filter4,filter5,filter6,filter7))
        filter8 =  SimpleFilter_ClosePriceNewHigh.CSimpleFilter_ClosePriceNewHigh(90)
        res = filter8.Filter(df,(filter1,filter11))
        if res == True:
            print(fullpath)
            #print(filter1.callStack)
            print('\n\n\n')
            count = count +1
            #input()
    print(count)

def TestFile():
    file_ = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/最近合并/000021.SZ.xlsx'
    df = pd.read_excel(file_, index_col = None, encoding='utf_8_sig')
    
    filter1 = SimpleFilter_TradingDay.CSimpleFilter_TradingDay([250,9999999]) #非新股和次新股
    filter11 =  SimpleFilter_NotST.CSimpleFilter_NotST() #Not ST
    filter2 = SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(5) #MA5
    filter3 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(20) #MA5
    filter4 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(30) #MA5
    filter5 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(60) #MA5

    res = filter1.Filter(df,(filter11,filter2,filter3,filter4,filter5))


def MultiProcessFunction(fileName):
        stockID = fileName[fileName.rfind('/')+1:fileName.find('.')]
        filter0 =  SimpleFilter_Market.CSimpleFilter_Market((stockID,(SimpleFilter_Market.STOCK_MARKET_ZHONGXIAOBAN,SimpleFilter_Market.STOCK_MARKET_SHANGHAI,SimpleFilter_Market.STOCK_MARKET_CHUANGYEBAN))) #
        if filter0.FilterCurrentOnly(None) == False:
            return
        df = pd.read_excel(fileName, index_col = None, encoding='utf_8_sig')
        filter1 = SimpleFilter_TradingDay.CSimpleFilter_TradingDay([250,9999999]) #非新股和次新股
        filter11 =  SimpleFilter_NotST.CSimpleFilter_NotST() #Not ST
        filter2 = SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(5) #MA5
        filter21 = SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(10) #MA5
        filter3 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(20) #MA20
        filter4 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(30) #MA30
        filter5 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(60) #MA60
        filter6 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(120) #MA120
        filter7 =  SimpleFilter_GreatThanMA.CSimpleFilter_GreatThanMA(240) #MA240
        filter9 =  SimpleFilter_UpStates.CSimpleFilter_UpStates() #MA240
        res = filter1.Filter(df,(filter11,filter2,filter21,filter3,filter4,filter5,filter6,filter7,filter9))

        #filter8 =  SimpleFilter_ClosePriceNewHigh.CSimpleFilter_ClosePriceNewHigh(90)
        #res = filter8.Filter(df,(filter1,filter11))
        if res == True:
            print(fileName)
        

def TestMultiProcess():
    folder = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/最近合并/'
    files = os.listdir(folder)
    pool = multiprocessing.Pool(processes=8) # 创建8个进程
    for file_ in files:
        fullpath = '%s%s'%(folder,file_)
        if fullpath.find('.xlsx') == -1:
            continue
        pool.apply_async(MultiProcessFunction, (fullpath, ))
    pool.close() 
    pool.join()

if __name__ == '__main__':
    #Test()
    #TestFile()
    TestMultiProcess()