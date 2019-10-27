'''
Created on Apr 15, 2019

@author: mac
'''
import pandas as pd
DIRECTION_UP = 'Up'
DirectION_DOWN = 'Down'


class CStockAdvanceFilter_LineTurning(object):
    def __init__(self):
        pass

    def GetAllTurnPoints(self, data):
        if not isinstance(data,pd.DataFrame):
            raise Exception("data must be a DataFrame")

        res = []
        size = data.shape
        if size[0] < 50:
            return res
    
        firstCol = data.iloc[:,0]
        smoothedData = self.Smooth(firstCol)
        deri = self.FirstDerivative(smoothedData)
        df = pd.DataFrame(deri.values, index= data.index)
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


if __name__ == '__main__':
    fileName = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/002241.SZ.xlsx'
    df = pd.read_excel(fileName,index_col=0)
    df1 = pd.DataFrame(df, index = df.index, columns=('10MA',),copy = True)
    #print(df1)
    up = CStockAdvanceFilter_LineTurning()
    #res = up.FilterBy(df1)
    # print(res[0])
    # print(res[1])

    up.GetAllTurnPoints(df1)
