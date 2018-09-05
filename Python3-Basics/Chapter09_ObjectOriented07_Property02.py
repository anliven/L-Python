# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):  # 使用get/set方法来封装对一个属性的访问
        return self.__score

    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score


s = Student('AAA', 59)
s.score = 85
print(s.get_score())
s.set_score(95)  # 但s.set_score()没有直接用s.score直接
print(s.get_score())


class Student2(object):

    @property  # 加上@property，实际上是用装饰器函数将get方法“装饰”成属性调用
    def score(self):
        return self._score

    @score.setter  # 这里的装饰器@score.setter，实际上把一个set方法变成属性赋值
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

    @property  # 用@property修饰grade的get方法实现只读属性
    def grade(self):
        if self.score < 60:
            return 'C'
        if self.score < 80:
            return 'B'
        return 'A'


s2 = Student2()
s2.score = 100  # 实际转化为setter方法的形式：s.set_score(100)
print(s2.score)  # 实际转化为getter方法的形式：s.get_score()
# s.score = 999  # 触发异常
s2.birth = 1986
print(s2.age)
print(s2.grade)

# ### @property装饰器
# 在对实例属性操作的时候，该属性很可能不是直接暴露的，而是通过get和set方法来实现的;
# Python内置的@property装饰器可以把一个方法变成属性调用；
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性；
