# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, User, engine
from shiyanlou.items import CourseItem, UserItem
from scrapy.exceptions import DropItem
from datetime import datetime

class ShiyanlouPipeline(object):



    def process_item(self, item, spider):
        if isinstance(item, CourseItem):
            self._process_course_item(item)
        else:
            self._process_user_item(item)

    def _process_course_item(self,item):
        item['students'] = int(item['students'])

        if item['students'] <1000:
            raise DropItem('Course student less than 1000')
        else:
            self.session.add(Course(**item))
        return item

    def _process_user_item(self,item):
        item['level'] = int(item['level'][1:])
        item['learn_courses_num'] = int(item['learn_courses_num'])
        item['join_date'] = datetime.strptime(item['join_date'].split()[0],'%Y-%m-%d').date()
        self.session.add(User(**item))

    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
