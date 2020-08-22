# 抓取 Elements : 抓 href > 抓 a/裡的文字 > 抓每一頁 > 存在csv裡 > 抓其他看板 > 存檔
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# 開啟Chrome 好翻譯 Javascript
driver = webdriver.Chrome()
text_a = ''
a_href = ''
#抓每一頁
for k in range(1,4,1):
    url = 'https://www.mygopen.com/search/label/%E8%AC%A0%E8%A8%80#archive-page-'+str(k)
    driver.get(url)
    driver.refresh()
    # WebDriverWait(driver,10).until(get_a_text_And_Href)
    WebDriverWait(driver,10).until(lambda d: d.find_elements_by_css_selector('.item-content .item-title a'))
    a_tag_1 = driver.find_elements_by_css_selector('.item-content .item-title a')
    for j in range(len(a_tag_1)):
        a_href = a_href + '\n' + a_tag_1[j].get_attribute('href')
        text_a = text_a + '\n' + a_tag_1[j].text
    print(a_href)
    print(text_a)
