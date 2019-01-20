# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_data = np.genfromtxt(r"ex3x.dat",delimiter="   ")
y_data = np.genfromtxt(r"ex3y.dat")

lr = 0.0000001
theta0 = 0
theta1 = 0
theta2 = 0
epochs = 200

def compute_error(x_data,y_data,lr,theta0,theta1,theta2,epochs):
    totalError = 0
    for i in range(len(x_data)):
        totalError += (theta0+theta1*x_data[i,0]+theta2*x_data[i,1]-y_data[i])**2
    return totalError/float(len(x_data))/2.0

def gradient_descent_runner(x_data,y_data,theta0,theta1,theta2,lr,epochs):
    m = float(len(x_data))
    for i in range(epochs):
        theta0_grad = 0
        theta1_grad = 0
        theta2_grad = 0
        for j in range(len(x_data)):
            theta0_grad += (1/m)*(theta0+theta1*x_data[j,0]+theta2*x_data[j,1]-y_data[j])
            theta1_grad += (1/m)*(theta0+theta1*x_data[j,0]+theta2*x_data[j,1]-y_data[j])*x_data[j,0]
            theta2_grad += (1/m)*(theta0+theta1*x_data[j,0]+theta2*x_data[j,1]-y_data[j])*x_data[j,1]
        theta0 = theta0-lr*theta0_grad
        theta1 = theta1-lr*theta1_grad
        theta2 = theta2-lr*theta2_grad
    return theta0,theta1,theta2

ax = plt.figure().add_subplot(111,projection = "3d")
ax.scatter(x_data[:,0],x_data[:,1],y_data,c='r',marker='o',s=100)
x0 = x_data[:,0]
x1 = x_data[:,1]
x0,x1 = np.meshgrid(x0,x1)
theta0,theta1,theta2 = gradient_descent_runner(x_data,y_data,theta0,theta1,theta2,lr,epochs)
z = theta0+theta1*x0+theta2*x1
ax.plot_surface(x0,x1,z)
plt.show()