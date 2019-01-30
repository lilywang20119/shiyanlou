# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import redis
from scrapy.exceptions import DropItem

class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        item['score'] = float(item['score'])
        if item['score'] < 8.0:
            raise DropItem('score less than 8.0')


        self.redis.lpush('douban_movie:items',json.dumps(dict(item)))
 #       if self.redis.llen('douban_movie:items') > 30:
  #          self.redis.shutdown()

        return item


    def open_spider(self,spider):
        self.redis = redis.StrictRedis(host='localhost',port=6379,db=0)

    def close_spider(self,spider):
        pass
