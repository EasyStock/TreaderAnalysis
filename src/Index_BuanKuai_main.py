'''
Created on Aug 29, 2019

@author: mac
'''
from PathManager.StockPathManager import GetRawDataFolder_Index_BanKuai, GetDailyDataFolder_Index_BanKuai
import os
from IndexDataItemIO.IndexItemIO import CIndexItemIO


def ConverHTMLToXlSX():
    folder = GetRawDataFolder_Index_BanKuai()
    outFolder = GetDailyDataFolder_Index_BanKuai()
    filenames=os.listdir(folder)
    for htmlFile in filenames:
        if htmlFile.find('.xls') == -1:
            continue
        fName = htmlFile[:htmlFile.rfind('.')]
        srcFileName = os.path.join(folder,htmlFile)
        outFullName = u'%s/%s.xlsx' %(outFolder,fName)
        if os.path.exists(outFullName):
            continue
        io = CIndexItemIO()
        io.readFrom(srcFileName)
        io.saveTo(outFullName)
        
        
if __name__ == '__main__':
    ConverHTMLToXlSX()