#! python3
# -*- coding: utf-8 -*-


def func(a, b):
    return a / b


if __name__ == '__main__':
    import sys
    import traceback

    try:
        func(1, 0)
    except Exception as e:
        print("# Print_exception()")
        exc_type, exc_value, exc_tb = sys.exc_info()  # 通过sys.exc_info()函数获取异常相关的数据
        print('# The exc type is:', exc_type)  # exc_type：异常的对象类型
        print('# The exc value is:', exc_value)  # exc_value：异常的值
        print('# The exc tb is:', exc_tb)  # exc_tb：一个traceback对象，包含出错的行数、位置等数据
        traceback_details = {
            'filename': exc_tb.tb_frame.f_code.co_filename,
            'line number': exc_tb.tb_lineno,
            'name': exc_tb.tb_frame.f_code.co_name,
            'type': exc_type.__name__
        }
        # for filename, num, funcname, source in traceback.extract_tb(exc_tb):  # extract_tb函数解读traceback对象包含的数据
        #     print("%-23s:%s '%s' in %s()" % (filename, num, source, funcname))
        traceback.print_exception(exc_type, exc_value, exc_tb)  # print_exception函数打印异常栈跟踪信息
        print(traceback_details)

# ### 标准库traceback模块
# 用于处理异常栈， 提供了print_exception、format_exception等输出异常栈等常用的工具函数；
# - Print or retrieve a stack traceback
# - 官方文档：https://docs.python.org/3/library/traceback.html
