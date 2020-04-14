'''
 Created on Wed Jan 01 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''

from StockRecordMap import ALL_STOCK_RECORDS_SHORT_KEYS,LongNameToShort,ShortNameToLong
import json

class CStockRecord(object):
    def __init__(self):
        self.stockRecord = {}
    
    def FromJson(self, jsonStr):
        res = json.loads(jsonStr)
        longNameDict = {ShortNameToLong(k) : v for k, v in res.items()}
        self.stockRecord.update(longNameDict)

    def ToJson(self):
        shortNameDict = {LongNameToShort(k) : v for k, v in self.stockRecord.items()}
        return json.dumps(shortNameDict,indent=1,ensure_ascii=False)

    def FromDict(self,_dict):
        self.stockRecord.update(_dict)

    def ToDict(self):
        return self.stockRecord

    
    def __str__(self):
        msg = json.dumps(self.stockRecord,indent=1,ensure_ascii=False)
        return msg


if __name__ == '__main__':
    dict_ = {
        '股票名称':'AAA',
        '日期':'BBB',
        '股票代码':"CCC"
    }
    record = CStockRecord()
    record.FromDict(dict_)
    print(record)
    print(record.ToJson())

    jsonStr = '''
    {
    "name": "DDD",
    "date": "EEE",
    "id": "FFFFF"
    }
    '''
    record2 = CStockRecord()
    record2.FromJson(jsonStr)
    print(record2)
    print(record2.ToDict())
    print(record2.ToJson())

    