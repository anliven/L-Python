#! python3
# -*- coding: utf-8 -*-


def func(a, b):
    return a / b


def my_exception_handler(exc_type, exc_value, exc_tb):
    print("### I caught the exception:", )
    print('### The exc type is:', exc_type)
    print('### The exc value is:', exc_value)
    while exc_tb:
        print("### The line number:", exc_tb.tb_lineno)
        print("### The frame locals:", exc_tb.tb_frame.f_locals)
        exc_tb = exc_tb.tb_next


if __name__ == '__main__':
    import cgitb
    cgitb.enable(format='text')
    # import sys
    # sys.excepthook = my_exception_handler
    func(1, 0)

# ### 标准库cgitb模块
# 能够输出异常上下文所有相关变量的信息，不必每次手动加debug log，适合在开发过程中进行调试；
# Traceback manager for CGI scripts
# https://docs.python.org/3/library/cgitb.html
#
# cgitb覆盖了sys.excepthook函数（默认的全局异常拦截器），因此能获取详细的出错信息；
# 可以自定义sys.excepthook函数
