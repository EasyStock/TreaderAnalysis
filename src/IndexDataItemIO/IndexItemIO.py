'''
Created on May 3, 2019

@author: mac
'''

class CIndexItemIO(object):

    def __init__(self):
        self.indexs = None
        self.__engine = None
    
    def readFromHTML(self,fileName):
        from IndexDataItemIO.IndexItemIO_HTML import CIndexItemIO_HTML
        ht = CIndexItemIO_HTML()
        ht.ReadFrom(fileName)
        self.__engine = ht
        self.indexs = ht.indexs
        
    def readFromCSV(self, fileName):
        from IndexDataItemIO.IndexItemIO_CSV import CIndexItemIO_CSV
        csv = CIndexItemIO_CSV()
        csv.ReadFromCSV(fileName)
        self.__engine = csv
        self.indexs = csv.indexs
    
    def readFromExcel(self, fileName):
        from IndexDataItemIO.IndexItemIO_XLS import CIndexItemIO_XLS
        io_xls = CIndexItemIO_XLS()
        io_xls.ReadFromExcel(fileName)
        self.__engine = io_xls
        self.indexs = io_xls.indexs
        
    def saveTo(self,fileName):
        self.__engine.SaveTo(fileName)

    def SaveToWithindexs(self,fileName, indexs):
        self.__engine.SaveToWithindexs(fileName, indexs)
    
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
    fileName = u'/Volumes/Data/indexAssistant/TreaderAnalysis/data/raw/2019-05-07.xls'
    fileName_dest = u'/Volumes/Data/indexAssistant/TreaderAnalysis/data/raw/2019-05-07.xlsx'
    fileName_dest1 = u'/Volumes/Data/Downloads/2019-05-02_out.xlsx'
    io = CIndexItemIO()
    io.readFrom(fileName)
    io.saveTo(fileName_dest)
    