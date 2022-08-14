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
hum1  = data1[:,1]
hum2  = data1[:,2]
hum3  = data2[:,1]
hum4  = data2[:,2]
hum5  = data3[:,1]
hum6  = data3[:,2]
aa1 = np.exp(hum1)
aa2 = np.exp(hum2)
aa3 = np.exp(hum3)
aa4 = np.exp(hum4)
aa5 = np.exp(hum5)
aa6 = np.exp(hum6)
aa1 = aa1/100.0
aa2 = aa2/100.0
aa3 = aa3/100.0
aa4 = aa4/100.0
aa5 = aa5/100.0
aa6 = aa6/100.0

plt.subplots(figsize=(6,12))
#----------------------------------------
#----------------------------------------
plt.subplot(3,1,1)
plt.xlim(-10,80)
plt.ylim(-10,80)
plt.scatter(aa1, aa2, s=0.1)

plt.subplot(3,1,2)
plt.xlim(-10,80)
plt.ylim(-10,80)
plt.scatter(aa3, aa4, s=0.1)

plt.subplot(3,1,3)
plt.xlim(-10,80)
plt.ylim(-10,80)
plt.scatter(aa5, aa6, s=0.1)
plt.show()
rmse1 = metrics.mean_squared_error(aa1,aa2, squared=False)
rmse2 = metrics.mean_squared_error(aa3,aa4, squared=False)
rmse3 = metrics.mean_squared_error(aa5,aa6, squared=False)
print(rmse1)
print(rmse2)
print(rmse3)
#---------------------------
#---------------------------
