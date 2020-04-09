'''
Created on May 3, 2019

@author: mac
'''
from StockDataItem.StockItemT import CStockItemTemplate
from StockDataItem.StockItemDef import stock_GaiNian, stock_XinTai

class CStockItemBase(CStockItemTemplate):

    def __init__(self):
        CStockItemTemplate.__init__(self)
        self.__banKuaiInfo = []
        self.__jishuXinTai = []
        self.__banKuaiExcept = []
    
    def __parseBanKuai(self):
        gaiNian = self.stockInfo[stock_GaiNian]
        self.__banKuaiInfo = []
        if gaiNian:
            words = gaiNian.split(';')
            for word in words:
                if word not in self.__banKuaiExcept:
                    self.__banKuaiInfo.append(word)
    
    def __parseJiShuXinTai(self):
        xinTai = self.stockInfo[stock_XinTai]
        self.__jishuXinTai = []
        if xinTai and isinstance(xinTai,str):
            words = xinTai.split(';')
            self.__jishuXinTai.extend(words)
                    
    def getColunmInfo(self):
        return self.stockInfo.keys()
    
    def formatToDict(self):
        return self.stockInfo
    
    def getStockInfo(self):
        return self.stockInfo
     
    def FilterBy(self, stockFilter):
        if stockFilter:
            return stockFilter.FilterBy(self)
        else:
            return False
        
    def initWithDict(self,dict_):
        for key in dict_:
            self.stockInfo[key] = dict_[key]
        
        self.validate()
        self.__parseBanKuai()
        self.__parseJiShuXinTai()
            
    def validate(self):
        keys = self.stockInfo.keys()
        for key in keys:
            if self.stockInfo[key] == None:
                msg = 'Key:%s, not set!'%(key)
                raise Exception(msg)
    
    def getBanKuai(self):
        return self.__banKuaiInfo
     
    def isKeyInBanKuai(self, key):
        gaiNian = self.stockInfo[stock_GaiNian]
        if gaiNian.find(key) != -1:
            return True
        else:
            return False
     
    def isAllKeysInBanKuai(self, keys):
        for key in keys:
            if not self.isKeyInBanKuai(key):
                return False
        return True
    
    def isOneKeyInBanKuai(self, keys):
        for key in keys:
            if self.isKeyInBanKuai(key):
                return True
        return False
    