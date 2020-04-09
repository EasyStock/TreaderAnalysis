#!/usr/bin/env python
# coding=utf-8

import pymysql

SQL_HOST = '192.168.1.12'
SQL_PORT = 3306
SQL_USER = 'jianpinh'
SQL_PWD = '861022'

def connectdb(dbName):
    print('connecting to mysql server...')
    # 打开数据库连接
    # 
    db = pymysql.connect(host= SQL_HOST,
                             port=SQL_PORT,
                             user=SQL_USER,
                             password=SQL_PWD,
                             db=dbName,
                             charset='utf8')

    print('conencted to mysql server successfully!')
    return db

def executeSQL(db, sql):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # SQL 插入语句
   
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # Rollback in case there is any error
        print('插入数据失败!', e)
        db.rollback()

def querydb(db,sql_statement):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # SQL 查询语句   
    try:
        # 执行SQL语句
        cursor.execute(sql_statement)
        # 获取所有记录列表
        results = cursor.fetchall()
        return results
    except:
        print ("Error: unable to fecth data")

def closedb(db):
    db.close()

if __name__ == '__main__':
    db = connectdb()
    sql = '''select * from stock_baseinfo_sh;'''
    executeSQL(db,sql)
