# 在两层隐藏层和输出层都加有偏执值
# 效果还行，学习较快，迭代次数较少
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("XOR_Layout.txt",delimiter=",")
x_data = data[1:, :-1]
y_data = data[1:, -1]
X_data = np.concatenate((np.ones((200, 1)), x_data), axis=1)
y_data = y_data[:,np.newaxis]
# x_data = np.array([[0, 0],
#                     [0, 1],
#                     [1, 0],
#                     [1, 1]])
# X_data = np.concatenate((np.ones((4, 1)), x_data), axis=1)
# y_data = np.array([[0],
#               [1],
#               [1],
#               [0]])

plt.scatter(x_data[:, 0], x_data[:, 1], c=y_data[:,0])
plt.show()

V1 = np.random.random((3, 4)) * 2 - 1
V2 = np.random.random((5, 2)) * 2 - 1
W = np.random.random((3, 1)) * 2 - 1
lr = 0.01

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def dsigmoid(sig):
    return sig * (1 - sig)

for i in range(200000):
    L1 = sigmoid(np.dot(X_data, V1)) #L1(200, 4)
    L1 = np.concatenate((np.ones((200, 1)), L1), axis=1) # L1(200, 5)
    L2 = sigmoid(np.dot(L1, V2)) # L2(200, 2)
    L2 = np.concatenate((np.ones((200, 1)), L2), axis=1)  # L2(200, 3)
    O = sigmoid(np.dot(L2, W)) # O(200, 1)

    O_delta = (y_data - O) * dsigmoid(O) # O_delta(200, 1)
    L2_delta = O_delta.dot(W.T) * dsigmoid(L2) # L2_delta(200, 3)
    L1_delta = L2_delta[:,1:].dot(V2.T) * dsigmoid(L1) # L1_delta(200, 5)

    W_C = lr * L2.T.dot(O_delta)
    V2_C = lr * L1.T.dot(L2_delta)
    V1_C = lr * X_data.T.dot(L1_delta)

    W = W + W_C
    V1 = V1 + V1_C[:, 1:]
    V2 = V2 + V2_C[:, 1:]
    if i % 2000 == 0:
        L1_test = sigmoid(np.dot(X_data, V1))
        L1_test = np.concatenate((np.ones((200, 1)), L1_test), axis=1)
        L2_test = sigmoid(np.dot(L1_test, V2))
        L2_test = np.concatenate((np.ones((200, 1)), L2_test), axis=1)
        O = sigmoid(np.dot(L2_test, W))
        print('Error: ', np.mean(np.abs(y_data - O)))

L1_test = sigmoid(np.dot(X_data, V1))
L1_test = np.concatenate((np.ones((200, 1)), L1_test), axis=1)
L2_test = sigmoid(np.dot(L1_test, V2))
L2_test = np.concatenate((np.ones((200, 1)), L2_test), axis=1)
O_test = sigmoid(np.dot(L2_test, W))
print(O_test[90:110])
