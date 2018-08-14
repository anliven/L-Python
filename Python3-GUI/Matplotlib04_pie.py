# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

plt.pie(np.random.rand(7) * 100, labels=labels, autopct='%1.1f%%')  #
plt.axis('equal')  # 坐标轴大小一致
plt.legend()  # 绘制图例

plt.show()

# ### 饼状图（matplotlib.pyplot.pie）
# pie函数可用来绘制饼状图；
# 详细信息及示例：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html
