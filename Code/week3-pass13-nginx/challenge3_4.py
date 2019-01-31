#!/usr/bin/env python3
import re
from datetime import datetime
import pandas as pd

def open_parses(filename):
    with open(filename) as logfile:
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP 地址
                   r'\[(.+)\]\s'  # 时间
                   r'"GET\s(.+)\s\w+/.+"\s'  # 请求路径
                   r'(\d+)\s'  # 状态码
                   r'(\d+)\s'  # 数据大小
                   r'"(.+)"\s'  # 请求头
                   r'"(.+)"'  # 客户端信息
                   )
        parsers = re.findall(pattern,logfile.read())
    return parsers

def main():
    logs = open_parses('nginx.log')
    df = pd.DataFrame(logs,columns=['IP','date','url','statuscode','datasize','requesthead','clientinfo'])
    df.date = df.date.map(lambda x: x.split(':')[0])
    group_data1 = df[df['date'] == '11/Jan/2017']
    count_data1 = group_data1['IP'].value_counts()
    ip_dict = {str(count_data1.index[0]):count_data1[0]}
    group_data2 = df[df['statuscode']=='404']
    count_data2 = group_data2['url'].value_counts()
    url_dict = {str(count_data2.index[0]):count_data2[0]}

    return ip_dict,url_dict

if __name__ == '__main__':
    ip_dict,url_dict = main()
    print(ip_dict,url_dict)




