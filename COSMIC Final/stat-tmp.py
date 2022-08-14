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
tmp1  = data1[:,3]
tmp2  = data1[:,4]
tmp3  = data2[:,3]
tmp4  = data2[:,4]
tmp5  = data3[:,3]
tmp6  = data3[:,4]

plt.subplots(figsize=(6,12))
#----------------------------------------
#----------------------------------------
plt.subplot(3,1,1)
plt.xlim(150,350)
plt.ylim(150,350)
plt.scatter(tmp1, tmp2, s=0.1)

plt.subplot(3,1,2)
plt.xlim(150,350)
plt.ylim(150,350)
plt.scatter(tmp3, tmp4, s=0.1)

plt.subplot(3,1,3)
plt.xlim(150,350)
plt.ylim(150,350)
plt.scatter(tmp5, tmp6, s=0.1)
plt.show()
rmse1 = metrics.mean_squared_error(tmp1,tmp2,squared=False)
rmse2 = metrics.mean_squared_error(tmp3,tmp4,squared=False)
rmse3 = metrics.mean_squared_error(tmp5,tmp6,squared=False)
print(rmse1)
print(rmse2)
print(rmse3)
#---------------------------
#---------------------------
