# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:32:21 2019

@author: crl
"""
#from 1klearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x_data = np.genfromtxt("ex3x.dat", delimiter = "   ")
y_data = np.genfromtxt("ex3y.dat")

#print(x_data)
#print(y_data)

#数据归一化
max_x0 = max(x_data[0:, 0])
max_x1 = max(x_data[0:, 1])
min_x0 = min(x_data[0:, 0])
min_x1 = min(x_data[0:, 1])

max_y = max(y_data)
min_y = min(y_data)
#用sklearn做数据归一化
# =============================================================================
# min_max_scaler = preprocessing.MinMaxScaler()  
# X_minMax = min_max_scaler.fit_transform(x_data)
# print(X_minMax)
# =============================================================================

for i in range(x_data.shape[0]):
    x_data[i, 0] = (x_data[i, 0] - min_x0) / (max_x0 - min_x0)
    x_data[i, 1] = (x_data[i, 1] - min_x1) / (max_x1 - min_x1)
#print(x_data)

for i in range(y_data.shape[0]):
    y_data[i] = (y_data[i] - min_y) / (max_y - min_y)

#学习率
lr = 0.08
#参数

theta0 = 0
theta1 = 0
theta2 = 0

#最大迭代次数
epochs = 100

#最小二乘法
def compute_error(theta0, theta1, theta2, x, y):
    totalError = 0
    for i in range(len(x)):
        totalError += (y[i] - (theta1 * x[i,0] + theta2 * x[i,1] + theta0)) **2
    return totalError / float(len(x)) / 2.0
def gradient_descent_runner(x, y, theta0, theta1, theta2, lr, epochs):
    m = float(len(x))
    for i in range(epochs):
        theta0_grad = 0
        theta1_grad = 0
        theta2_grad = 0
        for j in range(len(x)):
            theta0_grad += (1/m) * ((theta1 * x[j,0] + theta2 * x[j,1] + theta0) - y[j])  #代价函数对西塔2求导的梯度总和
            theta1_grad += (1/m) * x[j,0] * ((theta1 * x[j,0] + theta2 * x[j,1] + theta0) - y[j]) #代价函数对西塔1求导的梯度总和
            theta2_grad += (1/m) * x[j,1] * ((theta1 * x[j,0] + theta2 * x[j,1] + theta0) - y[j])
        theta0 = theta0 - (lr * theta0_grad)
        theta1 = theta1 - (lr * theta1_grad)
        theta2 = theta2 - (lr * theta2_grad)
    return theta0, theta1, theta2

print("Starting theta0:{0}, theta1:{1}, theta2:{2}, error:{3}".format(theta0, theta1, theta2, \
      compute_error(theta0, theta1, theta2, x_data, y_data)))
print("Running...")
theta0, theta1, theta2 = gradient_descent_runner(x_data, y_data, theta0, theta1, theta2, lr, epochs)
print("After theta0:{0}, theta1:{1}, theta2:{2}, error:{3}".format(epochs, theta0, theta1, theta2, \
      compute_error(theta0, theta1, theta2, x_data, y_data)))

ax = plt.figure().add_subplot(111, projection = '3d')
ax.scatter(x_data[:,0], x_data[:,1], y_data, c = 'r', marker = 'o', s = 100) #c表示颜色，s是大小
x0 = x_data[:,0]
x1 = x_data[:,1]
#生成网格矩阵
x0, x1 = np.meshgrid(x0, x1)
z = theta0 + theta1 * x0 + theta1 * x1
print(z)
#画3D图
ax.plot_surface(x0, x1, z)
#设置坐标轴
ax.set_xlabel('Miles')
ax.set_ylabel('Num of Deliveries')
ax.set_zlabel('Time')
plt.show()

















