'''
Created on May 3, 2019

@author: mac
'''
import os

if __name__ == '__main__':
    folder = '/usr/local/bin/'
    command = (
                'python3 -m pip install -U pip',
                'python3 -m pip install -U matplotlib',
                'pip3 install --upgrade pip',
                "pip3 install pandas",
                "pip3 install xlwt",
                "pip3 install xlrd",
                'pip3 install openpyxl',
                "pip3 install lxml",
                "pip3 install selenium",
                "pip3 install html5lib",
                "pip3 install BeautifulSoup4",
                )
    os.chdir(folder)
    for cmd in command:
        ret = os.system(cmd)
