#!/usr/bin/env python3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def data_clean():
    df_temperature = pd.read_csv('GlobalSurfaceTemperature.csv')
    df_co2 = pd.read_csv('CO2ppm.csv')
    df_gas = pd.read_csv('GreenhouseGas.csv')

    df_temperature = df_temperature.set_index('Year')

    df_gas.index = df_gas.Year
    df_gas_drop = df_gas.drop(columns=['Year', 'N2O', 'CH4'])
    df_gas_drop.loc['2014'] = np.NaN
    df_gas_drop.loc['2015'] = np.NaN
    df_gas_drop.loc['2016'] = np.NaN
    df_gas_drop.loc['2017'] = np.NaN
    df_gas2 = df_gas_drop.interpolate()

    df_co2 = df_co2.set_index('Year')
    df_co2.loc['2017'] = np.NaN
    df_co2 = df_co2.interpolate()

    df1 = pd.concat([df_co2, df_gas2], axis=1, join_axes=[df_co2.index])
    df1 = df1.interpolate()

    df2 = pd.concat([df1, df_temperature], axis=1, join_axes=[df1.index])
   # df = df2.iloc[:31, :]
   # df3 = df2.iloc[31:, :]

    return df2



def Temperature():
    df= data_clean()
    feature = df[['CO2 concentrations (NOAA (2017)) (parts per million)', 'CO2']]
    feature_train = feature.iloc[:31,:]
    feature_test = feature.iloc[31:,:]
   # target = df[['Median', 'Upper', 'Lower']]

   # train_feature, test_feature, train_target, test_target =train_test_split(feature, target, test_size=0.33, random_state=56)

    target_Median = df[['Median']]
    target_Median_train = target_Median.iloc[:31,:]
    model_Median = LinearRegression()
    model_Median.fit(feature_train, target_Median_train)
    MedianPredict = model_Median.predict(feature_test)
    #errors = mean_absolute_error(test_target, results)

    target_Upper = df[['Upper']]
    target_Upper_train = target_Upper.iloc[:31, :]
    model_Upper = LinearRegression()
    model_Upper.fit(feature_train, target_Upper_train)
    UpperPredict = model_Upper.predict(feature_test)

    target_Lower = df[['Lower']]
    target_Lower_train = target_Lower.iloc[:31, :]
    model_Lower = LinearRegression()
    model_Lower.fit(feature_train, target_Lower_train)
    LowerPredict = model_Lower.predict(feature_test)

    UpperPredict = np.round(UpperPredict,3)
    MedianPredict = np.round(MedianPredict,3)
    LowerPredict = np.round(LowerPredict,3)
    print(list(UpperPredict),list(MedianPredict),list(LowerPredict))
    return list(UpperPredict),list(MedianPredict),list(LowerPredict)



if __name__ == '__main__':
    Temperature()
