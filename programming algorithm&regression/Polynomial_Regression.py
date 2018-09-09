import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def PolynomialRegression(filename):
    dataset = pd.read_excel(filename)
    x_data = dataset["房屋面积"].values.reshape([-1,1])
    y_data = dataset["交易价格"].values.reshape([-1,1])
    PolyModel = PolynomialFeatures(degree=3)
    xPoly = PolyModel.fit_transform(x_data)
    LinearModel = LinearRegression()
    LinearModel.fit(xPoly,y_data)
    return x_data,y_data,LinearModel,PolyModel

x,y,aa,bb = PolynomialRegression("dataset.xlsx")
x_test = np.arange(min(x),max(x)).reshape([-1,1])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, color = 'red')
ax.plot(x_test,aa.predict(bb.fit_transform(x_test)))
plt.show()