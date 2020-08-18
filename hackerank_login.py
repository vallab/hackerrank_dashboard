from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass


username = input("Enter your username:")
password = getpass.getpass()
print('Password entered:', password)


browser = webdriver.Firefox(executable_path="E:\\algorithms\\dashboard\\hackerrank_dashboard\\geckodriver.exe")
browser.get('https://www.hackerrank.com/auth/login')

element = browser.find_element_by_id("input-1")

element.send_keys(username)
time.sleep(1)
pwd = browser.find_element_by_id("input-2")

pwd.send_keys(password)
time.sleep(1)
#login=browser.find_element_by_xpath('//*[@id="editor"]/html/body/div[9]/div/div/div/section/div/div/div[2]/div[1]/form/div[4]/button/div/span')[0]
#login.click()

#search_btn = browser.find_element_by_id("sb_form_go")
element.send_keys(Keys.RETURN)

time.sleep(10)
#browser.get('https://www.hackerrank.com/domains/algorithms?badge_type=problem-solving')
#btn id =base-card-2-link
#open algo link
#browser.get('https://www.hackerrank.com/domains/algorithms?badge_type=problem-solving')
#Algo_Button=browser.find_element_by_xpath('//html/body/div[4]/div/div/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div/div/a/div/span')
#Algo_Button.click()
time.sleep(3)