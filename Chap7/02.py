from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
input_first = browser.find_element_by_id("q")  # 获取单个节点
input_second = browser.find_element_by_css_selector("#q")  # 获取单个节点
input_third = browser.find_element_by_xpath('//*[@id="q"]')  # 获取单个节点
# print(input_first, input_second, input_third)
"""
<selenium.webdriver.remote.webelement.WebElement 
(session="4527e67f55248ff39586c65476e4f63e", element="9102371f-4882-4808-a601-e115e240de2b")>
"""

# 第二种写法find_element(By.ID, id)
input_fourth = browser.find_element(By.ID, "q") 
print(input_fourth)

# 对于多个节点的情况，使用find_elements()  返回的是列表的形式，其他的语法和上面一样
browser.close()