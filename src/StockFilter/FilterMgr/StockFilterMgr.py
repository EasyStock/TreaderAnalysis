'''
Created on May 6, 2019

@author: mac
'''
from StockDataItemIO.StockItemIO import CStockItemIO

class CStockFilterMgr(object):
    def __init__(self):
        pass
    
    def __filter(self,filter_, stocks):
        res = []
        for stock in stocks:
            if stock.FilterBy(filter_):
                res.append(stock)
        return res
        
    def FilterFile(self, srcFileName, filter_, destFileName):
        io = CStockItemIO()
        io.readFrom(srcFileName)
        stocks = io.stocks
        res = []
        for stock in stocks:
            if stock.FilterBy(filter_):
                res.append(stock)
                print(stock)
        if len(res) == 0:
            print('not filter result!')
            return

        io.SaveToWithStocks(destFileName, res)
    
    def FilterFileByFilters(self,srcFileName, filters, destFileName):
        io = CStockItemIO()
        io.readFrom(srcFileName)
        stocks = io.stocks
        for filter_ in filters:
            stocks = self.__filter(filter_, stocks)

        if len(stocks) == 0:
            print('not filter result!')
            return
        io.SaveToWithStocks(destFileName, stocks)

    
if __name__ == '__main__':
    pass