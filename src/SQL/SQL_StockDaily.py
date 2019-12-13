'''
Created on May 7, 2019

@author: mac
'''

SCHEMA_HISTORY_THS = 'tonghuashun'


def dropTable_Daily(stockID,schema = SCHEMA_HISTORY_THS):
    '''
    创建历史数据表
    '''
    sql = '''
        DROP TABLE %s.I_%s;
        '''%(schema,stockID)
    return sql

def createTable_Daily(stockID,schema = SCHEMA_HISTORY_THS):
    sql = '''
        CREATE TABLE IF NOT EXISTS %s.I_%s (date date NOT NULL, openPrice float, closePrice float, closePriceY float, highPrice float, lowPrice float, volumn float, turnover float, volumnRatio float, zhangdiefu float, 5MA varchar(45), 10MA varchar(45), 20MA varchar(45), 30MA varchar(45), 60MA varchar(45), 120MA varchar(45), 240MA varchar(45), MACD varchar(45), BOLL_UP varchar(45), BOLL_MID varchar(45), BOLL_DOWN varchar(45), BOLL_PERCENTAGE varchar(45), BOLL_WIDTH varchar(45), DIS_BOLL_UP varchar(45), DIS_BOLL_MID varchar(45), DIS_BOLL_DOWN varchar(45), BOLL_UP_DOWN_PERCENTAGE varchar(45), SHORT_GUAI_LI varchar(45), MID_GUAI_LI varchar(45), LONG_GUAI_LI varchar(45), RSI6 varchar(45), RSI12 varchar(45), RSI24 varchar(45), SHIZHI varchar(45), INDUSTRY varchar(300), GAINIAN varchar(300), DAYS varchar(45), XINGTAI varchar(300), DIS_MA5 varchar(45), DIS_MA10 varchar(45), DIS_MA20 varchar(45), DIS_MA30 varchar(45), DIS_MA60 varchar(45), DIS_MA120 varchar(45), DIS_MA240 varchar(45), PRIMARY KEY (date), CONSTRAINT date_UNIQUE UNIQUE (date)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE=utf8mb4_0900_ai_ci;
    ''' %(schema,stockID)
    return sql

def InsterInto(stockID,df,schema = SCHEMA_HISTORY_THS):
    pass
