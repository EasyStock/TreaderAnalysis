'''
Created on May 6, 2019

@author: mac
'''


from DB import mysql
from StockBaseInfo.StockBaseInfoFetcher import CStockBaseInfoFetcher
from SQL.SQL_StockBaseInfo import createStockBaseInfoTables,dropStockBaseInfoTables,queryAllStockInfo,queryOneStockInfo

SCHEMA_BASE = 'stock_base'
STOCK_BASIC_INFO_TABLE_SH = 'stock_basicinfo_sh'
STOCK_BASIC_INFO_TABLE_SZ = 'stock_basicinfo_sz'
STOCK_BASIC_INFO_TABLE_ALL = 'stock_basicinfo_all'

db = mysql.connectdb(SCHEMA_BASE)

def TruncateBaseTableSH():
    tuncateTable_SH = '''TRUNCATE TABLE %s;'''%(STOCK_BASIC_INFO_TABLE_SH)
    mysql.executeSQL(db,tuncateTable_SH)

def TruncateBaseTableSZ():
    tuncateTable_SZ = '''TRUNCATE TABLE %s;'''%(STOCK_BASIC_INFO_TABLE_SZ)
    mysql.executeSQL(db,tuncateTable_SZ)

def FetchStockBaseInfoSH():
    fetcher = CStockBaseInfoFetcher()
    sql = fetcher.FetchBaseInfoAndFormatSQLFromSH(STOCK_BASIC_INFO_TABLE_SH)
    if sql is not None:
        TruncateBaseTableSH()
        mysql.executeSQL(db,sql)

def FetchStockBaseInfoSZ():
    fetcher = CStockBaseInfoFetcher()
    sql = fetcher.FetchBaseInfoAndFormatSQLFromSZ(STOCK_BASIC_INFO_TABLE_SZ)
    if sql is not None:
        TruncateBaseTableSZ()
        mysql.executeSQL(db,sql)

def FetchStockBaseInfo():
    FetchStockBaseInfoSH()
    FetchStockBaseInfoSZ()

def TruncateBaseTable():
    TruncateBaseTableSH()
    TruncateBaseTableSZ()

def CreatBaseInfoTables():
    sqls = createStockBaseInfoTables(SCHEMA_BASE, STOCK_BASIC_INFO_TABLE_SH, STOCK_BASIC_INFO_TABLE_SZ, STOCK_BASIC_INFO_TABLE_ALL)
    for sql in sqls:
        mysql.executeSQL(db,sql)

def DropBaseInfoTables():
    sqls = dropStockBaseInfoTables(SCHEMA_BASE, STOCK_BASIC_INFO_TABLE_SH, STOCK_BASIC_INFO_TABLE_SZ, STOCK_BASIC_INFO_TABLE_ALL)
    for sql in sqls:
        mysql.executeSQL(db,sql)

def QueryAllBasicInfo():
    sql = queryAllStockInfo(SCHEMA_BASE, STOCK_BASIC_INFO_TABLE_SH, STOCK_BASIC_INFO_TABLE_SZ, STOCK_BASIC_INFO_TABLE_ALL)
    print(sql)
    return mysql.querydb(db,sql)

def QueryOneBasicInfo(stockID):
    sql = queryOneStockInfo(SCHEMA_BASE, STOCK_BASIC_INFO_TABLE_SH, STOCK_BASIC_INFO_TABLE_SZ, STOCK_BASIC_INFO_TABLE_ALL,stockID)
    print(sql)
    return mysql.querydb(db,sql)

if __name__ == '__main__':
    #DropBaseInfoTables()
    #
    #CreatBaseInfoTables()
    FetchStockBaseInfo()
    allInfos = QueryOneBasicInfo('000001')
    # print(allInfos)
    for allInfo in allInfos:
        print(allInfo[0],allInfo[1],allInfo[2])