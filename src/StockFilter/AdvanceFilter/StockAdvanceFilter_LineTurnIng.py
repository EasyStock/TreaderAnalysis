'''
Created on Apr 15, 2019

@author: mac
'''
import pandas as pd
DIRECTION_UP = 'Up'
DirectION_DOWN = 'Down'

class CStockAdvanceFilter_LineTurning(object):
    def __init__(self):
        self.smoothedData = None
        self.firstDerivativeData = None
        self.firstDerivativeDataFrame = None

    def GetAllTurnPoints(self, data):
        if not isinstance(data,pd.DataFrame):
            raise Exception("data must be a DataFrame")

        res = []
        size = data.shape
        if size[0] < 50:
            return res
    
        firstCol = data.iloc[:,0]
        smoothedData = self.Smooth(firstCol)
        self.smoothedData = smoothedData
        deri = self.FirstDerivative(smoothedData)
        self.firstDerivativeData = deri.to_list()
        df = pd.DataFrame(deri.values, index= data.index)
        self.firstDerivativeDataFrame = df
        lastDir = None
        for i in range(1, size[0]-1):
            if df.iloc[i,0] >0 and df.iloc[i+1,0] > 0:
                if lastDir is None or lastDir == DirectION_DOWN:
                    ret = {}
                    ret['Date'] = df.index[i]
                    ret['Value'] = df.iloc[i,0]
                    ret['Direction'] = DIRECTION_UP
                    res.append(ret)
                    lastDir = DIRECTION_UP

            elif df.iloc[i,0] <0 and df.iloc[i+1,0] <0:
                if lastDir is None or lastDir == DIRECTION_UP:
                    ret = {}
                    ret['Date'] = df.index[i]
                    ret['Value'] = df.iloc[i,0]
                    ret['Direction'] = DirectION_DOWN
                    res.append(ret)
                    lastDir = DirectION_DOWN
            else:
                continue 
        return res

    def Smooth(self,data):
        if isinstance(data, pd.Series):
            listData = data.tolist() # pandas.Series to list
        else:
            listData = data

        size = len(listData)
        returnData = []
        returnData.append(float(listData[0]))
        for i in range(1, size-1):
            tmp = (float(listData[i-1]) + float(listData[i]) + float(listData[i+1]))/3
            returnData.append(tmp)
        
        last = (float(listData[size-2]) + float(listData[size-1]))/2.0
        returnData.append(last)
        return pd.Series(returnData)

    def FirstDerivative(self,data):
        if isinstance(data, list):
            data = pd.Series(data)
        
        return data.diff()

def GetDerivativeDataWithStock(stockIDs):
    folder = '/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/股票/合并/'
    for stock in stockIDs:
        fileName = u'%s%s.xlsx' % (folder, stock)
        df = pd.read_excel(fileName,index_col=0)
        df1 = pd.DataFrame(df, index = df.index, columns=('20MA',),copy = True)
        up = CStockAdvanceFilter_LineTurning()
        ret = up.GetAllTurnPoints(df1)
        print("\n\n\n\n========================================")
        print(stock, df["股票简称"][-1])
        print(pd.DataFrame(ret))
        print(up.firstDerivativeDataFrame.tail(5))


if __name__ == '__main__':
    stockIDs = ['002271.SZ','600686.SH','600298.SH', '603722.SH','600779.SH','300014.SZ','002234.SZ']
    GetDerivativeDataWithStock(stockIDs)
