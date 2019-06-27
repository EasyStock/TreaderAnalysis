'''
Created on Apr 15, 2019

@author: mac
'''

class IAdvanceFilterBase(object):
    def __init__(self, params):
        self.filterName = None
        self.FilterDescribe = None
    
    def ValidateData(self, df):
        raise Exception("IAdvanceFilterBase ValidateData failed!")

    def FilterBy(self, df):
        return (False,)
        
        