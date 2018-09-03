# coding=utf-8


def check_odd_even(n: int) -> bool:  # 期望函数参数的类型和返回值类型
    if n % 2 == 0:
        print("This number is odd.")
        return True
    else:
        print("This number is even.")
        return False


check_odd_even(123)


def add(x: int, y: int) -> str:
    z = 123  # type:int
    return x + y + z  # 仅仅是“提示”，对于不符合期望的数据类型并不会报错


print(add(5, 6))

# ### 类型约束（类型提示）
# 可以在函数、方法、类的参数和返回值声明其类型，帮助编辑器提供更精准的提示；
# PEP484：https://www.python.org/dev/peps/pep-0484/
# 特别注意：类型约束（类型提示）仅仅是具备了“提示”功能，对于不符合期望的数据类型并不会报错；
