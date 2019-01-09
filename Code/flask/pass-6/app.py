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
from flask import render_template,abort

app = Flask('__name__')

class File(object):
    directory = os.path.normpath(os.path.join(os.path.dirname('__file__'),'..','files'))


    def __init__(self):
        self._files = self._read_all_files()

    def _read_all_files(self):
        result={}
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory,filename)
            with open(file_path) as f:
                result[filename[:-5]]=json.load(f)
        return result

    def get_title_list(self):
        return [item['title'] for item in self._files.values()]

    def get_by_filename(self,filename):
        return self._files.get(filename)

files = File()

@app.route('/')
def index():

    return render_template('index.html',title_list=files.get_title_list())

@app.route('/files/<filename>')
def file(filename):
    file_item = files.get_by_filename(filename)
    if not file_item:
        abort(404)
    return render_template('file.html',file_item=file_item)

@app.route('/nothing')#@app.erroehandler(404)
def nothing():
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run()
    


