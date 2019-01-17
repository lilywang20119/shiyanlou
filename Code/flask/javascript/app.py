#!/usr/bin/env python3
#-*-coding:utf-8-*-
#1.读取/home/shiyanlou/files目录下json title >>> app.py def index [os.listdir] data=json.load(f) render_template >>index.html
#return data['title']
#2.分别读取/home/shiyanlou/files/<filename>下的json内容>>app.py  def file  if os.path.exits {data['content']} render_template>>file.html
# or{404}>>404.html
#base.html>>模版继承 block  extends
#3.flask run 3000
#4 404 notfound
from flask import Flask
import os
import json
from flask import render_template
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pymongo import MongoClient


app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)
client = MongoClient('127.0.0.1',27017)
db_m = client.shiyanlou

class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category')


    def __init__(self,title,category,content,created_time=None):
        self.title = title
        self.category = category
        self.content = content
        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time

    def add_tag(self,tag_name):
        file_item = db_m.files.find_one({'file_id':self.id})
        if file_item:
            tags = file_item['tags']
            if tag_name not in tags:
                tags.append(tag_name)
            db_m.files.update_one({'file_id':self.id},{'$set':{'tags':tags}})

        else:
            tags = [tag_name]
            db_m.files.insert_one({'file_id':self.id,'tags':tags})
        return tags

    def remove_tag(self,tag_name):
        file_item = db_m.files.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            try:
                tags.remove(tag_name)
                new_tags = tags
            except ValueError:
                return tags
            db_m.files.update_one({'file_id':self.id},{'$set':{'tags':tags}})
            return new_tags
        return []

    def __repr__(self):
        return "<File(name=%s)>" %self.name

    @property
    def tags(self):
        file_item = db_m.files.find_one({'file_id':self.id})
        if file_item:
            return file_item['tags']
        else:

            return []


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File')

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "<Category(name=%s)>" %self.name

def insert_datas():
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', java, 'File Content - Java is cool!')
    file2 = File('Hello Python', python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()

    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')


@app.route('/')
def index():

    return render_template('index.html',files=File.query.all())



@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html',file_item=file_item)

@app.route('/nothing')
def nothing():
    return render_template('404.html', )




if __name__ == '__main__':
    app.run()


