'''
Created on Apr 15, 2019

@author: mac
'''

stock_Date = u'日期'
stock_ID = u'股票代码'
stock_Name = u'股票简称'
stock_OpenPrice = u'开盘价'
stock_ClosePrice = u'收盘价'
stock_ClosePrice_Yesterday = u'昨日收盘价'
stock_HighPrice = u'最高价'
stock_LowerPrice = u'最低价'
stock_Volumn = u'成交量(股)'
stock_Volumn_Ratio = u'量比' # 0~0.8, 0.8~1.5, 1.5~2.5 2.5~5, 5~10 10~ 
stock_Turnover = u'成交额(元)'
stock_ZhangDieFu = u'涨跌幅(%)'

stock_MA5 = u'5MA'
stock_MA10 = u'10MA'
stock_MA20 = u'20MA'
stock_MA30 = u'30MA'
stock_MA60 = u'60MA'
stock_MA120 = u'120MA'
stock_MA240 = u'240MA'

stock_MA5_ACC = u'5MA'
stock_MA10 = u'10MA'
stock_MA20 = u'20MA'
stock_MA30 = u'30MA'
stock_MA60 = u'60MA'
stock_MA120 = u'120MA'
stock_MA240 = u'240MA'

stock_MACD = u'MACD'

stock_BOLLUp = u'BOLL上轨'
stock_BOLLMid = u'BOLL中轨'
stock_BOLLDown = u'BOLL下轨'
stock_BOLL_Percent = u'BOLL百分比'
stock_BOLL_Band_width = u'BOLL带宽'
stock_CLOSE_TO_BOLLUP = u'到BOLL上轨'
stock_CLOSE_TO_BOLLDOWN = u'到BOLL下轨'
stock_CLOSE_TO_BOLLMID = u'到BOLL中轨'
stock_CLOSE_TO_BOLL_DOWN_TO_UP = u'BOLL上下轨百分比'

stock_DISTANCE_MA_SHORT = u'短线均线乖离度' #MA5, MA10, MA20
stock_DISTANCE_MA_MID = u'中线均线乖离度' #MA5, MA10,MA20,MA60
stock_DISTANCE_MA_LONG = u'长线均线乖离度' #MA5,MA10,MA20,MA60,MA120,MA240

stock_RSI_6 = u'rsi6值'
stock_RSI_12 = u'rsi12值'
stock_RSI_24 = u'rsi24值'

stock_GaiNian = u'所属概念'    
stock_ShiZhi = u'a股流通市值'

stock_HangYe = u'所属行业'
stock_Days = u'上市天数'
stock_XinTai = u'技术形态'

stock_DistanceMA5 = u'股价距离5日线距离' 
stock_DistanceMA10 = u'股价距离10日线距离'
stock_DistanceMA20 = u'股价距离月线距离' #乖离率
stock_DistanceMA30 = u'股价距离30日线距离' 
stock_DistanceMA60 = u'股价距离季线距离' 
stock_DistanceMA120 = u'股价距离半年线距离'
stock_DistanceMA240 = u'股价距离年线距离'


STOCK_TABLE_INDEX = [
    stock_OpenPrice,
    stock_ClosePrice,
    stock_ClosePrice_Yesterday,
    stock_HighPrice,
    stock_LowerPrice,
    stock_Volumn,
    stock_Turnover,
    stock_Volumn_Ratio,
    stock_ZhangDieFu,

    stock_MA5,
    stock_MA10,
    stock_MA20,
    stock_MA30,
    stock_MA60,
    stock_MA120,
    stock_MA240,

    stock_MACD,
    stock_BOLLUp,
    stock_BOLLMid,
    stock_BOLLDown,
    stock_BOLL_Percent,
    stock_BOLL_Band_width,
    stock_CLOSE_TO_BOLLUP,
    stock_CLOSE_TO_BOLLDOWN,
    stock_CLOSE_TO_BOLLMID,

    stock_CLOSE_TO_BOLL_DOWN_TO_UP,
    stock_DISTANCE_MA_SHORT,
    stock_DISTANCE_MA_MID,
    stock_DISTANCE_MA_LONG,
    stock_RSI_6,
    stock_RSI_12,
    stock_RSI_24,

    stock_ShiZhi,
    stock_HangYe,
    stock_GaiNian,
    
    stock_Days,
    stock_XinTai,
    stock_DistanceMA5,
    stock_DistanceMA10,
    stock_DistanceMA20,
    stock_DistanceMA30,
    stock_DistanceMA60,
    stock_DistanceMA120,
    stock_DistanceMA240
]

class CSimpleFilterBase(object):
    def __init__(self, params = None):
        self.filterName = None
        self.filterDescribe = None
        self.filterResult = {}
        self.callStack = []
        
    def Filter(self, dataFrame, nextFilter = None):
        res = self.FilterCurrentOnly(dataFrame)
        self.filterResult['Result'] = res
        self.callStack.append(self.filterResult)
        if res == False or res == None:
            return False

        returnFlag,result = self.FilterNext(dataFrame,nextFilter)
        self.callStack.extend(result)
        return returnFlag

    
    def FilterCurrentOnly(self, dataFrame):
        return False

    def FilterNext(self, dataFrame, nextFilter = None):
        if dataFrame is None :
            raise Exception('FilterNext dataFrame is None')
        
        if nextFilter is None:
            return (True,[])
        
        if isinstance(nextFilter,(list, tuple)) == False:
            raise Exception('nextFilter should be a list or tuple!')

        nextFiltersize = len(nextFilter)
        if nextFiltersize == 0:
            return (True,[])

        next = nextFilter[0]
        res = next.FilterCurrentOnly(dataFrame)
        next.filterResult['Result'] = res
        next.callStack.append(next.filterResult)
        if res == False:
            return (False,next.callStack)
        else:
            if nextFiltersize == 1:
                return (True, next.callStack)
            else:
                nextParameter = nextFilter[1:]
                returnFlag,result = next.FilterNext(dataFrame,nextParameter)
                next.callStack.append(result)
                return( returnFlag, next.callStack)
