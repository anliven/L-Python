# -*- coding: utf-8 -*-


def deco(func):
    def wrapper(*args, **kwargs):
        print("Wrap start.")
        func(*args, **kwargs)
        print("Wrap end.\n")

    return wrapper


@deco  # 装饰器@deco等价于“foo = deco(foo)”
def foo(x):
    print("In foo():")
    print("I have a para: %s" % x)


@deco
def foo_2(x, z='para'):
    print("In foo_2:")
    print("I have two para, %s and %s" % (x, z))


if __name__ == "__main__":
    foo('x')
    foo_2('x', z='test_para')

# ### 装饰器（Decorator）
# 可以为已存在的功能添加额外的功能，但只在初始化脚本的时候执行一次；
