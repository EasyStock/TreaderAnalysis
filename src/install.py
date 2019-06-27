'''
Created on May 3, 2019

@author: mac
'''
import os

if __name__ == '__main__':
    folder = '/usr/local/bin/'
    command = ("./pip3 install pandas",
               "./pip3 install xlwt",
               "./pip3 install xlrd",
               './pip3 install openpyxl',
               'python3 -m pip install -U pip',
               'python3 -m pip install -U matplotlib'
               
               )
    os.chdir(folder)
    for cmd in command:
        ret = os.system(cmd)
