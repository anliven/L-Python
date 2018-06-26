# coding=utf-8


class Field(object):  # 定义Field类，负责保存数据库表的字段名和字段类型
    def __init__(self, name, column_type):  # 类实例化时将得到两个参数，并被绑定为Field的私有属性
        self.name = name
        self.column_type = column_type

    def __str__(self):  # 将Field转化为字符串时，将返回“Field:XXX”，XXX是传入的name名称
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):  # 在Field的基础上进一步定义类型
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')  # 类实例初始化时，自动调用父类的初始化方式


class IntegerField(Field):  # 在Field的基础上进一步定义类型
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')  # 类实例初始化时，自动调用父类的初始化方式


class ModelMetaclass(type):  # 定义元类
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()  # 创建一个新的字典mapping
        for k, v in attrs.items():  # 将每一个类的属性，通过.items()遍历其键值对
            if isinstance(v, Field):  # 如果值是Field类，则打印键值
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v  # 并将这一对键值绑定到mapping字典
        for k in mappings.keys():  # 将刚刚传入值为Field类的属性删除
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 创建一个专门的__mappings__属性，保存字典mapping（属性和列的映射关系）
        attrs['__table__'] = name  # 创建一个专门的__table__属性，保存传入的类的名称，这里的表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):  # 使用元类来定制基类Model，在Model类中定义各种操作数据库的方法
    def __init__(self, **kwarg):
        super(Model, self).__init__(**kwarg)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):  # 模拟建表操作
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):  # 从Model创建一个子类User，用来操作对应的数据库表User
    id = IntegerField('id')  # 定义类的属性到列的映射
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 父类Model和属性类型StringField、IntegerField由ORM框架提供；
# “id = IntegerField('id')”会自动解析为“Model.__setattr__(self, 'id', IntegerField('id'))”;
# - 因为“IntergerField('id')”是Field子类的实例，自动触发元类的“__new__”；
# - 所以将“IntergerField('id')”存入“__mappings__”并删除这个键值对；
# 查找metaclass的顺序：
# - 当定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass；
# - 如果没有找到，就继续在父类Model中查找metaclass，使用Model中定义的metaclass（这里是ModelMetaclass）来创建User类，
# - 也就是说，metaclass可以隐式地继承到子类，但子类自己感觉不到；


u = User(id=12345, name='Batman', email='batman@nasa.org', password='iamback')  # 创建一个实例
# 先调用“Model.__setattr__”将键值载入私有对象；
# 然后调用元类（ModelMetaclass.__new__）将Model中的私有对象，只要是Field的实例，都自动存入“u.__mappings__”；
u.save()  # 通过u.save()模拟数据库存入操作，遍历“__mappings__”，虚拟sql并打印；

# ### ORM框架（Object Relational Mapping，对象关系映射）
# - 对象：表示使用框架的对象和编程语言，例如 Python；
# - 关系：表示正在使用的RDBMS数据库(关系数据库管理系统)；
# - 映射：表示前两部分（对象和数据库表）之间的桥梁和连接；
# 简而言之，ORM是为了将编程语言与数据库之间相连，以便简化创建依赖于数据的应用程序过程；
# 也就是将关系数据库的一行映射为一个对象（一个类对应一个表），这样写代码更简单，不用直接操作SQL语句；
# Python中典型的ORM框架有Django和SQLAlchemy等；
