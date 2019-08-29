'''
Created on May 3, 2019

@author: mac
'''

from collections import OrderedDict
from IndexDataItem.IndexItemDef import *

class CIndexItemTemplate(object):
    def __init__(self):
        self.indexInfo = OrderedDict()
        self.indexInfo[index_ID] = None
        self.indexInfo[index_Name] = None
        self.indexInfo[index_OpenPrice] = None
        self.indexInfo[index_ClosePrice] = None
        self.indexInfo[index_ClosePrice_Yesterday] = None
        self.indexInfo[index_HighPrice] = None
        self.indexInfo[index_LowerPrice] = None
        self.indexInfo[index_Volumn] = None
        self.indexInfo[index_Turnover] = None
        self.indexInfo[index_Volumn_Ratio] = None
        self.indexInfo[index_ZhangDieFu] = None

        self.indexInfo[index_MA5] = None
        self.indexInfo[index_MA10] = None
        self.indexInfo[index_MA20] = None
        self.indexInfo[index_MA30] = None
        self.indexInfo[index_MA60] = None
        self.indexInfo[index_MA120] = None
        self.indexInfo[index_MA240] = None

        #indexs
        # 1. MACD
        self.indexInfo[index_MACD] = None
        
        #2. BOLL
        self.indexInfo[index_BOLLUp] = None
        self.indexInfo[index_BOLLMid] = None
        self.indexInfo[index_BOLLDown] = None
        self.indexInfo[index_BOLL_Percent] = None
        self.indexInfo[index_BOLL_Band_width] = None
        self.indexInfo[index_CLOSE_TO_BOLLUP] = None
        self.indexInfo[index_CLOSE_TO_BOLLMID] = None
        self.indexInfo[index_CLOSE_TO_BOLLDOWN] = None
        self.indexInfo[index_CLOSE_TO_BOLL_DOWN_TO_UP] = None
        self.indexInfo[index_DISTANCE_MA_SHORT] = None
        self.indexInfo[index_DISTANCE_MA_MID] = None
        self.indexInfo[index_DISTANCE_MA_LONG] = None

#         # 3.RSI
        self.indexInfo[index_RSI_6] = None
        self.indexInfo[index_RSI_12] = None
        self.indexInfo[index_RSI_24] = None
        
        self.indexInfo[index_Type] = None
        
    def __str__(self):
        return self.indexInfo.__str__()


if __name__ == '__main__':
    '''
    板块指数,开盘价,收盘价,最高价,最低价,成交量,成交额,量比,涨跌幅,5日均线, 10日均线,20日均线,30日均线,60日均线,120日均线,240日均线,macd, boll(upper)值,boll(mid)值,boll(lower)值,RSI(6),RSI(12),RSI(24),昨日收盘价
    '''
    t = CIndexItemTemplate()
    print(t)