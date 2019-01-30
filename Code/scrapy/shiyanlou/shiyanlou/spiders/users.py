# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem


class UsersSpider(scrapy.Spider):
    name = 'users'

    @property
    def start_urls(self):
        url_tmpl= 'https://www.shiyanlou.com/user/{}/'
        return (url_tmpl.format(i) for i in range(1000,2000))
#name,type join_date level status  school_job learn_courses_num
    def parse(self, response):
        item = UserItem({
            'name':response.css('span.username::text').extract_first(),
            'level':response.css('span.user-level::text').extract_first(),
            'type': response.css('a.member-icon img.user-icon::attr(title)').extract_first(default='普通用户'),
            'status':response.xpath('//div[@class="userinfo-banner-status"]/span[1]/text()').extract_first(),
            'school_job':response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),
            'join_date':response.css('span.join-date::text').extract_first(),
            #'learn_courses_num':response.xpath('//span[@class="latest-learn-num"]/text()').extract_first()
            'learn_courses_num': response.css('span.latest-learn-num::text').extract_first()


        })
        yield item