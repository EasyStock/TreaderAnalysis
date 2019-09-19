'''
Created on Sep 19, 2019

@author: mac
'''
from _decimal import Decimal

def CalcZhangTingBan_XinGu(price, N):
    if N == 1:
        res = float(price)*1.2*1.2
        closePrice = float(Decimal(res).quantize(Decimal('0.00')))
        leiji = (closePrice - price)/price *100
        leijiShouyi = (closePrice - price)
        print('第%2s个涨停板收盘价是:%-10.2f 当前涨幅:%6.2f%%    累计涨幅%8.2f%%    500股累计收益 %-8.2f元    1000股累计收益 %.2f元'%(N,res,leiji,leiji, leijiShouyi*500, leijiShouyi*1000))
        return Decimal(closePrice).quantize(Decimal('0.00'))
    else:
        last = float(CalcZhangTingBan_XinGu(price, N-1))
        priceTmp = last * 1.1
        closePrice = float(Decimal(priceTmp).quantize(Decimal('0.00')))
        leiji = (priceTmp - price)/price *100
        leijiShouyi = (closePrice - price)
        currentZhangfu = (closePrice - last)/last*100
        print('第%2s个涨停板收盘价是:%-10.02f 当前涨幅:%6.2f%%    累计涨幅%8.2f%%    500股累计收益 %-8.2f元    1000股累计收益 %.2f元'%(N,closePrice,currentZhangfu,leiji, leijiShouyi*500, leijiShouyi*1000))
        return Decimal(closePrice).quantize(Decimal('0.00'))
        

if __name__ == '__main__':
    CalcZhangTingBan_XinGu(4.84, 35)