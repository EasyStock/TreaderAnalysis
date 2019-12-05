'''
Created on May 6, 2019

@author: mac
'''


from DB import mysql
from StockBaseInfo.StockBaseInfoFetcher import CStockBaseInfoFetcher

db = mysql.connectdb()

tuncateTable_SH = '''TRUNCATE TABLE stock_baseinfo_sh;'''
tuncateTable_SZ = '''TRUNCATE TABLE stock_baseinfo_sz;'''
def FetchStockBaseInfoSH():
    fetcher = CStockBaseInfoFetcher()
    df = fetcher.FetchBaseInfoFromSH()
    if df is not None:
        mysql.executeSQL(db,tuncateTable_SH)
        sql = fetcher.FormatSQLOfSH(df)
        mysql.executeSQL(db,sql)

def FetchStockBaseInfoSZ():
    fetcher = CStockBaseInfoFetcher()
    df = fetcher.FetchBaseInfoFromSZ()
    if df is not None:
        mysql.executeSQL(db,tuncateTable_SZ)
        sql = fetcher.FormatSQLOfSZ(df)
        mysql.executeSQL(db,sql)

def FetchStockBaseInfo():
    FetchStockBaseInfoSH()
    FetchStockBaseInfoSZ()
    
if __name__ == '__main__':
    FetchStockBaseInfo()