#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def data_clean():
    data = pd.read_excel('ClimateChange.xlsx',sheet_name='Data').set_index('Country code')
    #print(data)
    data_co2 = data[data['Series code'] == 'EN.ATM.CO2E.KT']
    #data_co2.drop(columns=['Country name','Series code','Series name', 'SCALE', 'Decimals'], inplace=True)
    data_co2_nan = data_co2.replace({'..': np.NaN})
    #我出错在这里下面等式没有写等号赋值
    data_co2_fill = data_co2_nan.iloc[:,5:].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)

    data_co2_fill['co2-sum'] = data_co2_fill.sum(axis=1)



    data_gdp = data[data['Series code'] == 'NY.GDP.MKTP.CD']

    #data4 = pd.DataFrame(data3,columns=['gdp-sum'])
    #data_gdp.drop(columns=['Country name','Series code','Series name', 'SCALE', 'Decimals'], inplace=True)
    data_gdp_nan = data_gdp.replace({'..': np.NaN})
    data_gdp_fill = data_gdp_nan.iloc[:,5:].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data_gdp_fill['gdp-sum'] = data_gdp_fill.sum(axis=1)

    data_merge = pd.concat([data_co2_fill['co2-sum'], data_gdp_fill['gdp-sum']], axis=1)
    data_merge = data_merge.fillna(value=0)
    #data_merge = data_merge.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
    data_merge = (data_merge-data_merge.min())/(data_merge.max()-data_merge.min())
    #print(data_merge)
    return data_merge



def co2_gdp_plot():
    df = data_clean()
    #print(df)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('GDP-CO2')
    ax.set_xlabel('Countries')
    ax.set_ylabel('Values')

    countries_labels = ['USA', 'CHN', 'FRA', 'RUS', 'GBR']
    xticks = []
    xticks_position = []
    for i in range(len(df)):
        if df.index[i] in countries_labels:
            xticks.append(df.index[i])
            xticks_position.append(i)

    ax.set_xticks(xticks_position)
    ax.set_xticklabels(xticks,rotation='vertical')
    ax.plot(df['co2-sum'].values,'b-',label="CO2-SUM")
    ax.plot(df['gdp-sum'].values,'r-',label="GDP-SUM")
    ax.legend(loc=2)
    fig.show()
    plt.show()

    china_co2 = np.round(df.loc['CHN'][0],3).tolist()
    china_gdp = np.round(df.loc['CHN'][1],3).tolist()
    china = [china_co2,china_gdp]

    print(china)

    return ax,china

if __name__ == '__main__':
    data_clean()
    co2_gdp_plot()