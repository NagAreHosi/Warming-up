# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:27:55 2019

@author: crl
"""

import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt


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
#min_max_scaler = preprocessing.MinMaxScaler()  
#x_data = min_max_scaler.fit_transform(x_data)
#y_data = min_max_scaler.fit_transform(y_data[:,np.newaxis])
#print(x_data[:4])
#print(y_data[:4])



for i in range(x_data.shape[0]):
     x_data[i, 0] = (x_data[i, 0] - min_x0) / (max_x0 - min_x0)
     x_data[i, 1] = (x_data[i, 1] - min_x1) / (max_x1 - min_x1)
 #print(x_data)
 
for i in range(y_data.shape[0]):
     y_data[i] = (y_data[i] - min_y) / (max_y - min_y)
y_data = y_data[:,np.newaxis]


print(x_data.shape)
#构造矩阵
print(np.mat(x_data).shape)
print(np.mat(y_data).shape)

#给样本添加偏置顶,添加100行1列的偏置值1
#把偏置值和x_data合并，axis表示合并的方向，将x_data从第一列放入生成的np.ones((100, 1)里
X_data = np.concatenate((np.ones((47, 1)), x_data), axis = 1)
print(X_data)


#标准方程法求解回归参数

def weights(xArr, yArr):
    #转化矩阵
    xMat = np.mat(xArr) 
    yMat = np.mat(yArr)
    xTx = xMat.T * xMat  #矩阵乘法
    #如果矩阵相乘值为0， 则没有逆矩阵
    if np.linalg.det(xTx) == 0.0:
        print("This matrix cannot do inverse")
        return
    # xTx.I 为xTx 的逆矩阵
    ws = xTx.I * xMat.T * yMat
    return ws

ws = weights(X_data, y_data)
print('ws = ',ws)

def compute_error(theta0, theta1, theta2, x, y):
    totalError = 0
    for i in range(len(x)):
        totalError += ((theta1 * x[i,0] + theta2 * x[i,1] + theta0) - y[i] ) **2
    return totalError / float(len(x)) / 2.0

print("error = %f"%float(compute_error(ws[0], ws[1], ws[2], x_data, y_data)))



ax = plt.figure().add_subplot(111, projection = '3d')
ax.scatter(x_data[:,0], x_data[:,1], y_data, c = 'r', marker = 'o', s = 100) #c表示颜色，s是大小
x0 = x_data[:,0]
x1 = x_data[:,1]

#生成网格矩阵
x0, x1 = np.meshgrid(x0, x1)
z = float(ws[0]) + float(ws[1]) * x0 + float(ws[2]) * x1
print(z)
#画3D图
ax.plot_surface(x0, x1, z)
#设置坐标轴
ax.set_xlabel('Miles')
ax.set_ylabel('Num of Deliveries')
ax.set_zlabel('Time')
plt.show()

