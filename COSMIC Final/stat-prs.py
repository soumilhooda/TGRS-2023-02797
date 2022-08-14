import numpy as np
import math
from matplotlib import pyplot as plt
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from keras.models import model_from_json
from sklearn import metrics

data1 = np.loadtxt('Output20_Train.txt')
data2 = np.loadtxt('Output20_Test.txt')
data3 = np.loadtxt('Output21_Test.txt')
prs1  = data1[:,5]
prs2  = data1[:,6]
prs3  = data2[:,5]
prs4  = data2[:,6]
prs5  = data3[:,5]
prs6  = data3[:,6]

plt.subplots(figsize=(6,12))
#----------------------------------------
#----------------------------------------
plt.subplot(3,1,1)
plt.xlim(0,1150)
plt.ylim(0,1150)
plt.scatter(prs1, prs2, s=0.1)

plt.subplot(3,1,2)
plt.xlim(0,1150)
plt.ylim(0,1150)
plt.scatter(prs3, prs4, s=0.1)

plt.subplot(3,1,3)
plt.xlim(0,1150)
plt.ylim(0,1150)
plt.scatter(prs5, prs6, s=0.1)
plt.show()
rmse1 = metrics.mean_squared_error(prs1,prs2,squared=False)
rmse2 = metrics.mean_squared_error(prs3,prs4,squared=False)
rmse3 = metrics.mean_squared_error(prs5,prs6,squared=False)
print(rmse1)
print(rmse2)
print(rmse3)
#---------------------------
#---------------------------
