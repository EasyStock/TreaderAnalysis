# coding=utf-8
'''
 Created on Tue Jan 07 2020 10:46:03
 @author: jianpinh
'''
import os
import pandas as pd

srcFolder = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/多日过滤/'
destFolder = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output'

def ListAllTheFolders(srcFolder, category,fromDay = None, toDay = None):
    allfile=[]
    for root,_,filenames in os.walk(srcFolder):
        date = root.split('/')[-1]
        if (len(date.split('-')))!= 3: #not a data 
            continue

        if fromDay is not None and date < fromDay:
            continue
        if toDay is not None and date > toDay:
            continue

        for name in filenames:
            if name.find('.xlsx') == -1:
                continue
            if name.find(category) == -1:
                continue
            allfile.append(os.path.join(root, name))
    
    allfile.sort(reverse=False)
    return allfile


def ReadAllFiles(fileList,index = ['股票代码']):
    res = []
    for fileName in fileList:
        try:
            df = pd.read_excel(fileName, index_col = 0, encoding='utf_8_sig')
            df = df.set_index(index)
        except:
            print(fileName)
        res.append((df,fileName))
    return res

def Merge(first,next,dataFrameMerged, extraInfo, appendix):
    if not extraInfo:
        firstDataFrame = first[0]
        dataFrameMerged = firstDataFrame.copy()
        firstDate = first[1].split('/')[-2]
        firstKeys = firstDataFrame.index.to_list()
        for key in firstKeys:
            extraInfo[key] = "%s%s"%(firstDate,appendix[0])

        return Merge(first,next,dataFrameMerged,extraInfo,appendix) #递归
    else:
        secondFrame = next[0]
        secondDate = next[1].split('/')[-2]
        secondKeys = secondFrame.index.to_list()
        for key in secondKeys:
            if key not in extraInfo:
                extraInfo[key] = "%s%s"%(secondDate,appendix[0]) #增加
                dataFrameMerged.loc[key] = secondFrame.loc[key]
            else:
                extraInfo[key] = "%s;%s%s"%(extraInfo[key],secondDate,appendix[1]) #修改
                dataFrameMerged.loc[key] = secondFrame.loc[key]

        for key in extraInfo.keys():
            if key not in secondKeys:
                splitInfos = extraInfo[key].split(":")
                if splitInfos[-1].find(appendix[2]) !=-1:
                    continue
                extraInfo[key] = "%s;%s%s"%(extraInfo[key],secondDate,appendix[2]) #删除

    return dataFrameMerged

def StaticsResult(srcFolder, DestFile, category, fromDay = None, toDay = None, index = ['股票代码'],appendix = ["新增","更新","删除","查询"]):
    files = ListAllTheFolders(srcFolder,category,fromDay=fromDay, toDay=toDay)
    extraInfo = {}
    dataFrames = ReadAllFiles(files,index)
    count = len(dataFrames)
    dataFrameMerged = None
    for i in range(count-1):
        dataFrameMerged = Merge(dataFrames[i],dataFrames[i+1], dataFrameMerged,extraInfo,appendix)
        i = i + 1
    dataFrameMerged["备注"] = None
    for key in extraInfo:
        dataFrameMerged.loc[key,"备注"] = extraInfo[key]
    
    dataFrameMerged.to_excel(DestFile,encoding="utf_8_sig", index=True)


if __name__ == '__main__':
    destFile = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/DD.xlsx'
    category = '20日均线向上并且值大于0.05'
    category1 = '预测均线'
    category2 = '90日新高'
    StaticsResult(srcFolder, destFile,category2)