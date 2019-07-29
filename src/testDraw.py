'''
Created on Jun 22, 2019

@author: mac
'''
import pandas as pd
import matplotlib.pyplot as plt
        
if __name__ == '__main__':
    fileName = u'/Volumes/Data/StockAssistant/EasyStock/TreaderAnalysis/data/output/合并/000038.SZ.xlsx'
    df = pd.read_excel(fileName, encoding='utf_8_sig', index_col = 0)
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    df1 = pd.DataFrame(df, index = df.index.copy(), columns=('短线均线乖离度',))
    pd.set_option('display.max_columns', None)
    print(df1)
    df1.plot()
    plt.show()
    