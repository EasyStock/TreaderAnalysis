'''
Created on May 7, 2019

@author: mac
'''

SCHEMA_BASE = 'stock_base'
STOCK_BASIC_INFO_TABLE_SH = 'stock_basicinfo_sh'
STOCK_BASIC_INFO_TABLE_SZ = 'stock_basicinfo_sz'
STOCK_BASIC_INFO_TABLE_ALL = 'stock_basicinfo_all'

def dropStockBaseInfoTables(schema, table_sh, table_sz,view_all):
    '''
    创建基础数据表
    '''
    sqlSH = '''
        DROP TABLE %s.%s;
    '''%(schema, table_sh)

    sqlSZ = '''
        DROP TABLE %s.%s;
    '''%(schema, table_sz)

    sqlALL = '''
        DROP VIEW %s.%s;
        '''%(schema, view_all)

    return [sqlSH,sqlSZ, sqlALL]

def createStockBaseInfoTables(schema, table_sh, table_sz,view_all):
    '''
    创建基础数据表
    '''
    sqlSH = '''
        CREATE TABLE IF NOT EXISTS %s.%s (stockID varchar(12) NOT NULL, stockName varchar(45), listingDate date COMMENT '上市日期', PRIMARY KEY (stockID), CONSTRAINT stockID_UNIQUE UNIQUE (stockID)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE=utf8mb4_0900_ai_ci;
    '''%(schema, table_sh)

    sqlSZ = '''
        CREATE TABLE IF NOT EXISTS %s.%s (stockID varchar(12) NOT NULL, stockName varchar(45), listingDate date COMMENT '上市日期', PRIMARY KEY (stockID), CONSTRAINT stockID_UNIQUE UNIQUE (stockID)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE=utf8mb4_0900_ai_ci;
    '''%(schema, table_sz)

    sqlALL = '''
        CREATE VIEW %s.%s
        as
        select * from %s.%s
        union all
        select * from %s.%s;
        '''%(schema, view_all, schema, table_sh, schema, table_sz)

    return [sqlSH,sqlSZ, sqlALL]

def queryAllStockInfo(schema, table_sh, table_sz,view_all):
    sql = '''
    select * from %s.%s
    '''%(schema, view_all)
    return sql

def queryOneStockInfo(schema, table_sh, table_sz,view_all,stockID):
    sql = '''
    select * from %s.%s where stockID = %s
    '''%(schema, view_all,stockID)
    return sql