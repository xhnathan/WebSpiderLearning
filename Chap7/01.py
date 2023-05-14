from selenium import webdriver

# 1、初始化浏览器对象
# browser = webdriver.Edge()
browser = webdriver.Chrome()
# browser = webdriver.Safari()

# 2、访问页面
browser.get('https://www.taobao.com')
print(browser.page_source)  # 打印页面源码
browser.close()