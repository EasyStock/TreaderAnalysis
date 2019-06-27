'''
Created on Jun 10, 2019

@author: mac
'''
import pandas as pd
import os
from StockDataItem.StockItemDef import stock_ID
from datetime import date


class CAdvanceFilterMgr(object):
    def __init__(self):
        pass
    
    def FilterFile(self, srcFileName, filter_):
        df = pd.read_excel(srcFileName, index_col = None, encoding='utf_8_sig')
        return filter_.FilterBy(df)
            
    def FilterFolder(self,folder,filter_, outFolder):
        filenames=os.listdir(folder)
        ret = []
        for xlsxFile in filenames:
            if xlsxFile.find('.xlsx') == -1:
                continue
            stockID = xlsxFile[:xlsxFile.rfind('.')]
            srcFileName = os.path.join(folder,xlsxFile)
            res = self.FilterFile(srcFileName, filter_)
            if res[0]:
                res[1][stock_ID] = stockID
                ret.append(res[1])
                print(stockID, srcFileName)
        
        if len(ret) > 0:
            df = pd.DataFrame(ret)
            fileName = u'%s/%s_%s.xlsx' %(outFolder, filter_.filterName,date.today())
            df.to_excel(fileName,encoding="utf_8_sig", index=False)
        
    def FilterFileByFilter(self,srcFileName, filters):
        df = pd.read_excel(srcFileName, index_col = None, encoding='utf_8_sig')
        
        res = True
        ret = {}
        for filter_ in filters:
            res = filter_.FilterBy(df)
            if not res[0]:
                res = False
                break
            else:
                ret.update(res[1])
        return (res, ret)
    
    def FilterFileByFilter_Folder(self,folder,filters, outFolder):
        filenames=os.listdir(folder)
        ret = []
        for xlsxFile in filenames:
            if xlsxFile.find('.xlsx') == -1:
                continue
            stockID = xlsxFile[:xlsxFile.rfind('.')]
            srcFileName = os.path.join(folder,xlsxFile)
            res = self.FilterFileByFilter(srcFileName, filters)
            if res[0]:
                res[1]["1股票代码"] = stockID
                ret.append(res[1])
                print(stockID, srcFileName)
        
        filterName = None
        for f in filters:
            if filterName is None:
                filterName = f.filterName
            else:
                filterName = u'%s_%s' %(filterName, f.filterName)
        if len(ret) > 0:
            col = sorted(ret[0].keys())
            print(col)
            df = pd.DataFrame(ret,columns=col)
            fileName = u'%s/%s_%s.xlsx' %(outFolder, filterName,date.today())
            df.to_excel(fileName,encoding="utf_8_sig", index=False)
    
if __name__ == '__main__':
    pass