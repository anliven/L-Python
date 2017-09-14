# -*- coding: utf-8 -*-


def get_two_values():  # return two different values from a function
    return (123, 'test')


returnNum, returnStr = get_two_values()
print('Values-1:', returnNum, '\nValues-2:', returnStr)

a = 555
b = 888
print('a:', a, 'b:', b)
a, b = b, a  # the fastest way to swap two variables in Python
print('a:', a, 'b:', b)
