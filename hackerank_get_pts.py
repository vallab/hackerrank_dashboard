from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass


algo_url = 'https://www.hackerrank.com/domains/algorithms'
browser = webdriver.Firefox()

browser.get(algo_url)


