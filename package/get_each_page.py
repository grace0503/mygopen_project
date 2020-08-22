from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# 開啟Chrome 好翻譯 Javascript
driver = webdriver.Chrome()
a_text = ''
for k in range(1,4,1):
    url = 'https://www.mygopen.com/search/label/%E8%AC%A0%E8%A8%80#archive-page-'+str(k)
    driver.get(url)
    # driver.refresh()
    # 抓取 Elements : 抓 href > 抓 a/裡的文字 > 抓每一頁 > 存在csv裡 > 抓其他看板 > 存檔
    a_tag = driver.find_elements_by_css_selector('.item-content .item-title a')
    for i in range(len(a_tag)):
        href_attr = a_tag[i].get_attribute('href')
        print(href_attr)
    for j in range(len(a_tag)):
        a_text = a_text + '\n' + a_tag[j].text
        # print(a_text)
    # driver.find_element_by_class_name('.shad.archive-page-pagination-button archive-page-pagination-button-'+str(i+1)).click()

print(a_text)