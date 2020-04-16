'''
Created on Apr 15, 2019

@author: mac
'''
from . import SimpleFilterBase

class CSimpleFilter_ZhangDieFu(SimpleFilterBase.CSimpleFilterBase):
    def __init__(self, params):
        if isinstance(params, (list,tuple)) == False:
            raise Exception('CSimpleFilter_ZhangDieFu paramater error!')
        self.params = params
        SimpleFilterBase.CSimpleFilterBase.__init__(self,None)
        self.filterName = '涨跌幅%.2f-%.2f'%(params[0], params[1])
        self.filterDescribe = '涨跌幅在%.2f-%.2f之间过滤'%(params[0], params[1])
    
    def FilterCurrentOnly(self, dataFrame):
        if dataFrame is None:
            raise Exception('CSimpleFilter_ZhangDieFu dataFrame is None!')

        self.filterResult['111'] = 222
        self.filterResult['FilterName'] = self.filterName
        zhangdieFu = float(dataFrame.iloc[-1][SimpleFilterBase.stock_ZhangDieFu])
        if float(self.params[0])<= zhangdieFu < float(self.params[1]):
            return True
        else:
            return False