'''
 Created on Wed Jan 01 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''


import logging
import os
import pandas as pd
import StockRecord

class CStocRecordReader(object):
    def __init__(self):
        pass
    

    def ReadFromXLSFile(self,fileName):
        if os.path.exists(fileName) == False:
            logging.error('file %s not exist!',fileName)
            return
        df = pd.read_excel(fileName, index_col = None, encoding='utf_8_sig').T
        d = df.to_dict()
        for key in d:
            record = StockRecord.CStockRecord()
            record.FromDict(d[key])
            #print(record.ToJson())
            print(record)

    def ReadFromJsonSt(self,jsonStr):
        pass

    def ReadFromJsonFile(self,jsonFile):
        pass


if __name__ == '__main__':
    fileName = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/000550.SZ.xlsx'
    reader = CStocRecordReader()
    reader.ReadFromXLSFile(fileName)