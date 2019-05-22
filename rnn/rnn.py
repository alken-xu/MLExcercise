#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:42:09 2019

@author: xuguoqi
"""

#Part 1 data preprocessing
# importing the libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

# importing data
dataset_train = pd.read_csv('Google_Stock_Price_Train.csv')
traing_set = dataset_train.iloc[:,1:2].values

# feature scaling
from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler(feature_range=(0,1))
traing_set_scaled = sc.fit_transform(traing_set)


# creating a data structure with 60 timesteps and 1 output
X_train = []
Y_train = []

for i in range(60,1258):
    X_train.append(traing_set_scaled[i-60:i,0])
    Y_train.append(traing_set_scaled[i,0])
    
X_train, Y_train = np.array(X_train), np.array(Y_train)

# Reshaping
X_train = np.reshape(X_train, (X_train.shape[0],X_train.shape[1],1))

# Part2 building the RNN
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

# initializing the RNN
regressor = Sequential()

# Adding the first LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1],1)))
regressor.add(Dropout(0.2))

# Adding
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

# Adding the output layer
regressor.add(Dense(units=1))


# compiling the RNN
regressor.compile(optimizer='adam', loss= 'mean_squared_error')

# Fitting the RNN to the Training set 
regressor.fit(X_train, Y_train, epochs=100, batch_size=32)

# Part3 Making the predictions and visualizing the results
dataset_test = pd.read_csv('Google_Stock_Price_Test.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values

# Getting the predicted stock price of 2017
dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis = 0) # vertical concate = 0, horizontal = 1
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

X_test = []
for i in range(60, 80):
    X_test.append(inputs[i-60:i, 0]) # 60 timesteps 
X_test = np.array(X_test) 
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1)) # num rows, num columns, num indicator
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)


# Visualising the results
plt.plot(real_stock_price, color = 'red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()

