'''
Created on Jul 29, 2019

@author: mac
'''

from PathManager.StockPathManager import GetMergedFolder, GetOutDataFolder
from ThresholdCalc.ThresholdCalc import ThresholdCalc

def CalcThreshold():
    folder = GetMergedFolder()
    destFileName = '%s/threshold.xlsx'%(GetOutDataFolder())
    threshold = ThresholdCalc()
    threshold.calcThreshold_Folder(folder, destFileName)
    

if __name__ == '__main__':
    CalcThreshold()