# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(low=0, high=100, size=7)  # 包含7个随机整数数（0, 100）的列表
colors = np.random.rand(21).reshape(7, -1)  # 生成21个随机数，然后分成7行列表
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

plt.subplot(2, 1, 1)
plt.title("Weekday Data")  # 指定图形标题
plt.bar(np.arange(7), data, alpha=0.8, color=colors, tick_label=labels)

data2 = [np.random.randint(0, n, n) for n in [3000, 4000, 5000]]
labels2 = ['3K', '4K', '5K']
bins = [0, 100, 500, 1000, 2000, 3000, 4000, 5000]  # 指定直方图显示的数据点

plt.subplot(2, 1, 2)
plt.hist(data2, bins=bins, label=labels2)  # 参数label指定标签
plt.legend()  # 指定图例

plt.show()

# ### 条形图（matplotlib.pyplot.bar）
# bar函数可用来绘制条形图；
# 详细信息及示例：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html
#
# ### 直方图（matplotlib.pyplot.hist）
# hist函数可用来绘制直方图；
# 详细信息及示例：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
