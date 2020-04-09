# coding=utf-8
'''
 Created on Tue Jan 07 2020 10:46:03
 @author: jianpinh
'''
import logging
from  datetime import date

LOG_STOCK_COMMON = '/tmp/stock_Common_%s.log'%(date.today())
LOG_STOCK_FILTER = '/tmp/stock_Filter_%s.log'%(date.today())

allLogFiles = {
    LOG_STOCK_COMMON:None,
    LOG_STOCK_FILTER:None,
}

def INFO_LOG(msg):
    msg_console = "\033[0;32;40m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.info(msg)

def DEBUG_LOG(msg):
    msg_console = "\033[0;32;40m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.debug(msg)

def WARNING_LOG(msg):
    msg_console = "\033[0;33;40m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.warning(msg)


def ERROR_LOG(msg):
    msg_console = "\033[0;37;41m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.error(msg)


def CRITICAL_LOG(msg):
    msg_console = "\033[0;37;41m%s\033[0m"%(msg)
    print(msg_console)

    logger = logging.getLogger('logfile')
    logger.critical(msg)


def ConfigLogWithFile(key):
    if key not in allLogFiles:
        return
    
    if allLogFiles[key] is not None:
        return

    # init file 
    
    logger = logging.getLogger('logfile')
    logger.setLevel('DEBUG')
    
    BASIC_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename=key, filemode='w',format=BASIC_FORMAT,datefmt=DATE_FORMAT)
    allLogFiles[key] = logger

def ConfigLog(key):
    ConfigLogWithFile(key)

if __name__ == '__main__':
    #ConfigLog(LOG_JMT_REPORT_MONITOR)
    ConfigLog(LOG_STOCK_COMMON)
    DEBUG_LOG("this is debug info")
    INFO_LOG("this is info info")
    WARNING_LOG("this is warning info")
    ERROR_LOG("this is error info")
    CRITICAL_LOG("this is critical info")

