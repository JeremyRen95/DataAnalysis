from scipy import optimize as op
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from matplotlib import pyplot as plt

# this programme task is:
# Max: Z = 2x1 + 3x2 - 5x3
# s.t. x1 + x2 + x3 = 7
#      2x1 - 5x2 + x3 >= 10
#      x1 + 3x2 + x3 <= 12
#      x1,x2,x3 >= 0
# use: scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None,
#                             method='simplex', callback=None, options=None)
def LinearProgramming():
    C = np.array([2,3,-5])
    A_ub = np.array([[-2,5,-1],[1,3,1]]) #muti-dimension
    b_ub = np.array([-10,12])
    A_eq = np.array([[1,1,1]])  #muti-dimension
    b_eq = np.array([7])
    x1 = np.array([0,7])
    x2 = np.array([0,7])
    x3 = np.array([0,7])
    res = op.linprog(-C,A_ub,b_ub,A_eq,b_eq,bounds=[x1,x2,x3])
    print(res)

# unengaged programming task
# the local minimum & the global minimum
def f(x):
    return x**2 + 10*np.sin(x)
# need init guess value x0 and get local minimum
x1 = op.minimize(f,0,method='SLSQP')
x2 = op.fmin_bfgs(f,0)
#print(x2); print(x1)

# LinearRegression task
x = [[1,1,1],[1,1,2],[1,2,1]]
y = [[6],[9],[8]]

model_linear = LinearRegression()
model_linear.fit(x,y)
x2 = [[1,3,5]]
y2 = model_linear.predict(x2)

x1 = np.linspace(1/30,14/30,14).reshape(14,1)
y1 = np.array([11.86,15.67,20.60,26.69,33.71,41.93,51.13,61.49,72.90,85.44,99.08,113.77,129.54,146.48]).reshape(14,1)
model_polynoimal = PolynomialFeatures(degree=3)
model_polynoimal.fit(x1,y1)
y3 = model_polynoimal.transform(0)
print(y3)