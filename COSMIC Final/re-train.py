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

# -------------------------------------------------
# -------------------------------------------------
df = read_csv("/home/guest/SMLH/DATA/UR-WF/" + "ur-era-ncep-hum-evp-tmp-prs2020-india.txt", delim_whitespace=True, header=None)
feature_names = ['HUM', 'EVP','TMP', 'PRS', 'REF', 'HGT', 'LAT', 'LON', 'MON', 'DAY', 'HR']
df.columns = feature_names

X = df.drop(['HUM', 'EVP', 'TMP', 'PRS', 'DAY'], axis = 1)
y = df[['HGT','EVP', 'TMP', 'PRS']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 20)

y_train_no_height = y_train.iloc[:,1:].values
y_test_no_height = y_test.iloc[:,1:].values
y_train_only_height = y_train.iloc[:,:1].values
y_test_only_height = y_test.iloc[:,:1].values

scaler=StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -------------------------------------------------
# -------------------------------------------------
df = read_csv("/home/guest/SMLH/DATA/UR-WF/" + "ur-era-ncep-hum-evp-tmp-prs2021-india.txt", delim_whitespace=True, header=None)
feature_names = ['HUM', 'EVP', 'TMP', 'PRS', 'REF', 'HGT', 'LAT', 'LON', 'MON', 'DAY', 'HR']
df.columns = feature_names

X_test1 = df.drop(['HUM', 'EVP', 'TMP', 'PRS', 'DAY'], axis = 1)
y_test1 = df[['HGT','EVP', 'TMP', 'PRS']]

y_test1_no_height = y_test1.iloc[:,1:].values
y_test1_only_height = y_test1.iloc[:,:1].values

scaler.fit(X_test1)
X_test1_scaled = scaler.transform(X_test1)

# -------------------------------------------------
# load model and weights
# -------------------------------------------------
json_file = open('model.json', 'r')
loaded_model = json_file.read()
json_file.close()
model = model_from_json(loaded_model)
model.load_weights("model.h5")
# -------------------------------------------------
# Training
# -------------------------------------------------
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
history = model.fit(X_train_scaled, y_train_no_height, validation_split=0.3, epochs=10, batch_size=800)
loss = history.history['loss']
print(loss)
np.savetxt('loss.ascii',(loss))
# -------------------------------------------------
# write model and Weight to JSON/h5
# -------------------------------------------------
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
        # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk")
# -------------------------------------------------
# -------------------------------------------------
# -------------------------------------------------
predictions20_Train = model.predict(X_train_scaled)
predictions20_Test = model.predict(X_test_scaled)
Output20_Train = np.append(y_train_only_height, y_train_no_height[:,:1], axis=1)
Output20_Train = np.append(Output20_Train, predictions20_Train[:,:1],axis=1)
Output20_Train = np.append(Output20_Train, y_train_no_height[:,1:2],axis=1)
Output20_Train = np.append(Output20_Train, predictions20_Train[:,1:2],axis=1)
Output20_Train = np.append(Output20_Train, y_train_no_height[:,2:3] ,axis=1)
Output20_Train = np.append(Output20_Train, predictions20_Train[:,2:3] ,axis=1)
print(Output20_Train.shape)

Output20_Test = np.append(y_test_only_height, y_test_no_height[:,:1], axis=1)
Output20_Test = np.append(Output20_Test, predictions20_Test[:,:1],axis=1)
Output20_Test = np.append(Output20_Test, y_test_no_height[:,1:2],axis=1)
Output20_Test = np.append(Output20_Test, predictions20_Test[:,1:2],axis=1)
Output20_Test = np.append(Output20_Test, y_test_no_height[:,2:3] ,axis=1)
Output20_Test = np.append(Output20_Test, predictions20_Test[:,2:3] ,axis=1)
print(Output20_Test.shape)

np.savetxt("Output20_Train.txt", Output20_Train, fmt="%10.4f")
np.savetxt("Output20_Test.txt", Output20_Test, fmt="%10.4f")

# -------------------------------------------------
# -------------------------------------------------
predictions21_Test = model.predict(X_test1_scaled)
Output21_Test = np.append(y_test1_only_height, y_test1_no_height[:,:1], axis=1)
Output21_Test = np.append(Output21_Test, predictions21_Test[:,:1],axis=1)
Output21_Test = np.append(Output21_Test, y_test1_no_height[:,1:2],axis=1)
Output21_Test = np.append(Output21_Test, predictions21_Test[:,1:2],axis=1)
Output21_Test = np.append(Output21_Test, y_test1_no_height[:,2:3] ,axis=1)
Output21_Test = np.append(Output21_Test, predictions21_Test[:,2:3] ,axis=1)
print(Output21_Test.shape)

np.savetxt("Output21_Test.txt", Output21_Test, fmt="%10.4f")

# -------------------------------------------------
# -------------------------------------------------
