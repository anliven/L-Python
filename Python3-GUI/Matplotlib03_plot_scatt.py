# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

plt.subplot(2, 1, 1)
plt.plot([1, 2, 3], [3, 6, 9], '-r')  # 红色的直线
plt.plot([1, 2, 3], [2, 4, 9], ':b')  # 蓝色的点线
plt.plot([1, 2, 3], [2, 5, 7], color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)

plt.subplot(2, 1, 2)
plt.scatter(np.random.rand(10) * 100, np.random.rand(10) * 100, c='r', s=100, alpha=0.5)  # 参数c表示点的颜色
plt.scatter(np.random.rand(15) * 100, np.random.rand(15) * 100, c='g', s=200, alpha=0.5)  # 参数s表示点的大小
plt.scatter(np.random.rand(20) * 100, np.random.rand(20) * 100, c='b', s=300, alpha=0.5)  # 参数alpha表示透明度

plt.show()

# ### Gallery
# Matplotlib可以生成种类繁多的图形式样（https://matplotlib.org/gallery/index.html）；
#
# ### matplotlib.pyplot
# The matplotlib.pyplot module contains functions that allow you to generate many kinds of plots quickly.
# The Pyplot API：https://matplotlib.org/api/pyplot_summary.html
# Functions List：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html
#
# ### 线性图（matplotlib.pyplot.plot）
# plot函数可用来绘制线性图；
# 详细信息及示例：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
#
# ### 散点图（matplotlib.pyplot.scatt）
# scatt函数可用来绘制散点图；
# 详细信息及示例：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html
