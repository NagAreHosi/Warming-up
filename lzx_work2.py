# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

x_data = np.genfromtxt(r"ex3x.dat",delimiter="   ")
y_data = np.genfromtxt(r"ex3y.dat")

model = linear_model.LinearRegression()
model.fit(x_data,y_data)

ax = plt.figure().add_subplot(111,projection='3d')
ax.scatter(x_data[:,0],x_data[:,1],y_data,c='r',marker='o',s=100)

x0 = x_data[:,0]
x1 = x_data[:,1]

x0,x1 = np.meshgrid(x0,x1)
z = model.intercept_+model.coef_[0]*x0+model.coef_[1]*x1

ax.plot_surface(x0,x1,z)

ax.show()


