'''
 Created on Wed Jan 29 2020

 Copyright (c) 2020 yuchonghuang@sina.cn
'''


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def start(site = "http://x.iwencai.com/"):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(site)
    return driver

def login(driver):
    driver.find_element_by_link_text(u"登录").click()
    time.sleep(2)
    driver.switch_to.frame(2)
    driver.find_element_by_xpath("//input[@id='username']").click()
    driver.find_element_by_xpath("//input[@id='username']").clear()
    driver.find_element_by_xpath("//input[@id='username']").send_keys("yuchon2")
    driver.find_element_by_xpath("//label[2]").click()
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys("pass123")
    driver.find_element_by_xpath("//div[2]/div/span").click()
    time.sleep(2)

def downloadFile(driver):
    driver.switch_to.default_content()
    driver.find_element_by_id("auto").click()
    driver.find_element_by_id("auto").clear()
    driver.find_element_by_id("auto").send_keys(u"开盘价,收盘价,最高价,最低价,成交量,成交额,量比,涨跌幅,5日均线, 10日均线,20日均线,30日均线,60日均线,120日均线,240日均线,macd, boll(upper)值,boll(mid)值,boll(lower)值,RSI(6),RSI(12),RSI(24),a股流通市值,行业，概念,上市天数,技术形态,昨日收盘价")
    driver.find_element_by_id("qs-enter").click()
    driver.find_element_by_xpath("//body/div[9]/div/span").click()
    driver.find_element_by_xpath("//div[@id='table_top_bar']/table/tbody/tr/td/div/ul/li[3]").click()

def end(driver):
    driver.quit()

if __name__ == '__main__':
    driver = start()
    login(driver)
    downloadFile(driver)
    end(driver)
