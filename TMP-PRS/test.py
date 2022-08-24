import numpy as np
from pandas import read_csv
from tensorflow import keras
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
df = read_csv("/home/deep/RAN/DATA/UCAR/" + "ucar-hum-evp-tmp-prs-2020-india-ntopo.txt", delim_whitespace=True, header=None)
feature_names = ['HUM', 'EVP','TMP', 'PRS', 'REF', 'HGT', 'LAT', 'LON', 'MON', 'DAY', 'HR']
df.columns = feature_names
#df['PRS'] = df['PRS']/1046.15
#df['EVP'] = np.log(df['EVP'])
#df['REF'] = np.log(df['REF'])
#df['LAT'] = np.abs(df['LAT'])
#df['LON'] = np.abs(df['LON'])
#df['EVP'] = np.exp(df['EVP'])
#df['EVP'] = df['EVP']*100
print(df.head())
print(df.describe())
#-----------------
X = df.drop(['HUM', 'EVP', 'TMP', 'PRS',  'DAY', 'HR'], axis = 1)
y = df[['LAT','LON','HGT','EVP', 'TMP', 'PRS', 'MON']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 20)
#y_train_no_height = y_train.iloc[:,3:6].values
#y_test_no_height = y_test.iloc[:,3:6].values
y_train_no_height = y_train.iloc[:,4:6].values
y_test_no_height = y_test.iloc[:,4:6].values
y_train_only_height = y_train.iloc[:,2:3].values
y_test_only_height = y_test.iloc[:,2:3].values
y_train_only_latlon = y_train.iloc[:,:2].values
y_test_only_latlon = y_test.iloc[:,:2].values
y_train_only_month = y_train.iloc[:,6:7].values
y_test_only_month = y_test.iloc[:,6:7].values

scaler=StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

#-------------------------------------------------
#-------------------------------------------------
df = read_csv("/home/deep/RAN/DATA/UCAR/" + "ucar-hum-evp-tmp-prs-2021-india-ntopo.txt", delim_whitespace=True, header=None)
feature_names = ['HUM', 'EVP','TMP', 'PRS', 'REF', 'HGT', 'LAT', 'LON', 'MON', 'DAY', 'HR']
df.columns = feature_names
#df['PRS'] = df['PRS']/1046.15
#df['EVP'] = np.log(df['EVP'])
#df['REF'] = np.log(df['REF'])
#df['LAT'] = np.abs(df['LAT'])
#df['LON'] = np.abs(df['LON'])
#df['EVP'] = np.exp(df['EVP'])
#df['EVP'] = df['EVP']*100
print(df.head())
print(df.describe())

X_test1 = df.drop(['HUM', 'EVP', 'TMP', 'PRS', 'DAY', 'HR'], axis = 1)
y_test1 = df[['HGT', 'TMP', 'PRS']]
latlon21 = df[['LAT', 'LON']]
month21 = df[['MON']]

y_test1_no_height = y_test1.iloc[:,1:].values
y_test1_only_height = y_test1.iloc[:,:1].values
lat21 = latlon21.iloc[:,:1].values
lon21 = latlon21.iloc[:,1:2].values
month21 = month21.iloc[:,:].values

scaler.fit(X_test1)
X_test1_scaled = scaler.transform(X_test1)
#-------------------------------------------------
#-------------------------------------------------
model = Sequential()
model.add(Dense(500, input_dim=5, activation='sigmoid'))
model.add(Dense(2, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
model.summary()

history = model.fit(X_train_scaled, y_train_no_height, validation_split=0.3, epochs=1000, batch_size=500)

loss = history.history['loss']
print(loss)
np.savetxt('loss.ascii',(loss))
# -------------------------------------------------
# -------------------------------------------------

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
    model.save_weights("model.h5")
    print("Saved model to disk")

# -------------------------------------------------
# -------------------------------------------------
predictions20_Train = model.predict(X_train_scaled)
predictions20_Test = model.predict(X_test_scaled)

Output20_Train = np.append(y_train_only_latlon, y_train_only_height, axis=1)
Output20_Train = np.append(Output20_Train, y_train_no_height[:,:1], axis=1)
Output20_Train = np.append(Output20_Train, predictions20_Train[:,:1],axis=1)
Output20_Train = np.append(Output20_Train, y_train_no_height[:,1:2],axis=1)
Output20_Train = np.append(Output20_Train, predictions20_Train[:,1:2],axis=1)
#Output20_Train = np.append(Output20_Train, y_train_no_height[:,2:3] ,axis=1)
#Output20_Train = np.append(Output20_Train, predictions20_Train[:,2:3] ,axis=1)
Output20_Train = np.append(Output20_Train, y_train_only_month ,axis=1)
print(Output20_Train.shape)

Output20_Test = np.append(y_test_only_latlon, y_test_only_height, axis=1)
Output20_Test = np.append(Output20_Test, y_test_no_height[:,:1], axis=1)
Output20_Test = np.append(Output20_Test, predictions20_Test[:,:1],axis=1)
Output20_Test = np.append(Output20_Test, y_test_no_height[:,1:2],axis=1)
Output20_Test = np.append(Output20_Test, predictions20_Test[:,1:2],axis=1)
#Output20_Test = np.append(Output20_Test, y_test_no_height[:,2:3] ,axis=1)
#Output20_Test = np.append(Output20_Test, predictions20_Test[:,2:3] ,axis=1)
Output20_Test = np.append(Output20_Test, y_test_only_month ,axis=1)
print(Output20_Test.shape)

np.savetxt("Output20_Train.txt", Output20_Train, fmt="%10.4f")
np.savetxt("Output20_Test.txt", Output20_Test, fmt="%10.4f")

# -------------------------------------------------
# -------------------------------------------------
predictions21_Test = model.predict(X_test1_scaled)

Output21_Test = np.append(lat21, lon21, axis=1)
Output21_Test = np.append(Output21_Test, y_test1_only_height, axis=1)
Output21_Test = np.append(Output21_Test, y_test1_no_height[:,:1], axis=1)
Output21_Test = np.append(Output21_Test, predictions21_Test[:,:1],axis=1)
Output21_Test = np.append(Output21_Test, y_test1_no_height[:,1:2],axis=1)
Output21_Test = np.append(Output21_Test, predictions21_Test[:,1:2],axis=1)
#Output21_Test = np.append(Output21_Test, y_test1_no_height[:,2:3] ,axis=1)
#Output21_Test = np.append(Output21_Test, predictions21_Test[:,2:3] ,axis=1)
Output21_Test = np.append(Output21_Test, month21 ,axis=1)
print(Output21_Test.shape)
np.savetxt("Output21_Test.txt", Output21_Test, fmt="%10.4f")
# -------------------------------------------------
