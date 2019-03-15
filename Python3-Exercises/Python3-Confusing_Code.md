# Confusing_Code



## 01
以下代码的执行结果是什么？
```python
testList = ['a', 'b', 'c']
print(testList[5:])
```


## 02
以下代码的执行结果是什么？
```python
a = [123, "xxx", "yyy"]
b = a
c = a[:]

print(a is b, a is c, b is c)
print(a == b, a == c, b == c)
```


## 03
以下代码的执行结果是什么？
```python
a = [[]] * 3
print(a)
a[0].append(111)
a[1].append(222)
a.append('AAA')
print(a)

b = [[] for _ in range(10)]
b[0].append(10)
print(b)

c = [[0]] * 5
c[0][0] = 1
print(c)

d = [[456]] * 5
d[0][0] = 0
d[1].append(789)
print(d)
```


## 04
以下代码的执行结果是什么？
```python
list_1 = [111, 333, 555, "aaa", "ccc"]
list_2 = [111, 222, 333, "ccc"]
print(list_1 + list_2)
print([x for x in list_1 if x in list_2])
print([i for i in list_1 if i not in list_2])
print([i for i in list_2 if i not in list_1])
```


## 05
以下代码的执行结果是什么？
```python
list1 = [(2), (0), (1), (8)]
list2 = [(2,), (0,), (1,), (8,)]

print(type((list1[0])))
print(type((list2[0])))
```


## 06
在Python3和Python2中分别执行如下代码，结果分别是什么？
```python
print(5/2, 5./2)
print(10//3, (-10)//3)
print(10//5, (-10)//5)
```


## 07
以下代码的执行结果是什么？
```python
class Parent():
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
```


## 08
以下代码的执行结果是什么？
```python
def multipliers(x):
    return (x * i for i in range(5))


def test1():
    return [lambda x: x * i for i in range(5)]


def test2():
    for i in range(5):
        yield lambda x: i * x


def test3():
    return [lambda x, i=i: i * x for i in range(5)]


print(list(multipliers(2)))
print([m(2) for m in test1()])
print([m(2) for m in test2()])
print([m(2) for m in test3()])
```


## 09
以下代码的执行结果是什么？
```python
A = 'abc'
B = ''.join(['a', 'b', 'c'])
print(A is B, A == B)

a = "hello world"
b = "hello world"
c = "hello world" * 50
d = "hello world" * 50
e = [1, 2, 3]
f = [1, 2, 3]

print(a is b, c is d, e is f)
print(a == b, c == d, e == f)
```


## 10
以下代码的执行结果是什么？
```python
a = "abc"
id_a1 = id(a)
a.replace("a", "A")
a += "def"
id_a2 = id(a)
print(a, id_a1 == id_a2)

b = ['333', '222', '111']
id_b1 = id(b)
b.sort()
b.append('000')
id_b2 = id(b)
print(b, id_b1 == id_b2)

c = b
c.append("666")
print(c is b, c == b)
```


## 11
以下代码的执行结果是什么？
```python
a = 111
b = []


def fun(x):
    x = 222
    print(x)


def fun2(x):
    x.append("AAA")
    print(x)


fun(a)
fun2(b)
print(a, b)
```


## 12
以下代码的执行结果是什么？
```python
a = [1, 2, 3]
b = a[:]
print(a == b, a is b)

c = {'1': "one", '2': 'two'}
d = c
d[3] = 'three'
print(c == d, c is d)

e = (111, 333)
f = e
f = (555, 777)
print(e == f, e is f)
```


## 13
以下代码的执行结果是什么？
```python
class Person:
    name = "test"
    money = []


AAA = Person()
AAA.name = "winner"
AAA.money.append(100000000)
BBB = Person()

print(AAA.name, AAA.money, BBB.name, BBB.money, Person.name, Person.money)
```


## 14
以下代码的执行结果是什么？
```python
import copy

a = [6, [0, 1], 8]
b = copy.copy(a)
a[1].append(2)
print(b, a == b, a is b)
c = copy.deepcopy(a)
a[1].append(3)
print(c, a == c, a is c)
```


## 15
以下代码的执行结果是什么？
```python
import copy

a = [1, 2, 3, ['a', 'b']]
b = a
cc = copy.copy(a)
cd = copy.deepcopy(a)

a.append(4)
a[3].append('c')
print("a= ", a, "\nb= ", b, "\ncc= ", cc, "\ncd= ", cd)
```


## 16
以下代码的执行结果是什么？
```python
test = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
test1 = [test[x] for x in test]
test2 = {i: i * i for i in range(5)}
test3 = [[i, i * i] for i in range(10) if i % 2 == 0]

print("\n", test1, "\n", test2, "\n", test3)
```


