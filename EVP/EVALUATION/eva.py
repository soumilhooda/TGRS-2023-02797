import numpy as np
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from keras.models import model_from_json
from matplotlib import pyplot as plt
import pandas
from sklearn.preprocessing import StandardScaler
np.random.seed(7)
#-------------------------------------------------
#-------------------------------------------------
df = read_csv("/home/guest/SMLH/DATA/UCAR/" + "ucar-hum-evp-tmp-prs-2020-india-ntopo.txt", delim_whitespace=True, header=None)
feature_names = ['HUM', 'EVP','TMP', 'PRS', 'REF', 'HGT', 'LAT', 'LON', 'MON', 'DAY', 'HR']
df.columns = feature_names
df['EVP'] = df['EVP']/34.6566
#print(df.head())
#print(df.describe())
#-----------------
X = df.drop(['HUM', 'EVP', 'TMP', 'PRS', 'DAY', 'HR'], axis = 1)
y = df[['LAT','LON','HGT','EVP', 'TMP', 'PRS', 'MON']]
y_no_height = y.iloc[:,3:4].values
y_only_height = y.iloc[:,2:3].values
y_only_latlon = y.iloc[:,:2].values
y_only_month = y.iloc[:,6:7].values
scaler=StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
#-------------------------------------------------
#-------------------------------------------------
######################################################################
# load model and weights
######################################################################
model = Sequential()
json_file = open('model.json', 'r')
loaded_model = json_file.read()
json_file.close()
model = model_from_json(loaded_model)
model.load_weights("model.h5")
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
# -------------------------------------------------
# -------------------------------------------------
predictions20 = model.predict(X_scaled)
Output20 = np.append(y_only_latlon, y_only_height, axis=1)
Output20 = np.append(Output20, y_no_height[:,:1], axis=1)
Output20 = np.append(Output20, predictions20[:,:1],axis=1)
#Output20 = np.append(Output20, y_no_height[:,1:2],axis=1)
#Output20 = np.append(Output20, predictions20[:,1:2],axis=1)
Output20 = np.append(Output20, y_only_month ,axis=1)
print(Output20.shape)
np.savetxt("Output20.txt", Output20, fmt="%10.4f")
# -------------------------------------------------
# -------------------------------------------------
df = read_csv("/home/guest/SMLH/DATA/UCAR/" + "ucar-hum-evp-tmp-prs-2021-india-ntopo.txt", delim_whitespace=True, header=None)
feature_names = ['HUM', 'EVP','TMP', 'PRS', 'REF', 'HGT', 'LAT', 'LON', 'MON', 'DAY', 'HR']
df.columns = feature_names
df['EVP'] = df['EVP']/34.6566
#print(df.head())
#print(df.describe())
#-----------------
X = df.drop(['HUM', 'EVP', 'TMP', 'PRS', 'DAY', 'HR'], axis = 1)
y = df[['LAT','LON','HGT','EVP', 'TMP', 'PRS', 'MON']]
y_no_height = y.iloc[:,3:4].values
y_only_height = y.iloc[:,2:3].values
y_only_latlon = y.iloc[:,:2].values
y_only_month = y.iloc[:,6:7].values
scaler=StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
######################################################################
predictions21 = model.predict(X_scaled)
Output21 = np.append(y_only_latlon, y_only_height, axis=1)
Output21 = np.append(Output21, y_no_height[:,:1], axis=1)
Output21 = np.append(Output21, predictions21[:,:1],axis=1)
#Output21 = np.append(Output21, y_no_height[:,1:2],axis=1)
#Output21 = np.append(Output21, predictions21[:,1:2],axis=1)
Output21 = np.append(Output21, y_only_month ,axis=1)
print(Output21.shape)
np.savetxt("Output21.txt", Output21, fmt="%10.4f")
######################################################################
