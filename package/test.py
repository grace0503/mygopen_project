from selenium import webdriver
# 開啟Chrome 好翻譯 Javascript
driver = webdriver.Chrome()
url = 'https://www.mygopen.com/search/label/%E8%AC%A0%E8%A8%80'
driver.get(url)
# 抓取 Elements
a_tag = driver.find_elements_by_css_selector('.item-content .item-title a')
href_attr = a_tag[0].get_attribute('href')
print(href_attr)