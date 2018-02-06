#! python3
# -*- coding: utf-8 -*-


class Student(object):

    @property  # 加上@property，实际上是将getter方法变成属性score
    def score(self):
        return self._score

    @score.setter  # 这里的装饰器@score.setter，实际上把一个setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):  # 只读属性
        return self._birth

    @birth.setter
    def birth(self, value):  # 可写属性
        self._birth = value

    @property
    def age(self):  # 只读属性
        return 2018 - self._birth


s = Student()
s.score = 100  # 实际转化为setter方法的形式：s.set_score(100)
print(s.score)  # 实际转化为getter方法的形式：s.get_score()
# s.score = 999  # 触发异常
s.birth = 1986
print(s.age)

# ### @property装饰器
# 在对实例属性操作的时候，该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的;
# Python内置的@property装饰器可以把一个方法变成属性调用；
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性；
