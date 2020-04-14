'''
 Created on Wed Jan 01 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''


from .StockQuarterlyRecord import CStockQuarterlyRecord

class CStockYearlyRecord(object):
    def __init__(self):
        self.records = []
        self.year = None
        self.stockID = None
        self.stockName = None
    
    def FromJson(self, jsonStr):
        pass

    def ToJson(self):
        pass


    def FromDict(self,_dict):
        pass


    def ToDict(self):
        pass