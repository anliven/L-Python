# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# ----------------------------------------------------------------------------------------------------------------------
### 装饰器
# 装饰器模式（Decorator，别名Wrapper）是一种设计模式。
# 在不必改变原类文件和使用继承的情况下，动态地扩展一个对象的功能。它是通过创建一个包装对象，也就是装饰来包裹真实的对象。
# 从增加对象的行为来说，Decorator模式相比生成子类更为灵活。

# 可以利用装饰器为多个已经写好的函数添加一个共同功能。
# 也可以将多个函数的重复代码代码单独整理成一个装饰器，然后对每个函数调用该装饰器，实现代码的复用，并简化原来的函数。
# 装饰器是解决插入日志、性能测试、事务处理等需求场景的绝佳设计。

# 设计原则：
# 1. 多用组合，少用继承。
# 2. 类应设计的对扩展开放，对修改关闭。

# 要点：
# 1． 装饰者和被装饰对象有相同的超类型。
# 2． 可以用一个或多个装饰者包装一个对象。
# 3． 装饰者可以在所委托被装饰者的行为之前或之后，加上自己的行为，以达到特定的目的。
# 4． 对象可以在任何时候被装饰，所以可以在运行时动态的，不限量的用你喜欢的装饰者来装饰对象。
# 5． 装饰模式中使用继承的关键是想达到装饰者和被装饰对象的类型匹配，而不是获得其行为。
# 6． 装饰者一般对组件的客户是透明的，除非客户程序依赖于组件的具体类型。在实际项目中可以根据需要为装饰者添加新的行为，做到“半透明”装饰者。
# 7． 适配器模式的用意是改变对象的接口而不一定改变对象的性能，而装饰模式的用意是保持接口并增加对象的职责。

# Python与Decorator
# Python通过Decorators对函数、方法或类进行装饰，从而达到增加对象的职责，或控制对象调用的作用。
# python中的装饰器实际上是一种“语法糖”，是一种语句的简便写法。

# ----------------------------------------------------------------------------------------------------------------------

### 简单例子--逐步理解装饰器：

# 如何查看执行如下foo函数用了多长时间：
# def foo():
#     print 'in foo()'
# foo()


# 代码示例一： 改动了foo函数的定义，但没有改动调用代码。
# import time
# def foo():
#     start = time.clock()  # 在WINDOWS中，第一次调用返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。
#     print start
#     print 'in foo()'
#     end = time.clock()  # 这里是第二个clock()，输出的都是与第一个clock的时间间隔。
#     print 'used:', end - start
# foo()  # 调用代码


# 代码示例二： 不改动foo函数定义，但改动了调用代码。
# 重新定义一个函数timeit，将foo的引用传递给它，然后在timeit中调用foo并进行计时。
# import time
# def foo():  # foo函数
#     print 'in foo()'
# def timeit(func):  # 重新定义一个函数timeit
#     start = time.clock()
#     func()  # 这里实际调用了foo
#     end = time.clock()
#     print 'used:', end - start
# timeit(foo)  # 将foo的引用传递给timeit，这里将调用代码foo()修改成了：timeit(foo)
# 但如果foo在很多地方都被调用甚至某处调用的代码无法修改，代码更改都不是一件容易的事。


# 代码示例三： 既不改动foo函数定义的方式，也不改动调用代码。
# import time
# def foo():
#     print 'in foo()'
# def timeit(func):  # 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
#     def wrapper():  # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
#         start = time.clock()
#         func()
#         end = time.clock()
#         print 'used:', end - start
#     return wrapper  # 将包装后的函数返回
# foo = timeit(foo)
# foo()  # 虽然没有修改调用代码，但这里调用foo()实际产生调用timeit(foo)的效果。


# 代码示例四： 既不改动foo函数定义的方式，也不改动调用代码。Python提供了一个语法糖来降低字符输入量。
# import time
# def timeit(func):  # 装饰函数
#     def wrapper():
#         start = time.clock()
#         func()
#         end = time.clock()
#         print 'used:', end - start
#     return wrapper
# @timeit
# def foo():
#     print 'in foo()'
# foo()

# ----------------------------------------------------------------------------------------------------------------------

### 定义示例：无参数的装饰器
#
#
# def deco(func):  # 函数deco是装饰函数，它的参数就是被装饰的函数对象
#     print("deco")  # 在deco函数内对传入的函数对象做一番“装饰”
#     return func  # 返回这个对象（一定要返回对象 ，不然外面调用foo的地方将会无函数可用。）
#
#
# @deco
# def foo():  # 被装饰的函数
#     print("foo")
#
# foo()  # 实际上此时foo=deco(foo)，也就是说foo()相当于deco(foo)()


