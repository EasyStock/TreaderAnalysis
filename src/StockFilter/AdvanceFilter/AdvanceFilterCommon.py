'''
Created on Apr 15, 2019

@author: mac
'''
from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_ZhangDieFu, stock_Name,\
    stock_ClosePrice_Yesterday, stock_OpenPrice, stock_ShiZhi, stock_RSI_6,\
    stock_ClosePrice, stock_Date, stock_HighPrice, stock_LowerPrice, stock_Days,\
    stock_MA5, stock_MA20, stock_MA10

class AdvanceFilterCommon(IAdvanceFilterBase):
    def __init__(self):
        IAdvanceFilterBase.__init__(self, None)
    
    
    def HasZhangTing(self,df, percentage, N):
        ret = {}
        key = '最近%s天大于%s天数'%(N,percentage)
        aa = (df.ix[-N:][stock_ZhangDieFu] > percentage)
        t = df.loc[aa]
        ret[key] = t.shape[0]
        return ret

    def isST(self,df):
        if df.iloc[-1][stock_Name].find("ST") != -1:
            #msg = '股票名称:%s 是否是ST: 是' % (df.iloc[-1][stock_Name])
            #print(msg)
            return True
        else:
            return False
    
    def isOpenLowerThanYesterdayClose(self,df):
        res = {}
        key = "是否低开"
        if float(df.iloc[-1][stock_OpenPrice]) < float(df.iloc[-1][stock_ClosePrice_Yesterday]):
            res[key] = "是"
        else:
            res[key] = "否"
        return res

    def isPositive(self,df):
        res = {}
        key = "是否阳线"
        if float(df.iloc[-1][stock_OpenPrice]) < float(df.iloc[-1][stock_ClosePrice]):
            res[key] = "是"
        else:
            res[key] = "否"
        return res

    def isGreaterThan5MA(self,df):
        res = {}
        key = "是否大于MA5"
        if float(df.iloc[-1][stock_ClosePrice]) > float(df.iloc[-1][stock_MA5]):
            res[key] = "是"
        else:
            res[key] = "否"
        return res

    def isGreaterThan10MA(self,df):
        res = {}
        key = "是否大于MA10"
        if float(df.iloc[-1][stock_ClosePrice]) > float(df.iloc[-1][stock_MA10]):
            res[key] = "是"
        else:
            res[key] = "否"
        return res
    
    def isGreaterThan20MA(self,df):
        res = {}
        key = "是否大于中轨"
        if float(df.iloc[-1][stock_ClosePrice]) > float(df.iloc[-1][stock_MA20]):
            res[key] = "是"
        else:
            res[key] = "否"
        return res
    
    def shiZhi(self,df):
        res = {}
        key = "流通市值(亿)"
        shizhi = float(df.iloc[-1][stock_ShiZhi])/100000000
        res[key] = int(shizhi)
        return res
         

    def RSI(self,df):
        index_Rsi6 = df[stock_RSI_6].idxmin()
        min_row_rsi6= df.loc[index_Rsi6]
        index_closePrice = df[stock_ClosePrice].idxmin()
        min_row_closePrice = df.loc[index_closePrice]
        
        ret = {}
        ret['RSI6最低日'] = min_row_rsi6[stock_Date]
        ret['RSI6最低值'] = min_row_rsi6[stock_RSI_6]
        ret['收盘价与RSI背离'] = (min_row_rsi6[stock_Date] != min_row_closePrice[stock_Date])
        ret['最低收盘价日期'] = min_row_closePrice[stock_Date]
        ret['最低收盘价'] = min_row_closePrice[stock_ClosePrice]
        return ret
    
    def KBody(self,df):
        ret = {}
        date = df.iloc[-1][stock_Date]
        close1 = float(df.iloc[-1][stock_ClosePrice])
        open1 = float(df.iloc[-1][stock_OpenPrice])
        high1 = float(df.iloc[-1][stock_HighPrice])
        low1 = float(df.iloc[-1][stock_LowerPrice])
        close_yesterday = float(df.iloc[-1][stock_ClosePrice_Yesterday])
        ret["%s_收盘价"%(date)] = close1
        ret["%s_K线实体"%(date)] = abs((close1 -  open1))/close_yesterday*100
        ret["%s_K线上影线"%(date)] = (high1 - max(close1, open1)) / close_yesterday *100
        ret["%s_K线下影线"%(date)] = (min(close1,open1) - low1) / close_yesterday*100
        return ret
    
    def IsDayGreaterThan(self,df,N):
        try:
            day = float(df.iloc[-1][stock_Days])
            msg = '股票名称:%s 上市天数: %s 小于%s' % (df.iloc[-1][stock_Name],df.iloc[-1][stock_Days],N)
            if day <= N:
                print(msg)
                return False
        except:
            print('股票名称:%s 上市天数: %s' % (df.iloc[-1][stock_Name],df.iloc[-1][stock_Days]))
        
        return True