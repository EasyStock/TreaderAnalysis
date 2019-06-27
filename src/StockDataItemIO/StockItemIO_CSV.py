'''
Created on May 3, 2019

@author: mac
'''
import pandas as pd
from StockDataItem.StockItemBase import CStockItemBase
import os

class CStockItemIO_CSV(object):

    def __init__(self):
        self.stocks = None

    def __splictToItems(self, df):
        '''
        格式统一化,
        '''
        datas = df.to_dict('index')
        keys = datas.keys()
        stocks = []
        for key in keys:
            data = datas[key]
            stock = CStockItemBase()
            stock.initWithDict(data)
            stocks.append(stock)
        self.stocks = stocks
        return stocks

    def __formatResultToDataFrame(self, stocks):
        stockList = [t.formatToDict() for t in stocks]
        columns = stocks[0].getColunmInfo()
        d = pd.DataFrame(stockList,columns=columns)
        return d

    def __saveToCSV(self,fileName, stocks):
        df = self.__formatResultToDataFrame(stocks)
        df.to_csv(fileName,encoding="utf_8_sig", index=False)

    def __saveToExcel(self, fileName, stocks):
        df = self.__formatResultToDataFrame(stocks)
        df.to_excel(fileName,encoding="utf_8_sig", index=False)
        
    def ReadFromCSV(self,fileName):
        df = pd.read_csv(fileName, index_col = None, encoding='utf_8_sig')
        self.__splictToItems(df)
    
    
    def SaveTo(self, fileName):
        return  self.SaveToWithStocks(fileName, self.stocks)

    def SaveToWithStocks(self,fileName, stocks):
        ext = fileName[fileName.rfind('.')+1:]
        path = fileName[:fileName.rfind('/')+1]
        if not os.path.exists(path):
            os.makedirs(path)
        if ext == 'csv':
            self.__saveToCSV(fileName, stocks) 
        elif ext == 'xlsx' or ext == 'xls':
            self.__saveToExcel(fileName, stocks)
            
    
if __name__ == '__main__':
    fileName = u'/Volumes/Data/Downloads/2019-05-02_x.csv'
    destFileName = u'/Volumes/Data/Downloads/2019-05-02_x.xlsx'
    stockCSV = CStockItemIO_CSV()
    stockCSV.ReadFromCSV(fileName)