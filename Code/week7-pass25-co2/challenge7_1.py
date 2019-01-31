#!/usr/bin/env python3
import pandas as pd
import numpy as np

def data_clean():
    data = pd.read_excel('ClimateChange.xlsx',sheet_name='Data')


    data = data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    data.drop(data.columns[:5],axis=1,inplace=True)
    #data.drop(labels=['Country name','Series code','Series name','SCALE','Decimals'],axis=1,inplace=True)
    data.replace({'..':np.NaN},inplace=True)
    data = data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    #print(data)
    data.dropna(how='all',inplace=True)
    #print(data)
    data['Sum emissions'] = data.sum(axis=1)
    data = data['Sum emissions']
    #print(data)
    country = pd.read_excel('ClimateChange.xlsx', sheet_name='Country')
    country.set_index('Country code',inplace=True)
    #country.drop(labels=['Capital city', 'Region', 'Lending category'], axis=1,inplace=True)
    #country.set_index('Country code',inplace=True)
    #print(country)
    result = pd.concat([data,country[['Income group','Country name']]],axis=1)

    #print(result)
    return result


def co2():
    df = data_clean()
    df_sum = df.groupby('Income group').sum()
    #要先对values排序再groupby
    df_max = df.sort_values(by='Sum emissions',ascending=0).groupby('Income group').head(1).set_index('Income group')
    #df_max = df.groupby('Income group').max()
    df_max.rename(columns={'Country name': 'Highest emission country',
                           'Sum emissions': 'Highest emissions'}, inplace=True)
    #df_min = df.groupby('Income group').min()
    #print(df_min)
    df_min = df.sort_values(by='Sum emissions',ascending=1).groupby('Income group').head(1).set_index('Income group')
    df_min.rename(columns={'Country name': 'Lowest emission country',
                           'Sum emissions': 'Lowest emissions'}, inplace=True)
    results = pd.concat([df_sum,df_max,df_min],axis=1)

    print(results)
    return results


if __name__ == '__main__':
    co2()
    data_clean()
