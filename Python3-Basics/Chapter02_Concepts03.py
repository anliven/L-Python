def is_palindrome(text):  # 判断是否是回文
    text2 = text[::-1]
    return text == text2


something = input("Enter text: ")  # Python交互式命令行：标准键盘输入
# print(type(something))  # 内置函数type()查看对象类型
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

# ### input()与print()
# 使用内置input()函数与print()函数可以分别实现输入与输出；
# - input()：实现标准键盘输入，可以接收一行文本并返回该文本(注意：返回的是str类型)；
# - print()：实现标准输出，输出结果默认会换行，可以使用“end=''”参数实现不换行；
