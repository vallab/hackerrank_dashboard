from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass

url_1 = 'https://cn.bing.com'

url_2 = 'https://www.baidu.com'

browser = webdriver.Firefox()

browser.get(url_1)
time.sleep(10)
browser.get(url_2)
time.sleep(10)
browser.quit()
