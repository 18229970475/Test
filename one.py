# -*- coding:utf-8 -*-
i = "语文"
print(i)

'''
多行注释
注释
'''
"""
遗憾注释
第二行注释
"""
# 多行语句使用‘\’来实现
year = 2021
month = 4
day = 10
date = year + \
       month + \
       day
print(date)

# 使用三引号（'''或"""）可以指定一个多行字符串
paragraph = """这是一个段落，
可以由多行组成"""
print(paragraph)

# 使用转义字符‘\’
print("hello world\nwill")

# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
print(r"hello world\nwill")

# 按字面意义级联字符串，如“this”“is”“string”会被自动转换为this is string
print("今天天气""qingsks")

# 字符串可以用+运算符连接在一起，用*运算符重复
print("dsjfd"+"gggg")
print("abc"*2)

# Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
str = "hello word"
print(str[0])
print(str[-1])

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始到最后的所有字符
print(str[1:9:2])  # 输出从第二个开始到第9个且每隔两个的字符

# 用户输入
'''
useName = raw_input("请输入用户名：")
passWord = raw_input("请输入密码：")
if useName == "wh" and passWord == "123":
    print("登录成功")
else:
    print("登录失败")
'''

# type()函数可以用来查询变量所指的对象类型
a, b, c, d = 10, 2.5, True, 4+3j
print(type(a),type(b),type(c),type(d))







