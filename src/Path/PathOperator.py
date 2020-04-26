# coding=utf-8
'''
 Created on Fri Jan 03 2020 10:29:53
 @author: jianpinh
'''
import os

def lastPathComponent(folder):
    if folder[-1] == '/':
        return lastPathComponent(folder[:-1])
    else:
        Components = folder.split('/')
        return Components[-1]

def removePathComponent(folder):
    if folder[-1] == '/':
        return removePathComponent(folder[:-1])
    else:
        return folder[:folder.rfind('/')+1]

def listAllFilesInFolder(folder):
    allfile=[]
    for dirpath,_,filenames in os.walk(folder):
        for name in filenames:
            allfile.append(os.path.join(dirpath, name))
    return allfile

def listAllFoldersInFolder(folder):
    allfile=[]
    for dirpath,dirnames,_ in os.walk(folder):
        for dir in dirnames:
            allfile.append(os.path.join(dirpath,dir))
    return allfile

if __name__ == '__main__':
    path = '/Volumes/Data/AA/2019-11-25/'
    c = listAllFoldersInFolder(path)
    print(c)
