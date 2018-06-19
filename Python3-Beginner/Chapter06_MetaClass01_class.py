# coding=utf-8


class Foo():
    foo = True


def echo(cls):
    print(cls)


def select(name):
    if name == 'foo':
        return Foo  # 返回值是一个类


echo(Foo)  # 把类作为参数传递给函数
c = select("foo")  # 函数select的返回值是一个类，并赋给变量
print(c)

# ### 类也是对象
# - 可以把类赋值给一个变量；
# - 可以把类作为函数参数进行传递；
# - 可以把类作为函数的返回值；
# - 可以在运行时动态地创建类；
