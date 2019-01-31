#!/usr/bin/env python3
import pandas as pd

def quarter_volume():
    """
    data = pd.read_csv('apple.csv',header=0)
    data1 = data[['Date','Volume']].groupby('Date').sum()
    i = pd.to_datetime(data1.index)
    data2 = pd.Series(data1.Volume,i)
    data3 = data2.resample('Q').sum()
    second_volume = data3.sort_values(ascending=False)[1]
    """
    df = pd.read_csv('apple.csv',header=0)
    s = df.Volume
    s.index = pd.to_datetime(df.Date)
    second_volume = s.resample('Q').sum().sort_values(ascending=False)[1]

    return second_volume
if __name__ == '__main__':
    quarter_volume()