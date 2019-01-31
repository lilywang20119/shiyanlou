#!/usr/bin/env python3
import sys
from pymongo import MongoClient
import pandas as pd

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests
    df = pd.DataFrame(list(contests.find()))
    if user_id in list(df['user_id']):
        group_data = df[['user_id','score','submit_time']].groupby('user_id').sum()
        sort_data = group_data.sort_values(['score','submit_time'],ascending=[0,1])
        reindex_data = sort_data.reset_index()
        reindex_data['rank'] = reindex_data.index + 1
        user_data = reindex_data[reindex_data['user_id']==user_id]
        rank = int(user_data['rank'].values)
        score = int(user_data['score'].values)
        submit_time = int(user_data['submit_time'].values)
    else:
        print('NOTFOUND')
        exit()

    return rank,score,submit_time

if __name__ == '__main__':
    if len(sys.argv) !=2:
        print('Parameter Error')
        exit(1)

    user_id = int(sys.argv[1])
    userdata = get_rank(user_id)
    print(userdata)

