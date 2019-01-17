#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from lxml import etree

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://category.vip.com/search-3-0-1.html?q=3|30036||&rp=30074|30063&ff=women|0|2|2&adidx=1&f=ad&adp=65001&adid=326630")
time.sleep(3)
for i in range(1,10):
        js = "var q=document.body.scrollTop" + str(500*i)
        js = "var q=document.documentElement.scrollTop" + str(500*i)

        driver.execute_script(js)
        print('========================')
        time.sleep(3)

html = etree.HTML(driver.page_source)
all_img_list = []

img_group_list = html.xpath('//img[contains(@id,"J_pic")]')

for img_group in img_group_list:
        img_of_group = img_group.xpath('.//@data-original | .//@data-img-back | .//@data-img-side')
        print(img_of_group)
        all_img_list.append('\n'.join(img_of_group)+'\n')

with open('vip.txt','w',encoding='utf8') as f:
        f.write('\n'.join(all_img_list))

"""

#print(driver.save_screenshot("zhihu_nocookies.png"))

#zhihu_cookies = {
# 'aliyungf_tc' : 'AQAAAAR4YFOeswAAnLFJcVRd4MKOTTXu',
        'l_n_c': '1',
        'q_c1': '8572377703ba49138d30d4b9beb30aed|1514626811000|1514626811000',
        'r_cap_id': 'MTc5M2Y0ODUzMjc0NDMzNmFkNTAzZDBjZTQ4N2EyMTc=|1514626811|a97b2ab0453d6f77c6cdefe903fd649ee8531807',
        'cap_id': 'YjQyZTEwOWM4ODlkNGE1MzkwZTk3NmI5ZGU0ZTY2YzM=|1514626811|d423a17b8d165c8d1b570d64bc98c185d5264b9a',
        'l_cap_id': 'MGE0NjFjM2QxMzZiNGE1ZWFjNjhhZmVkZWQwYzBkZjY=|1514626811|a1eb9f2b9910285350ba979681ca804bd47f12ca',
        'n_c': '1',
        'd_c0': 'AKChpGzG6QyPThyDpmyPhXaV-B9_IYyFspc=|1514626811',
        '_xsrf': 'ed7cbc18-03dd-47e9-9885-bbc1c634d10f',
        'capsion_ticket': '2|1:0|10:1514626813|14:capsion_ticket|44:NWY5Y2M0ZGJiZjFlNDdmMzlkYWE0YmNjNjA4MTRhMzY=|6cf7562d6b36288e86afaea5339b31f1dab2921d869ee45fa06d155ea3504fe1',
        '_zap': '3290e12b-64dc-4dae-a910-a32cc6e26590',
        'z_c0': '2|1:0|10:1514626827|4:z_c0|92:Mi4xYm4wY0FRQUFBQUFBb0tHa2JNYnBEQ1lBQUFCZ0FsVk5DNjAwV3dCb2xMbEhxc1FTcEJPenpPLWlqSS1qNm5KVEFR|d89c27ab659ba979a977e612803c2c886ab802adadcf70bcb95dc1951bdfaea5',
        '__utma': '51854390.2087017282.1514626889.1514626889.1514626889.1',
        '__utmb': '51854390.0.10.1514626889',
        '__utmc': '51854390',
        '__utmz': '51854390.1514626889.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        '__utmv': "51854390.100--|2=registration_date=20150408=1'3=entry_date=20150408=1",
#}
"""
#for k,v in zhihu_cookies.items():
 #   driver.add_cookie({'domain': 'zhihu.com','name': k,'value': v })

#driver.get("https://www.zhihu.com")
#time.sleep(3)
#print(driver.save_screenshot("zhihu_cookies.png"))
#driver.find_element_by_id("loginName").send_keys("515388298@qq.com")


#driver.find_element_by_id("loginPassword").send_keys('wyl000000')
#driver.find_element_by_id("loginAction").click()
#time.sleep(3)

#print(driver.save_screenshot("jietu.png"))

#print(driver.page_source)

#driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
#driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

#driver.find_element_by_id("kw").send_keys('美女')
#driver.find_element_by_id("su").send_keys(Keys.RETURN)
#time.sleep(3)

#driver.find_element_by_id("kw").clear()
#driver.save_screenshot("美女.png")

#print(driver.current_url)


#data = driver.find_element_by_id("wrapper").text
#print(data)

#print(driver.title)
#driver.save_screenshot("baidu.png")
driver.quit()