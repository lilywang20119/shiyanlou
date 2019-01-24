# -*- coding: utf-8 -*-
import scrapy
from douban2.items import Douban2Item
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor





class AwesomeMovieSpider(scrapy.spiders.CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']
    rules = (Rule(LinkExtractor(allow='https://movie.douban.com/subject/.*/?from=subject-page'),
                  callback='parse_page',follow=True),)



    def parse_movie_item(self, response):
        item = Douban2Item()
        item['url'] = response.url
        item['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first()
        item['summary'] = response.xpath('//span[@property="v:summary"]/text()').extract_first()
        item['score'] = response.xpath('//strong[@property="v:average"]/text()').extract_first()

        return item

    def parse_start_url(self,response):
        yield self.parse_movie_item(response)


    def parse_page(self,response):
        yield self.parse_movie_item(response)