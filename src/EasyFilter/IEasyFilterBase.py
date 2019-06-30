'''
Created on Jun 27, 2019

@author: mac
'''
from PathManager.StockPathManager import GetDailyDataFolder, GetMergedFolder

class IEasyFilterBase(object):
    def __init__(self):
        self.filterName = None
        self.FilterDescribe = None
        self.dailyFolder = GetDailyDataFolder()
        self.mergeFolder = GetMergedFolder()
        
    def Filter(self):
        return False

if __name__ == '__main__':
    base = IEasyFilterBase()
    print(base.filterName)