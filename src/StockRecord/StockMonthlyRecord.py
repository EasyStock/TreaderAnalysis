'''
 Created on Wed Jan 01 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''


from .StockDailyRecord import CStockDailyRecord

class CStockMonthlyRecord(object):
    def __init__(self):
        self.records = []
        self.month = None
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