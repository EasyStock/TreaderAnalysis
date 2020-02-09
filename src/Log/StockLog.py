# coding=utf-8
'''
 Created on Tue Jan 07 2020 10:46:03
 @author: jianpinh
'''

def INFO_LOG(msg):
    msg = "\033[0;32;40m%s\033[0m"%(msg)
    print(msg)

def DEBUG_LOG(msg):
    pass

def WARNING_LOG(msg):
    msg = "\033[0;33;40m%s\033[0m"%(msg)
    print(msg)


def ERROR_LOG(msg):
    msg = "\033[0;37;41m%s\033[0m"%(msg)
    print(msg)


if __name__ == '__main__':
    INFO_LOG("Test")
    DEBUG_LOG("Test")
    WARNING_LOG("Test")
    ERROR_LOG("Test")

