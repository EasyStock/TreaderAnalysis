'''
Created on May 3, 2019

@author: mac
'''

class CStockItemIO(object):

    def __init__(self):
        self.stocks = None
        self.__engine = None
    
    def readFromHTML(self,fileName):
        from StockDataItemIO.StockItemIO_HTML import CStockItemIO_HTML
        ht = CStockItemIO_HTML()
        ht.ReadFrom(fileName)
        self.__engine = ht
        self.stocks = ht.stocks
        
    def readFromCSV(self, fileName):
        from StockDataItemIO.StockItemIO_CSV import CStockItemIO_CSV
        csv = CStockItemIO_CSV()
        csv.ReadFromCSV(fileName)
        self.__engine = csv
        self.stocks = csv.stocks
    
    def readFromExcel(self, fileName):
        from StockDataItemIO.StockItemIO_XLS import CStockItemIO_XLS
        io_xls = CStockItemIO_XLS()
        io_xls.ReadFromExcel(fileName)
        self.__engine = io_xls
        self.stocks = io_xls.stocks
        
    def saveTo(self,fileName):
        self.__engine.SaveTo(fileName)

    def SaveToWithStocks(self,fileName, stocks):
        self.__engine.SaveToWithStocks(fileName, stocks)
    
    def readFrom(self,fileName):
        ext = fileName[fileName.rfind('.')+1:]
        if ext == 'csv':
            self.readFromCSV(fileName)
        elif ext == 'xlsx':
            self.readFromExcel(fileName)
        elif ext == 'xls':
            self.readFromHTML(fileName)
    
    def readFromHTMLAndSaveTo(self,srcFileName, destFileName):
        self.readFromHTML(srcFileName)
        self.saveTo(destFileName)
        

            
if __name__ == '__main__':
    fileName = u'/Volumes/Data/StockAssistant/TreaderAnalysis/data/raw/2019-05-07.xls'
    fileName_dest = u'/Volumes/Data/StockAssistant/TreaderAnalysis/data/raw/2019-05-07.xlsx'
    fileName_dest1 = u'/Volumes/Data/Downloads/2019-05-02_out.xlsx'
    io = CStockItemIO()
    io.readFrom(fileName)
    io.saveTo(fileName_dest)
    