#！/usr/bin/env python3
import json
import pandas as pd

def analysis(file,user_id):
    times = 0
    minutes = 0
    try:
        df = pd.read_json(file)
    except ValueError:
        return 0
    times = df[df['user_id']==user_id].minutes.count()
    minutes = df[df['user_id']==user_id].minutes.sum()
    #times = df.groupby('user_id').size().loc[user_id]
    #minutes =df[['user_id','minutes']].groupby('user_id').sum().loc[user_id]
    return times,minutes