## 17
以下代码的执行结果是什么？
```python
class A(object):
    def go(self):
        print("class A go!")

    def stop(self):
        print("class A stop!")


class B(A):
    def go(self):
        super(B, self).go()
        print("class B go!")


class C(A):
    def go(self):
        super(C, self).go()
        print("class C go!")

    def stop(self):
        super(C, self).stop()
        print("class C stop!")


class D(B, C):
    def go(self):
        super(D, self).go()
        print("class D go!")

    def stop(self):
        super(D, self).stop()
        print("class D stop!")


class E(B, C):
    pass


a = A()
b = B()
c = C()
d = D()
e = E()

print("a.go", "#" * 20), a.go()
print("b.go", "#" * 20), b.go()
print("c.go", "#" * 20), c.go()
print("d.go", "#" * 20), d.go()
print("e.go", "#" * 20), e.go()

print("a.stop", "&" * 20), a.stop()
print("b.stop", "&" * 20), b.stop()
print("c.stop", "&" * 20), c.stop()
print("d.stop", "&" * 20), d.stop()
print("e.stop", "&" * 20), e.stop()
```


## 18
以下代码的执行结果是什么？
```python
st = "abc"
st_new = st.replace("a", "A")
print("after: ", st, st_new)

li = ['333', '222', '111']
li_new = li.sort()
print("after: ", li, li_new)
```


## 19
以下代码的执行结果是什么？
```python
import copy

tu = (1, 2, 3)
a = tu
b = copy.copy(tu)
c = copy.deepcopy(tu)
print(tu == a, tu == b, tu == c)
print(id(tu) == id(a), id(tu) == id(b), id(tu) == id(c))

li = [111, 222, 333]
aaa = li
bbb = copy.copy(li)
ccc = copy.deepcopy(li)
print(li == aaa, tu == bbb, tu == ccc)
print(id(li) == id(aaa), id(li) == id(bbb), id(li) == id(ccc))
```


## 20
以下代码的执行结果是什么？
```python
def f(x, li=[]):
    for i in range(x):
        li.append(i * i)
    print(li)


f(2)
f(3, [3, 2, 1])
f(3)
```


## 21
以下代码的执行结果是什么？
```python
def append_list(val, var=[]):
    var.append(val)
    return var


f1 = append_list(1)
f2 = append_list(2, [])
f3 = append_list('Python')
print(f1)
print(f2)
print(f3)
```


## 22
以下代码的执行结果是什么？
```python
def extendList(val, tl=[]):
    tl.append(val)
    return tl


def extendList2(val, tl=None):
    if tl is None:
        tl = []
    tl.append(val)
    return tl


list1 = extendList(123)
list2 = extendList(789, [])
list3 = extendList('abc')
list4 = extendList2(111)
list5 = extendList2(999, [])
list6 = extendList2('ABC')

print("list1= %s, list2= %s, list3= %s" % (list1, list2, list3))
print("list4= %s, list5= %s, list6= %s" % (list4, list5, list6))
```


## 23
以下代码的执行结果是什么？
```python
def func(var1, var2=[]):
    var2.append(var1)
    print(var2)


def func2(var1, var2=None):
    if not var2:
        var2 = []
    var2.append(var1)
    print(var2)


func(1)
func(2)
func(3)
func2("a")
func2("b")
func2("c")
```


## 24
```python
class Student:
    score = []


stu1 = Student()
stu2 = Student()
stu1.score.append(99)
stu1.score.append(96)
stu2.score.append(98)
print(stu1.score)
print(stu2.score)
```


## 25
以下代码的执行结果是什么？
```python
class Test():
    var = []

    def add_str(self, string):
        self.var.append(string)


class Test2():
    def __init__(self):
        self.var = []

    def add_str(self, string):
        self.var.append(string)


a = Test()
a.add_str('111')
b = Test()
b.add_str('222')
print(a.var, b.var)
c = Test2()
c.add_str('333')
d = Test2()
d.add_str('444')
print(c.var, d.var)
```


## 26
以下代码的执行结果是什么？
```python
a = 1 or 3
b = 1 and 3
c = 1 < (3 == 3)
d = 1 < 3 == 3
e = 0 and 2 and 1
f = 0 and 2 or 1
g = 0 and 2 or 1 or 4
h = 0 or False and 1

print(a, b, c, d, e, f, g, h)
```


## 27
以下代码的执行结果是什么？
```python
num = 6


def func1():
    num = 8


def func2():
    print(num)


func2()
func1()
func2()
```


## 28
以下代码的执行结果是什么？
- Temp.py
```python
n = 111
```
- Test.py
```python
import Temp
import sys

n = 222
n += 1


def func1():
    global n
    n += 1
    Temp.n += 1
    m = sys.modules['Temp']
    m.n += 1
    print(n, Temp.n, m.n)


def func2():
    Temp.n += 1
    print(Temp.n)


def func3():
    m = sys.modules['Temp']
    m.n += 1
    print(m.n)


func1()
func2()
func3()
```

## 29
以下代码的执行结果是什么？
```python
def func():
    try:
        return 'test'
    finally:
        print('finally')


def func1():
    try:
        return 1
    finally:
        return 11


def func2():
    try:
        raise ValueError()
    except:
        return 2
    finally:
        return 22


def func3():
    try:
        raise ValueError()
    except IndexError:
        return 3
    finally:
        return 33


f = func()
print(f)
print(func1(), func2(), func3())
```

