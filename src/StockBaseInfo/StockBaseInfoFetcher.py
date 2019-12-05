'''
Created on Jun 14, 2019

@author: mac
'''
import http.client
import pandas as pd
import json

szse_site = 'www.szse.cn'
szse_url = '/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1110x&TABKEY=tab1&random=0.9111307005186757'


sse_site = 'query.sse.com.cn'
sse_url = '/security/stock/getStockListData2.do?&' \
        'isPagination=true&stockCode=&csrcCode=' \
        '&areaName=&stockType=1&pageHelp.cacheSize='\
        '1&pageHelp.beginPage=1&pageHelp.pageSize=3000&'\
        'pageHelp.pageNo=1&_=1481792573174'
sse_head = {'referer': 'http://www.sse.com.cn/assortment/stock/list/share/',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        'Accept-Encoding': 'gzip, deflate, sdch',
        }

head = [u'股票代码', u'股票名称', u'上市日期']

class CStockBaseInfoFetcher(object):
    def __init__(self):
        pass

    def StringToInt(self, value):
        return int(value.replace(',', ''))
    
    def FormatStockID(self, value):
        return '%06d'%(int(value))
    
    def FetchDataFrom(self, site, url, head = {}):
        try:
            conn = http.client.HTTPConnection(site)
            conn.request("GET", url,headers=head)
            r1 = conn.getresponse()
            if r1.status == 200 and r1.reason == 'OK':
                data = r1.read()
                conn.close()
                return data
            else:
                print(u'获取数据失败,原因', r1.status, r1.reason)
        except Exception as e:
            print(e)
        return None

    def FormatSQLOfSZ(self,df):
        return self.FormatSQLWithTableName(df,'stock_baseinfo_sz')
    
    def FormatSQLOfSH(self,df):
        return self.FormatSQLWithTableName(df,'stock_baseinfo_sh')

    def FormatSQLWithTableName(self, df,tableName):
        if df is None:
            return ""

        sql = '''insert into `%s` (stockID, stockName, listingDate) values''' %(tableName)
        size = len(df)
        for index in range(0, len(df)):
            row = df.iloc[index]
            stockID = row['股票代码']
            stockName = row['股票名称']
            stockListingDate =  row['上市日期']
            if len(stockListingDate.split('-')) != 3:
                stockListingDate = '1970-01-01'
            if index != size -1:
                sql = sql + '''('%s', '%s','%s'),\n'''%(stockID, stockName,stockListingDate)
            else:
                sql = sql + '''('%s', '%s', '%s');'''%(stockID, stockName, stockListingDate)
        return sql

    def FetchBaseInfoFromSZ(self):
        Rawdata = self.FetchDataFrom(szse_site, szse_url)
        if Rawdata == None:
            print('获取深圳交易所所有股票失败!')
            return None

        tmpFileName = u'/tmp/tmp.xlsx'
        with open(tmpFileName, 'wb+') as f:
            f.write(Rawdata)
            f.close()

        df = pd.read_excel(tmpFileName)
        sub = df.iloc[:, [5, 6, 7]].copy()
        sub = sub.dropna()
        sub.iloc[:, 0] = sub.iloc[:, 0].map(self.FormatStockID)
        sub.columns = head
        print(sub.head())
        print(u'获取深圳交易所所有股票成功！总共:%d' % (sub.shape[0]))
        return sub

    def FetchBaseInfoFromSH(self):
        Rawdata = self.FetchDataFrom(sse_site, sse_url, sse_head)
        if Rawdata == None:
            print('获取上海交易所所有股票失败!')
            return None

        allData = []
        js = json.loads(Rawdata)
        results = js[u'result']
        for data in results:
            rowData = [
                data[u'SECURITY_CODE_A'],
                data[u'SECURITY_ABBR_A'],
                data[u'LISTING_DATE']
                ]
            allData.append(rowData)
        df = pd.DataFrame(allData,columns = head)
        print('获取上海交易所所有股票成功！总共:%d' % (js[u'pageHelp'][u'total']))
        print(df.head())
        return df

if __name__ == '__main__':
    fetcher = CStockBaseInfoFetcher()
    df = fetcher.FetchBaseInfoFromSH()
    sql = fetcher.FormatSQLOfSH(df)
    print(sql)