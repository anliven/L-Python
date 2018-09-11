# -*- coding: utf-8 -*-


def confilct(state, next_x):  # 冲突检测
    next_y = len(state)
    for i in range(next_y):
        if abs(state[i] - next_x) in (0, next_y - i):  # 位于一条对角线或同一列
            return True
    return False


def queens(num=8, state=()):  # 参数num为皇后总数，参数state是一个元组存放已放置好的皇后位置
    for pos in range(num):
        if not confilct(state, pos):  # 基线条件：最后一个皇后
            if len(state) == num - 1:
                yield (pos,)
            else:  # 递归条件
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):  # 在终端输出结果
    def line(p, length=len(solution)):
        return ". " * p + "X " + ". " * (length - p - 1)

    for pos in solution:
        print(line(pos))


print(len(list(queens())))  # 8个皇后的解法数目

print(len(list(queens(4))))
print(list(queens(4)))
for s in list(queens(4)):
    print("#"*20)
    prettyprint(s)


# ### 示例：利用递归生成器解决八皇后问题
# 著名的计算机科学问题，使用生成器可以轻松解决；
# 将8个皇后放置棋盘上，任何一个皇后都不能威胁其他皇后（两个皇后不能放在同一行、列和对角线），求可行的放置方法数目；
