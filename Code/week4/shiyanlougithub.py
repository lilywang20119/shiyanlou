#-*coding:utf8-*-
import scrapy

class ShiyanlouGithub(scrapy.Spider):
    name = 'shiyanlou-github'

    @property
    def start_urls(self):
        urls = [
            'https://github.com/shiyanlou?tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wNlQyMjoyMToxMFrOBZKVZw%3D%3D&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories'
        ]
        return urls
    def parse(self, response):
        for resp in response.xpath('//li[contains(@class,"col-12")]'):
            yield {
                'name':resp.xpath('.//h3/a/text()').extract_first().strip(),
                'update_time':resp.xpath('.//relative-time/@datetime').extract_first()
            }