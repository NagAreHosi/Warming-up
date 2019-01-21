import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("homework2.txt", delimiter=',')

x_data = data[1:, :-1]
y_data = data[1:, -1, np.newaxis]

plt.scatter(x_data[:, 0], x_data[:, 1], c = y_data[:, 0])
plt.show()
#添加偏置顶
X_data = np.concatenate((np.ones((200, 1)), x_data), axis = 1)
#print(X_data)

lr = 0.01

#初始化权值
V1 = np.random.random((3, 4)) * 2 - 1
V2 = np.random.random((5, 2)) * 2 - 1
W = np.random.random((3, 1)) * 2 - 1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def dsigmoid(x):
    return x * (1 - x)

def update():
    global X_data, y_data, V1, V2, W
    Out1 = sigmoid(np.dot(X_data, V1))  #隐藏层1的输出
    Out1 = np.concatenate((np.ones((200, 1)), Out1), axis = 1) #(200,5)
    Out2 = sigmoid(np.dot(Out1, V2))    #隐藏层2的输出
    Out2 = np.concatenate((np.ones((200, 1)), Out2), axis = 1) #(200,3)
    Out = sigmoid(np.dot(Out2, W))      #最终输出 (200, 1)

    Out_delta = (y_data - Out) * dsigmoid(Out)                #(200, 1)
    Out2_delta = Out_delta.dot(W.T) * dsigmoid(Out2)          #(200, 3)
    Out1_delta = Out2_delta[:, 1:].dot(V2.T) * dsigmoid(Out1) #(200, 5)

    W = W + lr * Out2.T.dot(Out_delta)
    V2 = V2 + lr * Out1.T.dot(Out2_delta[:, 1:])
    V1 = V1 + lr * X_data.T.dot(Out1_delta[:, 1:])

for i in range(200000):
    update()

    if i % 5000 == 0 or i == 199999:
        Out1 = sigmoid(np.dot(X_data, V1))  # 隐藏层1的输出
        Out1 = np.concatenate((np.ones((200, 1)), Out1), axis=1)  # (200,5)
        Out2 = sigmoid(np.dot(Out1, V2))  # 隐藏层2的输出
        Out2 = np.concatenate((np.ones((200, 1)), Out2), axis=1)  # (200,3)
        Out = sigmoid(np.dot(Out2, W))  # 最终输出
        print('ERROR = ', np.mean(np.abs(y_data - Out)))  # 误差mean表示求平均值


def judge(x):
    if x >= 0.5:
        return 1
    else:
        return 0

for i in map(judge, Out[91:111, :]):
    print(i)


