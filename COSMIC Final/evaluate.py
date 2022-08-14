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

np.random.seed(7)
# load data and arrange into Pandas dataframe
df = read_csv("/home/guest/SMLH/DATA/UR-WF/" + "ur-era-ncep-hum-evp-tmp-prs2020-india.txt", delim_whitespace=True, header=None)
feature_names = ['HUM', 'EVP','TMP', 'PRS', 'REF', 'HGT', 'LAT', 'LON', 'MON', 'DAY', 'HR']
df.columns = feature_names
print(df.head())
print(df.describe())
X = df.drop(['HUM', 'EVP', 'TMP', 'PRS', 'DAY'], axis = 1)
y = df[['EVP', 'TMP', 'PRS']]
#Standardize features by removing the mean and scaling to unit variance
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
######################################################################
# load model and weights
######################################################################
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model_json = model_from_json(loaded_model_json)
model_json.load_weights("model.h5")
#---------------------------
#---------------------------
model_json.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
#history = model_json.fit(X_train_scaled, y_train, validation_split=0.5, epochs=100, batch_size=500)
#loss = history.history['loss']
#print(loss)
#np.savetxt('loss.ascii',(loss))
############################################
#Predict on test data
############################################
predictions = model_json.predict(X_scaled)
print("Predicted values are: ", predictions)
print("Real values are: ", y)
np.savetxt ('output1.ascii',(y))
np.savetxt ('output2.ascii',(predictions))
mse_neural, mae_neural = model_json.evaluate(X_scaled, y)
print('Mean squared error from neural net: ', mse_neural)
print('Mean absolute error from neural net: ', mae_neural)
##############################################
