'''
Created on Jun 14, 2019

@author: mac
'''
import pandas as pd
from StockDataItem.StockChuQuanXiItem import stock_ChuQuanXi_ID,\
    stock_ChuQuanXi_NoticeDay, stock_ChuQuanXi_EXE_Day, stock_ChuQuanXi_Detail,\
    stock_ChuQuanXi_ZhangDieFu, stock_ChuQuanXi_Day, stock_ChuQuanXi_Price,\
    stock_ChuQuanXi_Name, CStockChuQuanXiTemplate, stock_ChuQuanXi_FenHong,\
    stock_ChuQuanXi_HongLiLv

class CStockChuQuanXiItemIO(object):
    def __init__(self):
        self.stocks = None
        
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
        stocks = []
        for _, row in df.iterrows():
            stock = self.__formatToStockItem(row)
            stocks.append(stock)
        self.stocks = stocks
        return stocks

    def __formatResultToDataFrame(self, stocks):
        stockList = [t.formatToDict() for t in stocks]
        columns = stocks[0].getColunmInfo()
        d = pd.DataFrame(stockList,columns=columns)
        return d
    
    def __SplictFenHong(self,_dict):
        if stock_ChuQuanXi_Detail not in _dict:
            _dict[stock_ChuQuanXi_FenHong] = 0
            return
        rawData = _dict[stock_ChuQuanXi_Detail]
        if rawData == u'不分配不转增':
            _dict[stock_ChuQuanXi_FenHong] = 0
            return
        elif rawData == u'--':
            _dict[stock_ChuQuanXi_FenHong] = 0
            return
        else:
            try:
                if rawData.find('元') != -1:
                    fenHong = float(rawData[rawData.find('派')+1:rawData.find('元')])
                    _dict[stock_ChuQuanXi_FenHong] = fenHong
                    return
                else:
                    _dict[stock_ChuQuanXi_FenHong] = 0
            except Exception as e:
                print(rawData)
                raise e
            
    def __CalcFenHongRatio(self,_dict):
        if stock_ChuQuanXi_FenHong not in _dict:
            _dict[stock_ChuQuanXi_HongLiLv] = 0
            return
        
        if stock_ChuQuanXi_Price not in _dict:
            _dict[stock_ChuQuanXi_HongLiLv] = 0
            return
        
        try:
            price = float(_dict[stock_ChuQuanXi_Price])
            fenhong = _dict[stock_ChuQuanXi_FenHong]
            ratio = fenhong/ price  * 10
            _dict[stock_ChuQuanXi_HongLiLv] = ratio
            return
        except Exception as e:
            _dict[stock_ChuQuanXi_HongLiLv] = 0
        
        
    def __formatToStockItem(self, row_item):
        '''
        格式统一化
        '''
        item_info = {}
        item_info[stock_ChuQuanXi_ID] = row_item[0]
        item_info[stock_ChuQuanXi_Name] = row_item[1]
        try:
            item_info[stock_ChuQuanXi_Price] = float(row_item[2])
        except:
            item_info[stock_ChuQuanXi_Price] = row_item[2]

        item_info[stock_ChuQuanXi_ZhangDieFu] = row_item[3]
        item_info[stock_ChuQuanXi_Day] = row_item[4]
        item_info[stock_ChuQuanXi_Detail] = row_item[5]
        item_info[stock_ChuQuanXi_EXE_Day] = row_item[6]
        item_info[stock_ChuQuanXi_NoticeDay] = row_item[7]
        self.__SplictFenHong(item_info)
        self.__CalcFenHongRatio(item_info)
        
        item = CStockChuQuanXiTemplate()
        item.initWithDict(item_info)
        
        return item
    
    def ReadFrom(self, fileName):
        df = self.__readfromHTM(fileName)
        self.__splictToItems(df)

    def __saveToExcel(self, fileName, stocks):
        df = self.__formatResultToDataFrame(stocks)
        df.to_excel(fileName,encoding="utf_8_sig", index=False)
      
    def SaveTo(self, fileName):
        return self.__saveToExcel(fileName, self.stocks)
    
if __name__ == '__main__':
    fileName = u'/Volumes/Data/Downloads/aa.xls'
    fileName1 = u'/Volumes/Data/Downloads/bb.xlsx'
    io = CStockChuQuanXiItemIO()
    io.ReadFrom(fileName)
    io.SaveTo(fileName1)
    stocks = io.stocks
#     for stock in stocks:
#         print(stock)