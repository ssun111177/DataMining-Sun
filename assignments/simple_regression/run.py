import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('mortgage_rates.csv')
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.05, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)

plt.scatter(X_train,y_train,color='black')
plt.plot(X_train,regressor.predict(X_train),color='red')
plt.title('price VS rate')
plt.xlabel('rate')
plt.ylabel('price')
plt.show()
