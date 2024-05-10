# @Time    : 2023/8/9 16:56
# @Author  : SU_SHAN_WAN_YU
# @File    : 2 数据类型.py
# @Description :
'''
int 整形
float 浮点，带有小数点
string 字符串，引号里面的内容，单双或者三引号都是字符串
boolean 布尔类型，判断true或者false
'''
money = 82
# type()检查变量类型
print(type(money))  # 内置函数，负责输出结果
# money 是一个变量，后面的值允许变化
money = 10.9
print(type(money))
print(money)
money = '1万'  # 引号里的就是字符串，三 引号保留格式输出
# 布尔类型   Ture or False
# 开发当中的判断，是否登录成功
is_login = True  # 真
print(is_login)
is_login = False
print(type(is_login))
