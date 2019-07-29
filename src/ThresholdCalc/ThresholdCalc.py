'''
Created on Jul 28, 2019

@author: mac
'''
import pandas as pd
import os
from StockDataItem.StockItemDef import stock_DISTANCE_MA_SHORT,\
    stock_DISTANCE_MA_LONG, stock_DISTANCE_MA_MID, stock_BOLL_Band_width
 
class ThresholdCalc(object):
    def __init__(self, params = None):
        if params == None:
            self.param = 3
        else:
            self.param = params
    
    def _calc(self,data):
        ret = None
        try:
            sortedData = data.sort_values(ascending=True)
            li = sortedData.tolist()
            ret = (float(li[self.param-1]), float(li[-self.param]))
        except:
            pass
        return ret
    
    def calcThreshold(self,df):
        columns = df.columns.values.tolist()
        ret = {}
        high = u'high'
        low = u'low'
        for column in columns:
            res = self._calc(df[column])
            if res != None:
                key1 = u'%s_%s' %(column,low)
                key2 = u'%s_%s' %(column,high)
                ret[key1] = res[0]
                ret[key2] = res[1]
            else:
                return None
        return ret
    
    def calcThreshold_Folder(self,folder,outFileName):
        filenames=os.listdir(folder)
        res = {}
        for xlsxFile in filenames:
            if xlsxFile.find('.xlsx') == -1:
                continue
            stockName = xlsxFile[xlsxFile.rfind('/')+1: xlsxFile.rfind('.xlsx')]
            fullPath = os.path.join(folder,xlsxFile)
            raw = pd.read_excel(fullPath, encoding='utf_8_sig', index_col = 0)
            columns = [stock_DISTANCE_MA_SHORT,stock_DISTANCE_MA_MID, stock_DISTANCE_MA_LONG, stock_BOLL_Band_width]
            df = pd.DataFrame(raw, index = raw.index.copy(), columns= columns)
            ret = self.calcThreshold(df)
            if ret != None:
                res[stockName] = ret
                print(stockName)
        df = pd.DataFrame(res).T
        df.to_excel(outFileName,encoding="utf_8_sig", index=True)
        return res
            
            
if __name__ == '__main__':
    fileName = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/合并/000038.SZ.xlsx'
    df = pd.read_excel(fileName, encoding='utf_8_sig', index_col = 0)
    df1 = pd.DataFrame(df, index = df.index.copy(), columns=('短线均线乖离度','中线均线乖离度','长线均线乖离度'))
    folder = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/合并/'
    t = ThresholdCalc()
    #t.calcThreshold(df1)
    t.calcThreshold_Folder(folder)
    
    
    