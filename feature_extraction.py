# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 02:12:09 2020

@author: Jaysn
"""
from tsfresh import feature_extraction as fe
features = []

# Feature 1
def absolute_sum(data):
    feature = []
    for i in range(len(data)):
        feature.append(fe.feature_calculators.absolute_sum_of_changes(data.to_numpy()[i]))
    return feature
    

def autocorrelation(data):
    feature = []
    for i in range(len(data)):
        feature.append(fe.feature_calculators.autocorrelation(data.to_numpy()[i],5))
    return feature

def fft(data):
    feature = []
    for i in range(len(data)):
        feature.append(list(fe.feature_calculators.fft_coefficient(data.to_numpy()[i],[{"coeff":1,"attr":"real"}]))[0][1])
    return feature

def longest_strike(data):
    feature = []
    for i in range(len(data)):
        feature.append(fe.feature_calculators.longest_strike_above_mean(data.to_numpy()[i]))
    return feature
    
def max_slope_after_food(data):
    feature = []
    for i in range(len(data)):
        max_slope = float('-inf')
        for j in range(20):
            slope_edges = [data.iloc[i,j],data.iloc[i,j+10]]
            slope = difference(slope_edges)
            if max_slope < slope:
                max_slope = slope
                max_slope_start = j
        feature.append(max_slope_start - 5)
    return feature
        
def difference(points):
    return (points[0] - points[1])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        