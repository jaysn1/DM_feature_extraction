# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 02:34:34 2020

@author: Jaysn
"""

#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import feature_extraction as fe
import pca_plot as pp

#Load data for each patient
data1 = pd.read_csv("DataFolder/CGMSeriesLunchPat1.csv")
data2 = pd.read_csv("DataFolder/CGMSeriesLunchPat2.csv")
data3 = pd.read_csv("DataFolder/CGMSeriesLunchPat3.csv")
data4 = pd.read_csv("DataFolder/CGMSeriesLunchPat4.csv")
data5 = pd.read_csv("DataFolder/CGMSeriesLunchPat5.csv")

#Data Cleaning
def clean_data(data):
    data = data.iloc[:,:30]
    nan = data.isna().sum(axis = 1)
    for i in range(0,len(data)):
        if nan[i] >= 1:
            data = data.drop(nan.index[i])
    return data

data1 = clean_data(data1)
data2 = clean_data(data2)
data3 = clean_data(data3)
data4 = clean_data(data4)
data5 = clean_data(data5)
data1.to_csv('Data/PatientData1.csv', index = False)
data2.to_csv('Data/PatientData2.csv', index = False)
data3.to_csv('Data/PatientData3.csv', index = False)
data4.to_csv('Data/PatientData4.csv', index = False)
data5.to_csv('Data/PatientData5.csv', index = False)
final_data = pd.concat([data1, data2, data3, data4, data5])

features = []
#Feature 1
feature = fe.absolute_sum(final_data)
features.append(feature)

#Feature 2
feature = fe.autocorrelation(final_data)
features.append(feature)

#Feature 3
feature = fe.fft(final_data)
features.append(feature)

#Feature 4
feature = fe.longest_strike(final_data)
features.append(feature)

#Feature 5
feature = fe.max_slope_after_food(final_data)
features.append(feature)

#Feature Matrix
features = pd.DataFrame(features).transpose()

#Plot PCA values
pp.pca_plot(features)

features.plot.box(grid = True)





