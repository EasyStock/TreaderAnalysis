'''
Created on Jun 14, 2019

@author: mac
'''
from collections import OrderedDict

stock_ChuQuanXi_ID = u'股票代码'
stock_ChuQuanXi_Name = u'股票简称'
stock_ChuQuanXi_Price = u'现价(元)'
stock_ChuQuanXi_Day = u'除权除息日'
stock_ChuQuanXi_ZhangDieFu = u'涨跌幅(%)'
stock_ChuQuanXi_Detail = u'分红明细'
stock_ChuQuanXi_EXE_Day = u'分红实施公告日'
stock_ChuQuanXi_NoticeDay = u'预案公告日'
stock_ChuQuanXi_FenHong = u'分红'
stock_ChuQuanXi_HongLiLv = u'现金红利率'

class CStockChuQuanXiTemplate(object):
    def __init__(self):
        self.stockInfo = OrderedDict()
        self.stockInfo[stock_ChuQuanXi_ID] = None
        self.stockInfo[stock_ChuQuanXi_Name] = None
        self.stockInfo[stock_ChuQuanXi_Price] = None
        self.stockInfo[stock_ChuQuanXi_Day] = None
        self.stockInfo[stock_ChuQuanXi_ZhangDieFu] = None
        self.stockInfo[stock_ChuQuanXi_Detail] = None
        self.stockInfo[stock_ChuQuanXi_EXE_Day] = None
        self.stockInfo[stock_ChuQuanXi_NoticeDay] = None
        self.stockInfo[stock_ChuQuanXi_FenHong] = None
        self.stockInfo[stock_ChuQuanXi_HongLiLv] = None

    def initWithDict(self,dict_):
        for key in dict_:
            self.stockInfo[key] = dict_[key]
            
    def formatToDict(self):
        return self.stockInfo

    def getColunmInfo(self):
        return self.stockInfo.keys()
    
    def __str__(self):
        return self.stockInfo.__str__()

if __name__ == '__main__':
    pass
    