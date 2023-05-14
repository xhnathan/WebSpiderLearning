from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
input = browser.find_element(By.ID, "q")
input.send_keys("iPhone") # 输入iphone
time.sleep(1)
input.clear()   # 清空搜索栏
input.send_keys("iPad") # 输入ipad
button = browser.find_element(By.CLASS_NAME, "btn-search")
button.click()  # 点击操作
