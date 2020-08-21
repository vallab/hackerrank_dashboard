from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import getpass

username = input("Enter your username:")
password = getpass.getpass()
print('Password entered:', password)
login_url = 'https://www.hackerrank.com/auth/login'
algo_url = 'https://www.hackerrank.com/domains/algorithms'
browser_path = "E:\\algorithms\dashboard\hackerrank_dashboard\geckodriver.exe"

browser = webdriver.Firefox(executable_path=browser_path)

browser.get(login_url)

element = browser.find_element_by_id("input-1")

element.send_keys(username)
time.sleep(1)
pwd = browser.find_element_by_id("input-2")

pwd.send_keys(password)
element.send_keys(Keys.RETURN)
time.sleep(4)
#wait = WebDriverWait(browser,10)


browser.get(algo_url)
time.sleep(4)

#we have the full page source
text = (browser.page_source)

#now find rank
rank_index = text.find("Rank:")
#get rank
rank = int(text[rank_index+26:rank_index+32])

#now find points index
point_index = text.find("Points:")
point = float(text[point_index+36:point_index+42])

print("rank:",rank,"points:",point)

data = "rank : "+str(rank)+" points : "+str(point)
file = open('rank.txt','w')

file.write(data)
file.close()





browser.close()