#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_clean():
    df_temperature = pd.read_excel('GlobalTemperature.xlsx')
    df_climate = pd.read_excel('ClimateChange.xlsx',sheet_name='Data')

    df_temperature.Date = pd.to_datetime(df_temperature.Date)
    df_temperature.index = df_temperature.Date
    #print(df_temperature)
    df_temperature_drop = df_temperature.drop(columns=['Date','Land Max Temperature', 'Land Min Temperature'])
    #print(df_temperature_drop)
    #df_temperature_date = df_temperature_drop.loc['1990-12-31':'2010-12-31']
    df_temperature_date = df_temperature_drop.iloc[2880:3132, :]
    #print(df_temperature_date)


    df_temperature_A = df_temperature_date.resample('A').mean()

    df_temperature_Q = df_temperature_drop.resample('Q').mean()
    #print(df_temperature_Q )

    df_temperature_A.index = df_temperature_A.index.year
    #print(df_temperature_A)
    df_climate_series = df_climate.loc[df_climate['Series code'].isin(['EN.ATM.CO2E.KT','EN.ATM.METH.KT.CE',
                                                                       'EN.ATM.NOXE.KT.CE','EN.ATM.GHGO.KT.CE','EN.CLC.GHGR.MT.CE' ])]

    #print(df_climate_series)
    df_climate_nan = df_climate_series.replace({'..': pd.np.NaN})
    df_climate_fill = df_climate_nan.iloc[:, 6:27].fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    df_climate_drop = df_climate_fill.dropna(how='all').sum()
    df_climate_result = pd.DataFrame(df_climate_drop, columns=['Total GHG'])
    #print(df_climate_result)
    df_12 = pd.concat([df_climate_result, df_temperature_A], axis=1)

    df_12 = (df_12 - df_12.min()) / (df_12.max() - df_12.min())
    #print(df_12)
    return df_12,df_temperature_Q

def climate_plot():
    df, df_Q = data_clean()
    #print(df_Q)
    fig,axes = plt.subplots(nrows=2, ncols=2)


    ax1 = df.plot(kind='line',ax=axes[0,0],figsize=(16, 9),)
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Values')


    ax2 = df.plot(kind='bar',ax=axes[0,1],figsize=(16, 9),)
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Values')

    ax3 = df_Q.plot(kind='area',ax=axes[1,0],figsize=(16, 9),)
    ax3.set_xlabel('Quarters')
    ax3.set_ylabel('Temperature')


    ax4 = df_Q.plot(kind='kde',ax=axes[1,1],figsize=(16, 9),)
    ax4.set_xlabel('Values')
    ax4.set_ylabel('Values')

    plt.show()

    return fig

if  __name__ == '__main__':
    climate_plot()

