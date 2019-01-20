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
for i in range(x_data.shape[0]):
    x_data[i, 0] = (x_data[i, 0] - min_x0) / (max_x0 - min_x0)
    x_data[i, 1] = (x_data[i, 1] - min_x1) / (max_x1 - min_x1)
#print(x_data)
for i in range(y_data.shape[0]):
    y_data[i] = (y_data[i] - min_y) / (max_y - min_y)
#用sklearn做数据归一化
# =============================================================================
# min_max_scaler = preprocessing.MinMaxScaler()
# X_minMax = min_max_scaler.fit_transform(x_data)
# print(X_minMax)
# =============================================================================


#梯度下降法
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
theta0, theta1, theta2 = gradient_descent_runner(x_data, y_data, theta0, theta1, theta2, lr, epochs)
print("After theta0:{0}, theta1:{1}, theta2:{2}, error:{3}".format(epochs, theta0, theta1, theta2, \
      compute_error(theta0, theta1, theta2, x_data, y_data)))
predictNum = theta0 + theta1 * 3500 + theta1 * 2
print(predictNum)


#标准方程法
y_data = y_data[:,np.newaxis]
X_data = np.concatenate((np.ones((47, 1)), x_data), axis = 1)

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


#sklearn方法
y_data = y_data[:,np.newaxis]
model = linear_model.LinearRegression()
model.fit(x_data, y_data)

print("系数：",model.coef_)
print("截距：",model.intercept_)

x00 = (1203-min_x0)/(max_x0-min_x0)
x11 = (3-min_x1)/(max_x1-min_x1)
y0 = model.predict([[x00, x11]])
predict = y0 * (max_y - min_y) + min_y
print(predict)

