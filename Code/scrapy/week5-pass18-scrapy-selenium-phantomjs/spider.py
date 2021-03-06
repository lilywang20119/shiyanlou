#!/usr/bin/env python3
import scrapy
import json
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



results = []
def parse(response):
    for comment in response.css('div.comment-list-item'):
        result = {
            'name': comment.xpath('.//div[@class="user-username"]/a/text()').extract_first().strip(),
            'content':comment.xpath('.//div[@class="comment-item-content markdown-box"]/p/text()').extract_first(),
        }
        print("comment:{}".format(result))

        results.append(result)

def has_next_page(response):

    classes = response.xpath('//li[contains(@class,"next-page")]/@class').extract_first()  #link
    return 'disabled' not in classes





def goto_next_page(driver):

    driver.find_element_by_xpath('//li[contains(@class,"next-page")]').click()



def wait_page_return(driver,page):
    WebDriverWait(driver,10).until(
        EC.text_to_be_present_in_element((By.XPATH,'//ul[@class="pagination"]/li[@class="active"]'),str(page))
    )

def spider():
    driver = webdriver.Chrome()
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)
    page = 1

    while True:
        wait_page_return(driver,page)
        html = driver.page_source
        response = HtmlResponse(url=url,body=html.encode('utf8'))
        parse(response)

        if not has_next_page(response):
            break

        page +=1
        goto_next_page(driver)

    with open('/Users/lilywang/PycharmProjects/shiyanlou/scrapy/comments.json','w') as f:
        f.write(json.dumps(results))


if __name__ == '__main__':
    spider()