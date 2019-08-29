'''
Created on May 3, 2019

@author: mac
'''
import pandas as pd
from IndexDataItem.IndexItemBase import CIndexItemBase
import os

class CIndexItemIO_CSV(object):

    def __init__(self):
        self.indexs = None

    def __splictToItems(self, df):
        '''
        格式统一化,
        '''
        datas = df.to_dict('index')
        keys = datas.keys()
        indexs = []
        for key in keys:
            data = datas[key]
            index = CIndexItemBase()
            index.initWithDict(data)
            indexs.append(index)
        self.indexs = indexs
        return indexs

    def __formatResultToDataFrame(self, indexs):
        indexList = [t.formatToDict() for t in indexs]
        columns = indexs[0].getColunmInfo()
        d = pd.DataFrame(indexList,columns=columns)
        return d

    def __saveToCSV(self,fileName, indexs):
        df = self.__formatResultToDataFrame(indexs)
        df.to_csv(fileName,encoding="utf_8_sig", index=False)

    def __saveToExcel(self, fileName, indexs):
        df = self.__formatResultToDataFrame(indexs)
        df.to_excel(fileName,encoding="utf_8_sig", index=False)
        
    def ReadFromCSV(self,fileName):
        df = pd.read_csv(fileName, index_col = None, encoding='utf_8_sig')
        self.__splictToItems(df)
    
    
    def SaveTo(self, fileName):
        return  self.SaveToWithindexs(fileName, self.indexs)

    def SaveToWithindexs(self,fileName, indexs):
        ext = fileName[fileName.rfind('.')+1:]
        path = fileName[:fileName.rfind('/')+1]
        if not os.path.exists(path):
            os.makedirs(path)
        if ext == 'csv':
            self.__saveToCSV(fileName, indexs) 
        elif ext == 'xlsx' or ext == 'xls':
            self.__saveToExcel(fileName, indexs)
            
    
if __name__ == '__main__':
    fileName = u'/Volumes/Data/Downloads/2019-05-02_x.csv'
    destFileName = u'/Volumes/Data/Downloads/2019-05-02_x.xlsx'
    indexCSV = CIndexItemIO_CSV()
    indexCSV.ReadFromCSV(fileName)