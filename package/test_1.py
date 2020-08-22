from selenium import webdriver
# 開啟Chrome 好翻譯 Javascript
driver = webdriver.Chrome()
url = 'https://www.mygopen.com/search/label/%E8%AC%A0%E8%A8%80'
driver.get(url)
# 抓取 Elements : 抓 href > 抓 a/裡的文字 > 抓每一頁 > 存在csv裡 > 抓其他看板 > 存檔
a_tag = driver.find_elements_by_css_selector('.item-content .item-title a')
#don't know why it said 'list out of range.'
# a_text = a_tag[0].text
# print(a_text)

for i in range(len(a_tag)):
    href_attr = a_tag[i].get_attribute('href')
    print(href_attr)
for j in range(len(a_tag)):
    a_text = a_tag[j].text
    print(a_text)