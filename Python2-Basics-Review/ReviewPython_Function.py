# -*- coding: utf-8 -*-

###############################################################################

#函数是可重用的程序段，实现特定的功能。
#函数可以把某个功能的代码分离出来，在需要的时候重复使用，让程序结构更清晰。
#在Python中用关键字def定义一个函数。


def sayHello():  # sayHello是这个函数的名字，后面的括号里是参数，这里没有，表示不需要参数。
    print 'hello world!'  # 缩进的代码块就是整个函数的内容，称作函数体。
#调用这个函数：sayHello() 得到和直接执行print 'hello world!'一样的结果。

#--------------------------------------------------------------------------------

#函数里允许定义一些参数，参数写在括号里，如果有多个参数，用逗号隔开。
#参数在函数中相当于一个变量，变量的值是在调用函数的时候被赋予的。
#在函数内部，可以像使用变量一样使用它。


def hiHello(someone):
    print someone + ' says Hello!'


def plus(num1, num2):
    return num1+num2

#调用带参数的函数时，需要传入的参数值放在括号中，用逗号隔开。
#提供的参数值的数量和类型需要跟函数定义中的一致。
#hiHello('Crossin') #注意:字符串类型的值不能少了引号
#plus(3,4)

#return是函数的结束语句，return后面的值被作为这个函数的返回值。
#函数中任何地方的return被执行到的时候，这个函数就会结束。

################################################################################

#函数的参数传递
        
#--------------------------------------------------------------------------------

#最常用的函数定义方式


def func1(arg1, arg2):
    print arg1, arg2

#调用：func1(3, 7) 输出结果：3 7

#函数定义时的参数名（arg1、arg2）称为形参，调用时提供的参数（3、7）称为实参。
#这里是根据调用时提供参数的位置进行匹配，要求实参与行参的数量相等，默认按位置匹配参数。
#调用时，少参数或者多参数都会引起错误。
#调用时，也可根据形参的名称指定实参，但必须提供所有的参数：func1(arg2=3, arg1=7)，输出结果：7 3
        
#--------------------------------------------------------------------------------

#带默认值的函数定义
        
#函数定义增加了参数的默认值，当没有提供足够的参数时，会用默认值作为参数的值。
#定义参数默认值的函数可以在调用时更加简洁。


def func2(arg1=1, arg2=2, arg3=3):
    print arg1, arg2, arg3

#调用func2(2,3,4) 输出结果：2 3 4
#调用func2(5,6) 输出结果： 5 6 3
#调用func2(7) 输出结果： 7 2 3
#调用func2(arg2=8) 输出结果： 1 8 3
#调用func2(arg3=9,arg1=10) 输出结果: 10 2 9
#调用func2(11,arg3=12) 输出结果: 11 2 12

#注意:没有指定参数名的参数必须在所有指定参数名的参数前面，且参数不能重复,否则会报错。
#调用func(arg1=13, 14) 输出结果：SyntaxError: non-keyword arg after keyword arg
#调用func(15, arg1=16) 输出结果：TypeError: func2() got multiple values for keyword argument 'arg1'

#--------------------------------------------------------------------------------

#参数数量任意的函数定义
        
#函数在定义时在形参前加上星号前缀（*）,并不指明参数个数，就可以处理任意参数个数的情况。  
#调用时的实参会存储在一个 tuple（元组）对象中，赋值给形参。
#在函数内部，需要对参数进行处理时，只对这个tuple 类型的形参（这里是 args）进行操作。
#注意：tuple（元组）是有序的，所以 args 中元素的顺序受到赋值时的影响。


def func3(*args):
    for i in args:
        print i

#调用func3(1) 输出结果：1 
#调用func3(1,2) 输出结果：1 2
#调用func3(1,2,3) 输出结果：1 2 3
#调用func3(3,2,1) 输出结果：3 2 1 #调用顺序不同，结果也就不同。

#--------------------------------------------------------------------------------

#既可按参数名传递参数，不受位置的限制，又不受数量限制的函数定义
                
#把参数以键值对字典的形式传入,字典是无序的，在调用时，参数的顺序无所谓，只要对应合适的形参名就可以。
#在输出的时候，并不一定按照提供参数的顺序。


def func4(**kargs):
    for k in kargs:
        print k, ':', kargs[k]

#调用func4(a=1, b=2, c=3) 
#调用func4(x=4, y=5)

#--------------------------------------------------------------------------------

#多种参数传递方式混合使用
                
#定义函数形参的顺序：无默认值的形参(arg) 》有默认值的形参(arg=) 》元组参数(*args) 》字典参数(**kargs)
#调用参数顺序：指定参数名称的参数要在无指定参数名称的参数之后；不可以重复传递。
#函数被调用时，参数的传递过程为：
    #1.按顺序把无指定参数的实参赋值给形参；
    #2.把指定参数名称(arg=v)的实参赋值给对应的形参；
    #3.将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
    #4.将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。


def func5(x, y=5, *a, **b):
    print x, y, a, b

#调用func5(1) 输出结果：1 5 () {}
#调用func5(1,2) 输出结果：1 2 () {}
#调用func5(1,2,3) 输出结果：1 2 (3,) {}
#调用func5(1,2,3,4) 输出结果：1 5 () {}
#调用func5(x=1) 输出结果：1 5 () {}
#调用func5(x=1,y=1) 输出结果：1 1 () {}
#调用func5(x=1,y=1,a=1) 输出结果：1 1 () {'a': 1}
#调用func5(x=1,y=1,a=1,b=1) 输出结果：1 1 () {'a': 1, 'b': 1}
#调用func5(1,y=1) 输出结果：1 1 () {}
#调用func5(1,2,3,4,a=1) 输出结果：1 2 (3, 4) {'a': 1}
#调用func5(1,2,3,4,k=1,t=2,o=3) 输出结果：1 2 (3, 4) {'k': 1, 't': 2, 'o': 3}

################################################################################