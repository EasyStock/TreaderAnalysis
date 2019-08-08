'''
Created on Aug 8, 2019

@author: mac
'''
from CombinedFilter.CombinedFilter_BOLL_Volumn import CCombinedFilter_BOLL_Volumn
from PathManager.StockPathManager import GetMergedFolder,\
    GetOutDataFolder, GetCombinedFilterFolder

def CombinedFilter_BOLL_Volumn():
    combine = CCombinedFilter_BOLL_Volumn()
    srcFolder = GetMergedFolder()
    folder_dest = GetCombinedFilterFolder()
    threholdFile = '%s/threshold.xlsx'%(GetOutDataFolder())
    combine.Filter(srcFolder, folder_dest, threholdFile)
    
    
if __name__ == '__main__':
    CombinedFilter_BOLL_Volumn()