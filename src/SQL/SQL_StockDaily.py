'''
Created on May 7, 2019

@author: mac
'''
from StockDataItem.StockItemDef import STOCK_TABLE_INDEX,stock_ID

#Drop Table
def dropTable_Daily(stockID,schema):
    sql = '''
        DROP TABLE %s.I_%s;
        '''%(schema,stockID)
    return sql

def dropTable_DailyWithDataFrame(df,schema):
    size = len(df)
    sqls = []
    for index in range(0, size):
        row = df.iloc[index]
        stockID = row[stock_ID]
        stockID = stockID[:stockID.rfind('.')]
        sql = dropTable_Daily(stockID,schema)
        sqls.append(sql)
    return sqls

def dropTable_DailyWithStockIDs(stockIDs,schema):
    sqls = []
    for stockID in stockIDs:
        sql = dropTable_Daily(stockID,schema)
        sqls.append(sql)
    return sqls
# Drop Table End


# Create Table Begin
def createTable_Daily(stockID,schema):
    sql = '''
        CREATE TABLE IF NOT EXISTS %s.I_%s (date date NOT NULL, openPrice float, closePrice float, closePriceY float, highPrice float, lowPrice float, volumn float, turnover float, volumnRatio float, zhangdiefu float, 5MA varchar(45), 10MA varchar(45), 20MA varchar(45), 30MA varchar(45), 60MA varchar(45), 120MA varchar(45), 240MA varchar(45), MACD varchar(45), BOLL_UP varchar(45), BOLL_MID varchar(45), BOLL_DOWN varchar(45), BOLL_PERCENTAGE varchar(45), BOLL_WIDTH varchar(45), DIS_BOLL_UP varchar(45), DIS_BOLL_MID varchar(45), DIS_BOLL_DOWN varchar(45), BOLL_UP_DOWN_PERCENTAGE varchar(45), SHORT_GUAI_LI varchar(45), MID_GUAI_LI varchar(45), LONG_GUAI_LI varchar(45), RSI6 varchar(45), RSI12 varchar(45), RSI24 varchar(45), SHIZHI varchar(45), INDUSTRY varchar(300), GAINIAN varchar(300), DAYS varchar(45), XINGTAI varchar(300), DIS_MA5 varchar(45), DIS_MA10 varchar(45), DIS_MA20 varchar(45), DIS_MA30 varchar(45), DIS_MA60 varchar(45), DIS_MA120 varchar(45), DIS_MA240 varchar(45), PRIMARY KEY (date), CONSTRAINT date_UNIQUE UNIQUE (date)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE=utf8mb4_0900_ai_ci;
    ''' %(schema,stockID)
    return sql

def createTable_DailyWithDataFrame(df,schema):
    size = len(df)
    sqls = []
    for index in range(0, size):
        row = df.iloc[index]
        stockID = row[stock_ID]
        stockID = stockID[:stockID.rfind('.')]
        sql = createTable_Daily(stockID,schema)
        sqls.append(sql)
    return sqls

def createTable_DailyWithStockIDs(stockIDs,schema):
    sqls = []
    for stockID in stockIDs:
        sql = createTable_Daily(stockID,schema)
        sqls.append(sql)
    return sqls
#Create Table End


#TRUNCATE Table begin
def truncateTable_Daily(stockID,schema):
    sql = '''
        TRUNCATE TABLE %s.I_%s;
        '''%(schema,stockID)
    return sql

def truncateTable_DailyWithDataFrame(df,schema):
    size = len(df)
    sqls = []
    for index in range(0, size):
        row = df.iloc[index]
        stockID = row[stock_ID]
        stockID = stockID[:stockID.rfind('.')]
        sql = truncateTable_Daily(stockID,schema)
        sqls.append(sql)
    return sqls
    
def truncateTable_DailyWithStockIDs(stockIDs,schema):
    sqls = []
    for stockID in stockIDs:
        sql = truncateTable_Daily(stockID,schema)
        sqls.append(sql)
    return sqls
# TRUNCATE Table End

def InsterDailyDataInto(date, df,schema,stockIDs):
    if df is None:
        return ""

    size = len(df)
    sqls = []
    for index in range(0, size):
        row = df.iloc[index]
        stockID = row[stock_ID]
        stockID = stockID[:stockID.rfind('.')]
        if stockID not in stockIDs:
            sql = createTable_Daily(stockID,schema)
            print(sql)
            sqls.append(sql)
            
        sql = '''
        INSERT INTO `%s`.`I_%s` (
        `date`, `openPrice`, `closePrice`,
        `closePriceY`, `highPrice`, `lowPrice`,
        `volumn`, `turnover`, `volumnRatio`, 
        `zhangdiefu`, `5MA`, `10MA`, `20MA`,
        `30MA`, `60MA`, `120MA`, `240MA`, 
        `MACD`, `BOLL_UP`, `BOLL_MID`, `BOLL_DOWN`,
        `BOLL_PERCENTAGE`, `BOLL_WIDTH`, `DIS_BOLL_UP`,
        `DIS_BOLL_MID`, `DIS_BOLL_DOWN`, `BOLL_UP_DOWN_PERCENTAGE`,
        `SHORT_GUAI_LI`, `MID_GUAI_LI`, `LONG_GUAI_LI`,
        `RSI6`, `RSI12`, `RSI24`, `SHIZHI`,
        `INDUSTRY`, `GAINIAN`, `DAYS`, `XINGTAI`, `DIS_MA5`,
        `DIS_MA10`, `DIS_MA20`, `DIS_MA30`, `DIS_MA60`,
        `DIS_MA120`, `DIS_MA240`) VALUES
        ('%s',
        '''%(schema, stockID,date)
        index_count = len(STOCK_TABLE_INDEX)

        for index in range(0,index_count-1):
            data = row[STOCK_TABLE_INDEX[index]]
            sql = sql + ''' '%s',''' %(data)
        
        sql = sql + ''' '%s');
        '''%(row[STOCK_TABLE_INDEX[index_count -1]])
        sqls.append(sql)
    return sqls


if __name__ == '__main__':
    import pandas as pd
    fileName = '''/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/每日数据/2019-06-05.xlsx'''
    df = pd.read_excel(fileName, index_col = None, encoding='utf_8_sig')
    print(df.head(5))
    date = '2019-06-05'
    InsterInto(df,'tonghuashun')