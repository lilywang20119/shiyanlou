#-*-coding:utf8-*-
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    name = 'shiyanlou-courses'
    @property
    def start_urls(self):
        url_start = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (url_start.format(i) for i in range(1,24))




    def parse(self, response):
        for course in response.xpath('//div[@class="course-body"]'):
            yield {
                'name':course.xpath('.//div[@class="course-name"]/text()').extract_first(),
                'description':course.xpath('.//div[@class="course-desc"]/text()').extract_first(),
                'type':course.xpath('.//span[contains(@class,"pull-right")]/text()').extract_first(default='Free'),
                'students':course.xpath('.//span[contains(@class,"pull-left")]/text()').re_first('\s*(\d+)\s*')
            }
