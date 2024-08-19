from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text="달러 환율"
search_box=driver.find_element(by=By.CSS_SELECTOR,value="#query")
search_box.send_keys(query_text)
search_button=driver.find_element(by=By.ID,value="search-btn")
search_button.click()
temp_div=driver.find_element(by=By.CSS_SELECTOR,value="#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.gsrt.GDBPqd > span.DFlfde.SwHCTb")
time.sleep(10)
#김건호


