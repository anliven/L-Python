#! python3
# -*- coding: utf-8 -*-


class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))  # {:d},十进制

    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod  # 使用装饰器（Decorator）标记为类方法，@classmethod装饰器等价于调用“how_many = classmethod(how_many)”
    def how_many(cls):  # how_many是一个属于类而非属于对象的方法
        print("We have {:d} robots.".format(cls.population))


robot1 = Robot("Robot-1")
robot1.say_hi()
Robot.how_many()
robot2 = Robot("Robot-2")
robot2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
robot1.die()
robot2.die()
Robot.how_many()

# ### 实例变量（Instance Variables）与类变量（Class Variables）
# - 类变量（Class Variable）是共享的（Shared），可以被属于该类的所有实例访问；
# - 对象变量（Object variable）不会被共享，由类的每一个独立对象或实例所拥有；
# - 注意当一个对象变量与一个类变量名称相同时，类变量将会被隐藏；
#
# ### 属性引用（AttributeReference）
# - 使用self来引用同一对象的变量与方法;
