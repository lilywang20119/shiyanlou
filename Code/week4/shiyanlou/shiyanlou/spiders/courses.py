# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseItem


class CoursesSpider(scrapy.Spider):
    name = 'courses'
    @property

    def start_urls(self):
        urls= 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (urls.format(i) for i in range(1,24))

    def parse(self, response):
        for course in response.xpath('//div[@class="course-body"]'):
            item = CourseItem()
            item['name'] = course.xpath('.//div[class="course-name"]/text()').extract_first()
            item['description'] = course.xpath('.//div[@class="course-desc"]/text()').extract_first()
            item['type'] = course.xpath('.//span[contains(@class,"pull-right")]/text()').extract_first(default="Free")
            item['students'] = course.xpath('.//span[contains(@class,"pull-left")]/text()[2]').re_first('\s*(\d+)\s*')
        yield item
