'''
Created on May 3, 2019

@author: mac
'''
import pandas as pd
from IndexDataItem.IndexItemDef import *
from IndexDataItem.IndexItemBase import CIndexItemBase
import os
import numpy as np 
from _operator import index

class CIndexItemIO_HTML(object):

    def __init__(self):
        self.indexs = None
    
    def __readfromHTM(self, fileName):
        dfs = pd.read_html(fileName,encoding='utf-8', header = 0)
        df =dfs[0]
        for index in range(len(df.columns)):
            print(index, df.columns[index])
        return df

    def __splictToItems(self, df):
        '''
        格式统一化,
        '''
        indexs = []
        for _, row in df.iterrows():
            index = self.__formatToIndexItem(row)
            indexs.append(index)
        self.indexs = indexs
        return indexs

    def __formatResultToDataFrame(self, indexs):
        indexList = [t.formatToDict() for t in indexs]
        columns = indexs[0].getColunmInfo()
        d = pd.DataFrame(indexList,columns=columns)
        return d

    def __calcBOLL_Percent(self,_dict):
        if index_ClosePrice not in _dict:
            return

        if index_BOLLUp not in _dict:
            return
        
        if index_BOLLDown not in _dict:
            return
        
        close = _dict[index_ClosePrice]
        bollDown = _dict[index_BOLLDown]
        bollUp = _dict[index_BOLLUp]
        try:
            percentage = (float(close) - float(bollDown)) / (float(bollUp) - float(bollDown))
            _dict[index_BOLL_Percent] = percentage
        except:
            _dict[index_BOLL_Percent] = '--'

    def __calcCloseToBoll(self,_dict):
        if index_ClosePrice not in _dict:
            return

        if index_BOLLUp not in _dict:
            return

        if index_BOLLDown not in _dict:
            return

        if index_BOLLMid not in _dict:
            return

        close = _dict[index_ClosePrice]
        bollDown = _dict[index_BOLLDown]
        bollUp = _dict[index_BOLLUp]
        bollMid = _dict[index_BOLLMid]
        try:
            p1 = (float(bollUp) - float(close) ) / float(close) * 100
            p2 = (float(bollMid) - float(close) ) / float(close) * 100
            p3 = (float(bollDown) - float(close) ) / float(close)* 100
            _dict[index_CLOSE_TO_BOLLUP] = p1
            _dict[index_CLOSE_TO_BOLLMID] = p2
            _dict[index_CLOSE_TO_BOLLDOWN] = p3
        except:
            _dict[index_CLOSE_TO_BOLLUP] = '--'
            _dict[index_CLOSE_TO_BOLLMID] = '--'
            _dict[index_CLOSE_TO_BOLLDOWN] = '--'


    def __calcBOLL_Band_Width(self,_dict):
        if index_BOLLMid not in _dict:
            return

        if index_BOLLUp not in _dict:
            return
        
        if index_BOLLDown not in _dict:
            return
        
        bollMid = _dict[index_BOLLMid]
        bollDown = _dict[index_BOLLDown]
        bollUp = _dict[index_BOLLUp]
        try:
            bandWidth = (float(bollUp) - float(bollDown))/float(bollMid)*100
            _dict[index_BOLL_Band_width] = bandWidth
        except:
            _dict[index_BOLL_Band_width] = '--'
            
    def __calcBOLL_DOWN_TO_UP(self,_dict):
        if index_ClosePrice not in _dict:
            return

        if index_BOLLUp not in _dict:
            return
        
        if index_BOLLDown not in _dict:
            return
        
        close = _dict[index_ClosePrice]
        bollDown = _dict[index_BOLLDown]
        bollUp = _dict[index_BOLLUp]
        try:
            bandWidth = (float(bollUp) - float(bollDown))/float(close)*100
            _dict[index_CLOSE_TO_BOLL_DOWN_TO_UP] = bandWidth
        except:
            _dict[index_CLOSE_TO_BOLL_DOWN_TO_UP] = '--'
    
    def calcDistance(self,v):
        k = [(v[0] - x)/v[0]*100 for x in v]
        return np.var(k)
        
    def __calcDistanceOfMA_Short(self, _dict):
        if index_MA5 not in _dict:
            _dict[index_DISTANCE_MA_SHORT] = '--'
            return

        if index_MA10 not in _dict:
            _dict[index_DISTANCE_MA_SHORT] = '--'
            return
        
        if index_MA20 not in _dict:
            _dict[index_DISTANCE_MA_SHORT] = '--'
            return

        if index_ClosePrice not in _dict:
            _dict[index_DISTANCE_MA_SHORT] = '--'
            return
        try:
            close = float(_dict[index_ClosePrice])
            ma5 = float(_dict[index_MA5])
            ma10 = float(_dict[index_MA10])
            ma20 = float(_dict[index_MA20])
            distance = self.calcDistance((close,ma5, ma10, ma20))
            _dict[index_DISTANCE_MA_SHORT] = distance
        except:
            _dict[index_DISTANCE_MA_SHORT] = '--'

    def __calcDistanceOfMA_Mid(self, _dict):
        if index_MA5 not in _dict:
            _dict[index_DISTANCE_MA_SHORT] = '--'
            return

        if index_MA10 not in _dict:
            _dict[index_DISTANCE_MA_SHORT] = '--'
            return
        
        if index_MA20 not in _dict:
            _dict[index_DISTANCE_MA_SHORT] = '--'
            return
        
        if index_MA60 not in _dict:
            _dict[index_DISTANCE_MA_SHORT] = '--'
            return
        
        if index_ClosePrice not in _dict:
            _dict[index_DISTANCE_MA_SHORT] = '--'
            return
        try:
            close = float(_dict[index_ClosePrice])
            ma5 = float(_dict[index_MA5])
            ma10 = float(_dict[index_MA10])
            ma20 = float(_dict[index_MA20])
            ma60 = float(_dict[index_MA60])
            distance = self.calcDistance((close,ma5, ma10, ma20,ma60))
            _dict[index_DISTANCE_MA_MID] = distance
        except:
            _dict[index_DISTANCE_MA_MID] = '--'
    
    def __calcDistanceOfMa_Long(self,_dict):
        if index_MA5 not in _dict:
            _dict[index_DISTANCE_MA_LONG] = '--'
            return

        if index_MA10 not in _dict:
            _dict[index_DISTANCE_MA_LONG] = '--'
            return
        
        if index_MA20 not in _dict:
            _dict[index_DISTANCE_MA_LONG] = '--'
            return

        if index_ClosePrice not in _dict:
            _dict[index_DISTANCE_MA_LONG] = '--'
            return
        
        try:
            close = float(_dict[index_ClosePrice])
            ma5 = float(_dict[index_MA5])
            ma10 = float(_dict[index_MA10])
            ma20 = float(_dict[index_MA20])
            ma60 = float(_dict[index_MA60])
            ma120 = float(_dict[index_MA120])
            ma240 = float(_dict[index_MA240])
            distance = self.calcDistance((close, ma5, ma10, ma20, ma60, ma120, ma240))
            _dict[index_DISTANCE_MA_LONG] = distance
        except:
            _dict[index_DISTANCE_MA_LONG] = '--'
    
    def __calcGuaiLiRatio(self, ma, price):
        ret = '--'
        try:
            p = float(price)
            m = float(ma)
            ret = (p - m)/ p * 100
        except:
            ret = '--'
        return ret
    
    def __calcAllGaiLiRatio(self,_dict):
        if index_ClosePrice not in _dict:
            _dict[index_DistanceMA5] = '--'
            _dict[index_DistanceMA10] = '--'
            _dict[index_DistanceMA20] = '--'
            _dict[index_DistanceMA60] = '--'
            _dict[index_DistanceMA120] = '--'
            _dict[index_DistanceMA240] = '--'
            return
        
        if index_MA5 not in _dict:
            _dict[index_DistanceMA5] = '--'
            return

        if index_MA10 not in _dict:
            _dict[index_DistanceMA10] = '--'
            return
        
        if index_MA20 not in _dict:
            _dict[index_DistanceMA20] = '--'
            return
        
        if index_MA30 not in _dict:
            _dict[index_DistanceMA30] = '--'
            return

        if index_MA60 not in _dict:
            _dict[index_DistanceMA60] = '--'
            return

        if index_MA120 not in _dict:
            _dict[index_DistanceMA120] = '--'
            return
        
        if index_MA240 not in _dict:
            _dict[index_DistanceMA240] = '--'
            return
        
        r5 = self.__calcGuaiLiRatio(_dict[index_MA5], _dict[index_ClosePrice])
        r10 = self.__calcGuaiLiRatio(_dict[index_MA10], _dict[index_ClosePrice])
        r20 = self.__calcGuaiLiRatio(_dict[index_MA20], _dict[index_ClosePrice])
        r30 = self.__calcGuaiLiRatio(_dict[index_MA30], _dict[index_ClosePrice])
        r60 = self.__calcGuaiLiRatio(_dict[index_MA60], _dict[index_ClosePrice])
        r120 = self.__calcGuaiLiRatio(_dict[index_MA120], _dict[index_ClosePrice])
        r240 = self.__calcGuaiLiRatio(_dict[index_MA240], _dict[index_ClosePrice])
        
        _dict[index_DistanceMA5] = r5
        _dict[index_DistanceMA10] = r10
        _dict[index_DistanceMA20] = r20
        _dict[index_DistanceMA30] = r30
        _dict[index_DistanceMA60] = r60
        _dict[index_DistanceMA120] = r120
        _dict[index_DistanceMA240] = r240
        
        
    def __formatToIndexItem(self, row_item):
        '''
        格式统一化
        '''
        item_info = {}
        item_info[index_ID] = row_item[0]
        item_info[index_Name] = row_item[1]
        item_info[index_ClosePrice] = row_item[2]
        item_info[index_ClosePrice_Yesterday] = row_item[3]
        item_info[index_ZhangDieFu] = row_item[4]
        item_info[index_Type] = row_item[5]
        item_info[index_OpenPrice] = row_item[6]
        item_info[index_HighPrice] = row_item[7]
        item_info[index_LowerPrice] = row_item[8]
        item_info[index_Volumn] = row_item[9]
        item_info[index_Turnover] = row_item[10]
        
        item_info[index_Volumn_Ratio] = row_item[11]
        
        item_info[index_MA5] = row_item[12]
        item_info[index_MA10] = row_item[13]
        item_info[index_MA20] = row_item[14]
        item_info[index_MA30] = row_item[15]
        item_info[index_MA60] = row_item[16]
        item_info[index_MA120] = row_item[17]
        item_info[index_MA240] = row_item[18]
        
        item_info[index_MACD] = row_item[19]
        
        item_info[index_BOLLUp] = row_item[20]
        item_info[index_BOLLMid] = row_item[21]
        item_info[index_BOLLDown] = row_item[22]
        
        item_info[index_RSI_6] = row_item[23]
        item_info[index_RSI_12] = row_item[24]
        item_info[index_RSI_24] = row_item[25]

        self.__calcBOLL_Percent(item_info)
        self.__calcBOLL_Band_Width(item_info)
        self.__calcCloseToBoll(item_info)
        self.__calcBOLL_DOWN_TO_UP(item_info)
        self.__calcDistanceOfMa_Long(item_info)
        self.__calcDistanceOfMA_Short(item_info)
        self.__calcDistanceOfMA_Mid(item_info)
        self.__calcAllGaiLiRatio(item_info)
        
        item = CIndexItemBase()
        item.initWithDict(item_info)
        return item

        
    def ReadFrom(self, fileName):
        df = self.__readfromHTM(fileName)
