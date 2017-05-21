# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 面向对象编程语言(Object Oriented Programming Language)
# 模块(module)是包含函数和变量的Python文件。import这个文件后，可以使用 ‘.’ 操作符访问到模块中的函数和变量。
# 类(class)是在Python文件中的一种代码结构，包含函数和数据。通过类，相当于把函数和数据放到一个容器中，从而用 ‘.’ 操作符访问到它们。
# 将一个类“实例(instance)化”以后，就得到了一个对象(object)。

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print "I AM CLASSY APPLES!"

thing = MyStuff() #实例化一个对象thing
thing.apple()
print thing.tangerine

#实例化对象的过程
# 1. Python看到了MyStuff()并且知道了它是定义过的一个类。
# 2. Python创建了一个空的对象，里边包含了在类MyStuff()中用def创建的所有函数。
# 3. 然后Python回去检查是不是在里边创建了一个__init__魔法函数，如果有创建，它就会调用这个函数，从而对你的空对象实现了初始化。
# 4. 在__init__ 函数里的self，就是Python创建的空对象，可以对它进行类似模块、字典等的操作，或为它设置一些变量等。
# 5. 在__init__ 函数里，设置了变量self.tangerine并赋值，这样就初始化了该对象。
# 6. 最后Python将这个新建的对象赋给一个叫thing的变量，以供后面使用。


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family","With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

# 为什么创建 __init__ 或者别的类函数时需要多加一个self变量？# 说明这指的是实例的属性。
