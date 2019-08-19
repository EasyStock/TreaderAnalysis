'''
Created on Jun 10, 2019

@author: mac
'''

from StockFilter.AdvanceFilter.AdvanceFilterBase import IAdvanceFilterBase
from StockDataItem.StockItemDef import stock_Days, stock_Date,\
    stock_BOLL_Band_width, stock_Name, stock_ZhangDieFu, stock_BOLLMid, stock_CLOSE_TO_BOLLMID,\
    stock_CLOSE_TO_BOLLUP

class CAdvanceFilter_BOLL_WIDTH(IAdvanceFilterBase):

    def __init__(self,threshold = None):
        '''
        params threshold_min
        '''
        IAdvanceFilterBase.__init__(self,None)
        self.filterName = u'BOLL带宽'
        self.FilterDescribe = u'BOLL带宽连续2天 带宽变大'
        self.threshold = threshold
        
    def _validateData(self, df):
        try:
            day = float(df.iloc[-1][stock_Days])
            if day < 250:
                return False
        except:
            pass

        try:
            float(df.iloc[-3][stock_BOLL_Band_width])
        except:
            return False
    
        return True
    
    def _Case1(self,df):
        '''
        BOll带宽开始转折，股价站上中轨
        '''
        last1 = float(df.iloc[-1][stock_BOLL_Band_width])
        last2 = float(df.iloc[-2][stock_BOLL_Band_width])
        last3 = float(df.iloc[-3][stock_BOLL_Band_width])
        lastPriceToMid = float(df.iloc[-1][stock_CLOSE_TO_BOLLMID])
        if last2< last3 and last1 >= last2 and lastPriceToMid < 0:
            return True
        
        return False
    
    def _Case2(self,df):
        '''
        BOLL开口了，股价在中轨之上
        '''
        last1 = float(df.iloc[-1][stock_BOLL_Band_width])
        last2 = float(df.iloc[-2][stock_BOLL_Band_width])
        last3 = float(df.iloc[-3][stock_BOLL_Band_width])
        lastPriceToMid = float(df.iloc[-1][stock_CLOSE_TO_BOLLMID])
        if last1 >= last2 >= last3 and lastPriceToMid < 0:
            return True
        
        return False  
        

    def _calcFlag(self,df):
        l1 = float(df.iloc[-1][stock_BOLLMid])
        l2 = float(df.iloc[-2][stock_BOLLMid])
        flag = 'UnKnown'
        if l1 > l2:
            flag = 'UP'
        elif l1 < l2:
            flag = 'DOWN'
        
        return flag
    
    def _validateParam(self,df):
        if self.threshold == None:
            self.threshold = 15.3 #2倍标准差区间1.6 ~ 15.3
        elif self.threshold > 15.3:
            self.threshold = 15.3
        elif self.threshold < 1.6:
            self.threshold = 1.6

        last1 = float(df.iloc[-1][stock_BOLL_Band_width])
        last2 = float(df.iloc[-2][stock_BOLL_Band_width])
        last3 = float(df.iloc[-3][stock_BOLL_Band_width])

        if last1 > self.threshold and last2 > self.threshold and last3 > self.threshold:
            return False
        
        return True
            
    def FilterBy(self, df):
        if not self._validateData(df):
            return (False,)
        
        if not self._validateParam(df):
            return (False,)
        
        caseFlag = "case1"
        if not self._Case1(df):
            if not self._Case2(df):
                return (False,)
            else:
                caseFlag = "case2"
            


        flag = self._calcFlag(df)
        ret = {}
        ret["0日期"] = df.iloc[-1][stock_Date]
        ret["1股票简称"] = df.iloc[-1][stock_Name]
        ret[self.filterName] = "YES"
        ret["BOLL方向"] = flag
        ret["最后一天涨幅"] = float(df.iloc[-1][stock_ZhangDieFu])
        ret['BOLL带宽阈值'] = self.threshold
        ret["Case"] = caseFlag
        ret['到中轨的距离'] = float(df.iloc[-1][stock_CLOSE_TO_BOLLMID])
        ret['到上轨的距离'] = float(df.iloc[-1][stock_CLOSE_TO_BOLLUP])
        return (True,ret)

    
if __name__ == '__main__':
    pass