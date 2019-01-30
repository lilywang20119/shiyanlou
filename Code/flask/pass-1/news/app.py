#!/usr/bin/env python3

from flask import Flask
import os
import json
from flask import render_template

app = Flask('__name__')

@app.route('/')
def index():
    files_list = os.listdir('/home/shiyanlou/files')
    print(files_list)

    data = []
    data_title = []
    for i in files_list:
        with open(os.path.join('/home/shiyanlou/files',i),'r') as f:
            data.append(json.load(f))
    for j in range(len(data)):
        data_title.append(data[j]['title'])
    #print(data_title)



    return render_template('index.html',data=data_title)



@app.route('/files/<filename>')
def file(filename):
    files_list = os.listdir('/home/shiyanlou/files')
    print(files_list)

    data = []
    data_content = []
    if filename + '.json' in files_list:
        for i in files_list:
            with open(os.path.join('/home/shiyanlou/files', i), 'r') as f:
                 data.append(json.load(f))
        for j in range(len(data)):

            data_content.append(data[j]['content'])

        return render_template('file.html', data=data_content)
    else:
        return render_template('404.html',)

@app.route('/nothing')
def nothing():
    return render_template('404.html', )


if __name__ == '__main__':
    app.run()

