"""
动作链
"""
# from selenium import webdriver
# from selenium.webdriver import ActionChains

# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')  # 切换到iframe
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)  # 实例化一个动作链
# actions.drag_and_drop(source, target)  # 拖拽动作
# actions.perform()  # 执行动作


"""
运行javascript
"""
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 执行js代码
browser.execute_script('alert("To Bottom")')  # 执行js代码
alert = browser.switch_to.alert  # 切换到alert弹窗   有弹窗不能直接调用close()关闭浏览器，会报错，先切换到弹窗关闭
print(alert.text)  # 打印弹窗文本
time.sleep(1)
alert.accept()  # 点击确认按钮
time.sleep(1)
browser.close()