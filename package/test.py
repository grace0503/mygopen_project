from selenium import webdriver
# 開啟Chrome 好翻譯 Javascript
driver = webdriver.Chrome()
url = 'https://www.mygopen.com/search/label/%E8%AC%A0%E8%A8%80'
driver.get(url)
# 抓取 Elements
a_tag = driver.find_elements_by_css_selector('.item-content .item-title a')
# for href_attr in a_tag:
#     all_href = href_attr.get_attribute('href')
#     print(all_href)
for i in range(len(a_tag)):
    href_attr = a_tag[i].get_attribute('href')
    print(href_attr)