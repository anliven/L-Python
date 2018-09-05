# -*- coding: utf-8 -*-


class Rectangle(object):  # 新式类
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    current_size = property(get_size, set_size)  # 创建了一个特性并关联到名称


r = Rectangle(5, 6)
print(r.width, r.height, r.get_size())
r.current_size = 7, 8
print(r.width, r.height, r.get_size())

# ### 特性（property）
# 通过存取方法定义的属性通常称为特性（property）；
# 函数property只能用于新式类；
# 通过调用函数property并将存取方法作为参数（获取方法在前，设置方法在后）就可以创建一个特性；
