#!/usr/bin/env python3
#-*-coding:utf8-*-

import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    #在全collections20条记录中，统计指定用户的总分数和总提交时间
    pipeline = [
        #选取指定用户记录
        {'$match':{'user_id':user_id}},
        #按用户ID分组统计总分数和总时间，由于只选取一个用户的记录，所以分组只有一个
        {'$group':{
            '_id':'$user_id',
            'total_score':{'$sum':'$score'},
            'total_time':{'$sum':'$submit_time'}
        }}
    ]
    #通过list转换，读取到所有结果，db.contests.aggregate是个多集合，每个集合对应一个id
    #results = [{'$user_id','total_score','total_time'},{},{}],其实里面最多一条有用记录
    results = list(contests.aggregate(pipeline))
    #指定用户不存在
    if len(results) == 0:
        print('NOTFOUND')
        sys.exit(0)

    # results[0],从第一条记录开始
    data = results[0]
#在全collections20条记录中，计算指定用户排名信息
    pipeline = [
        #分组计算所有用户的总分数和总时间
        { '$group':{
            '_id':'$user_id',
            'total_score':{'$sum':'$score'},
            'total_time':{'$sum':'$submit_time'}
        }},
        #从上一步的分组结果筛选出排在指定用户之前的，也就是总分比指定用户高或者总分相等但总时间较少的
        {'$match':{
            '$or':[
                {'total_score':{'$gt': data['total_score']}},
                {'total_time':{'$lt': data['total_time']},
                 'total_score':data['total_score']
                 }
            ]
        }},
        #$match用于筛选记录，将符合条件的记录送到下一步$group进行处理
        #把上一步筛选出来的文档归为一个分组（_id 为NONE）并计算总数（count是排在该ID前面的人数，+1就是该ID在所有人中的排名）
        {'$group':{'_id':None,'count':{'$sum':1}}}
    ]

    results = list(contests.aggregate(pipeline))
    #results =[{'NOne','count'},]
    # 实际上只有一条结果results[0]是选取那个有用记录的意思
    if len(results)> 0:
        rank = results[0]['count'] + 1
    else:
        #结果集为空，代表没有比用户更高排名的，该用户排名第一
        rank = 1

    score = data['total_score']
    submit_time = data['total_time']
    return rank,score,submit_time

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Parameter Error")
        sys.exit(1)
    user_id = int(sys.argv[1])
    userdata = get_rank(user_id)
    print(userdata)