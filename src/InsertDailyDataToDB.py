'''
Created on Jun 14, 2019

@author: mac
'''

from SQL.SQL_StockDaily import InsterDailyDataInto,createTable_DailyWithDataFrame,dropTable_DailyWithDataFrame,truncateTable_DailyWithDataFrame
import pandas as pd
from DB import mysql
import os
  
SCHEMA_HISTORY_THS = 'tonghuashun'

db = mysql.connectdb(SCHEMA_HISTORY_THS)

def CreateTablesWithDataFrame(df):
    sqls = createTable_DailyWithDataFrame(df,SCHEMA_HISTORY_THS)
    for sql in sqls:
        #print(sql)
        mysql.executeSQL(db,sql)

def DropTabelWithDataFrame(df):
    sqls = dropTable_DailyWithDataFrame(df,SCHEMA_HISTORY_THS)
    for sql in sqls:
        #print(sql)
        mysql.executeSQL(db,sql)

def TruncateTable_DailyWithDataFrame(df):
    sqls = truncateTable_DailyWithDataFrame(df,SCHEMA_HISTORY_THS)
    index = 1
    for sql in sqls:
        #print(sql)
        print('start to truncate  with index:%06s'%(index))
        mysql.executeSQL(db,sql)
        index = index + 1

def InsertDataTo(date,df,stockIDs):
    sqls = InsterDailyDataInto(date,df,SCHEMA_HISTORY_THS,stockIDs)
    index = 1
    for sql in sqls:
        print('start to insert with index:%06s'%(index))
        mysql.executeSQL(db,sql)
        index = index + 1

def InsertDailyDataWithFile(fileName,stockIDs):
    date = fileName[fileName.rfind('/')+1:fileName.rfind('.')]
    df = pd.read_excel(fileName, index_col = None, encoding='utf_8_sig')
    InsertDataTo(date,df,stockIDs)

def TruncateTableWithFile(fileName):
    df = pd.read_excel(fileName, index_col = None, encoding='utf_8_sig')
    TruncateTable_DailyWithDataFrame(df)

def SelectTableNamesFromDB():
    sql = '''select table_name from information_schema.tables where table_schema = '%s' '''%(SCHEMA_HISTORY_THS)
    print(sql)
    tableNames = mysql.querydb(db,sql)
    stockIDs = []
    for tableName in tableNames:
        tableName = tableName[0]
        stockIDs.append(tableName[tableName.find('_')+1:])
    return stockIDs

def InserDataWithFolder(folderName,stockIDs):
    filenames=os.listdir(folderName)
    for fileName in filenames:
        if fileName.find('.xls') == -1:
            continue
        print(fileName)
        srcFileName = os.path.join(folderName,fileName)
        InsertDailyDataWithFile(srcFileName,stockIDs)



if __name__ == '__main__':
    fileName = '''/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/每日数据/2019-06-05.xlsx'''
    #InsertDailyDataWithFile(fileName)
    #xTruncateTableWithFile(fileName)
    folder = '''/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/每日数据'''
    stockIDs = SelectTableNamesFromDB()
    InserDataWithFolder(folder,stockIDs)