## 30
以下代码的执行结果是什么？
```python
class BBB(object):
    def func(self):
        print('class BBB func')

    def __init__(self):
        print("class BBB init")


class AAA(object):
    def func(self):
        print('class AAA func')

    def __new__(cls, num):
        print("class AAA new", num)
        if num > 10:
            return super(AAA, cls).__new__(cls)
        return BBB()

    def __init__(self, num):
        print("class AAA init", num)


t1 = AAA(5)
t1.func()

t2 = AAA(20)
t2.func()
```


## 31
以下代码的执行结果是什么？
```python
class Test(object):
    def __init__(self):
        print('class Test init')

    def mydefault(self, *args):
        print('class Test default', args)

    def __getattr__(self, name):
        return self.mydefault


t1 = Test()
t1.func1()
t1.func2(111)
```


## 32
以下代码的执行结果是什么？
```python
class A(object):
    def __init__(self, value):
        self.val = value


class B(A):
    def __init__(self, val):
        super(B, self).__init__(val)
        self.val += 2


class C(A):
    def __init__(self, val):
        super(C, self).__init__(val)
        self.val *= 5


class D(C, B):
    pass


class E(D):
    e = super(D)

    def __init__(self, val):
        self.e.__init__(val)
        self.val += 1


t = E(5)
print(t.val)
```


## 33
以下代码的执行结果是什么？
```python
gen = (x for x in range(3))
# print(list(gen))
print(1 in gen, 2 in gen, 1 in gen, 2 in gen)
print(list(gen))

gen2 = (x for x in range(3))
test_list = list(gen2)
print(test_list)
print(1 in test_list, 2 in test_list, 1 in test_list, 2 in test_list)
```


## 34
以下代码的执行结果是什么？
```python
test_list = [lambda: i for i in range(3)]
for t in test_list:
    print("test_list:", t())

test_list2 = [lambda x=i: x for i in range(3)]
for t in test_list2:
    print("test_list2:", t())

test_gen = (lambda: i for i in range(3))
for t in test_gen:
    print("test_gen:", t())
```


## 35
以下代码的执行结果是什么？
```python
def test(items, size):
    return zip(*[iter(items)] * size)


t = test(range(9), 3)
print(list(t))
```


## 36
以下代码的执行结果是什么？
```python
test_list = [2, 4, 5, 6]
for i in test_list:
    print(i)
    if not i % 2:
        test_list.remove(i)
print(test_list)

test_list2 = [2, 4, 5, 6]
for index, item in enumerate(test_list2):
    print("Index:%s - Item:%s" % (index, item))
    if not item % 2:
        test_list2.remove(item)
print(test_list2)
```


## 37
以下代码的执行结果是什么？
```python
test_list = [0]

test_list += [1]
id_1 = id(test_list)

test_list = test_list + [2]
id_2 = id(test_list)

test_list.append(3)
id_3 = id(test_list)

test_list.extend([4])
id_4 = id(test_list)

print(test_list)
print(id_1 == id_2, id_3 == id_4)
```


## 38
以下代码的执行结果是什么？
```python
print(isinstance(True, int))
print(True + 3 * True - False)
print(True << 10)
```


## 39
以下代码的执行结果是什么？
```python
tup = ([],)
tup[0].extend([1])
print(tup)

tup2 = (1,)
tup2 += (2,)
tup2 = tup2 + tup
print(tup2)
```


## 40
以下代码的执行结果是什么？
```python
a = float('inf')
b = float('inf')*2
c = float('nan')
d = float('nan')
print(a is b, a == b)
print(c is c, c == c)
print(c is d, c == d)
```


## 41
以下代码的执行结果是什么？
```python
numbers = [1, 2, 3]
numbers2 = (1, 2, 3)
print(sum(numbers), sum(numbers2))

squares = (n + n for n in numbers)
print(sum(squares))

squares2 = (n + n for n in numbers)
print(tuple(squares2))
print(sum(squares2))

squares3 = (n + n for n in numbers)
print(6 in squares3, 6 in squares3)
```


## 42
以下代码的执行结果是什么？
```python
test_dict = {"AAA": 111, "BBB": 222, "CCC": 333}
x, y, z = test_dict
print("x - {}, y - {}, z - {}".format(x, y, z))
part, *rest = test_dict
print("*rest - ", *rest)
```


## 43
以下代码的执行结果是什么？
```python
a, b = 2, 3
print("Hi") if a < b else print("Bye")
```


## 44
以下代码的执行结果是什么？
```python
Data = dict(zip(('a', 'b', 'c'), (1, 2, 3)))
Data2 = [Data[s] for s in Data]
print("Data:", Data)
print("Data2:", Data2)

print({i: i * i for i in Data2})
print([[i, i * i] for i in Data2])
```

## 45
以下代码的执行结果是什么？
```python
a = []
for _ in range(5):
    a.append(0)
b = [0] * 5
print(a == b)

c = [[0]] * 5
print(c)
c[0][0] = 123
print(c)

d = [[0] for _ in range(5)]
print(d)
d[0][0] = 123
print(d)
```