#         pd.set_option('display.max_columns', None)
#         print(df.head(10))
#         df.to_csv("./a.csv",encoding="utf_8_sig", index=False)
        self.__splictToItems(df)
        
    def __saveToCSV(self,fileName, indexs):
        df = self.__formatResultToDataFrame(indexs)
        df.to_csv(fileName,encoding="utf_8_sig", index=False)

    def __saveToExcel(self, fileName, indexs):
        df = self.__formatResultToDataFrame(indexs)
        df.to_excel(fileName,encoding="utf_8_sig", index=False)
      
      
    def SaveTo(self, fileName):
        return self.SaveToWithIndexs(fileName, self.indexs)
    
    def ReadFromHTMLAndSaveTo(self, srcFileName, destFileName):
        self.ReadFrom(srcFileName)
        self.SaveTo(destFileName)
        
    def SaveToWithIndexs(self,fileName, indexs):
        ext = fileName[fileName.rfind('.')+1:]
        path = fileName[:fileName.rfind('/')+1]
        if not os.path.exists(path):
            os.makedirs(path)
        if ext == 'csv':
            self.__saveToCSV(fileName, indexs) 
        elif ext == 'xlsx' or ext == 'xls':
            self.__saveToExcel(fileName, indexs)


if __name__ == '__main__':
    fileName = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/indexRawData/2019-08-29.xls'
    destFileName = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/indexRawData/2019-08-29.xlsx'
    htmlIO = CIndexItemIO_HTML()
    htmlIO.ReadFromHTMLAndSaveTo(fileName, destFileName)
