# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import GithubItem


class RepositorySpider(scrapy.Spider):
    name = 'repository'
    @property
    def start_urls(self):
        urls = ['https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories'
                ]
        return (urls)

    def parse(self, response):
        for res in response.css('li.col-12'):
            item = GithubItem({
                'name' : res.xpath('.//a/text()').extract_first().strip(),
                'update_time' : res.xpath('.//relative-time/@datetime').extract_first()
        })
            yield item






