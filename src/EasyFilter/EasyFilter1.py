'''
Created on Jun 27, 2019

@author: mac
'''
from EasyFilter.IEasyFilterBase import IEasyFilterBase

class EasyFilter1(IEasyFilterBase):
    def __init__(self):
        IEasyFilterBase.__init__(self)
        self.FilterDescribe = 'EasyFilter1'
        self.FilterDescribe = '''
        选股条件:
            1. 股价 > MA60
            2. 股价 > MA5
            3. 股价 > MA20
            4. 三线(MA5, MA10, MA20)纠结, 纠结系数<0.01
            
            输出:
            1. 过滤器名称
            2. 股票名称
            3. BOLL线开合信息
            4. 红三兵信息
        '''
    def Filter(self):
        pass