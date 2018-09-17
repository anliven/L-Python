# coding=utf-8
import shelve


def store_person(db):  # 存储用户输入数据到shelf对象中
    pid = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')
    db[pid] = person


def lookup_person(db):  # 从shelf对象中查询数据
    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()  # 忽略大小写
    try:
        print(field.capitalize() + ':', db[pid][field])
    except KeyError:
        print("No record.")


def print_help():  # 帮助信息
    print('The available commands are:')
    print('store  : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit   : Save changes and exit')
    print('?      : Prints this message')


def enter_command():  # 获取用户输入的命令
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()  # 忽略大小写
    return cmd


def main():
    database = shelve.open('Chapter18_shelve_db')  # 打开一个数据库文件
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()  # 关闭数据库


if __name__ == '__main__':
    main()

# ### 标准库shelve模块
# - Python object persistence
# - 官方文档：https://docs.python.org/3/library/shelve.html
# - shelve模块可以简单地将数据存储在文件中；
#
# ### 文件的打开与关闭
# shelve.open()函数将一个文件名作为参数，并返回一个可用来存储数据的shelf对象，其类似与所有键都为字符串的字典；
# 如果shelve.open()函数的参数writeback设置为True，那么操作过程中的数据结构都将保存在内存中，直到关闭shelf对象时才写入磁盘；
# 如果处理的数据量不多，建议将参数writeback设置为True；
# 操作完成后，可以调用shelf对象的close()方法关闭；
#
# ### 特别注意
# 修改使用模块shelve存储的对象，必须将获取的副本赋值给一个临时变量，并在这个副本后再次存储；
