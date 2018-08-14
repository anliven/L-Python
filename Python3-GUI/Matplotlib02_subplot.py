# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0, 101)
plt.subplot(2, 2, 1)  # 作为2行2列图形矩阵中的第1个subplot
plt.plot(data)

data2 = np.arange(100, 201)
plt.subplot(2, 2, 2)  # 作为2行2列图形矩阵中的第2个subplot
plt.plot(data2)

data3 = np.arange(200, 301)
plt.subplot(223)  # 如果三个整数都在10之内，可以合并为一个整数
plt.plot(data3)

data4 = np.arange(300, 401)
plt.subplot(224)  # 作为2行2列图形矩阵中的第4个subplot
plt.plot(data4)

data5 = np.arange(400, 501)
plt.figure()  # 通过plt.figure()创建新的图形窗口
plt.plot(data5)

plt.show()

# ### matplotlib.pyplot.subplot
# subplot函数可在同一个窗口中以矩阵的形式显示多个图形；
# 前两个参数分别指定了矩阵的行数和列数，第三个参数是指矩阵中的索引；
# 详细信息及示例：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html
