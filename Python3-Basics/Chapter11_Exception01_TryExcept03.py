# -*- coding: utf-8 -*-

while True:
    try:
        x = int(input("Enter the first number:"))
        y = int(input("Enter the second number:"))
        value = x / y
        print("x / y is ", value)
    # except:
    except Exception as e:  # 不会捕获从BaseException（Exception的超类）派生而来的异常
        print("Invalid input. Please try again.", e)
    else:  # 没有错误发生时，自动执行else子句的代码
        break  # 跳出循环

# ### 捕获所有异常
# 如果在except语句中不具体指定任何异常类，将捕获所有的异常；
# 一般不建议这样做，因为这也将捕获用户的“Ctrl+C”操作、函数sys.exit等；
# 大多数情况下，建议使用“except Exception as e”并对异常对象进行检查；
#
# ### else子句
# 可以将一个else子句与try..except代码块相关联，在没有发生异常的时，将执行else子句中的代码块；
