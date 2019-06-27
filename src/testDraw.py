'''
Created on Jun 22, 2019

@author: mac
'''
import pandas as pd
import matplotlib.pyplot as plt
if __name__ == '__main__':
    fileName = u'/Volumes/Data/StockAssistant/TreaderAnalysis/data/output/合并/601318.SH.xlsx'
    df = pd.read_excel(fileName, index_col = None, encoding='utf_8_sig')
    df1 = pd.DataFrame(df, columns=('日期','收盘价', '股价距离5日线距离','股价距离10日线距离','股价距离月线距离','股价距离30日线距离','股价距离季线距离','股价距离半年线距离','股价距离年线距离'))
    pd.set_option('display.max_columns', None)
    print(df1)
    df1.plot()
    plt.show()
    