import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# creating a dummy dataset
np.random.seed(10)
x = np.random.rand(50, 1)
y = 3 + 3 * x + np.random.rand(50, 1)


#scatterplot

plt.scatter(x,y,s=10)
plt.xlabel('x_dummy')
plt.ylabel('y_dummy')
plt.show()

#creating a model
from sklearn.linear_model import LinearRegression

# creating a object
regressor = LinearRegression()

#training the model
regressor.fit(x, y)

#using the training dataset for the prediction
pred = regressor.predict(x)

#model performance
from sklearn.metrics import r2_score, mean_squared_error
mse = mean_squared_error(y, pred)
r2 = r2_score(y, pred)#Best fit lineplt.scatter(x, y)
plt.plot(x, pred, color = 'Black', marker = 'o')


#Results
print("Mean Squared Error : ", mse)
print("R-Squared :" , r2)
print("Y-intercept :"  , regressor.intercept_)
print("Slope :" , regressor.coef_)