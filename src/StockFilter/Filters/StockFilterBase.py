'''
Created on Apr 15, 2019

@author: mac
'''

class IStockFilter(object):
    def __init__(self, params):
        self.filterName = None
        self.FilterDescribe = None
        
    def FilterBy(self, stockInfo):
        return False
        
        