'''
Created on Jun 15, 2019

@author: mac
'''
from PathManager.StockPathManager import GetFilterFolderWithFilterName, GetDailyDataFolder
from StockFilter.FilterMgr.StockFilterMgr import CStockFilterMgr
from StockFilter.Filters.StockFilterCROSS_MA_N import CStockFilterCROSS_MA_N
from StockFilter.Filters.StockFilterGreater_Than_MA_N import CStockFilterGreater_Than_MA_N
from StockFilter.Filters.StockFilter_CROSS_MULTI_LINES import CStockFilterCROSS_MULTI_LINES
from StockFilter.Filters.StockFilter_ZhangDiefu import CStockFilterZhangDieFu
from StockFilter.Filters.StockFilter_BOLLUP_Volumn import CStockFilterBOLLUP
from StockFilter.Filters.StockFilter_BOLLMID_TO_UP import CStockFilterBOLL_MID_TO_UP
from StockFilter.Filters.StockFilter_BOLL_DOWN_TO_MID import CStockFilterBOLL_DOWN_TO_MID
from StockFilter.Filters.StockFilter_NO_Filter import CStockFilterNoFilter
from StockFilter.FilterMgr.StockFilterBanKuaiMgr import CStockFilterBanKuaiMgr
from StockFilter.FilterMgr.StockFilterCountMgr import CStockFilterCountMgr
from StockFilter.Filters.StockFilter_Distance_MA_LONG import CStockFilter_Distance_MA_LONG
from StockFilter.Filters.StockFilter_Distance_MA_Short import CStockFilter_Distance_MA_Short
import os

def Filter(fileName,filter_):
    filterFolder = GetFilterFolderWithFilterName(filter_.filterName)
    mgr = CStockFilterMgr()
    fName = fileName[fileName.rfind('/')+1: fileName.rfind('.')]
    destFileName = '%s/%s.xls' %(filterFolder,fName)
    mgr.FilterFile(fileName, filter_, destFileName)


def Filter_Folder(filter_):
    srcfolder = GetDailyDataFolder()
    outFolder = GetFilterFolderWithFilterName(filter_.filterName)
    filenames=os.listdir(srcfolder)
    mgr = CStockFilterMgr()
    for xlsxFile in filenames:
        if xlsxFile.find('.xlsx') == -1:
            continue
        fName = xlsxFile[:xlsxFile.rfind('.')]
        srcFileName = os.path.join(srcfolder,xlsxFile)
        outFullName = u'%s/%s.xlsx' %(outFolder,fName)
        print(outFullName)
        if os.path.exists(outFullName):
            continue
        mgr.FilterFile(srcFileName, filter_, outFullName)
        

def FilterFolderWithFilters(filters):
    for filter_ in filters:
        Filter_Folder(filter_)
        

def DoFilterCROSS_MA_N():
    filter0 = CStockFilterCROSS_MA_N((5,1.5))
    filter1 = CStockFilterCROSS_MA_N((10,1.5))
    filter2 = CStockFilterCROSS_MA_N((20,1.5))
    filter3 = CStockFilterCROSS_MA_N((30,1.5))
    filter4 = CStockFilterCROSS_MA_N((60,1.5))
    filter5 = CStockFilterCROSS_MA_N((120,1.5))
    filter6 = CStockFilterCROSS_MA_N((240,1.5))
    filters = [filter0, filter1, filter2, filter3, filter4, filter5,filter6]
    FilterFolderWithFilters(filters)
    
def DoFilterGREATER_THAN_MA_N():
    filter0 = CStockFilterGreater_Than_MA_N(5)
    filter1 = CStockFilterGreater_Than_MA_N(10)
    filter2 = CStockFilterGreater_Than_MA_N(20)
    filter3 = CStockFilterGreater_Than_MA_N(30)
    filter4 = CStockFilterGreater_Than_MA_N(60)
    filter5 = CStockFilterGreater_Than_MA_N(120)
    filter6 = CStockFilterGreater_Than_MA_N(240)
    filters = [filter0, filter1, filter2, filter3, filter4, filter5,filter6]
    FilterFolderWithFilters(filters)


def DoFilterCROSS_MULTI_LINES():
    filter3 = CStockFilterCROSS_MULTI_LINES((1,2.5))
    filter4 = CStockFilterCROSS_MULTI_LINES((2,2.5))
    filter5 = CStockFilterCROSS_MULTI_LINES((3,2.5))
    filter6 = CStockFilterCROSS_MULTI_LINES((4,2.5))
    filter7 = CStockFilterCROSS_MULTI_LINES((5,2.5))
    filter8 = CStockFilterCROSS_MULTI_LINES((6,2.5))
    filter9 = CStockFilterCROSS_MULTI_LINES((7,2.5))
    filters = [filter3, filter4, filter5,filter6,filter7,filter8,filter9]
    FilterFolderWithFilters(filters)


def DoFilterZhangDieFu():
    filter1 = CStockFilterZhangDieFu(-10.5,-9.8)
    filter2 = CStockFilterZhangDieFu(-9.8,-7)
    filter3 = CStockFilterZhangDieFu(0,3.0)
    filter4 = CStockFilterZhangDieFu(3.0,5.0)
    filter5 = CStockFilterZhangDieFu(5.0,7.0)
    filter6 = CStockFilterZhangDieFu(7.0,9.8)
    filter7 = CStockFilterZhangDieFu(9.8, 10.5)
    filters = [filter1,filter2, filter3, filter4, filter5,filter6,filter7]
    FilterFolderWithFilters(filters)   

def DoFilterNoraml():
    filter0 = CStockFilterBOLLUP(2.5)
    filter1 = CStockFilterBOLL_MID_TO_UP((0,20))
    filter2 = CStockFilterBOLL_DOWN_TO_MID((0,20))
    filter3 = CStockFilterNoFilter()
    filter4 = CStockFilter_Distance_MA_Short(3)
    filter5 = CStockFilter_Distance_MA_LONG(3)
    filters = [filter0, filter1, filter2,filter3,filter4,filter5]
    FilterFolderWithFilters(filters)
    
    
def AnalysisBanKuai():
    mgr=CStockFilterBanKuaiMgr()
    mgr.Analysis()
    
def AnalysisBanKuaiRepeatable():
    mgr=CStockFilterBanKuaiMgr()
    mgr.AnalysisRepeatly()

def Count():
    print("\n\n           start to counting......\n\n")
    mgr=CStockFilterCountMgr()
    mgr.Analysis()

def DoFilterMain():
    DoFilterNoraml()
    DoFilterCROSS_MULTI_LINES()
    DoFilterCROSS_MA_N()
    DoFilterGREATER_THAN_MA_N()
    DoFilterZhangDieFu()
    AnalysisBanKuai()
    AnalysisBanKuaiRepeatable()
    Count()
    
    
if __name__ == '__main__':
    DoFilterMain()