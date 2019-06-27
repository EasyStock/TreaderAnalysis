'''
Created on May 3, 2019

@author: mac
'''

from collections import OrderedDict
from StockDataItem.StockItemDef import *
    
class CStockItemTemplate(object):
    def __init__(self):
        self.stockInfo = OrderedDict()
        self.stockInfo[stock_ID] = None
        self.stockInfo[stock_Name] = None
        self.stockInfo[stock_OpenPrice] = None
        self.stockInfo[stock_ClosePrice] = None
        self.stockInfo[stock_ClosePrice_Yesterday] = None
        self.stockInfo[stock_HighPrice] = None
        self.stockInfo[stock_LowerPrice] = None
        self.stockInfo[stock_Volumn] = None
        self.stockInfo[stock_Turnover] = None
        self.stockInfo[stock_Volumn_Ratio] = None
        self.stockInfo[stock_ZhangDieFu] = None

        self.stockInfo[stock_MA5] = None
        self.stockInfo[stock_MA10] = None
        self.stockInfo[stock_MA20] = None
        self.stockInfo[stock_MA30] = None
        self.stockInfo[stock_MA60] = None
        self.stockInfo[stock_MA120] = None
        self.stockInfo[stock_MA240] = None

        #indexs
        # 1. MACD
        self.stockInfo[stock_MACD] = None
        
        #2. BOLL
        self.stockInfo[stock_BOLLUp] = None
        self.stockInfo[stock_BOLLMid] = None
        self.stockInfo[stock_BOLLDown] = None
        self.stockInfo[stock_BOLL_Percent] = None
        self.stockInfo[stock_BOLL_Band_width] = None
        self.stockInfo[stock_CLOSE_TO_BOLLUP] = None
        self.stockInfo[stock_CLOSE_TO_BOLLMID] = None
        self.stockInfo[stock_CLOSE_TO_BOLLDOWN] = None
        self.stockInfo[stock_CLOSE_TO_BOLL_DOWN_TO_UP] = None
        self.stockInfo[stock_DISTANCE_MA_SHORT] = None
        self.stockInfo[stock_DISTANCE_MA_MID] = None
        self.stockInfo[stock_DISTANCE_MA_LONG] = None

#         # 3.RSI
        self.stockInfo[stock_RSI_6] = None
        self.stockInfo[stock_RSI_12] = None
        self.stockInfo[stock_RSI_24] = None
        
        #info
        self.stockInfo[stock_ShiZhi] = None
        self.stockInfo[stock_HangYe] = None
        self.stockInfo[stock_GaiNian] = None
        self.stockInfo[stock_Days] = None
        self.stockInfo[stock_XinTai] = None
        
    def __str__(self):
        return self.stockInfo.__str__()
    

if __name__ == '__main__':
    '''
    开盘价,收盘价,最高价,最低价,成交量,成交额,量比,涨跌幅,5日均线, 10日均线,20日均线,30日均线,60日均线,120日均线,240日均线,macd, boll(upper)值,boll(mid)值,boll(lower)值,RSI(6),RSI(12),RSI(24),a股流通市值,行业，概念,上市天数,技术形态,昨日收盘价
    '''
    t = CStockItemTemplate()
    print(t)