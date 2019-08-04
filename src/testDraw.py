'''
Created on Jun 22, 2019

@author: mac
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def Test1():
    fileName = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/合并/000038.SZ.xlsx'
    df = pd.read_excel(fileName, encoding='utf_8_sig', index_col = 0)
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    df1 = pd.DataFrame(df, index = df.index.copy(), columns=('短线均线乖离度',))
    pd.set_option('display.max_columns', None)
    print(df1)
    df1.plot()
    plt.show()

def Test2():
    fileName = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/threshold.xlsx'
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    df = pd.read_excel(fileName, encoding='utf_8_sig', index_col = 0)
    #data = df['短线均线乖离度_low'].values
    data = df['BOLL带宽_low'].values
    
    arr_mean = np.mean(data)
    arr_var = np.var(data)
    arr_std = np.std(data,ddof=1)
    print("平均值为：%f" % arr_mean)
    print("方差为：%f" % arr_var)
    print("标准差为:%f" % arr_std)
    print("2倍标准差区间:%f---%f",(arr_mean-2*arr_std),(arr_mean+2*arr_std))
    plt.hist(data, bins=100, normed=1, facecolor="blue", edgecolor="black", alpha=0.7)
    plt.show()
    
if __name__ == '__main__':
    Test2()
    