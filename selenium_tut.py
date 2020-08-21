from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

#PATH for webdriver and also extra \ because windows reads \\ as \
path = "E:\\algorithms\dashboard\hackerrank_dashboard\geckodriver.exe"

URL = "https://cn.bing.com"

fellow = webdriver.Firefox(executable_path=path)

fellow.get(URL)

#print(fellow.title)

search = fellow.find_element_by_name("q")
search.send_keys("hello world")
search.send_keys(Keys.RETURN)

#wait to be clicable
#wait = WebDriverWait(fellow, 10)
#element = wait.until(EC.element_to_be_clickable((By.ID, "b_results")))


#wait for presence
try:
    main = WebDriverWait(fellow, 10).until(
        EC.presence_of_element_located((By.ID, "b_results"))
    )
    articles = main.find_element_by_class("b_algo")
    print(articles.text)
except:
    time.sleep(10)
    fellow.quit()
#
#main = fellow.find_element_by_id("b_results")
#print(main.text)
#fellow.quit()
