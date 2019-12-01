#!/usr/bin/env python
# coding=utf-8

import pymysql

SQL_HOST = '******'
SQL_PORT = '******'
SQL_USER = '******'
SQL_PWD = '******'
SQL_DB = '******'

def connectdb():
    print('connecting to mysql server...')
    # 打开数据库连接
    # 
    db = pymysql.connect(host= SQL_HOST,
                             port=SQL_PORT,
                             user=SQL_USER,
                             password=SQL_PWD,
                             db=SQL_DB,
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
    except:
        # Rollback in case there is any error
        print('插入数据失败!')
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
    sql = '''use world; select * from city;'''
    executeSQL(db,sql)
