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
hum1  = 34.2383*data1[:,3]
hum2  = 34.2383*data1[:,4]
hum3  = 34.2383*data2[:,3]
hum4  = 34.2383*data2[:,4]
hum5  = 34.2383*data3[:,3]
hum6  = 34.2383*data3[:,4]

plt.subplots(figsize=(6,12))
#----------------------------------------
#----------------------------------------
plt.subplot(3,1,1)
plt.xlim(-10,60)
plt.ylim(-10,60)
plt.scatter(hum1, hum2, s=0.1)

plt.subplot(3,1,2)
plt.xlim(-10,60)
plt.ylim(-10,60)
plt.scatter(hum3, hum4, s=0.1)

plt.subplot(3,1,3)
plt.xlim(-10,60)
plt.ylim(-10,60)
plt.scatter(hum5, hum6, s=0.1)
plt.show()
rmse1 = metrics.mean_squared_error(hum1,hum2,squared=False)
rmse2 = metrics.mean_squared_error(hum3,hum4,squared=False)
rmse3 = metrics.mean_squared_error(hum5,hum6,squared=False)
print(rmse1)
print(rmse2)
print(rmse3)
#---------------------------
#---------------------------
