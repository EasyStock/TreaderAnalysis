'''
Created on Aug 8, 2019

@author: mac
'''
from StockFilter.FilterMgr.StockAdvanceFilterMgrEx import CStockAdvanceFilterMgrEx,\
    K_ADVANCE_FILTER_EX_BOLL_WIDTH
import os
from StockFilter.AdvanceFilter.StockAdvanceFilter_Big_Volumn import CAdvanceFilter_BigVolumn
from StockDataItem.StockItemDef import stock_ID
import pandas as pd
from datetime import date

class CCombinedFilter_BOLL_Volumn(object):
    '''
    BOLL开口，低点放大量
    '''
    def __init__(self):
        pass
    
    def Filter(self,srcFolder, outFolder, threholdFile):
        ret = []
        filenames=os.listdir(srcFolder)
        advanceMgr = CStockAdvanceFilterMgrEx()
        advanceMgr.ReadThreshold(threholdFile)
        for xlsxFile in filenames:
            res = {}
            if xlsxFile.find('.xlsx') == -1:
                continue
            stockID = xlsxFile[:xlsxFile.rfind('.')]
            srcFileName = os.path.join(srcFolder,xlsxFile)
            df = advanceMgr.ReadSrcFile(srcFileName)
            res1 = advanceMgr.FilterFile(stockID, srcFileName, K_ADVANCE_FILTER_EX_BOLL_WIDTH)
            if res1[0]:
                bigVolumn = CAdvanceFilter_BigVolumn(40, 3)
                res2 = bigVolumn.FilterBy(df)
                if res2[0]:
                    res[stock_ID] = stockID
                    res.update(res1[1])
                    res.update(res2[1])
                    ret.append(res)
                    print(stockID, srcFileName)

        if len(ret) > 0:
            df = pd.DataFrame(ret)
            fileName = u'%s/BOLL开口_底部爆大量过滤_%s.xlsx' %(outFolder,date.today())
            df.to_excel(fileName,encoding="utf_8_sig", index=False)
        
        