### 定义示例：有参数的装饰器--被装饰函数无参数
#
#
# def deco(argv):  # 函数deco是装饰函数，它的参数是用来“加强装饰”的。
#     def decorator(func):  # 装饰函数并非被装饰的函数对象，所以在内部必须至少创建一个接受被装饰函数的函数，然后返回这个对象
#         print("decorator")
#         return func
#     print("deco")
#     print argv
#     return decorator  # 返回这个对象
#
# @deco("123")
# def foo():  # 被装饰函数
#     print("foo")
#
# foo()  # 实际上此时foo = deco("123")(foo)，也就是说foo()相当于deco("123")(foo)()


### 定义示例：有参数的装饰器--被装饰函数有参数
#
#
# def deco(argv):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print("wrapper")
#             return func(*args, **kwargs)
#         print("decorator")
#         return wrapper
#     print("deco")
#     print(argv)
#     return decorator
#
# @deco("123")
# def foo(data):
#     "this is foo"
#     print("foo")
#     print(data)
#
# foo("test")


### 定义示例：有参数的装饰器
#
#
# def BeforeAfter(f):
#     def wrapper(x):  #
#         print 'before function'
#         f(x)
#         print 'after function'
#     return wrapper
#
#
# def func1(x):
#     print 'this is function'
#     print 'I have a parameter : %s' % x
# xFunc = BeforeAfter(func1)  # BeforeAfter函数的参数是func1的函数地址，并且返回一个函数地址。
# print xFunc  # 显示返回的函数地址（也是最终真正调用的地址）,这里是function wrapper
# xFunc('test')  # 普通方式调用，相当于“BeforeAfter(func1)('test')”
#
#
# @BeforeAfter  # 装饰器BeforeAfter
# def func2(x):
#     print 'this is function'
#     print 'I have a parameter : %s' % x
# func2('test')  # 装饰器方式调用，相当于“BeforeAfter(func2('test'))”

# ----------------------------------------------------------------------------------------------------------------------

### 示例--利用Python参数魔法装饰不同参数列表的多个函数：
# 定义函数时： *params:收集其余的位置参数，返回元组。 **params:收集其余的关键字参数，返回字典。
# 调用函数时： *params:将元组拆分为位置参数传入。 **params:将字典拆分为关键字参数传入。
#
# 由于有参数的装饰函数在调用时只会使用应用时的参数 而不接收被装饰的函数做为参数，所以必须在其内部再创建一个函数。


# def deco(func):  # 装饰函数deco
#     def wrapper(*args, **kwargs):
#         print "Wrap start"
#         func(*args, **kwargs)
#         print "Wrap end\n"
#     return wrapper
#
#
# @deco
# def foo(x):
#     print "In foo():"
#     print "I have a para: %s" % x
#
#
# @deco
# def bar(x, y):
#     print "In bar():"
#     print "I have two para: %s and %s" % (x, y)
#
#
# @deco
# def foo_dict(x, z='dict_para'):
#     print "In foo_dict:"
#     print "I have two para, %s and %s" % (x, z)
#
# if __name__ == "__main__":
#     foo('x')
#     bar('x', 'y')
#     foo_dict('x', z='dict_para')



# ----------------------------------------------------------------------------------------------------------------------

### 实例--多装饰器组合使用--如何打印出 “ <b><i>Hello world<i></b> ”？
#
#
# def MakeNew(fn):
#     def wrapped():
#         return "<b><i>" + fn() + "<i></b>"
#     return wrapped
#
#
# def MakeItalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped
#
#
# @MakeBold  # 注意多个装饰器的执行顺序，应该是先执行下面的，然后是上面的。
# @MakeItalic  # 这里是MakeItalic先执行。
# def hello():
#     return "hello world"
# print hello()  # 相当于“MakeBold(MakeItalic(hello()))”, 结果返回“<b><i>hello world</i></b>”

# # 等同于
# def hello():
#     return "hello world"
# say = MakeBold(MakeItalic(hello))
# print say()

# ----------------------------------------------------------------------------------------------------------------------

### 实例--无参数的装饰器，检查函数的文档说明是否存在

# def deco_functionNeedDoc(func):
#     if func.__doc__ == None :
#         print func, "has no __doc__, it's a bad habit."
#     else:
#         print func, ':', func.__doc__, '.'
#     return func
# @deco_functionNeedDoc
# def f():
#     print 'f() Do something'
# @deco_functionNeedDoc
# def g():
#     'I have a __doc__'
#     print 'g() Do something'
# f()
# g()

# ----------------------------------------------------------------------------------------------------------------------

