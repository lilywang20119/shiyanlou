#!/usr/bin/env python3
import scrapy

class ShiyanlouGithubSpider(scrapy.Spider):
    name = 'shiyanlou-github'
    @property
    def start_urls(self):
        urls = ['https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories'
                ]
        return (urls)



    def parse(self, response):
        for directory in response.css('li.col-12'):
            yield{
                'name':directory.xpath('.//a/text()').extract_first().strip(),
                'updated_time':directory.xpath('.//relative-time/@datetime').extract_first()
            }
