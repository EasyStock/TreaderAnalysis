'''
Created on May 18, 2019

@author: mac
'''
from StockDataItemIO.StockItemIO import CStockItemIO
import pandas as pd
import os
from PathManager.StockPathManager import GetAnalysisBanKuaiFolder, GetAnalysisBanKuaiSummaryFolder,\
    GetAnalysisBanKuaiFolder_Repeatable,\
    GetAnalysisBanKuaiSummaryFolder_Repeatable, GetFilterFolder
from _collections import OrderedDict

class CStockFilterBanKuaiMgr(object):
    
    def __init__(self):
        self.__banKuaiExcept = ['沪股通','深股通','融资融券','转融券标的',u'证金持股',u'地方国资改革','年报预增',u'央企国资改革']
 
    def getAllKeysOfBanKuai(self, stocks, banKuaiExcept):
        allKeys = []
        for stock in stocks:
            allKeys.extend(stock.getBanKuai())

        allKeys=list(set(allKeys))
        retKeys = []
        for key in allKeys:
            if key in banKuaiExcept:
                continue
            else:
                retKeys.append(key)
        return retKeys
    
    def groupStockByBanKuaiEX(self, stocks):
        allkeys = self.getAllKeysOfBanKuai(stocks, self.__banKuaiExcept)
        ret = {}
        for key in allkeys:
            if key not in ret:
                ret[key] = []
            for stock in stocks:
                if stock.isKeyInBanKuai(key):
                    ret[key].append(stock)

        sortedData = sorted(ret.items(), key=lambda item:len(item[1]),reverse=True)
        dirtyData = []
        orderRet = OrderedDict()

        for stock in stocks:
            process = False
            for item in sortedData:
                key = item[0]
                if key not in orderRet:
                    orderRet[key] = []
                if stock.isKeyInBanKuai(key) and stock not in dirtyData:
                    orderRet[key].append(stock)
                    dirtyData.append(stock)
                    process = True
                    break;
            if not process:
                for key in self.__banKuaiExcept:
                    if key not in orderRet:
                        orderRet[key] = []
                    if stock.isKeyInBanKuai(key) and stock not in dirtyData:
                        orderRet[key].append(stock)
                        dirtyData.append(stock)

        return orderRet
         
         
    def groupStockByBanKuai(self, stocks):
        allKeys = self.getAllKeysOfBanKuai(stocks, self.__banKuaiExcept)
        ret = {}
        #print('with %d stocks and %d keys' % (len(stocks), len(allKeys)))
        for stock in stocks:
            process = False
            for key in allKeys:
                if key not in ret:
                    ret[key] = []
                if stock.isKeyInBanKuai(key):
                    ret[key].append(stock)
                    process = True
            if not process:
                for newKey in self.__banKuaiExcept:
                    if newKey not in ret:
                        ret[newKey] = []
                    if stock.isKeyInBanKuai(newKey):
                        ret[newKey].append(stock)
        return ret
    
    def getBanKuaiResult(self, fName, outFileName, mapOfResult ):
        res = sorted(mapOfResult.items(), key=lambda d:len(d[1]), reverse = True)
        key2 = u'%s' %(fName)
        ret ={
            u'板块':[r[0] for r in res],
            key2:[len(r[1]) for r in res],
        }
        df = pd.DataFrame.from_dict(ret)
        df = df[[u'板块', key2]]
        df.to_excel(outFileName,encoding="utf_8_sig", index=False)
    
    def mergeFiles(self,folderSrc,fileDest):
        datas = []
        filenames=os.listdir(folderSrc)
        for f in filenames:
            if f.find('.xlsx') == -1:
                continue
            fullPath = os.path.join(folderSrc, f)
            df = pd.read_excel(fullPath, index_col = 0, encoding='utf_8_sig')
            datas.append(df)
        if len(datas) == 0:
            print("mergeFiles Failed! ")
            print(folderSrc)
            print(fileDest)
            return None
        res = pd.concat(datas, axis=1,join='outer',sort=False)
        res = res.fillna(0)
        res.to_excel(fileDest,encoding='utf_8_sig')

    def AnalysisBanKuaiOfOneFile(self,fileName,outFileName, repeatable=False):
        if os.path.exists(outFileName):
            return

        fName = fileName[fileName.rfind('/')+1: fileName.rfind('.')]
        io = CStockItemIO()
        io.readFrom(fileName)
        if repeatable:
            mapOfResult = self.groupStockByBanKuai(io.stocks)
        else:
            mapOfResult = self.groupStockByBanKuaiEX(io.stocks)
        self.getBanKuaiResult(fName, outFileName,mapOfResult)
    
    def AnalysisOneFoler(self,srcFolder,destFolder,repeatable = False):
        filenames=os.listdir(srcFolder)
        for fileName in filenames:
            fullName = os.path.join(srcFolder, fileName)
            outFileName= os.path.join(destFolder, fileName)
            self.AnalysisBanKuaiOfOneFile(fullName, outFileName,repeatable)
    
    
    def AnalysisRepeatly(self):
        foler = GetFilterFolder()
        banKuaiFolder = GetAnalysisBanKuaiFolder_Repeatable()
        filenames=os.listdir(foler)
        SummaryFolder =GetAnalysisBanKuaiSummaryFolder_Repeatable()
        for fileName in  filenames:
            srcFolder = u'%s/%s/' %(foler, fileName)
            destFolder = u'%s/%s/'%(banKuaiFolder, fileName)
            fileDest = u'%s.xlsx'%(os.path.join(SummaryFolder,fileName))
            if not os.path.exists(destFolder):
                os.makedirs(destFolder)
            try:
                self.AnalysisOneFoler(srcFolder, destFolder,True)
                self.mergeFiles(destFolder, fileDest)
            except Exception as e:
                print(srcFolder)
                print(destFolder)
                print(fileDest)
                print(e)
                
    def Analysis(self):
        foler = GetFilterFolder()
        banKuaiFolder = GetAnalysisBanKuaiFolder()
        filenames=os.listdir(foler)
        SummaryFolder =GetAnalysisBanKuaiSummaryFolder()
        for fileName in  filenames:
            srcFolder = u'%s/%s/' %(foler, fileName)
            destFolder = u'%s/%s/'%(banKuaiFolder, fileName)
            fileDest = u'%s.xlsx'%(os.path.join(SummaryFolder,fileName))
            if not os.path.exists(destFolder):
                os.makedirs(destFolder)
            try:
                self.AnalysisOneFoler(srcFolder, destFolder,False)
                self.mergeFiles(destFolder, fileDest)
            except Exception as e:
                print(srcFolder)
                print(destFolder)
                print(fileDest)
                print(e)
        
if __name__ == '__main__':
    fileName = u'/Volumes/Data/StockAssistant/TreaderAnalysis/data/output/转换数据/2019-05-24.xlsx'
    io = CStockItemIO()
    io.readFrom(fileName)
    
    mgr=CStockFilterBanKuaiMgr()
    res = mgr.groupStockByBanKuai(io.stocks)
    print(len(io.stocks))
    sortedData = sorted(res.items(), key=lambda item:len(item[1]),reverse=True)
    allCount = 0
    for data in sortedData:
        allCount = allCount +  len(data[1])
        print(data[0],len(data[1]),allCount)