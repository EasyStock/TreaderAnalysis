'''
Created on Apr 15, 2019

@author: mac
'''
from . import SimpleFilterBase
import re

STOCK_MARKET_NONE = 'NONE'
STOCK_MARKET_SHANGHAI = '主板'
STOCK_MARKET_ZHONGXIAOBAN= '中小板'
STOCK_MARKET_CHUANGYEBAN = '创业板'
STOCK_MARKET_KECHUANGBAN= '科创板'

class CSimpleFilter_Market(SimpleFilterBase.CSimpleFilterBase):
    def __init__(self, params = None):
        SimpleFilterBase.CSimpleFilterBase.__init__(self,None)
        self.filterName = '交易板块过滤'
        self.filterDescribe = '交易板块过滤'
        self.stockID = params[0]
        self.banKuai = params[1]
        
    def FilterCurrentOnly(self, dataFrame):
        self.filterResult['FilterName'] = self.filterName
        res = STOCK_MARKET_NONE
        if re.search('^60',self.stockID) is not None:
            res = STOCK_MARKET_SHANGHAI
        elif re.search('^30',self.stockID) is not None:
            res = STOCK_MARKET_CHUANGYEBAN
        elif re.search('^00',self.stockID) is not None:
            res = STOCK_MARKET_ZHONGXIAOBAN
        elif re.search('^68',self.stockID) is not None:
            res = STOCK_MARKET_KECHUANGBAN
        else:
            res = STOCK_MARKET_NONE
        
        if isinstance(self.banKuai,(list,tuple)) == True:
            if res in self.banKuai:
                return True
            else:
                return False

        else:
            if self.banKuai == res:
                return True
            else:
                return False

        return False