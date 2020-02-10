# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 04:28:31 2020

@author: Jaysn
"""

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
pca_model = PCA()

def pca_plot(features):
    new_features = pca_model.fit_transform(features)
    new_features = new_features.transpose()
    for i in range(len(new_features)):
        plt.plot(new_features[i])
        plt.show()
